---
title: Redirect to App
deprecated: false
hidden: false
metadata:
  robots: noindex
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

## End-to-end flow

Your app → Basiq Consent UI → Bank selected
→ Bank app opens (your app in background)
→ Consumer authenticates + approves
→ Redirect URL → Your app resumes

The bank controls how sign-in and approval look and work, so the experience can differ between banks.

## Who does what

|                    | Responsibility                                                                                                                      |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| Bank (Data Holder) | Authenticates the consumer and records the approval                                                                                 |
| Basiq              | Runs the consent journey, starts the CDR request with the bank, manages the connection, and returns the result to your redirect URL |
| Your app           | Launches the Consent UI, receives the redirect, resumes the journey, and handles success, cancellation and failure                  |

Neither Basiq nor your app ever collects the consumer's bank username, password, PIN or other credentials.

## Returning the consumer to your app

Basiq sets up and manages the Redirect to App connection with each bank, including the redirect from the bank's app back to Basiq. You don't need to register anything with the bank for R2A.

When the journey ends, Basiq returns the consumer to the redirect URL registered on your Basiq application, the same as today. If your app already handles this redirect, it will keep working.

Each Basiq application has one registered redirect URL. If you offer both a web and a mobile journey, make sure that URL works for both. For example, use an HTTPS link that opens your app when it's installed and your website when it isn't.

## If the journey is interrupted

The consumer is outside your app while they're in the bank's app, so they may not finish the journey. Plan for these cases:

| Scenario                                               | What happens                                                                                  | What your app should do                                                                                      |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Consumer finishes in the bank app                      | The bank completes the approval and the consumer is returned to your registered redirect URL  | Read the result and continue the journey                                                                     |
| Consumer cancels in the bank app                       | The consumer is returned to your registered redirect URL with a cancelled or error result     | Show a clear message and offer to try again                                                                  |
| Consumer closes the bank app before finishing          | The bank app may not send a redirect. The consumer may need to go back to your app themselves | When your app returns to the foreground without a result, check the connection status and offer to try again |
| Consumer doesn't come back                             | The consent session expires after a time limit and the connection is not created              | Treat the attempt as incomplete and let the consumer start again                                             |
| Bank app not installed, or R2A not available           | The bank uses its web sign-in instead (Redirect to Web with one-time password)                | No change needed. Your app should support both experiences                                                   |
| The phone closes your app while it's in the background | The consumer returns through your registered redirect URL to a fresh app launch               | Save the journey state before handing off, so you can pick it up again                                       |

> **Key point:** Don't assume a redirect will always arrive. Your app should be able to recover when the consumer comes back without one.

## Do's and don'ts

### Do

- Make sure your registered redirect URL brings the consumer back into your app
- Save the journey state before the consumer leaves your app
- Handle success, cancellation, failure and "returned without a result"
- Support both the bank-app and web sign-in experiences

### Don't

- Assume every bank behaves the same way
- Leave the consumer on a blank or loading screen if no redirect arrives
