# growth-ideas

An Agent Skill for Claude that turns what you know about a product or company — a full brief, a few notes, or just a brand name or website — into growth hypotheses you can start testing within two weeks.

It works the same way whether you know a lot or almost nothing:
- **Your own product** — it reads the notes and files you already have and asks only about what is missing.
- **A client you already work with** — the same, and it splits each first step into "we do" and "needed from the client".
- **A presale** — give it a name or a website; with web search on, it researches the company first and turns the gaps into questions for the first meeting.

## How it works

1. **Collects what is already there** — the conversation, attached files, files in the working folder — and researches the rest on the web: the company's site, competitors, directories, reviews. Every fact gets a source (you, a file, or a URL and date).
2. **Asks, then waits.** Only questions whose answers would change the ideas, each tied to an idea and with options to pick from; for money and people it offers two or three options with a stop-loss instead of asking for a number. If you say you are unavailable, it proceeds on labelled assumptions instead.
3. **Compares competitors** and the customer's main alternative (often doing nothing).
4. **Generates wide, then narrows.** It goes through channels and partners, the product itself, the site or app journey, price and packaging, and existing customers before dropping anything. Ideas that need development are allowed when they can be tested cheaply (a prototype, a fake door, a manual version).

## What you get

A short document:
1. **Summary** — the goal, the main bet, what to do first.
2. **What we found** — the main problems and opportunities, with facts.
3. **Table** — what each idea brings, what it needs, ICE and RICE scores (an input nobody has estimated stays "?" instead of a made-up number).
4. **Hypothesis cards** for ideas ready to test, grouped by angle, bold bets marked. Each has what we do, why (facts), what it brings with the calculation shown (each input marked as a fact or an assumption), what it needs, how we test it (cheapest test, metric and window, a stop condition with a number and a date), risks and legal points.
5. **Directions** — useful ideas not yet ready to test, each with the problem, the proposed solution, what is unknown and the next step. Uncertainty sets the next step; it does not drop the idea.
6. **Competitors** — a comparison table.
7. **Fix first** — tracking and site defects, kept apart from growth ideas.
8. **Questions** — for the owner or client; for a presale, the agenda of the first meeting.
9. **Appendix** — facts with sources, gaps, assumptions, dropped ideas.

As many hypotheses as pass the filter — no fixed number. Channels and legal checks follow the product's market; for Russia there is a reference with primary sources ([`references/markets/ru.md`](skills/growth-ideas/references/markets/ru.md)). It replies in your language.

## Install

**Claude Code**
```
claude plugin marketplace add pugofka/growth-ideas-skill
claude plugin install growth-ideas@pugofka
```
or with the [skills](https://github.com/vercel-labs/skills) CLI: `npx skills add pugofka/growth-ideas-skill`.

**Claude desktop — Cowork:** Customize → Plugins → Add marketplace → `pugofka/growth-ideas-skill`, then install `growth-ideas`.

**Claude desktop or claude.ai — chat:** download `growth-ideas.zip` from the latest release (or build it with `python3 tools/package.py`), then Customize → Skills → + → Create skill → Upload a skill. "Code execution and file creation" must be on (Settings → Capabilities).

**Team and Enterprise:** an organization Owner can add the skill once for everyone in Organization settings → Plugins & skills.

For research on a company you know little about, turn on web search.

## Usage

> We have a meeting next week with example.com. Research them and give growth hypotheses we could pitch.

> Here are our call notes and last quarter's numbers. Give growth hypotheses for the next two months.

## Development

- `python3 tools/check-skill.py` — checks the skill installs everywhere (description ≤ 200 characters, allowed frontmatter keys only, no Claude Code-only syntax) and that no eval fixture name has leaked into the skill text.
- `python3 tools/package.py` — runs the check and builds `dist/growth-ideas.zip` for upload.
- `python3 tools/gen-evals.py` — generates `evals/`: regression checks of form only, on fictional products. Edit the generator, not the case files. Run with `claude plugin eval . --runs 3 --ablation with-without --scaffold --trust-plugin --no-publish --allow-tools Write Edit`.

The evals show that the skill did not break, not that it is useful. Usefulness is judged by blind human ratings, by someone who knows the business, on products the skill was never tuned on, against plain Claude with the same output format.

**Status: experimental.** Blind ratings so far are mixed and small: ahead of plain Claude with the same format on one product, about even on three unfamiliar ones. It is not yet a proven tool. Never copy an eval case, a grader's wording or an example from it into the skill text.

## License

MIT
