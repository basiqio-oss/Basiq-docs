---
title: Consent
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

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Component
      </th>

      <th style={{ textAlign: "left" }}>
        Relationship
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Consent policy
      </td>

      <td style={{ textAlign: "left" }}>
        The consent policy is a pre-defined set of requirements that a partner configures for their specific application (use case). The policy identifies all of the consents that need to be acquired from the user, and identifies the requirements for each one e.g. the duration of how long a consent should be held for.

        The consent policy enables partners to configure a consent policy per application. This consent policy will then be used to render the consent capture UI and capture additional configuration from the user which will be stored as the “user consent” object. 

        For each application, a partner will configure their [consent policy](https://api.basiq.io/v3.0/reference/consent-policy) according to their data requirements. This consent policy provides a framework for:

        * *Data Collection*  - defines that data they wish to seek permission to e.g. “accounts”.
        * *Data Retention* - whether the partner would like to retain this data (upon consent expiry) in an anonymised format.
        * *Data Usage* - the intention of how the users data will be used.
        * *Data Sharing* - list of 3rd parties that the data will be shared with. 
        * How the consent flow is rendered via the Basiq Consent UI
        * The underlying governance around access, storage, and removal of data

        Consent policies are versioned, and only one version may be active at any time, so any changes to a consent policy will only be applied to new user consents. User consents created under previous policies will remain valid, however for new policy changes to take effect they will need to re-consent.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Consent UI
      </td>

      <td style={{ textAlign: "left" }}>
        The [Basiq Consent UI](https://api.basiq.io/docs/consent-ui) renders the defined application consent policy within a flow that aligns with the rules and requirements proposed by the CDR, and the latest CX Guidelines.

        Partners will need to redirect their user to the Consent UI to record their consent and connect their institutions. It supports both DDC and CDR flows.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        User consent
      </td>

      <td style={{ textAlign: "left" }}>
        When a user consents via the Consent UI, a snapshot of that consent is stored against their user object. This will determine how their data is managed, and for how long.

        User consent will also contain a list of all related Data Holder arrangements.
      </td>
    </tr>
  </tbody>
</Table>

## Changing the Consent Policy

It is worth noting that whilst multiple consent policies may exist for a single application, only one Policy can be “current“. 

This can occur when a partner configures an application to capture for example “account details” only, then later due to added functionality within their app changes the consent policy to also acquire “transactions”. In this example, a the application will have 2 consent policies of which one will be the latest (the one that needs accounts and transactions). 

If a consent policy is amended, it will result in multiple policies against that application. This could, for example, lead to scenarios where legacy users have selected to share only accounts, and new users have consented to share both accounts and transactions.

A Partner will need to manage this scenario and decide whether to toggle off the new features for existing users or to ask their existing users to move across to the new consent policy to enable these consumers to benefit from the latest capabilities they are offering, this may (dependent on the type of change) require each consumer to go through the full consent flow.
