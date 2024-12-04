---
title: Testing
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
There’s nothing worse than developing against an API with crappy test data. We get that! This is why we have put a lot of effort into ensuring that our test data mimics real production data that your app will consume.

The test data that we provide (below) has been designed to mimic a real life user. This means that just a like a real user would spend and receive funds throughout the day - our test accounts have been designed to do the same thing. Therefore you should expect to see new transaction records being created throughout the day, and the account balances adjusted accordingly.

The transaction data is completely random to best replicate the type of data that you should expect to see for your own customers. 

> 🚧 Sandbox environment
> 
> You can use our sandbox environment for free right now - just grab an API key to get started (via the [Developer Dashboard](https://dashboard.basiq.io/)). We recommend using our test bank `Hooli`.

**Note:** There is a limit of 500 for sandbox connections.  If you reach your limit and need to have this increased, feel free to reach out to [support@basiq.io](mailto:support@basiq.io).

> 📘 🆕 Initial Testing and Billing Policy
> 
> For initial testing, BASIQ services are available at no cost. This free access allows you to extensively test our platform's capabilities using our sandbox environment. However, once you transition from testing to becoming a paying customer, charges will apply for any users on your platform. This billing policy ensures that you have the opportunity to fully explore and understand the value of BASIQ services before any financial commitment is required. 
> 
> If you have questions about transitioning to a paying customer or about our billing structure, please contact our support team at [support@basiq.io](mailto:support@basiq.io).

<br />

[block:parameters]
{
  "data": {
    "h-0": "loginId",
    "h-1": "password",
    "h-2": "persona",
    "h-3": "suitable use case",
    "0-0": "Wentworth-Smith",
    "0-1": "whislter",
    "0-2": "This is a joint account.  \n  \n**income (transaction account)**: 2 sources of salary, monthly stable salary & fortnightly stable salary.  \n  \n**liabilities**: mortgage (mortgage account) and car loan (payments in the transaction account)  \n  \n**expenses**: has predictable expenses (credit-card account)",
    "0-3": "- Verify income\n- Review expenses\n- Affordability assessment\n- Assess liabilities\n- PFM\n- Access transaction data\n- Identify spending patterns\n- Personalised financial advice\n- Capture account details",
    "1-0": "Whistler",
    "1-1": "ShowBox",
    "1-2": "**income (transaction account)**: 1 source of salary, fortnightly salary  \n  \n**liabilities**: has BNPL (transaction account), no mortgage / personal loan  \n  \n**expenses**: no daily expenses  \n  \n**risk flags**: large amount of external transfer (debit to Jared)",
    "1-3": "- Verify income\n- Assess liabilities\n- Access transaction data\n- Personalised financial advice\n- Capture account details",
    "2-0": "Gilfoyle",
    "2-1": "PiedPiper",
    "2-2": "**income** (transaction account): stop fortnightly salary, unemployment benefits  \n  \n**liabilities**: increase in BNPL (transaction account)  \n  \n**expenses**: has predictable expenses (credit-card account)  \n  \n**risk flags**: late fee (credit-card account)",
    "2-3": "- Verify income\n- Assess liabilities\n- Expense check\n- Affordability assessment\n- Identify spending patterns\n- PFM\n- Analyse creditworthiness\n- Access transaction data\n- Personalised financial advice\n- Capture account details",
    "3-0": "gavinBelson",
    "3-1": "hooli2016",
    "3-2": "**income** (transaction account): 1 salary + 1 additional earning, increase monthly salary + extra income (tutoring weekly volatile)  \n  \n**liabilities**: personal loan (loan account)  \n  \n**expenses**: predictable expenses (credit-card account)  \n  \n- HooliGov Bank (AU00004)",
    "3-3": "- Verify income\n- Assess liabilities\n- Expense check\n- Affordability assessment\n- Identify spending patterns\n- PFM\n- Analyse creditworthiness\n- Access transaction data\n- Personalised financial advice\n- Capture account details",
    "4-0": "jared",
    "4-1": "django",
    "4-2": "**income** (transaction account): weekly volatile income from uber + credit transfers from Whistler  \n  \n**liabilities**: unshared mortgage account (payments in the transaction account), car loan (payments in the transaction account)  \n  \n**expenses**: predictable expenses (credit-card account)  \n  \n**assets**: term deposit",
    "4-3": "- Verify income\n- Assess liabilities\n- Expense check\n- Affordability assessment\n- Identify spending patterns\n- PFM\n- Analyse creditworthiness\n- Access transaction data\n- Personalised financial advice\n- Capture account details",
    "5-0": "richard",
    "5-1": "tabsnotspaces",
    "5-2": "**income** (transaction account): high stable fortnightly income, 2 rental incomes  \n  \n**liabilities**: 3 mortgages (1 shared mortgage account & 2 unshared mortgages), 2 car loans (payments in the transaction account), 4 credit cards (1 shared credit card account & 3 unshared credit card accounts)  \n  \n**expenses**: predictable expenses (credit-card account)",
    "5-3": "- Verify income\n- Assess liabilities\n- Expense check\n- Affordability assessment\n- Identify spending patterns\n- PFM\n- Analyse creditworthiness\n- Access transaction data\n- Personalised financial advice\n- Capture account details",
    "6-0": "laurieBream",
    "6-1": "business2024",
    "6-2": "Happy path persona with business fields and business consumer consent",
    "6-3": "- Business Consumer Consent",
    "7-0": "ashMann",
    "7-1": "hooli2024",
    "7-2": "**income** (transaction account): 1 salary monthly income, rental income  \n  \n**liabilities**: unshared credit card transactions (payments in the transaction account)  \n  \n**expenses**: predictable expenses (credit-card account), rental expense  \n  \n**risk flags**: gambling behaviours, cash withdrawal, crypto exchange",
    "7-3": "- Verify income\n- Assess liabilities\n- Expense check\n- Affordability assessment\n- Identify spending patterns\n- PFM\n- Analyse creditworthiness\n- Access transaction data\n- Personalised financial advice\n- Capture account details"
  },
  "cols": 4,
  "rows": 8,
  "align": [
    null,
    null,
    null,
    null
  ]
}
[/block]


# Unhappy path test users

> 🚧 Unhappy path test users
> 
> The following users will _always_ return the same errors at the same job step. We created them to ensure you could fully test the unhappy paths your user may encounter while connecting their accounts via DDC and handle them appropriately. See [here](ref:jobs) on how to best handle these scenarios.

[block:parameters]
{
  "data": {
    "h-0": "loginID",
    "h-1": "password",
    "h-2": "Failure scenario",
    "0-0": "bighead",
    "0-1": "password",
    "0-2": "**Error:** `invalid-credentials`  \n**Detail:** \"Account is locked\"",
    "1-0": "",
    "1-1": "",
    "1-2": "",
    "2-0": "erlich",
    "2-1": "aviato",
    "2-2": "**Error:** `account-not-accessible-requires-user-action`  \n**Detail:** \"An action is required from end-user before account details can be returned.\"",
    "3-0": "",
    "3-1": "",
    "3-2": "",
    "4-0": "jianYang",
    "4-1": "nothotdog",
    "4-2": "**Error:** `service-unavailable`  \n**Detail:** \"Service is currently unavailable. Please try again later.\""
  },
  "cols": 3,
  "rows": 5,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


# MFA users

We have two test banks to test MFA challenges 

- Pied Piper Bank  (`mfa-challenge` _always_)
- Nucleus Bank (`mfa-challenge`_ intermittent - 50/50_)

| loginId         | password      | mfaChallengeMethod | mfaChallengeInput                                                        | mfaChallengeSolution |
| :-------------- | :------------ | :----------------- | :----------------------------------------------------------------------- | :------------------- |
| jared           | django        | token              | ["OTP Password"]                                                         | ["1234"]             |
| richard         | tabsnotspaces | token              | ["OTP Password"]                                                         | ["1234"]             |
| gavinBelson     | hooli2016     | security-questions | ["What's your first company?"]                                           | ["Hooli"]            |
| Gilfoyle        | PiedPiper     | security-questions | ["What's your first company?"]                                           | ["Hooli"]            |
| Whistler        | ShowBox       | security-questions | ["What's your favourite company?", "What's the ID of this institution?"] | ["Basiq", "AU00000"] |
| Wentworth-Smith | whislter      | security-questions | ["What's your favourite company?", "What's the ID of this institution?"] | ["Basiq", "AU00000"] |