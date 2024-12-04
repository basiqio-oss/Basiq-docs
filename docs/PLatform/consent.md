---
title: Consent Management
excerpt: >-
  For a data recipient (Basiq) to collect, use and disclose CDR data, they must
  have consent from the consumer to do so. For this reason, *partners wishing to
  access v3.0 of the Basiq API are required to use the Basiq Consent UI in their
  application.*
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
# Consent

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

        For each application, a partner will configure their [consent policy](https://api.basiq.io/docs/dash-configuration) according to their data requirements. This consent policy provides a framework for:  

        * *Data Collection*  - defines that data they wish to seek permission to e.g. “accounts”.
        * *Data Retention* -  Partners should be aware that all data on Basiq is deleted upon expiration or revocation of consent. Partners may wish to keep a de-identified version of the data based on the retainData settings within Basiq customise UI. There may be circumstances where partners are subject to other legal obligations that necessitate the retention of data. These obligations could arise from laws related to financial record-keeping, anti-money laundering regulations, or other relevant legislation. Under these circumstances and based on independent legal advice partners might be able to retain the data beyond expiry date in accordance to relevant legislation.
        * *Data Usage* - the intention of how the user's data will be used.
        * *Data Sharing* - list of 3rd parties that the data will be shared with.
        * How the consent flow is rendered via the Basiq Consent UI
        * The underlying governance around access, storage, and removal of dataConsent policies are versioned, and only one version may be active at any time, so any changes to a consent policy will only be applied to new user consents. User consents created under previous policies will remain valid, however for new policy changes to take effect they will need to re-consent.Read more about [Consent Scopes](https://api.basiq.io/docs/consent-scopes)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Consent UI
      </td>

      <td style={{ textAlign: "left" }}>
        The [Basiq Consent UI](https://api.basiq.io/docs/consent-ui-customisation) renders the defined application consent policy within a flow that aligns with the rules and requirements proposed by the CDR, and the latest CX Guidelines.  

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

## Consent UI

The Basiq Consent UI is designed to handle all of the complexity behind **CDR legislation**, **consent management**, and **CX guidelines**, so partners can fast track their access to Open Banking data, and focus on innovation. 

The Consent UI is driven by the application's own [Consent Policy](https://api.basiq.io/docs/basiq-customise-ui), which acts as a contract for end users to agree to before proceeding to connect their institutions.

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/Nbq3exhwkOepyigiXMbF?embed" title="Consent UI " frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

## Dynamic switching

The Consent UI focuses on providing a seamless user experience no matter the method of data retrieval. What this means, is that it can be used for both web, and Open Banking, connections. Consent applies to the application/user level, so all connections made under this will be handled the same way. The institutions presented to the user are decided by the partner and can be configured at any point via the [dashboard](https://api.basiq.io/docs/dash-configuration). Everything else is handled by the UI. 

## Implementation

The Consent UI is hosted by Basiq and accessed by passing a `CLIENT_SCOPE`. This token must be bound to the `userId` for security, preventing unauthorised consents:

```json URL
https://consent.basiq.io/home?token={{client_token_bound_to_userId}}
```

Access token and userId can be obtained through the Basiq API (See the [quick start guide](https://api.basiq.io/docs/navigating-the-dashboard)).
