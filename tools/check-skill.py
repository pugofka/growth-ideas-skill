"""Checks that every skill in skills/ installs everywhere: Claude Code, Cowork, and a claude.ai ZIP upload.

Also guards against overfitting: no eval fixture term (evals/fixture-terms.txt) may appear in a skill's text.
Exit code 1 on any problem.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWED_KEYS = {'name', 'description', 'license', 'compatibility', 'metadata', 'allowed-tools'}
DESCRIPTION_MAX = 200  # claude.ai upload guide: "200 characters maximum"
NAME_RE = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
NON_PORTABLE = [
    (re.compile(r'!`'), 'Claude Code-only command injection (!`...`)'),
    (re.compile(r'(?<![\w.])(/Users/|/home/|~/|[A-Z]:\\)'), 'absolute or home path'),
]

def frontmatter(text):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m:
        return None
    fields = {}
    for line in m.group(1).splitlines():
        if line and not line[0].isspace() and ':' in line:
            key, value = line.split(':', 1)
            fields[key.strip()] = value.strip()
    return fields

def fixture_terms():
    path = os.path.join(ROOT, 'evals', 'fixture-terms.txt')
    if not os.path.exists(path):
        return []
    return [t.strip() for t in open(path, encoding='utf-8') if t.strip() and not t.startswith('#')]

def check_skill(skill_dir, terms):
    errors = []
    name = os.path.basename(skill_dir)
    skill_md = os.path.join(skill_dir, 'SKILL.md')
    if not os.path.exists(skill_md):
        return [f'{name}: SKILL.md is missing']
    text = open(skill_md, encoding='utf-8').read()
    fm = frontmatter(text)
    if fm is None:
        return [f'{name}: SKILL.md has no frontmatter']
    extra = set(fm) - ALLOWED_KEYS
    if extra:
        errors.append(f'{name}: frontmatter keys not allowed in claude.ai uploads: {sorted(extra)}')
    if fm.get('name') != name:
        errors.append(f'{name}: frontmatter name {fm.get("name")!r} does not match the folder name')
    if not NAME_RE.match(name) or len(name) > 64:
        errors.append(f'{name}: name must be 1-64 chars of a-z, 0-9 and single hyphens')
    description = fm.get('description', '')
    if not 1 <= len(description) <= DESCRIPTION_MAX:
        errors.append(f'{name}: description is {len(description)} chars, must be 1-{DESCRIPTION_MAX}')

    files = [skill_md] + [os.path.join(d, f) for d, _, fs in os.walk(skill_dir) for f in fs
                          if f.endswith('.md') and os.path.join(d, f) != skill_md]
    for path in files:
        rel = os.path.relpath(path, ROOT)
        body = open(path, encoding='utf-8').read()
        for pattern, what in NON_PORTABLE:
            if pattern.search(body):
                errors.append(f'{rel}: {what}')
        for term in terms:
            if re.search(r'\b' + re.escape(term) + r'\b', body, re.I):
                errors.append(f'{rel}: contains eval fixture term {term!r}')
    for link in re.findall(r'`([\w-]+/[\w./-]+\.(?:md|txt|json|py|sh))`', text):
        if not os.path.exists(os.path.join(skill_dir, link)):
            errors.append(f'{name}: SKILL.md references missing file {link}')
    return errors

def main():
    skills_root = os.path.join(ROOT, 'skills')
    terms = fixture_terms()
    errors = []
    for entry in sorted(os.listdir(skills_root)):
        if os.path.isdir(os.path.join(skills_root, entry)):
            errors += check_skill(os.path.join(skills_root, entry), terms)
    for line in errors:
        print('FAIL', line)
    if not terms:
        print('WARN evals/fixture-terms.txt is missing: the fixture leak check did not run')
    print('OK' if not errors else f'{len(errors)} problem(s)')
    return 1 if errors else 0

if __name__ == '__main__':
    sys.exit(main())
