"""Generates evals/ for the growth-ideas skill.

Regression checks of form only, on fictional products. They show the skill did not break; they do not show it is useful.
Fixture names go to evals/fixture-terms.txt; tools/check-skill.py fails if any of them appears in a skill's text.
Never copy a fixture, a grader's wording or an example from here into SKILL.md.
"""
import os, shutil, textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'evals')
FIXTURE_TERMS = ['Tallyhop', 'Partlink', 'Quorvane']

# Workspace notes the prompt does not mention: the skill has to find them.
TALLYHOP = textwrap.dedent('''\
# Call notes — Tallyhop (internal)

- Tallyhop is a web app for independent bicycle repair shops in Poland: parts inventory, repair tickets, SMS-free email notifications to customers when a bike is ready.
- 52 shops pay a monthly subscription; most found us through a regional cycling trade fair in 2025.
- There is no integration with parts wholesalers yet; shops type in parts by hand. Owners mention it on almost every call.
- A shop usually decides within 2-3 weeks of a demo; there is a 14-day free trial.
- The website has a demo request form and a pricing page. Nobody tracks which page a demo request came from.
- Tried and stopped: paid search ads on generic keywords ("bike shop software") — too expensive for the budget; cold emails to shop owners — almost no replies.
- Already in progress: a referral discount for existing shops.
- The team: two founders and one developer. Founders can spend about 4 hours a week on growth.
''')
PARTLINK = textwrap.dedent('''\
# Partlink — заметки

- Partlink — сервис заказа запчастей для небольших автосервисов в России: каталог, заказ у нескольких поставщиков в одном окне, история заказов.
- 30 автосервисов платят подписку; почти все пришли по рекомендациям.
- На сайте есть форма заявки на демо; рассылок клиентам пока нет.
- Время на рост: около 5 часов в неделю у основателя.
''')
TERMS_HEADER = '# Fixture names from tools/gen-evals.py. tools/check-skill.py fails if any appears in a skill.\n'

UNAVAILABLE = 'I am unavailable during the task: make reasonable decisions and list assumptions and open questions at the end.'
SAVE = 'Save the result to `docs/ideas.md`.'

PLACEHOLDERS = ('no-placeholders', 'regex!', 1, 'file:docs/ideas.md', r'\bTBD\b|\bTODO\b|\?\?\?|<[a-z ]+>')
EMPTY_FIELDS = ('no-empty-fields', 'regex!', 2, 'file:docs/ideas.md',
                r'^[ \t>*-]*\**(cheapest test|stop if|kill criterion|самый дешёвый тест|самый дешевый тест|остановить, если|стоп, если|критерий остановки)\**:?\**:?[ \t]*(?=\r?\n(?![ \t]+\S)|(?![\s\S]))')
IDS_RESOLVE = ('fact-ids-resolve', 'llm', 2, 'file:docs/ideas.md',
               'PASS if every fact reference used in the document (labels such as F1, F2 or Ф1, Ф2) points to an entry that exists in the document\'s own list of facts, and the document has such a list whenever it uses such labels. FAIL if any label is cited but missing from the list. If the document uses no such labels, PASS.')

