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

> 🚧 Sandbox environment
>
> You can use our sandbox environment for free right now - just grab an API key to get started (via the [Developer Dashboard](https://dashboard.basiq.io/)). We recommend using our test bank `Hooli`.

**Note:** There is a limit of 500 for sandbox connections.  If you reach your limit and need to have this increased, feel free to reach out to [support@basiq.io](mailto:support@basiq.io).

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        loginId
      </th>

      <th style={{ textAlign: "left" }}>
        password
      </th>

      <th style={{ textAlign: "left" }}>

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
        Happy path persona with steady income, mortgage, credit card  and predictable expenses
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
        Persona with income, missing expenses, BNPL activity and balance going up over time
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
        Persona with balances ranging between stable and diminishing over time
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
        Standard
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
        Standard
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
        Standard
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
        HooliGov Bank (AU00004)
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

* Pied Piper Bank: AU00002  (`mfa-challenge` *always*)
* Nucleus Bank: AU00003 (`mfa-challenge` *intermittent - 50/50*)

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        loginId
      </th>

      <th style={{ textAlign: "left" }}>
        password
      </th>

      <th style={{ textAlign: "left" }}>
        mfaChallengeMethod
      </th>

      <th style={{ textAlign: "left" }}>
        mfaChallengeInput
      </th>

      <th style={{ textAlign: "left" }}>
        mfaChallengeSolution
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        jared
      </td>

      <td style={{ textAlign: "left" }}>
        django
      </td>

      <td style={{ textAlign: "left" }}>
        token
      </td>

      <td style={{ textAlign: "left" }}>
        ["OTP Password"]
      </td>

      <td style={{ textAlign: "left" }}>
        ["1234"]
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
        token
      </td>

      <td style={{ textAlign: "left" }}>
        ["OTP Password"]
      </td>

      <td style={{ textAlign: "left" }}>
        ["1234"]
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
        security-questions
      </td>

      <td style={{ textAlign: "left" }}>
        ["What's your first company?"]
      </td>

      <td style={{ textAlign: "left" }}>
        ["Hooli"]
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
        security-questions
      </td>

      <td style={{ textAlign: "left" }}>
        ["What's your first company?"]
      </td>

      <td style={{ textAlign: "left" }}>
        ["Hooli"]
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
        security-questions
      </td>

      <td style={{ textAlign: "left" }}>
        ["What's your favourite company?", "What's the ID of this institution?"]
      </td>

      <td style={{ textAlign: "left" }}>
        ["Basiq", "AU00000"]
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Wentworth-Smith
      </td>

      <td style={{ textAlign: "left" }}>
        whislter
      </td>

      <td style={{ textAlign: "left" }}>
        security-questions
      </td>

      <td style={{ textAlign: "left" }}>
        ["What's your favourite company?", "What's the ID of this institution?"]
      </td>

      <td style={{ textAlign: "left" }}>
        ["Basiq", "AU00000"]
      </td>
    </tr>
  </tbody>
</Table>
