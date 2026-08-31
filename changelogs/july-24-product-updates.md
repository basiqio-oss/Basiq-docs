---
title: July '24 - API & Consent UI Updates
author: Ashman Malik
hidden: false
published_at: '2024-07-26T00:27:25.217Z'
type: improved
---
We're thrilled to announce significant improvements to the Basiq API & Consent UI.

## New Features 🌟

### Consent History in Consent UI - Manage Action

On the Consent Management screen, you can now view the history of previously expired/revoked consents. Additionally, if you trigger `action=manage` with no active consent, a list of all previously revoked or expired consents will be displayed. You can read more [here](https://api.basiq.io/docs/consent-actions#consent-history).

<HTMLBlock>{`

<div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/RT2oVGipLNLvmhDwgksF?embed" title="action=manage | List of expired/revoked consents" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: dark;"></iframe></div>
`}</HTMLBlock>

<hr/>

## Enhancements ✨

### DH Authorization Errors in the Jobs Endpoint

**Enhanced Error Reporting**: If the DH authorization flow is not successfully completed by the user (e.g., user cancels the flow or encounters other DH-related issues), the error details are now exposed in the [jobs endpoint](https://api.basiq.io/reference/getjobs). This helps our partners better understand the issues.

<HTMLBlock>{`

<div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/8tdAfjKorvBPeH1JNTLX?embed" title="DH Auth Failed" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

<hr/>

### Basiq Connect (AuthUI)

* The length of the OTP code has been increased from 4 to 6 characters to enhance security.
* The [@basiq/connect-auth NPM package](https://www.npmjs.com/package/@basiq/connect-auth) has been updated to [version 1.1.0](https://www.npmjs.com/package/@basiq/connect-auth).

<HTMLBlock>{`

<div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/DhU1AMDeKC4f6PxNmJcP?embed" title="Basiq | OTP " frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

Read more [here](https://api.basiq.io/reference/authlinks).

<hr/>

### ConsentUI - Trusted Adviser

We have updated the appearance of the Trusted Adviser (TA) banner and popup for a more streamlined and user-friendly experience. Additionally, we have added a TA disclaimer message above the consent confirmation button to provide clearer information and improve the overall transparency of the consent process. You can read more [here](https://api.basiq.io/docs/trusted-advisor#consentui---trusted-adviser).

<HTMLBlock>{`

<div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/5FZJ6bqKc5r5aqotc60W" title="Trusted Advisor Model Demo" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: dark;"></iframe></div>
`}</HTMLBlock>

<hr/>

## Stay Updated :loudspeaker:

<HTMLBlock>{`<a href="https://api.basiq.io/changelog.rss" target="_blank"> <img src="https://img.shields.io/badge/RSS-Subscribe-orange?style=for-the-badge" alt="RSS Subscribe"> </a>`}</HTMLBlock>

If you have any questions or need further assistance, don't hesitate to reach out to our [support team](https://basiq.atlassian.net/servicedesk/customer/portal/3). <hr/>