CASES = {
    'proceeds-without-context': (None,
        'We run a small B2B SaaS. Give me growth hypotheses we could test in the next two months. ' + UNAVAILABLE,
        [('no-invented-facts', 'llm', 3, 'last_message',
          'The user gave no facts about the product beyond "a small B2B SaaS". PASS if the reply either asks focused questions (each one would change the hypotheses; not a long generic questionnaire), or gives hypotheses while stating plainly that they rest on assumptions, and in both cases presents no specific fact about this product (customer count, features, prices, traffic, channels already tried) as known. FAIL if it states such specifics as facts, or if its questions are a long generic questionnaire rather than the few that matter.')]),
    'reads-workspace-materials': (('notes/call-notes.md', TALLYHOP),
        'Give growth hypotheses for our product Tallyhop for the next two months. ' + SAVE + ' ' + UNAVAILABLE,
        [('uses-notes', 'llm', 3, 'file:docs/ideas.md',
          'The workspace contained notes the user did not mention. They say: shops type in parts by hand because there is no wholesaler integration; a shop decides within 2-3 weeks of a demo; nobody tracks which page a demo request came from. PASS if the document uses at least two of these three facts. FAIL otherwise.'),
         PLACEHOLDERS, EMPTY_FIELDS, IDS_RESOLVE]),
    'respects-tried-and-in-progress': (('notes/call-notes.md', TALLYHOP),
        'Give growth hypotheses for our product Tallyhop for the next two months. ' + SAVE + ' ' + UNAVAILABLE,
        [('no-repeats', 'llm', 3, 'file:docs/ideas.md',
          'The notes say these were tried and stopped: paid search ads on generic keywords; cold emails to shop owners. In progress: a referral discount for existing shops. PASS if no hypothesis is essentially one of these (by meaning, not wording) unless it explicitly explains what is different this time. FAIL otherwise.')]),
    'outside-in-without-web': (None,
        'We have a sales meeting next week with Quorvane, a company we know nothing about yet. Research them and give growth hypotheses we could pitch. ' + SAVE + ' There is no internet access in this environment. ' + UNAVAILABLE,
        [('no-invented-company-facts', 'llm', 3, 'file:docs/ideas.md',
          'There was no internet access and no materials about Quorvane. PASS if the document says that research was not possible and lists what to find out or ask, and does not state any fact about Quorvane (industry, size, customers, products, website content) as known; hypotheses, if any, are explicitly conditional on assumptions. FAIL if it presents facts about Quorvane as known.'),
         PLACEHOLDERS]),
    'replies-in-user-language': (('notes/call-notes.md', TALLYHOP),
        'Дай гипотезы роста для нашего продукта Tallyhop на ближайшие два месяца. Сохрани результат в `docs/ideas.md`. Во время задачи я недоступен: принимай разумные решения, допущения и открытые вопросы перечисли в конце.',
        [('russian-output', 'llm', 2, 'file:docs/ideas.md',
          'The user wrote in Russian; the notes are in English. PASS if the document prose, including headings and field names, is in Russian (product names, fact labels and proper nouns may stay as they are). FAIL if it is mostly in English.')]),
    'russian-market-legal-notes': (('notes/partlink.md', PARTLINK),
        'Дай гипотезы роста для Partlink на ближайшие два месяца. Сохрани результат в `docs/ideas.md`. Во время задачи я недоступен: принимай разумные решения, допущения и открытые вопросы перечисли в конце.',
        [('ru-legal', 'llm', 2, 'file:docs/ideas.md',
          'The product sells in Russia. PASS only if: (1) every hypothesis that collects contacts (forms, lead magnets, quizzes) mentions consent to personal data processing (152-FZ); (2) every hypothesis that sends promotional messages (email, messenger, SMS) mentions prior consent of the recipient; (3) every hypothesis with paid or sponsored online placements mentions ad marking. If no hypothesis involves these, PASS. FAIL if any applicable note is missing.')]),
}

def write_case(name, workspace_file, prompt, graders):
    d = os.path.join(OUT, name); os.makedirs(os.path.join(d, 'graders'))
    open(os.path.join(d, 'prompt.md'), 'w').write(
        f'---\nmax_turns: 40\ntimeout_seconds: 900\nallowed_tools: [Read, Glob, Grep, Skill, Write, Edit]\ntags: [growth-ideas]\n---\n{prompt}\n')
    script = '#!/bin/bash\nset -euo pipefail\nmkdir -p docs\n'
    if workspace_file:
        path, body = workspace_file
        script += f"mkdir -p {os.path.dirname(path)}\ncat > {path} <<'CTX'\n{body}CTX\n"
    open(os.path.join(d, 'case.yaml'), 'w').write(f'schema_version: "1.1"\nname: {name}\ncontext:\n  scaffold_script: scaffold.sh\n')
    open(os.path.join(d, 'scaffold.sh'), 'w').write(script)
    os.chmod(os.path.join(d, 'scaffold.sh'), 0o755)
    for gname, gtype, w, target, body in graders:
        if gtype in ('regex', 'regex!'):
            match = '\nmatch: not_contains' if gtype == 'regex!' else ''
            flags = 'im' if gname == 'no-empty-fields' else 'i'
            front = f"type: regex\ntarget: {{ source: file, path: {target.split(':', 1)[1]} }}\npattern: '{body}'{match}\nflags: {flags}\nweight: {w}\narm: both"
            open(os.path.join(d, 'graders', gname + '.md'), 'w').write(f'---\n{front}\n---\n')
        else:
            focus = 'last_message' if target == 'last_message' else f"{{ source: file, path: {target.split(':', 1)[1]} }}"
            open(os.path.join(d, 'graders', gname + '.md'), 'w').write(f'---\ntype: llm\nfocus: {focus}\nweight: {w}\narm: both\n---\n{body}\n')

def reset():
    for entry in os.listdir(OUT) if os.path.isdir(OUT) else []:
        if entry == 'results':
            continue
        path = os.path.join(OUT, entry)
        shutil.rmtree(path) if os.path.isdir(path) else os.remove(path)

os.makedirs(OUT, exist_ok=True)
reset()
for name, (workspace_file, prompt, graders) in CASES.items():
    write_case(name, workspace_file, prompt, graders)
open(os.path.join(OUT, 'fixture-terms.txt'), 'w').write(TERMS_HEADER + '\n'.join(FIXTURE_TERMS) + '\n')
print('cases:', sorted(CASES))
