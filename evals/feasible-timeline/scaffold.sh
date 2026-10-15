#!/bin/bash
set -euo pipefail
mkdir -p docs
cat > growth-context.md <<'CTX'
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
- F10. New clinics get a 30-day free trial; from first contact to a paid subscription usually takes 6-10 weeks.
## Related assets
- F9. The same team runs a small IT-outsourcing agency that already maintains websites for 30 local medical businesses.
## Red lines
- No pivots, no taking payments, no medical advice. Owner time budget: 3 hours per week.
## Already tried / rejected — do not propose
- Cold calling clinics (too much owner time, no results).
- Free "practice audit" that requires access to patient data (blocked by clinics' privacy concerns).
## Already approved / in progress — do not propose again
- A referral discount for existing clinics.
CTX
