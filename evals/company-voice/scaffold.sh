#!/bin/bash
set -euo pipefail
mkdir -p docs
cat > growth-context.md <<'CTX'
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
CTX
