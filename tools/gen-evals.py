"""Generates evals/ for the growth-ideas skill: abstract, fictional products; one behaviour per case."""
import os, shutil, textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'evals')

CLINIC = textwrap.dedent('''\
# Growth context: Lumen
## Goal
- Metric: number of paying clinics. Horizon: 2 months.
## Product facts
- F1. Lumen is a B2B appointment-scheduling SaaS for small private dental clinics in Russia.
- F2. Has: online booking widget, SMS-free email reminders, staff calendar, basic reports.
- F3. Does not have: payments, insurance integrations, mobile app (not planned).
- F4. Pricing: monthly subscription per clinic.
## Customers
- F5. 14 paying clinics, all small (1-3 chairs), most came from the founder's personal network.
- F6. Main sales blocker: clinics fear migrating patient records from their current software.
## Channels and data
- F7. Website gets few visits; no reliable analytics yet (lead source is not recorded).
- F8. The site FAQ promises "online prepayment", which the product does not have.
## Related assets
- F9. The same team runs a small IT-outsourcing agency that already maintains websites for 30 local medical businesses.
## Red lines
- No pivots, no taking payments, no medical advice. Owner time budget: 3 hours per week.
## Already tried / rejected — do not propose
- Cold calling clinics (too much owner time, no results).
- Free "practice audit" that requires access to patient data (blocked by clinics' privacy concerns).
## Already approved / in progress — do not propose again
- A referral discount for existing clinics.
''')
LEADER = textwrap.dedent('''\
# Growth context: Fernway
## Goal
- Metric: number of paying companies. Horizon: 2 months.
## Product facts
- F1. Fernway is an online form and survey builder for small businesses (up to 20 employees).
- F2. Has: drag-and-drop form editor, email notifications, basic response analytics, embeds for websites.
- F3. Does not have: advanced logic branching, enterprise SSO, data warehouse connectors, mobile app.
- F4. Price is several times lower than the market leader's.
## Competition
- F5. Formatica is the market leader, selling an enterprise suite to large corporations; Fernway has no feature parity with it.
## Customers
- F6. 40 paying small businesses.
## Related assets
- F7. The same owner runs a small marketing agency that builds websites for local businesses.
## Red lines
- No pivots. Client-facing copy must speak as "we" and must not name the agency or any internal team.
## Already tried / rejected — do not propose
- Paid search ads on generic keywords (too expensive for the budget).
''')

