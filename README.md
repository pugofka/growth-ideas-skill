# growth-ideas

A Claude Code skill that generates evidence-grounded growth hypotheses for a B2B product. You get a few ideas the owner can test within two weeks, not a long backlog.

Every hypothesis is grounded in a product context file. It cites the facts it relies on, respects what the owner has already rejected or approved, and comes with the cheapest test, a measurement window that fits the sales cycle, and a kill criterion. There is no target number of ideas: only the ones that pass the filter make it into the output.

## Why

Asked for "growth ideas", a model without context confidently suggests things that do not fit the business:
- tests on a customer base that does not exist;
- pivots;
- a "free audit" that needs the client's data;
- features the product already has;
- a head-on "switch from the market leader" campaign with no feature parity behind it.

This skill makes the model ask for context first. It then reasons from facts and filters out ideas that break the owner's constraints.

## What it does

1. **Context first.** Reads `growth-context.md`, a file of numbered facts, red lines, and lists of what was already tried or approved. If the file is missing or key sections are empty, the skill asks for them instead of guessing.
2. **Market.** Finds where the product sells and adapts channels, search engines, and legal checks to that market.
3. **Scope.** Offers the directions that follow from the facts: channels, website and product, marketplaces, B2B partners, retention. Then asks which ones to cover.
4. **Customer job (JTBD).** Works out what triggers the search, how customers solve the problem today, and what scares them.
5. **Opportunity tree, then an asset pass.** A second, independent pass goes through existing assets: content, customers, adjacent products, directories. It catches obvious moves the first pass misses.
6. **Filtering.** Drops repeats of rejected or approved ideas, red-line violations, ideas that rely on missing resources or invented numbers, and absurd leader-switch campaigns. Hygiene fixes go to a separate "Step 0".
7. **Hypotheses.** Each one includes: insight with fact IDs, mechanism, first step this week, metric and threshold, cheapest test, how it fails, outcomes (confirmed / refuted / not enough data), and kill criterion. The measurement window must fit the trial length or sales cycle; otherwise a leading indicator is used. Not enough data is not treated as a refutation.
8. **Output in two blocks by default.** A: channels and company. B: website and product improvements that affect sales. No fixed number of hypotheses — the list is never padded. After them come Step 0 (hygiene) and a list of assumptions to check.

**Grounding rule.** Every material claim about the product, site, customers, or competitors cites a fact that supports it or is marked as an assumption. "The context does not say" is not turned into "there is none".

The skill replies in the user's language.

**Local market.** Channels and legal checks follow the product's market from the context. For Russia there is a bundled reference ([`references/ru-market.md`](skills/growth-ideas/references/ru-market.md)): Yandex and Google, local channels, ad marking for online placements (erid; not required for email and push mailings), consent for promotional messages, personal data law (152-FZ), seasonality. For other markets the skill uses that market's channels and lists legal requirements as items to verify, without asserting specific rules.

## Install

As a Claude Code plugin:

```
claude plugin marketplace add pugofka/growth-ideas-skill
claude plugin install growth-ideas@pugofka
```

Or with the [skills](https://github.com/vercel-labs/skills) CLI:

```
npx skills add pugofka/growth-ideas-skill
```

## Usage

1. Copy [`skills/growth-ideas/templates/growth-context.md`](skills/growth-ideas/templates/growth-context.md) to your project root and fill it in. Give every fact an ID (F1, F2…). The sections "Market", "Red lines" and "Already tried / rejected" matter most.
2. Ask Claude something like:

   > Using `growth-context.md`, give me growth hypotheses for the next two months.

   You can also invoke the skill directly: `/growth-ideas:growth-ideas` when installed as a plugin, or `/growth-ideas` when installed with the skills CLI.

## Evals

`evals/` contains 12 cases on fictional products. Each case checks one behaviour:

| Case | Checks |
|---|---|
| `asks-for-context-when-missing` | Asks for context instead of guessing |
| `respects-rejected-and-approved` | Does not repeat rejected or approved ideas |
| `no-invented-numbers` | No invented traffic, conversion, or market numbers |
| `no-fake-ids-or-placeholders` | No nonexistent fact IDs, no "TBD" / "TODO" placeholders |
| `feasible-timeline` | Metrics are observable within their window given the sales cycle; "not enough data" is separate from refutation |
| `hygiene-is-step-zero` | Fixes are separated from growth hypotheses |
| `no-absurd-leader-switch` | No "switch from the leader" without parity |
| `company-voice` | Client-facing copy speaks as "we" |
| `proactive-site-block` | Separate block of website and product improvements |
| `russian-market-compliance` | Personal data consent, ad marking for placements, consent for messages; no erid for email/push |
| `local-market-not-russia` | A product sold in Germany gets no Russia-specific channels or rules |
| `replies-in-user-language` | Russian request → Russian output |

Run them with and without the skill:

```
claude plugin eval . --runs 3 -j 6 --ablation with-without --scaffold \
  --judge-model claude-opus-5-5 --trust-plugin --no-publish --allow-tools Write Edit
```

Last run, 2026-10-15, Claude Opus 5.5 with an Opus 5.5 judge, 3 runs per case and arm:
- with the skill, every check passes in all 3 runs;
- without it, 5 cases fail in all 3 runs: asking for context, feasible timeline, leader switch, site block, compliance;
- in the other 7 cases the skill and the plain model are equal;
- mean Δ +0.42.

**Not covered by evals.** The skill also requires a concrete cheapest test and kill criterion for every hypothesis, fact citations that match what the fact says, and no invented qualitative claims. LLM-judge checks for these gave different verdicts across runs on the same kind of output, so they were removed rather than reported as passing. The scope question (Step 0b) is not covered either: `claude plugin eval` runs headless, and the question tool is not available there.

The cases are generated by `tools/gen-evals.py`. Edit the generator, not the case files.

## License

MIT
