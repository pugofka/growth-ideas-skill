#!/bin/bash
set -euo pipefail
mkdir -p docs
mkdir -p notes
cat > notes/call-notes.md <<'CTX'
# Call notes — Tallyhop (internal)

- Tallyhop is a web app for independent bicycle repair shops in Poland: parts inventory, repair tickets, SMS-free email notifications to customers when a bike is ready.
- 52 shops pay a monthly subscription; most found us through a regional cycling trade fair in 2025.
- There is no integration with parts wholesalers yet; shops type in parts by hand. Owners mention it on almost every call.
- A shop usually decides within 2-3 weeks of a demo; there is a 14-day free trial.
- The website has a demo request form and a pricing page. Nobody tracks which page a demo request came from.
- Tried and stopped: paid search ads on generic keywords ("bike shop software") — too expensive for the budget; cold emails to shop owners — almost no replies.
- Already in progress: a referral discount for existing shops.
- The team: two founders and one developer. Founders can spend about 4 hours a week on growth.
CTX