CASES = {
    'asks-for-context-when-missing': (None,
        'We run a small B2B SaaS. Give me growth hypotheses we could test in the next two months.',
        [('asks-context', 'llm', 3, 'last_message',
          'PASS if the reply does not deliver a full list of growth hypotheses and instead asks for (or offers a template for) missing product context — at minimum customer base, red lines/constraints, and what was already tried or rejected. FAIL if it produces a list of concrete hypotheses without that context.')]),
    'respects-rejected-and-approved': (CLINIC, None,
        [('no-repeats', 'llm', 3, 'file:docs/ideas.md',
          'Context lists as rejected: cold calling clinics; a free practice audit requiring patient data. Approved/in progress: a referral discount for existing clinics. PASS if no hypothesis is essentially one of these (by meaning, not wording). FAIL otherwise.')]),
    'no-invented-numbers': (CLINIC, None,
        [('no-invented-numbers', 'llm', 3, 'file:docs/ideas.md',
          'The context contains no traffic volumes, search demand, conversion rates or market sizes. PASS if every such number in the document is either absent or explicitly marked as an assumption/target to be validated. FAIL if invented volumes, conversion rates or market sizes are stated as facts.')]),
    'cites-facts-and-kill-criteria': (CLINIC, None,
        [('cites-ids', 'regex', 1, 'file:docs/ideas.md', r'F[0-9]'),
         ('has-stop-criterion', 'regex', 2, 'file:docs/ideas.md', r'[Кк]ритери[йи] остановки|[Ss]top criteri|[Kk]ill criteri'),
         ('has-cheapest-test', 'regex', 1, 'file:docs/ideas.md', r'[Сс]амый дешёвый тест|[Сс]амый дешевый тест|[Cc]heapest test')]),
    'hygiene-is-step-zero': (CLINIC, None,
        [('hygiene-separated', 'llm', 2, 'file:docs/ideas.md',
          'Context facts: lead source is not recorded (F7) and the site FAQ promises prepayment that does not exist (F8). PASS if fixing these appears as a separate preliminary/hygiene step (not counted among the growth hypotheses). FAIL if they are presented as growth hypotheses themselves or ignored entirely.')]),
    'no-absurd-leader-switch': (LEADER, None,
        [('no-leader-switch', 'llm', 3, 'file:docs/ideas.md',
          'Fernway has no feature parity with the market leader Formatica and serves a much smaller, cheaper segment. PASS if no hypothesis is a head-on "switch from Formatica to us" campaign (comparison page, ads on the leader brand, outreach to the leader\'s customers). FAIL if such a campaign is proposed as a hypothesis.')]),
    'company-voice': (LEADER, None,
        [('no-internal-names', 'llm', 2, 'file:docs/ideas.md',
          'Red line: client-facing copy must speak as "we" and must not name the marketing agency or any internal team. PASS if any offer/copy text intended for customers speaks as "we" without naming the agency or an internal team (mentions in internal reasoning such as insight/mechanism are fine). FAIL if customer-facing copy names the agency/team.')]),
    'proactive-site-block': (CLINIC, None,
        [('site-block', 'llm', 3, 'file:docs/ideas.md',
          'The user asked generally for growth hypotheses and did not request any structure. The product has a website and a booking widget (F2, F7, F8). PASS if the document contains a separate block/section of website or product improvements that affect sales (conversion, booking flow, onboarding, pricing page etc.), distinct from channel/company ideas and distinct from hygiene fixes. FAIL if there is no such separate block.')]),
    'russian-market-compliance': (CLINIC, None,
        [('ru-compliance', 'llm', 2, 'file:docs/ideas.md',
          'The product operates in Russia. PASS if, for every hypothesis that collects contacts (forms, lead magnets) or uses paid/sponsored placements or promotional messaging, the document mentions the relevant requirement: consent to personal data processing (152-FZ) for data collection, ad marking (erid / ad data operator) for paid placements, prior consent for promotional messages. FAIL if such a hypothesis ignores the relevant requirement. If no hypothesis involves these, PASS.')]),
    'replies-in-user-language': (CLINIC,
        'Используя контекст продукта в `growth-context.md`, дай 3–5 гипотез роста на ближайшие два месяца. Сохрани их в `docs/ideas.md`. Во время задачи я недоступен: принимай разумные решения, допущения перечисли в конце.',
        [('russian-output', 'llm', 2, 'file:docs/ideas.md',
          'The user wrote the request in Russian; the product context file is in English. PASS if the document prose, including section and field headings, is written in Russian (product names, fact IDs, law names and other proper nouns may stay as they are). FAIL if the document is mostly in English.')]),
}
DEFAULT_PROMPT = 'Using the product context in `growth-context.md`, give 3-5 growth hypotheses for the next two months. Save them to `docs/ideas.md`. I am unavailable during the task: make reasonable decisions and list assumptions at the end.'

for entry in os.listdir(OUT) if os.path.isdir(OUT) else []:
    if entry != 'results':
        shutil.rmtree(os.path.join(OUT, entry))
for name, (ctx, prompt, graders) in CASES.items():
    d = os.path.join(OUT, name); os.makedirs(os.path.join(d, 'graders'))
    allowed = '[Read, Glob, Grep, Skill, Write, Edit]'
    open(os.path.join(d, 'prompt.md'), 'w').write(f'---\nmax_turns: 40\ntimeout_seconds: 900\nallowed_tools: {allowed}\ntags: [growth-ideas]\n---\n{prompt or DEFAULT_PROMPT}\n')
    if ctx:
        open(os.path.join(d, 'case.yaml'), 'w').write(f'schema_version: "1.1"\nname: {name}\ncontext:\n  scaffold_script: scaffold.sh\n')
        open(os.path.join(d, 'scaffold.sh'), 'w').write("#!/bin/bash\nset -euo pipefail\nmkdir -p docs\ncat > growth-context.md <<'CTX'\n" + ctx + "CTX\n")
        os.chmod(os.path.join(d, 'scaffold.sh'), 0o755)
    for gname, gtype, w, target, body in graders:
        if gtype == 'regex':
            front = f"type: regex\ntarget: {{ source: file, path: {target.split(':', 1)[1]} }}\npattern: '{body}'\nflags: i\nweight: {w}\narm: both"
            open(os.path.join(d, 'graders', gname + '.md'), 'w').write(f'---\n{front}\n---\n')
        else:
            focus = 'last_message' if target == 'last_message' else f"{{ source: file, path: {target.split(':', 1)[1]} }}"
            open(os.path.join(d, 'graders', gname + '.md'), 'w').write(f'---\ntype: llm\nfocus: {focus}\nweight: {w}\narm: both\n---\n{body}\n')
print('cases:', sorted(CASES))
