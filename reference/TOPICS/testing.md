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

<Table>
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

        * \*income (transaction account)\*\*: 2 sources of salary, monthly stable salary & fortnightly stable salary.  
        * \*liabilities\*\*: mortgage (mortgage account) and car loan (payments in the transaction account)  
        * \*expenses\*\*: has predictable expenses (credit-card account)
      </td>

      <td>
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
    </tr>

    <tr>
      <td>
        Whistler
      </td>

      <td>
        ShowBox
      </td>

      <td>
        * \*income (transaction account)\*\*: 1 source of salary, fortnightly salary  
        * \*liabilities\*\*: has BNPL (transaction account), no mortgage / personal loan  
        * \*expenses\*\*: no daily expenses  
        * \*risk flags\*\*: large amount of external transfer (debit to Jared)
      </td>

      <td>
        * Verify income
        * Assess liabilities
        * Access transaction data
        * Personalised financial advice
        * Capture account details
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
        * \*income\*\* (transaction account): stop fortnightly salary, unemployment benefits  
        * \*liabilities\*\*: increase in BNPL (transaction account)  
        * \*expenses\*\*: has predictable expenses (credit-card account)  
        * \*risk flags\*\*: late fee (credit-card account)
      </td>

      <td>
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
    </tr>

    <tr>
      <td>
        gavinBelson
      </td>

      <td>
        hooli2016
      </td>

      <td>
        * \*income\*\* (transaction account): 1 salary + 1 additional earning, increase monthly salary + extra income (tutoring weekly volatile)  
        * \*liabilities\*\*: personal loan (loan account)  
        * \*expenses\*\*: predictable expenses (credit-card account)  
        * HooliGov Bank (AU00004)
      </td>

      <td>
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
    </tr>

    <tr>
      <td>
        jared
      </td>

      <td>
        django
      </td>

      <td>
        * \*income\*\* (transaction account): weekly volatile income from uber + credit transfers from Whistler  
        * \*liabilities\*\*: unshared mortgage account (payments in the transaction account), car loan (payments in the transaction account)  
        * \*expenses\*\*: predictable expenses (credit-card account)  
        * \*assets\*\*: term deposit
      </td>

      <td>
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
    </tr>

    <tr>
      <td>
        richard
      </td>

      <td>
        tabsnotspaces
      </td>

      <td>
        * \*income\*\* (transaction account): high stable fortnightly income, 2 rental incomes  
        * \*liabilities\*\*: 3 mortgages (1 shared mortgage account & 2 unshared mortgages), 2 car loans (payments in the transaction account), 4 credit cards (1 shared credit card account & 3 unshared credit card accounts)  
        * \*expenses\*\*: predictable expenses (credit-card account)
      </td>

      <td>
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
        * Business Consumer Consent
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
        * \*income\*\* (transaction account): 1 salary monthly income, rental income  
        * \*liabilities\*\*: unshared credit card transactions (payments in the transaction account)  
        * \*expenses\*\*: predictable expenses (credit-card account), rental expense  
        * \*risk flags\*\*: gambling behaviours, cash withdrawal, crypto exchange
      </td>

      <td>
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
    </tr>
  </tbody>
</Table>

# Unhappy path test users

> 🚧 Unhappy path test users
>
> The following users will *always* return the same errors at the same job step. We created them to ensure you could fully test the unhappy paths your user may encounter while connecting their accounts via DDC and handle them appropriately. See [here](ref:jobs) on how to best handle these scenarios.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        loginID
      </th>

      <th style={{ textAlign: "left" }}>
        password
      </th>

      <th style={{ textAlign: "left" }}>
        Failure scenario
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        bighead
      </td>

      <td style={{ textAlign: "left" }}>
        password
      </td>

      <td style={{ textAlign: "left" }}>
        * \*Error:\*\* `invalid-credentials`  
        * \*Detail:\*\* "Account is locked"
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        erlich
      </td>

      <td style={{ textAlign: "left" }}>
        aviato
      </td>

      <td style={{ textAlign: "left" }}>
        * \*Error:\*\* `account-not-accessible-requires-user-action`  
        * \*Detail:\*\* "An action is required from end-user before account details can be returned."
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        jianYang
      </td>

      <td style={{ textAlign: "left" }}>
        nothotdog
      </td>

      <td style={{ textAlign: "left" }}>
        * \*Error:\*\* `service-unavailable`  
        * \*Detail:\*\* "Service is currently unavailable. Please try again later."
      </td>
    </tr>
  </tbody>
</Table>

# MFA users

We have two test banks to test MFA challenges 

* Pied Piper Bank  (`mfa-challenge` *always*)
* Nucleus Bank (`mfa-challenge` *intermittent - 50/50*)

| loginId         | password      | mfaChallengeMethod | mfaChallengeInput                                                        | mfaChallengeSolution |
| :-------------- | :------------ | :----------------- | :----------------------------------------------------------------------- | :------------------- |
| jared           | django        | token              | ["OTP Password"]                                                         | \["1234"]            |
| richard         | tabsnotspaces | token              | ["OTP Password"]                                                         | \["1234"]            |
| gavinBelson     | hooli2016     | security-questions | ["What's your first company?"]                                           | ["Hooli"]            |
| Gilfoyle        | PiedPiper     | security-questions | ["What's your first company?"]                                           | ["Hooli"]            |
| Whistler        | ShowBox       | security-questions | ["What's your favourite company?", "What's the ID of this institution?"] | ["Basiq", "AU00000"] |
| Wentworth-Smith | whislter      | security-questions | ["What's your favourite company?", "What's the ID of this institution?"] | ["Basiq", "AU00000"] |
