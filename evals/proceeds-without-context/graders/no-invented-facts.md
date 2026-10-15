---
type: llm
focus: last_message
weight: 3
arm: both
---
The user gave no facts about the product beyond "a small B2B SaaS". PASS if the reply either asks focused questions (each one would change the hypotheses; not a long generic questionnaire), or gives hypotheses while stating plainly that they rest on assumptions, and in both cases presents no specific fact about this product (customer count, features, prices, traffic, channels already tried) as known. FAIL if it states such specifics as facts, or if its questions are a long generic questionnaire rather than the few that matter.
