---
title: Oct'26 - Platform Improvements
author: Ashman Malik
hidden: false
metadata:
  robots: noindex
published_at: '2026-10-29T03:32:54.261Z'
type: added
---
## Basiq Dashboard

➕**&#x20;New: Filter accounts by status**

The **Accounts** page in the [Basiq Dashboard](https://dashboard.basiq.io/) now has an **Account status** filter, so you can hide closed accounts and work with large account lists more easily.

- **Available (open):** Shows only open accounts. This is the default.
- **Unavailable (closed):** Shows only closed accounts.
- **All accounts:** Shows both open and closed accounts.

The filters now run left to right in this order: **Institution, Connection status, Account type, Account status.**

Closed accounts aren't deleted. Their history is kept, and you can still view them with the filter.

## Basiq Customise UI

:heart_decoration:**&#x20;Improved: Input checks in the Customiser**

The Customiser now checks your values as you enter them, so a setting can't accidentally break your layout.

| Setting               | Minimum | Maximum |
| --------------------- | ------- | ------- |
| Heading size          | 8       | 128     |
| Paragraph size        | 8       | 128     |
| Border radius         | 0       | 100     |
| Wrapper desktop width | 320px   | 3840px  |

The Wrapper section now has a dividing line above it, which makes the Customiser easier to scan.

### 🛠️ Fixed: Colour fields accept only hex values

Colour fields now accept only hex values, such as #1A2B3C. Before this fix, an invalid value gave an unclear error message when you saved.

## Status page

➕**&#x20;New: Planned bank outages on the Basiq status page**

Planned full outages from major Australian banks now appear on [status.basiq.io](https://status.basiq.io/) as scheduled maintenance under CDR Connectors. This gives you time to warn your users and plan around potential downtime.

The outage monitoring automation now runs weekly across the **top 10 banks** and identifies planned full outages.

- Each notice is titled "\[Bank] Scheduled Outage". It includes the start and end times in UTC and AEST/AEDT.
- Subscribers get email alerts when maintenance starts and ends.
- Only **full outages** are posted. Partial outages aren't included.

To get these alerts, subscribe to **CDR Connectors** on [status.basiq.io](https://status.basiq.io/).

If you have any questions about these updates, please reach out to Basiq Support.