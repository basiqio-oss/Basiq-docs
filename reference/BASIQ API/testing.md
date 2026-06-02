---
title: Testing
excerpt: ''
deprecated: false
hidden: false
icon: fad fa-mobile
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
> You can use our sandbox environment for free right now - just grab an API key to get started (via the [Developer Dashboard](https://dashboard.basiq.io/)). We recommend using our test bank `Hooli` for openbanking flow.&#x20;

**Note:** There is a limit of 500 for sandbox connections.  If you reach your limit and need to have this increased, feel free to reach out to [support@basiq.io](mailto:support@basiq.io).

## 🆕 Open Banking Sandbox

The Open Banking (OB) sandbox introduces a deterministic consent-based flow using the Hooli OB institution (AU00000).

This mode is different from the standard sandbox test users. It simulates a full Data Holder consent lifecycle including authorization, re-authorization, refresh, and revocation.

### Key Differences (OB Sandbox vs Standard Sandbox)

- Uses a single institution: Hooli OB (AU00000)
- Consent-based flow is required before accessing data
- Deterministic login credentials are used for authorization
- Data access depends on consented accounts
- Supports full consent lifecycle (authorize, extend, refresh, revoke)

### Getting Started

Follow these steps to use the Open Banking sandbox:

#### Step 1: Enable Open Banking

Set institution method for **Hooli OB (AU00000)** to `open-banking` in the Dashboard Customizer UI, and use the following credentials.&#x20;

<HTMLBlock>{`
<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(62.793% + 41px); height: 0px; width: 100%;"><iframe src="https://demo.arcade.software/1QEVhWrUeCjVXe0PHF8r?embed&embed_mobile=tab&embed_desktop=inline" title="How to create a great Arcade for new features" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->
`}</HTMLBlock>

| Member Number | OTP    | Institution                                  |
| ------------- | ------ | -------------------------------------------- |
| 374829        | 227470 | **Hooli OB (AU00000) -&#x20;**`open-banking` |

> 📘 Initial Testing and Billing Policy
>
> For initial testing, BASIQ services are available at no cost. This free access allows you to extensively test our platform's capabilities using our sandbox environment. However, once you transition from testing to becoming a paying customer, charges will apply for any users on your platform. This billing policy ensures that you have the opportunity to fully explore and understand the value of BASIQ services before any financial commitment is required.
>
> If you have questions about transitioning to a paying customer or about our billing structure, please contact our support team at [support@basiq.io](mailto:support@basiq.io).

<br />

<Table align={["left","left","left","left","left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        loginId
      </th>

      <th>
        password
      </th>

      <th>
        persona
      </th>

      <th>
        suitable use case
      </th>

      <th>
        name
      </th>

      <th>
        phone
      </th>

      <th>
        email
      </th>

      <th>
        account number
      </th>

      <th>
        address
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Wentworth-Smith
      </td>

      <td>
        whislter
      </td>

      <td>
        This is a joint account.

        - **income (transaction account)**: 2 sources of salary, monthly stable salary & fortnightly stable salary.
        - **liabilities**: mortgage (mortgage account) and car loan (payments in the transaction account)
        - **expenses**: has predictable expenses (credit-card account)
      </td>

      <td>
        - Verify income
        - Review expenses
        - Affordability assessment
        - Assess liabilities
        - PFM
        - Access transaction data
        - Identify spending patterns
        - Personalised financial advice
        - Capture account details
      </td>

      <td>
        Max Wentworth-Smith
      </td>

      <td>
        0419000000
      </td>

      <td>
        [maxsmith@micr0soft.com](mailto:maxsmith@micr0soft.com)
      </td>

      <td>
        transaction:<br />45678945678901credit card: 23456723456789savings: 34567834567890mortgage:1 2345612345678
      </td>

      <td>
        13/91 Fisher Rd, Dee Why NSW 2099, Australia
      </td>
    </tr>

    <tr>
      <td>
        Whistler
      </td>

      <td>
        ShowBox
      </td>

      <td>
        - **income (transaction account)**: 1 source of salary, fortnightly salary
        - **liabilities**: has BNPL (transaction account), no mortgage / personal loan
        - **expenses**: no daily expenses
        - **risk flags**: large amount of external transfer (debit to Jared)
      </td>

      <td>
        - Verify income
        - Assess liabilities
        - Access transaction data
        - Personalised financial advice
        - Capture account details
      </td>

      <td>
        Whistler Smith
      </td>

      <td>
        0405000000
      </td>

      <td>
        [whistler@h0tmail.com](mailto:whistler@h0tmail.com)
      </td>

      <td>
        transaction: 000001919644181
      </td>

      <td>
        201 Sussex St, Sydney NSW 2000, Australia
      </td>
    </tr>

    <tr>
      <td>
        Gilfoyle
      </td>

      <td>
        PiedPiper
      </td>

      <td>
        - **income** (transaction account): stop fortnightly salary, unemployment benefits
        - **liabilities**: increase in BNPL (transaction account)
        - **expenses**: has predictable expenses (credit-card account)
        - **risk flags**: late fee (credit-card account)
      </td>

      <td>
        - Verify income
        - Assess liabilities
        - Expense check
        - Affordability assessment
        - Identify spending patterns
        - PFM
        - Analyse creditworthiness
        - Access transaction data
        - Personalised financial advice
        - Capture account details
      </td>

      <td>
        Gilfoyle Bertram
      </td>

      <td>
        0405000000
      </td>

      <td>
        [gilfoyle@mgail.com](mailto:gilfoyle@mgail.com)
      </td>

      <td>
        transaction: 000001919644171credit card: 000001919644170savings: 000001919644172
      </td>

      <td>
        Dee Why NSW 2099, Australia
      </td>
    </tr>

    <tr>
      <td>
        gavinBelson
      </td>

      <td>
        hooli2016
      </td>

      <td>
        - **income** (transaction account): 1 salary + 1 additional earning, increase monthly salary + extra income (tutoring weekly volatile)
        - **liabilities**: personal loan (loan account)
        - **expenses**: predictable expenses (credit-card account)
        - HooliGov Bank (AU00004)
      </td>

      <td>
        - Verify income
        - Assess liabilities
        - Expense check
        - Affordability assessment
        - Identify spending patterns
        - PFM
        - Analyse creditworthiness
        - Access transaction data
        - Personalised financial advice
        - Capture account details
      </td>

      <td>
        Gavin Belson
      </td>

      <td>
        0490000000
      </td>

      <td>
        [gavinbelson@h0tmail.com](mailto:gavinbelson@h0tmail.com)
      </td>

      <td>
        transaction: 000001000002credit card: 000001004381savings: 000001002935loan: 000001002955
      </td>

      <td>
        YARDARINO WA 6525, Australia
      </td>
    </tr>

    <tr>
      <td>
        jared
      </td>

      <td>
        django
      </td>

      <td>
        - **income** (transaction account): weekly volatile income from uber + credit transfers from Whistler
        - **liabilities**: unshared mortgage account (payments in the transaction account), car loan (payments in the transaction account)
        - **expenses**: predictable expenses (credit-card account)
        - **assets**: term deposit
      </td>

      <td>
        - Verify income
        - Assess liabilities
        - Expense check
        - Affordability assessment
        - Identify spending patterns
        - PFM
        - Analyse creditworthiness
        - Access transaction data
        - Personalised financial advice
        - Capture account details
      </td>

      <td>
        Jared Dunn
      </td>

      <td>
        0405000000
      </td>

      <td>
        [Jared.D@h0tmail.com](mailto:Jared.D@h0tmail.com)
      </td>

      <td>
        transaction: 000001023480credit card: 000001023483term deposit: 000001023482
      </td>

      <td>
        Tuggerah NSW 2259, Australia
      </td>
    </tr>

    <tr>
      <td>
        richard
      </td>

      <td>
        tabsnotspaces
      </td>

      <td>
        - **income** (transaction account): high stable fortnightly income, 2 rental incomes
        - **liabilities**: 3 mortgages (1 shared mortgage account & 2 unshared mortgages), 2 car loans (payments in the transaction account), 4 credit cards (1 shared credit card account & 3 unshared credit card accounts)
        - **expenses**: predictable expenses (credit-card account)
      </td>

      <td>
        - Verify income
        - Assess liabilities
        - Expense check
        - Affordability assessment
        - Identify spending patterns
        - PFM
        - Analyse creditworthiness
        - Access transaction data
        - Personalised financial advice
        - Capture account details
      </td>

      <td>
        Richard Birtles
      </td>

      <td>
        0482000000
      </td>

      <td>
        [r.birtles@tetlerjones.c0m.au](mailto:r.birtles@tetlerjones.c0m.au)
      </td>

      <td>
        transaction: 000001077380credit card: 000001077379mortgage: 000001077381
      </td>

      <td>
        51 Dabinett Rd, Ponde SA 5238, Australia
      </td>
    </tr>

    <tr>
      <td>
        laurieBream
      </td>

      <td>
        business2024
      </td>

      <td>
        Happy path persona with business fields and business consumer consent
      </td>

      <td>
        - Business Consumer Consent
      </td>

      <td>
        Laurie Bream
      </td>

      <td>
        0490000000
      </td>

      <td>
        [business@manlyaccountants.com.au](mailto:business@manlyaccountants.com.au)
      </td>

      <td>
        transaction: 062245684154861747642credit card: 772245684154861747642
      </td>

      <td>
        21 Sydney Rd, Manly NSW 2095, Australia
      </td>
    </tr>

    <tr>
      <td>
        ashMann
      </td>

      <td>
        hooli2024
      </td>

      <td>
        - **income** (transaction account): 1 salary monthly income, rental income
        - **liabilities**: unshared credit card transactions (payments in the transaction account). BPAY related CDR fields like `billerCode`, `billerName`, and `crn` are disclosed under “Bankwest credit card” transactions under this user as examples.
        - **expenses**: predictable expenses (credit-card account), rental expense
        - **risk flags**: gambling behaviours, cash withdrawal, crypto exchange
      </td>

      <td>
        - Verify income
        - Assess liabilities
        - Expense check
        - Affordability assessment
        - Identify spending patterns
        - PFM
        - Analyse creditworthiness
        - Access transaction data
        - Personalised financial advice
        - Capture account details
      </td>

      <td>
        Ash Mann
      </td>

      <td>
        0497000000
      </td>

      <td>
        [ashmann@gamil.com](mailto:ashmann@gamil.com)
      </td>

      <td>
        transaction: 090001077738credit card: 090001077779
      </td>

      <td>
        201 Sussex St, Sydney NSW 2000, Australia
      </td>
    </tr>
  </tbody>
</Table>

# Unhappy path test users

> 🚧 Unhappy path test users
>
> The following users will _always_ return the same errors at the same job step. We created them to ensure you could fully test the unhappy paths your user may encounter while connecting their accounts via DDC and handle them appropriately. See [here](ref:jobs) on how to best handle these scenarios.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        loginID
      </th>

      <th>
        password
      </th>

      <th>
        Failure scenario
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        bighead
      </td>

      <td>
        password
      </td>

      <td>
        - **Error:** `invalid-credentials`
        - **Detail:** "Account is locked"
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        erlich
      </td>

      <td>
        aviato
      </td>

      <td>
        - **Error:** `account-not-accessible-requires-user-action`
        - **Detail:** "An action is required from end-user before account details can be returned."
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        jianYang
      </td>

      <td>
        nothotdog
      </td>

      <td>
        - **Error:** `service-unavailable`
        - **Detail:** "Service is currently unavailable. Please try again later."
      </td>
    </tr>
  </tbody>
</Table>

# MFA users

We have two test banks to test MFA challenges

- Pied Piper Bank  (`mfa-challenge` _always_)
- Nucleus Bank (`mfa-challenge` _intermittent - 50/50_)

| loginId         | password      | mfaChallengeMethod | mfaChallengeInput                                                         | mfaChallengeSolution  |
| :-------------- | :------------ | :----------------- | :------------------------------------------------------------------------ | :-------------------- |
| jared           | django        | token              | \["OTP Password"]                                                         | \["1234"]             |
| richard         | tabsnotspaces | token              | \["OTP Password"]                                                         | \["1234"]             |
| gavinBelson     | hooli2016     | security-questions | \["What's your first company?"]                                           | \["Hooli"]            |
| Gilfoyle        | PiedPiper     | security-questions | \["What's your first company?"]                                           | \["Hooli"]            |
| Whistler        | ShowBox       | security-questions | \["What's your favourite company?", "What's the ID of this institution?"] | \["Basiq", "AU00000"] |
| Wentworth-Smith | whislter      | security-questions | \["What's your favourite company?", "What's the ID of this institution?"] | \["Basiq", "AU00000"] |

<br />

<br />
