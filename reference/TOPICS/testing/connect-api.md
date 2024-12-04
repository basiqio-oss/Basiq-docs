---
title: Connect API
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
The test data that we provide for the Connect API service (below) has been designed to mimic a real life user. This means that just a like a real user would spend and receive funds throughout the day - our test accounts have been designed to do the same thing. Therefore you should expect to see new transaction records being created throughout the day, and the account balances adjusted accordingly.

This should give you a good feel for the type of data that you should expect to see for your own customers. The transaction data is completely random, and even we are sometimes surprised by transactions that appear :-)
[block:callout]
{
  "type": "warning",
  "body": "You can use our sandbox environment for free right now - just grab an API key to get started (via the [Developer Dashboard](https://dashboard.basiq.io/))."
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "Ensure that you pass the institution code AU00000 when using the test accounts. Data for sandbox accounts is updated daily/weekly/monthly to provide realistic data for faster integration."
}
[/block]

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
    "h-2": "great for...",
    "0-2": "Connect and Affordability - happy path persona with steady income, mortgage, credit card  and predictable expenses",
    "1-2": "Connect and Affordability - persona with income, missing expenses, BNPL activity and balance going up over time",
    "3-2": "Connect",
    "4-2": "Connect",
    "5-0": "jared",
    "5-1": "django",
    "5-2": "Connect",
    "2-0": "Gilfoyle",
    "2-1": "PiedPiper",
    "2-2": "**new** Connect and Affordability - persona with balances ranging between stable and diminishing over time"
  },
  "cols": 3,
  "rows": 6
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
    "h-4": "mfaChallengeSolution",
    "0-0": "jared",
    "0-1": "django",
    "0-2": "token",
    "0-3": "[\"OTP Password\"]",
    "0-4": "[\"1234\"]",
    "1-0": "richard",
    "1-1": "tabsnotspaces",
    "1-2": "token",
    "1-3": "[\"OTP Password\"]",
    "1-4": "[\"1234\"]",
    "2-0": "gavinBelson",
    "2-1": "hooli2016",
    "2-2": "security-questions",
    "2-3": "[\"What's your first company?\"",
    "2-4": "[\"Hooli\"]",
    "3-0": "Gilfoyle",
    "3-1": "PiedPiper",
    "3-2": "security-questions",
    "3-3": "[\"What's your first company?\"]",
    "3-4": "[\"Hooli\"]",
    "4-0": "Whistler",
    "4-1": "ShowBox",
    "4-2": "security-questions",
    "5-2": "security-questions",
    "4-3": "[\"What's your favourite company?\", \"What's the ID of this institution?\"]",
    "5-3": "[\"What's your favourite company?\", \"What's the ID of this institution?\"]",
    "4-4": "[\"Basiq\", \"AU00000\"]",
    "5-4": "[\"Basiq\", \"AU00000\"]",
    "5-0": "Wentworth-Smith",
    "5-1": "whislter"
  },
  "cols": 5,
  "rows": 6
}
[/block]
# Unhappy path test users


[block:callout]
{
  "type": "warning",
  "body": "The following users will *always* return the same errors at the same job step. We created them to ensure you could fully test the unhappy paths your user may encounter while connecting their accounts and handle them appropriately. See [here](#handling-failed-jobs) on how to best handle these scenarios.",
  "title": ""
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

[block:callout]
{
  "type": "info",
  "title": "Whistler login - sandbox data",
  "body": "This user in sandbox has examples of the following:\n* Regular income over the last 13 months that shows some instability, e.g. some time spent as a casual worker, which then produces a stability score of < 0.8, and a more varied income/month graph\n* Gambling expenditure \n* BNPL activity\n* Higher than expected expenditure in some categories e.g. alchohol"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "POST /users/ea3a81/connections HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN                                           \nContent-Type: application/json\n\n{\n \"loginId\": \"Wentworth-Smith\",\n \"password\": \"whislter\",\n \"institution\":{\n   \"id\":\"AU00000\"\n }\n}",
      "language": "json",
      "name": "Create Connection (using test account)"
    }
  ],
  "sidebar": true
}
[/block]