---
title: Redirect to App
deprecated: false
hidden: true
metadata:
  robots: index
---
## Overview

Redirect to App (R2A) is a Consumer Data Right (CDR) authentication method. It lets a consumer sign in with their bank's own mobile app instead of entering details on a web page.

When a consumer connects their bank from your mobile app and their bank supports R2A, the bank's app opens. The consumer signs in and approves data sharing there, then returns to your app.

All Data Holders and Data Recipients must support R2A from **10 May 2027.** Some banks may turn it on earlier, so we recommend preparing your app now.

Official reference: [CDR CX Standards – Redirect to App](https://cx.dsb.gov.au/authenticate/redirect-to-app)

## What changes for your app

Today, the whole bank journey can run inside a single WebView in your app.

With R2A, the journey moves between two apps:

1. The consumer starts in your app and opens the Basiq Consent UI.
2. They choose their bank. The phone's operating system opens the bank's app, and your app moves to the background.
3. The consumer signs in and approves data sharing in the bank's app.
4. The consumer is sent back to your app through your registered redirect URL.

Your app needs to:

- let the consumer leave your app and come back again
- reopen in the right place when the redirect arrives
- handle cases where the consumer doesn't come back

<br />

<br />
