# Russia: what is specific to this market

Load this only when the product sells in Russia, and take only what applies to the hypotheses at hand. It holds Russia-specific knowledge; the general rules (check the jurisdiction's law, check that a channel is available, no search volumes without data) are in SKILL.md.

**Keeping it current.** Every legal item below has a primary source and the month it was last checked. Laws here change often. If you have web access, re-open the source of every item that ends up in a hypothesis and state the date you checked it. Without web access, write "checked 2026-10, verify before launch" next to it. This is not legal advice: flag anything that decides whether a hypothesis is allowed for a lawyer to confirm.

## Search, analytics, local presence

- Two search engines matter: Yandex and Google. Demand and rankings differ between them, so a search hypothesis that covers only one is incomplete.
- Demand and query wording: Yandex Wordstat. Site data: Yandex Metrica (goals, traffic sources, session replay), Yandex Webmaster, Google Search Console. Without an export from them, give a list of queries to check instead of volumes.
- Local presence and reviews: Yandex Business / Yandex Maps and 2GIS.

## Channels commonly used

- Paid: Yandex Direct, VK Ads, Telegram Ads, sponsored posts in Telegram channels.
- Content and communities: Telegram channels, VK communities, Dzen; for IT and digital audiences, Habr and vc.ru.
- Small-business services: Avito Services and niche aggregators.
- For software and integrators: partner directories and app marketplaces of the platforms their customers already use.

## Law (checked 2026-10)

**Online ad marking — Federal Law 38-FZ "On Advertising", Article 18.1.** Advertising on the internet may be distributed only after an ad data operator (ОРД) assigns it an ad identifier (erid); the ad carries the label "реклама" and names the advertiser (parts 16–17); data goes to Roskomnadzor through the ad data operator. This covers paid and sponsored placements: Yandex Direct, VK Ads, Telegram Ads, sponsored posts in channels, bloggers, partner sites. A hypothesis with such a placement must include marking in its plan.
- Not needed for email, push, and messenger messages sent to specific users who gave prior consent; needed when a messenger is used to reach a wide audience (a public channel or chat) — Roskomnadzor FAQ, updated 2026-02-25.
- The Government order behind this exception (No. 1362-р) words it narrowly: advertising of the advertiser's **own** goods, sent by the advertiser itself or its group of companies. Mailing someone else's ads is not covered.
- SMS: no official position on marking was found. Mark it "verify".
- A separate 3% levy on internet advertising (Article 18.2, since 2025-04-01) is paid by ad distributors and ad system operators, not by the advertiser directly (except when contracting a foreign party). Whether platforms pass it on in prices is not stated in the law — check with the platform when costing a paid placement.

**Consent for promotional messages — 38-FZ, Article 18, part 1.** Advertising over telecom networks (email, SMS, messengers, calls) is allowed only with the recipient's prior consent; the sender must prove the consent and stop at the recipient's request. Automatic dialing and automatic mailing are prohibited (part 2).
- Sending one by one does not make it non-advertising: FAS clarifications of 2012-06-14 define advertising as non-personalised promotional information "even if it is sent to a specific mailing list". A standard offer, case study or promo sent individually to partners or existing clients still needs consent. Either plan for consent or flag the message for a lawyer.
- Whether these 2012 clarifications are still in force was not checked.

**Personal data — Federal Law 152-FZ.** Any hypothesis that collects contacts (forms, quizzes, lead magnets, sign-ups) needs all three:
- consent to processing, formed separately from other information and documents the person confirms or signs (Article 9 part 1, since 2025-09-01);
- a published personal data processing policy (Article 18.1 part 2);
- Russian citizens' data processed with databases located in Russia (Article 18 part 5, wording since 2025-07-01).

**Cookies and analytics.** 152-FZ has no explicit cookie rule. A regional Roskomnadzor office treated failing to inform users about cookies as a violation (2023). At minimum inform users; ask a lawyer whether consent is needed. A consent banner can hide part of the traffic from analytics — account for it when measuring a test.

**Where ads may not appear — 38-FZ, Article 5.** No ads on the resources of foreign agents (part 10.5), of undesirable, extremist or terrorist organisations or on restricted resources (part 10.7, since 2025-09-01), and no ads of tools for bypassing blocks (part 10.8). Check this when a hypothesis uses bloggers, channels or partner sites.

## The B2B buyer

- Trust signals that buyers check: the company's legal details on the site (INN / OGRN registration numbers), a clear contract, payment by invoice.

## Calendar

- Business activity drops during the New Year holidays (early January) and the May holidays. Do not launch or evaluate tests in those weeks.

## Sources

- 38-FZ, Article 18.1: https://www.consultant.ru/document/cons_doc_LAW_58968/2c4537e4796f6ff8b2736ed1b0d4fef08e14458e/
- 38-FZ, Article 18.2: https://www.consultant.ru/document/cons_doc_LAW_58968/f5499f6a99f4f1011e473eae3412f6c7f0262387/
- 38-FZ, Article 18: https://www.consultant.ru/document/cons_doc_LAW_58968/f892dec1383709792452f18d36e7043306e2be0a/
- 38-FZ, Article 5: https://www.consultant.ru/document/cons_doc_LAW_58968/f67f81c57fdcdacc2643d19d59369f7e185e1156/
- Roskomnadzor FAQ on internet ad records: https://rkn.gov.ru/treatments/chasto-zadavaemye-voprosy/p1575/
- Government order No. 1362-р: https://base.garant.ru/404773803/
- FAS clarifications of 2012-06-14: https://www.consultant.ru/document/cons_doc_LAW_137312/
- 152-FZ, Article 9: https://www.consultant.ru/document/cons_doc_LAW_61801/6c94959bc017ac80140621762d2ac59f6006b08c/
- 152-FZ, Article 18: https://www.consultant.ru/document/cons_doc_LAW_61801/cbf4e15b7c330f9372e876cdf2bc928bad7950ef/
- 152-FZ, Article 18.1: https://www.consultant.ru/document/cons_doc_LAW_61801/eeeebe22bf738fd65bb66b95cc278911ae2525ee/
- Roskomnadzor regional office on cookies (2023): https://29.rkn.gov.ru/news/news340514.htm
