---
title: CDR Receipts
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: developer-tooling
      title: Developer tooling
---
## What are they?

A CDR receipt is a notification sent to a user who has consented to share their data via Open Banking with an application. It alerts the user of when consent was shared, who it was shared with and when it will expire. A user will receive multiple receipts over the life of their consent depending on events such as revoking consent, consent has expired, consent is current (sent every 90 days).

## Why they are required?

It is a CDR requirement that ADR’s notify their users of their consent in writing by means other than through the Consent UI. These notifications must be presented in the form of a CDR Receipt which can be sent either via email or SMS, and are triggered by multiple consent events:

- Created
- Updated
- Revoked or expired
- Consent is active/current - every 90 days from the day consent is collected

> 📘 Note: 
> 
> Users will receive notifications for the following cases only if an active CDR connection occurred:
> 
> - Consent Created
> - Consent Reminder
> - Consent Expiration
> - Consent Revocation

Click [here](https://www.legislation.gov.au/Series/F2020L00094) to view current CDR legislation requirements.

# Enablement

CDR receipts emails are enabled for all customers leveraging the Basiq platform to access CDR data. 

## Consent Revocation and Expiration

Consent revocation emails are sent only when the user has a CDR connection that was active at some point in time.

## Consent Active Reminder

A consent active reminder email will only be sent if the user has active CDR connections. 

## Consent Updated Email

Consent update emails are sent only if the user has an active CDR connection. 

See example below of what the different CDR receipts look like:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3668cad-receiptGIF.gif",
        "",
        ""
      ],
      "align": "center",
      "sizing": "50% "
    }
  ]
}
[/block]