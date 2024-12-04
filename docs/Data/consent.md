---
title: Accounts
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
Consent is a fundamental component of the Basiq Platform **for all data sharing**. The consent object describes the consent requested from a consumer to access specific data sets, and includes the purpose and duration of the consent. 

[block:parameters]
{
  "data": {
    "h-0": "Component",
    "h-1": "Relationship",
    "0-0": "Consent policy",
    "0-1": "The consent policy is a pre-defined set of requirements that a partner configures for their specific application (use case). The policy identifies all of the consents that need to be acquired from the user, and identifies the requirements for each one e.g. the duration of how long a consent should be held for.\n\nThe consent policy enables partners to configure a consent policy per application. This consent policy will then be used to render the consent capture UI and capture additional configuration from the user which will be stored as the “user consent” object. \n\nFor each application, a partner will configure their [consent policy](https://api.basiq.io/docs/dash-configuration#1-configuring-your-applications-consent-policy) according to their data requirements. This consent policy provides a framework for:\n\n- *Data Collection*  - defines that data they wish to seek permission to e.g. “accounts”.\n-  *Data Retention* - whether the partner would like to retain this data (upon consent expiry) in an anonymised format.\n- *Data Usage* - the intention of how the users data will be used.\n- *Data Sharing* - list of 3rd parties that the data will be shared with. \n- How the consent flow is rendered via the Basiq Consent UI\n- The underlying governance around access, storage, and removal of data\n\nConsent policies are versioned, and only one version may be active at any time, so any changes to a consent policy will only be applied to new user consents. User consents created under previous policies will remain valid, however for new policy changes to take effect they will need to re-consent.\n\nRead more about [Consent Scopes](doc:consent-scopes)",
    "1-0": "Consent UI",
    "2-0": "User consent",
    "1-1": "The [Basiq Consent UI](https://api.basiq.io/docs/consent-ui) renders the defined application consent policy within a flow that aligns with the rules and requirements proposed by the CDR, and the latest CX Guidelines.\n\nPartners will need to redirect their user to the Consent UI to record their consent and connect their institutions. It supports both DDC and CDR flows.",
    "2-1": "When a user consents via the Consent UI, a snapshot of that consent is stored against their user object. This will determine how their data is managed, and for how long.\n\nUser consent will also contain a list of all related Data Holder arrangements."
  },
  "cols": 2,
  "rows": 3
}
[/block]
## Changing the Consent Policy

It is worth noting that whilst multiple consent policies may exist for a single application, only one Policy can be “current“. 

This can occur when a partner configures an application to capture for example “account details” only, then later due to added functionality within their app changes the consent policy to also acquire “transactions”. In this example, a the application will have 2 consent policies of which one will be the latest (the one that needs accounts and transactions). 

If a consent policy is amended, it will result in multiple policies against that application. This could, for example, lead to scenarios where legacy users have selected to share only accounts, and new users have consented to share both accounts and transactions.

A Partner will need to manage this scenario and decide whether to toggle off the new features for existing users or to ask their existing users to move across to the new consent policy to enable these consumers to benefit from the latest capabilities they are offering, this may (dependent on the type of change) require each consumer to go through the full consent flow.