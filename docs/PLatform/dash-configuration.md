---
title: Dashboard
excerpt: >-
  Easily customise and fine-tune your application's settings using our
  user-friendly Dashboard configuration.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(54.55861070911722% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/x6T0LYwOQnJK5w5zRqN1?embed" title="Basiq - Dashboard Configuration" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

At Basiq, we've made it easy for partners to tailor and fine-tune their applications through our user-friendly Customise UI tab in the [dashboard](https://dashboard.basiq.io). Not only can partners set up and configure their applications here, but they can also get a live preview of the [Consent UI](doc:consent-ui) while making these changes. Let's walk through some of the key features:

## 1. Configuring your applications consent policy

By default, each application is assigned a Consent Policy when it is created, however this can be updated to more accurately reflect your applications needs by updating values including: 

* [Duration](doc:basiq-customise-ui)
* [Title & Subtitle](doc:basiq-customise-ui)
* [Purposes](doc:basiq-customise-ui)
* [Permissions](doc:consent-scopes)
* [Supporting parties](doc:basiq-customise-ui)

### Navigating Changes in Permissions

With the transition from dropdown to multiple choice for permissions, it's important to consider the impact on previously provided descriptions by partners. If partners haven't made any changes to the permissions section, the descriptions will remain unchanged from before the switch. However, once a partner modifies this section by selecting checkboxes, the descriptions will be updated to reflect the default values. This ensures consistency and accuracy in conveying the permissions granted within the consent policy.

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(54.55861070911722% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/8UrbIvcd9YSWNqUJPpkz?embed" title="Basiq - Dashboard" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

When defining these fields, you should keep in mind the rules and requirements as proposed by the CDR, and defined within the latest [CX Guidelines](https://consumerdatastandards.gov.au/guidelines-and-conventions/consumer-experience-guidelines/). 

## 2. Configuring your available institutions

As Open Banking becomes more widely adopted, the number of available institutions will increase, and in some cases there may be multiple ways to connect to a single institution - *such as ING Open Banking and ING Digital Data Capture*.

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(54.55861070911722% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/BXBlaLQWVjtSPwh0M9Ru?embed" title="Basiq - Customise UI " frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

 By selecting from the list of institutions, partners can configure which institutions they would like to present to their end users. *Note: The application dashboard Institution picker will only show Open Banking data sources for institutions if the partner is enabled. See[enablement](https://api.basiq.io/docs/open-banking#enabling-your-application-for-open-banking) for more information.*

**E.g.** Partners may choose to exclude any that specifically relate to business banking as they are irrelevant for their use case, or to only have Open Banking supported institutions available. 

## 3. Add your own Branding in the Header Image

You can now add your own branding in the header image. This will be shown to your end users.

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(54.55861070911722% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/8JXqARrd3aYJ3ZdANYsm?embed" title="Basiq - Customise UI" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

## 4. Configuring any optional fields

There a number of other additional fields that partners can configure, depending on how they would like the Consent UI to behave for their end users, including 

* **Redirect URL:** Where your user will be redirected to when they have finished with their banking portal
* **Skip success page:** If you are looking to reduce the number of screens you may choose to skip the final "Successfully connected to..." page and instead redirect straight back to your own application 
* **Allow multiple connections:** If your end user should be able to connect more than one institution at a time
* **Retain data:** Partners should be aware that all data on Basiq is deleted upon expiration or revocation of consent. Partners may wish to keep a de-identified version of the data based on the retainData settings within Basiq customise UI. There may be circumstances where partners are subject to other legal obligations that necessitate the retention of data. These obligations could arise from laws related to financial record-keeping, anti-money laundering regulations, or other relevant legislation. Under these circumstances and based on independent legal advice partners might be able to retain the data beyond expiry date in accordance to relevant legislation.
