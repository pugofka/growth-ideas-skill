"""Builds dist/<skill>.zip for claude.ai upload (Customize > Skills > Upload a skill).

The archive holds the skill folder at its root, as the upload guide requires. Runs check-skill.py first.
"""
import os, subprocess, sys, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, 'dist')

def main():
    check = subprocess.run([sys.executable, '-I', os.path.join(ROOT, 'tools', 'check-skill.py')])
    if check.returncode:
        print('check-skill.py failed: nothing packaged')
        return 1
    os.makedirs(DIST, exist_ok=True)
    skills_root = os.path.join(ROOT, 'skills')
    for name in sorted(os.listdir(skills_root)):
        skill_dir = os.path.join(skills_root, name)
        if not os.path.isdir(skill_dir):
            continue
        out = os.path.join(DIST, name + '.zip')
        with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
            for d, _, files in os.walk(skill_dir):
                for f in sorted(files):
                    if f == '.DS_Store':
                        continue
                    path = os.path.join(d, f)
                    z.write(path, os.path.relpath(path, skills_root))
        print('built', os.path.relpath(out, ROOT))
    return 0

if __name__ == '__main__':
    sys.exit(main())
