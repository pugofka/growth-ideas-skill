---
name: growth-ideas
description: Generates evidence-grounded growth hypotheses for a B2B product at the intersection of product and marketing — not backlog filler, but 3–5 ideas that can go into a test within 2 weeks. Works from a product context file (facts, constraints, what was already rejected or approved), follows the chain "customer job → opportunities → hypotheses → how it fails", and accounts for the Russian market. Use when asked for growth ideas, test hypotheses, "how to get more customers / leads / sales", or prioritization of growth ideas. Гипотезы роста, идеи роста, как получить больше клиентов, заявок, продаж.
---

# Growth hypotheses

The goal is a few strong, testable ideas the owner will actually launch. The number of ideas is secondary. Repeating the obvious, inventing numbers, or proposing ideas that contradict the owner's constraints means the task failed.

**Language.** Reply in the user's language. Translate the section and field names below into it; keep the structure.

## Step 0. Product context — do not start without it

Find the product context file (usually `growth-context.md` in the project root, or the path the user gave). The format is in `templates/growth-context.md`.

If there is no file, or the "Customers", "Red lines", or "Already tried / rejected" sections are empty, **stop and ask questions**, offering to fill in the template. Without these sections the model confidently proposes what the owner rejected long ago: tests on a customer base that does not exist; pivots; a "free audit" that depends on access to the client's data; things the product already has.

Always read the Russian market reference (`references/ru-market.md`).

## Step 0b. Clarify the scope if the user did not set it

Before generating, offer what you can work through based on the facts and ask whether they want everything or something specific. One question with options (through the question tool if one is available), for example:
- growth through channels and the company (acquisition, partners, community, offers);
- website and product improvements that affect sales;
- marketplaces and retail;
- B2B: partners, dealers, professional customers;
- retention and repeat sales (CRM, email, app).

Show only the directions that actually follow from the product facts; put the recommended option first. If the user answers, work within their scope. If no one can answer (background run, the user said they are unavailable), use the default structure from Step 5 and state in one line at the top of the reply which scope you chose and what else can be worked through separately.

## Step 1. The customer's job (Jobs-To-Be-Done)

From the facts in the context, not from general knowledge:
- **What job is the product "hired" to do?** Phrase it as the customer's progress: "when …, I want …, so that …".
- **What triggers the search** — the event after which a person starts looking for a solution (moving, changing a contractor, the season, a failing metric, a new law).
- **How they solve it now** — competitors, manual work, spreadsheets, "nothing". "Nothing" is the most common alternative in small B2B.
- **What scares them** — the anxieties that break the purchase (data access, timelines, complexity, cost of a mistake).

Cite a fact ID for every conclusion. Mark anything not in the facts as an "assumption".

## Step 2. Opportunity tree

Goal (the owner's metric) → opportunities (unmet needs and anxieties from Step 1) → solution options. Look for **opportunities that use assets the owner already has**: the same team's adjacent products, existing customers and case studies, search visibility, partners, plans already in progress. The strongest ideas usually sit where two assets meet.

Spread the options across levers: acquisition, activation, retention, monetization, referral. No more than two options per lever.

## Step 2b. Second pass — straight from the assets

Separately from Steps 1–2, without looking at their output, go through each asset in the context and ask: "how exactly can this asset bring in customers in the next 2 months?"
- **Content and visibility** (blog, pages, search rankings) — does the traffic and content that already exists turn into leads; where is the gap between what people read and what is sold.
- **Customers and case studies** — repeat sales and upsells to current customers, referrals, updating and publishing case studies.
- **Adjacent products and partners** — cross-selling, joint offers, shared channels.
- **Visibility in directories, ratings, and marketplaces** — where the buyer has already put demand into words.

This pass catches obvious strong moves that the method in Steps 1–2 often misses while chasing something new. Merge the candidates from both passes, remove duplicates by meaning, and only then move to filtering.

## Step 3. Filtering

Drop an option if:
- it repeats "already rejected" or "already approved / in progress" (by meaning, not wording);
- it crosses a red line (a pivot, large new infrastructure, owner's manual work beyond the time budget);
- it needs a resource the facts say does not exist (a large customer base, traffic, client data);
- it rests on numbers that are not in the facts;
- it is hygiene (fix tracking, remove an error on the site) — move it to "Step 0 for the owner", not into the hypotheses;
- it is a head-on "switch to us from the market leader" when the facts show no feature parity and the products are in different price segments. Check: how will the leader's customer read it? If it looks like "a small product calling people away from a big one for no reason", do not propose it.

## Company voice

Write offers in the company's voice ("we", "our team"). Do not reveal the internal setup — which related company, team, or contractor does the work — unless the context explicitly allows it.

## Step 4. Hypotheses

For each remaining idea:

- **Name** — short, to the point.
- **Lever.**
- **Insight** — why it should work, citing fact IDs.
- **Mechanism** — what exactly changes and why the customer will behave differently.
- **First step this week** — who does what, how many owner hours. Hand off to AI or a contractor whatever can be handed off.
- **Metric and success threshold for 4–6 weeks** — mark the threshold as a proposal for the owner to approve if the context has no benchmarks.
- **Cheapest test** — the minimal version that already gives a signal (fake door, manual delivery, one email, one page).
- **How it fails** — the most likely reason it won't work.
- **Kill criterion** — when we stop.
- **Why it does not contradict the constraints.**

## Step 5. Prioritization and output

**The default output has two blocks**, even if no one asked for them:
- **A. Growth through channels and the company** — acquisition, partners, customers and community, pricing and offers.
- **B. Website and product improvements** that affect sales — conversion, average order value, customer journey, onboarding, product cards, cart, customer account. If the facts mention a website, a store, or a product interface, this block is mandatory: proactively look for friction in the customer journey based on the facts about the site and propose improvements, even if the user asked about "growth in general".

Run Steps 1–3 separately for each block rather than building one list and splitting it afterwards. If the user asks for other blocks or only one, follow their structure. Hygiene (tracking, technical errors) does not count toward the blocks — it goes into "Step 0".

Sort by "strength of the signal in the facts × impact on the goal ÷ owner's time". Deliver **3–5 hypotheses** (or as many as requested), plus a separate short "Step 0 for the owner" block — the hygiene without which the result cannot be measured. End with a list of assumptions worth checking.

Write for an owner who reads between meetings: concrete, no filler, no generic phrases like "improve the content" or "strengthen the brand".
