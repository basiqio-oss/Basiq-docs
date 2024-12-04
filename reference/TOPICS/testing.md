---
title: Testing
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
There’s nothing worse than developing against an API with crappy test data. We get that! This is why we have put a lot of effort into ensuring that our test data mimics real production data that your app will consume.

The test data that we provide (below) has been designed to mimic a real life user. This means that just a like a real user would spend and receive funds throughout the day - our test accounts have been designed to do the same thing. Therefore you should expect to see new transaction records being created throughout the day, and the account balances adjusted accordingly.

The transaction data is completely random to best replicate the type of data that you should expect to see for your own customers. 
[block:callout]
{
  "type": "warning",
  "body": "You can use our sandbox environment for free right now - just grab an API key to get started (via the [Developer Dashboard](https://dashboard.basiq.io/)). We recommend using our test bank `Hooli`.",
  "title": "Sandbox environment"
}
[/block]

**Note:** There is a limit of 500 for sandbox connections.  If you reach your limit and need to have this increased, feel free to reach out to support@basiq.io.
[block:parameters]
{
  "data": {
    "h-0": "loginId",
    "h-1": "password",
    "0-0": "Wentworth-Smith",
    "0-1": "whislter",
    "3-0": "gavinBelson",
    "3-1": "hooli2016",
    "4-0": "richard",
    "4-1": "tabsnotspaces",
    "1-0": "Whistler",
    "1-1": "ShowBox",
    "h-2": "",
    "0-2": "Happy path persona with steady income, mortgage, credit card  and predictable expenses",
    "1-2": "Persona with income, missing expenses, BNPL activity and balance going up over time",
    "3-2": "Standard",
    "4-2": "Standard",
    "5-0": "jared",
    "5-1": "django",
    "5-2": "Standard",
    "2-0": "Gilfoyle",
    "2-1": "PiedPiper",
    "2-2": "Persona with balances ranging between stable and diminishing over time",
    "6-0": "gavinBelson",
    "6-1": "hooli2016",
    "6-2": "HooliGov Bank (AU00004)"
  },
  "cols": 3,
  "rows": 7
}
[/block]
# Unhappy path test users
[block:callout]
{
  "type": "warning",
  "body": "The following users will *always* return the same errors at the same job step. We created them to ensure you could fully test the unhappy paths your user may encounter while connecting their accounts via DDC and handle them appropriately. See [here](ref:jobs) on how to best handle these scenarios.",
  "title": "Unhappy path test users"
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "loginID",
    "h-1": "password",
    "h-2": "Failure scenario",
    "0-0": "bighead",
    "0-1": "password",
    "0-2": "**Error:** `invalid-credentials`\n**Detail:** \"Account is locked\"",
    "2-0": "erlich",
    "2-1": "aviato",
    "2-2": "**Error:** `account-not-accessible-requires-user-action`\n**Detail:** \"An action is required from end-user before account details can be returned.\"",
    "4-0": "jianYang",
    "4-1": "nothotdog",
    "4-2": "**Error:** `service-unavailable`\n**Detail:** \"Service is currently unavailable. Please try again later.\""
  },
  "cols": 3,
  "rows": 5
}
[/block]
# MFA users 

We have two test banks to test MFA challenges 
- Pied Piper Bank: AU00002  (`mfa-challenge` *always*)
- Nucleus Bank: AU00003 (`mfa-challenge`* intermittent - 50/50*)
[block:parameters]
{
  "data": {
    "h-0": "loginId",
    "h-1": "password",
    "h-2": "mfaChallengeMethod",
    "h-3": "mfaChallengeInput",
    "0-0": "jared",
    "0-1": "django",
    "0-2": "token",
    "0-3": "[\"OTP Password\"]",
    "h-4": "mfaChallengeSolution",
    "0-4": "[\"1234\"]",
    "1-0": "richard",
    "1-1": "tabsnotspaces",
    "1-2": "token",
    "1-3": "[\"OTP Password\"]",
    "1-4": "[\"1234\"]",
    "2-0": "gavinBelson",
    "2-1": "hooli2016",
    "2-2": "security-questions",
    "2-3": "[\"What's your first company?\"]",
    "2-4": "[\"Hooli\"]",
    "3-0": "Gilfoyle",
    "3-1": "PiedPiper",
    "3-2": "security-questions",
    "3-3": "[\"What's your first company?\"]",
    "3-4": "[\"Hooli\"]",
    "4-0": "Whistler",
    "4-1": "ShowBox",
    "4-2": "security-questions",
    "4-3": "[\"What's your favourite company?\", \"What's the ID of this institution?\"]",
    "4-4": "[\"Basiq\", \"AU00000\"]",
    "5-0": "Wentworth-Smith",
    "5-1": "whislter",
    "5-2": "security-questions",
    "5-3": "[\"What's your favourite company?\", \"What's the ID of this institution?\"]",
    "5-4": "[\"Basiq\", \"AU00000\"]"
  },
  "cols": 5,
  "rows": 6
}
[/block]