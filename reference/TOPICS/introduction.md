---
title: Introduction
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
Basiq provides a collection of APIs to help you build powerful financial solutions for a wide range of use cases. The most common use cases are:

- **Personal Financial Management.** Enable your customers to aggregate all of their financial data in one place, identify expenses and gain valuable insight of their spending.

- **Wealth Management.** Gain valuable insights and a clearer understanding of your customers’ financial positions to customize advice, recommendations, and product offerings.

- **Risk Insights.** Gain real-time and comprehensive visibility of your customers' assets, income, non-credit payment patterns, and transactional details.

- **Cashflow Analysis.** Provide tools that analyze cash flow and forecast future expenses and income.

- **Account Summary.** Display the big picture with financial account data listed alongside balance information.

- **Account Verification.** Instantly verify account ownership and balances in real time to improve the user experience and mitigate fraud and risk.

- **Data Enhancement.** Gain greater financial insights around consumer spending patterns and trends with categorised and enriched transaction data.
[block:callout]
{
  "type": "warning",
  "body": "Basiq APIs are currently only available in Australia and New Zealand. We are working to make them available in other countries - so check back soon. Use this link to see a complete list of [supported financial institutions](http://docs.basiq.io/the-basiq-platform/supported-financial-institutions)."
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "https://au-api.basiq.io",
      "language": "json",
      "name": "Base API"
    }
  ],
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "/oauth2/token",
      "language": "json",
      "name": "Authentication"
    }
  ],
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "/connections\n/connections/:id\n/connections/:id/accounts\n/connections/:id/accounts/:id\n/connections/:id/transactions\n/connections/:id/transactions/:id\n/institutions\n/institutions/:id",
      "language": "json",
      "name": "Connect Resources"
    }
  ],
  "sidebar": true
}
[/block]