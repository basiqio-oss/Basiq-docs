---
title: May'26 - Basiq Consent UI Improvement
author: amalik@cuscal.com.au
hidden: false
published_at: '2026-05-14T02:10:02.116Z'
type: added
---
We’ve introduced a new Customizer option called **Skip error screen**.

This allows partners to bypass Consent UI error screens entirely and redirect users directly back to their application when a connection fails or when any error is returned from the data holder. In these cases, partners can handle the error using the jobs endpoint and related error responses.

This is particularly useful for partners who want full control over the failure experience. Instead of users being shown a generic Consent UI error screen, they remain within the partner’s flow and can present a consistent, branded experience even when something goes wrong.

**Supported scenarios:**

* DCR errors
* Connection failures returned during verify-credentials flows

**Additional details:**

* Supported for WEB and Open Banking flows
* Requires Redirect URL configuration
* Independent from existing Skip success screen and Allow multiple connections options
* Error information remains available through existing jobs endpoint responses

**Documentation:**

[Consent UI Customisation](https://api.basiq.io/docs/consent-ui-customisation)

[Customise UI](https://api.basiq.io/docs/basiq-customise-ui)