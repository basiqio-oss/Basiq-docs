---
title: Nov'26 - Account Identity Verification
author: Ashman Malik
hidden: true
published_at: '2026-11-20T02:19:29.576Z'
type: added
---
We’ve added **Account Identity Verification** to the Insights API. Check a supplied BSB and account number against accounts shared under a customer’s consent and retrieve the consenting customer’s identity.

Use the existing **POST /insights** endpoint with the new **ACCOUNT_IDENTITY_VERIFICATION** insight type no new endpoint to integrate.

<Cards>
  <Card title="Verify an Account" href="https://api.basiq.io/reference/createinsight" icon="fa-shield-check">
    Submit a BSB and account number to check for a match against accounts shared under the customer’s consent.
  </Card>

  <Card title="Retrieve Identity Information" href="https://api.basiq.io/reference/createinsight" icon="fa-user-check">
    A match returns the identity associated with the matched connection. No match returns all identities available under the consent.
  </Card>

  <Card title="API Reference" href="https://api.basiq.io/reference/createinsight" icon="fa-code">
    Explore the request format, response details and integration requirements from [here](https://api.basiq.io/reference/createinsight).
  </Card>
</Cards>

### Getting started

- Supply **one user** per request.
- Provide the **BSB and account number combined** in `data.accountNumber`.

![](https://files.readme.io/88f1e30b0fbad6ac15c643409c084a6d4f9179bbae6f57d1ecbf1d557be2a343-Screenshot_2026-11-20_at_12.27.17.png)

- Ensure the consent policy includes **account.identity.verification**.

![Basiq Dashboard Customiser](https://files.readme.io/e03902d6d3685340902038e384a19841ce8e393cec314853e45b6443c5e8c7a6-Screenshot_2026-11-20_at_12.25.31.png)

For questions about this update, please contact Basiq Support.