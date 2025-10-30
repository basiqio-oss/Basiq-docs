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
> You can use our sandbox environment for free right now - just grab an API key to get started (via the [Developer Dashboard](https://dashboard.basiq.io/)). We recommend using our test bank `Hooli`.

**Note:** There is a limit of 500 for sandbox connections.  If you reach your limit and need to have this increased, feel free to reach out to [support@basiq.io](mailto:support@basiq.io).

> 📘 🆕 Initial Testing and Billing Policy
>
> For initial testing, BASIQ services are available at no cost. This free access allows you to extensively test our platform's capabilities using our sandbox environment. However, once you transition from testing to becoming a paying customer, charges will apply for any users on your platform. This billing policy ensures that you have the opportunity to fully explore and understand the value of BASIQ services before any financial commitment is required.
>
> If you have questions about transitioning to a paying customer or about our billing structure, please contact our support team at [support@basiq.io](mailto:support@basiq.io).

<br />

<Table align={["left","left","left","left","left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        loginId
      </th>

      <th style={{ textAlign: "left" }}>
        password
      </th>

      <th style={{ textAlign: "left" }}>
        persona
      </th>

      <th style={{ textAlign: "left" }}>
        suitable use case
      </th>

      <th style={{ textAlign: "left" }}>
        name
      </th>

      <th style={{ textAlign: "left" }}>
        phone
      </th>

      <th style={{ textAlign: "left" }}>
        email
      </th>

      <th style={{ textAlign: "left" }}>
        address
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Wentworth-Smith
      </td>

      <td style={{ textAlign: "left" }}>
        whislter
      </td>

      <td style={{ textAlign: "left" }}>
        This is a joint account.

        * **income (transaction account)**: 2 sources of salary, monthly stable salary & fortnightly stable salary.
        * **liabilities**: mortgage (mortgage account) and car loan (payments in the transaction account)
        * **expenses**: has predictable expenses (credit-card account)
      </td>

      <td style={{ textAlign: "left" }}>
        * Verify income
        * Review expenses
        * Affordability assessment
        * Assess liabilities
        * PFM
        * Access transaction data
        * Identify spending patterns
        * Personalised financial advice
        * Capture account details
      </td>

      <td style={{ textAlign: "left" }}>
        Max Wentworth-Smith
      </td>

      <td style={{ textAlign: "left" }}>
        0419000000
      </td>

      <td style={{ textAlign: "left" }}>
        maxsmith@micr0soft.com
      </td>

      <td style={{ textAlign: "left" }}>
        13/91 Fisher Rd, Dee Why NSW 2099, Australia
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Whistler
      </td>

      <td style={{ textAlign: "left" }}>
        ShowBox
      </td>

      <td style={{ textAlign: "left" }}>
        * **income (transaction account)**: 1 source of salary, fortnightly salary
        * **liabilities**: has BNPL (transaction account), no mortgage / personal loan
        * **expenses**: no daily expenses
        * **risk flags**: large amount of external transfer (debit to Jared)
      </td>

      <td style={{ textAlign: "left" }}>
        * Verify income
        * Assess liabilities
        * Access transaction data
        * Personalised financial advice
        * Capture account details
      </td>

      <td style={{ textAlign: "left" }}>
        Whistler Smith
      </td>

      <td style={{ textAlign: "left" }}>
        0405000000
      </td>

      <td style={{ textAlign: "left" }}>
        [whistler@h0tmail.com](mailto:whistler@h0tmail.com)
      </td>

      <td style={{ textAlign: "left" }}>
        201 Sussex St, Sydney NSW 2000, Australia
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Gilfoyle
      </td>

      <td style={{ textAlign: "left" }}>
        PiedPiper
      </td>

      <td style={{ textAlign: "left" }}>
        * **income** (transaction account): stop fortnightly salary, unemployment benefits
        * **liabilities**: increase in BNPL (transaction account)
        * **expenses**: has predictable expenses (credit-card account)
        * **risk flags**: late fee (credit-card account)
      </td>

      <td style={{ textAlign: "left" }}>
        * Verify income
        * Assess liabilities
        * Expense check
        * Affordability assessment
        * Identify spending patterns
        * PFM
        * Analyse creditworthiness
        * Access transaction data
        * Personalised financial advice
        * Capture account details
      </td>

      <td style={{ textAlign: "left" }}>
        Gilfoyle Bertram
      </td>

      <td style={{ textAlign: "left" }}>
        0405000000
      </td>

      <td style={{ textAlign: "left" }}>
        gilfoyle@mgail.com
      </td>

      <td style={{ textAlign: "left" }}>
        Dee Why NSW 2099, Australia
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        gavinBelson
      </td>

      <td style={{ textAlign: "left" }}>
        hooli2016
      </td>

      <td style={{ textAlign: "left" }}>
        * **income** (transaction account): 1 salary + 1 additional earning, increase monthly salary + extra income (tutoring weekly volatile)
        * **liabilities**: personal loan (loan account)
        * **expenses**: predictable expenses (credit-card account)
        * HooliGov Bank (AU00004)
      </td>

      <td style={{ textAlign: "left" }}>
        * Verify income
        * Assess liabilities
        * Expense check
        * Affordability assessment
        * Identify spending patterns
        * PFM
        * Analyse creditworthiness
        * Access transaction data
        * Personalised financial advice
        * Capture account details
      </td>

      <td style={{ textAlign: "left" }}>
        Gavin Belson
      </td>

      <td style={{ textAlign: "left" }}>
        0490000000
      </td>

      <td style={{ textAlign: "left" }}>
        gavinbelson@h0tmail.com
      </td>

      <td style={{ textAlign: "left" }}>
        YARDARINO WA 6525, Australia
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        jared
      </td>

      <td style={{ textAlign: "left" }}>
        django
      </td>

      <td style={{ textAlign: "left" }}>
        * **income** (transaction account): weekly volatile income from uber + credit transfers from Whistler
        * **liabilities**: unshared mortgage account (payments in the transaction account), car loan (payments in the transaction account)
        * **expenses**: predictable expenses (credit-card account)
        * **assets**: term deposit
      </td>

      <td style={{ textAlign: "left" }}>
        * Verify income
        * Assess liabilities
        * Expense check
        * Affordability assessment
        * Identify spending patterns
        * PFM
        * Analyse creditworthiness
        * Access transaction data
        * Personalised financial advice
        * Capture account details
      </td>

      <td style={{ textAlign: "left" }}>
        Jared Dunn
      </td>

      <td style={{ textAlign: "left" }}>
        0405000000
      </td>

      <td style={{ textAlign: "left" }}>
        Jared.D@h0tmail.com
      </td>

      <td style={{ textAlign: "left" }}>
        TUGGERAH NSW 2259, Australia
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        richard
      </td>

      <td style={{ textAlign: "left" }}>
        tabsnotspaces
      </td>

      <td style={{ textAlign: "left" }}>
        * **income** (transaction account): high stable fortnightly income, 2 rental incomes
        * **liabilities**: 3 mortgages (1 shared mortgage account & 2 unshared mortgages), 2 car loans (payments in the transaction account), 4 credit cards (1 shared credit card account & 3 unshared credit card accounts)
        * **expenses**: predictable expenses (credit-card account)
      </td>

      <td style={{ textAlign: "left" }}>
        * Verify income
        * Assess liabilities
        * Expense check
        * Affordability assessment
        * Identify spending patterns
        * PFM
        * Analyse creditworthiness
        * Access transaction data
        * Personalised financial advice
        * Capture account details
      </td>

      <td style={{ textAlign: "left" }}>
        Richard Birtles
      </td>

      <td style={{ textAlign: "left" }}>
        0482000000
      </td>

      <td style={{ textAlign: "left" }}>
        r.birtles@tetlerjones.c0m.au
      </td>

      <td style={{ textAlign: "left" }}>
        51 Dabinett Rd, Ponde SA 5238, Australia
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        laurieBream
      </td>

      <td style={{ textAlign: "left" }}>
        business2024
      </td>

      <td style={{ textAlign: "left" }}>
        Happy path persona with business fields and business consumer consent
      </td>

      <td style={{ textAlign: "left" }}>
        * Business Consumer Consent
      </td>

      <td style={{ textAlign: "left" }}>
        Laurie Bream
      </td>

      <td style={{ textAlign: "left" }}>
        0490000000
      </td>

      <td style={{ textAlign: "left" }}>
        	
        business@manlyaccountants.com.au
      </td>

      <td style={{ textAlign: "left" }}>
        21 Sydney Rd, Manly NSW 2095, Australia
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        ashMann
      </td>

      <td style={{ textAlign: "left" }}>
        hooli2024
      </td>

      <td style={{ textAlign: "left" }}>
        * **income** (transaction account): 1 salary monthly income, rental income
        * **liabilities**: unshared credit card transactions (payments in the transaction account). BPAY related CDR fields like `billerCode`, `billerName`, and `crn` are disclosed under “Bankwest credit card” transactions under this user as examples.
        * **expenses**: predictable expenses (credit-card account), rental expense
        * **risk flags**: gambling behaviours, cash withdrawal, crypto exchange
      </td>

      <td style={{ textAlign: "left" }}>
        * Verify income
        * Assess liabilities
        * Expense check
        * Affordability assessment
        * Identify spending patterns
        * PFM
        * Analyse creditworthiness
        * Access transaction data
        * Personalised financial advice
        * Capture account details
      </td>

      <td style={{ textAlign: "left" }}>
        Ash Mann
      </td>

      <td style={{ textAlign: "left" }}>
        0497000000
      </td>

      <td style={{ textAlign: "left" }}>
        ashmann@gmail.com
      </td>

      <td style={{ textAlign: "left" }}>
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
        * **Error:** `invalid-credentials`
        * **Detail:** "Account is locked"
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
        * **Error:** `account-not-accessible-requires-user-action`
        * **Detail:** "An action is required from end-user before account details can be returned."
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
        * **Error:** `service-unavailable`
        * **Detail:** "Service is currently unavailable. Please try again later."
      </td>
    </tr>
  </tbody>
</Table>

# MFA users

We have two test banks to test MFA challenges

* Pied Piper Bank  (`mfa-challenge` _always_)
* Nucleus Bank (`mfa-challenge` _intermittent - 50/50_)

| loginId         | password      | mfaChallengeMethod | mfaChallengeInput                                                        | mfaChallengeSolution |
| :-------------- | :------------ | :----------------- | :----------------------------------------------------------------------- | :------------------- |
| jared           | django        | token              | ["OTP Password"]                                                         | ["1234"]             |
| richard         | tabsnotspaces | token              | ["OTP Password"]                                                         | ["1234"]             |
| gavinBelson     | hooli2016     | security-questions | ["What's your first company?"]                                           | ["Hooli"]            |
| Gilfoyle        | PiedPiper     | security-questions | ["What's your first company?"]                                           | ["Hooli"]            |
| Whistler        | ShowBox       | security-questions | ["What's your favourite company?", "What's the ID of this institution?"] | ["Basiq", "AU00000"] |
| Wentworth-Smith | whislter      | security-questions | ["What's your favourite company?", "What's the ID of this institution?"] | ["Basiq", "AU00000"] |

<div
  style={{
    border: "2px solid #1E1E1E", // Dark border
    borderRadius: "8px",
    backgroundColor: "#1E1E1E", // Dark background
    padding: "16px",
    margin: "16px 0",
    fontFamily: "Arial, sans-serif",
    color: "#ffffff", // Light text for contrast
  }}
>
  <strong style={{ color: "#ffffff" }}>📢 Attention!</strong> If you have any issues, please reach out to our amazing support team.

  <div style={{ display: 'flex', alignItems: 'center' }}>
    <button
      onClick={() => Intercom('showNewMessage', 'issues on FAQs:')}
      style={{
        padding: '12px 30px',
        backgroundColor: '#1E1E1E',
        color: '#ffffff',
        border: '2px solid #ffffff', // Add contrast border if needed
        borderRadius: '50px',
        fontSize: '16px',
        fontWeight: '600',
        textTransform: 'uppercase',
        cursor: 'pointer',
        transition: 'background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease',
        outline: 'none',
        display: 'flex',
        justifyContent: 'center',
        height: '45px',
        position: 'relative',
        overflow: 'hidden',
        marginLeft: '10px',
        minWidth: '150px',
      }}
      onMouseEnter={(e) => {
        e.target.style.transform = 'scale(1.1)';
        e.target.style.backgroundColor = '#333333'; // Slightly lighter dark on hover
      }}
      onMouseLeave={(e) => {
        e.target.style.transform = 'scale(1)';
        e.target.style.backgroundColor = '#1E1E1E'; // Original dark
      }}
    >
      Support team
    </button>
  </div>
</div>
