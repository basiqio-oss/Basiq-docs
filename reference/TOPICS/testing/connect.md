---
title: Connect
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

> 🚧 You can use our sandbox environment for free right now - just grab an API key to get started (via the [Developer Dashboard](https://dashboard.basiq.io/)).

> 📘 Ensure that you pass the institution code AU00000 when using the test accounts. Data for sandbox accounts is updated daily/weekly/monthly to provide realistic data for faster integration.

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
        great for...
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
        Connect and Affordability - happy path persona with steady income, mortgage, credit card  and predictable expenses
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
        Connect and Affordability - persona with income, missing expenses, BNPL activity and balance going up over time
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
        * \*new\*\* Connect and Affordability - persona with balances ranging between stable and diminishing over time
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
        Connect
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
        Connect
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
        Connect
      </td>
    </tr>
  </tbody>
</Table>

# Unhappy path test users

> 🚧
>
> The following users will *always* return the same errors at the same job step. We created them to ensure you could fully test the unhappy paths your user may encounter while connecting their accounts and handle them appropriately. See [here](https://api.basiq.io/docs/handling-jobs) on how to best handle these scenarios.

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

> 📘 Whistler login - sandbox data
>
> This user in sandbox has examples of the following:
>
> * Regular income over the last 13 months that shows some instability, e.g. some time spent as a casual worker, which then produces a stability score of \< 0.8, and a more varied income/month graph
> * Gambling expenditure 
> * BNPL activity
> * Higher than expected expenditure in some categories e.g. alchohol

```json Create Connection (using test account)
POST /users/ea3a81/connections HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN                                           
Content-Type: application/json

{
 "loginId": "Wentworth-Smith",
 "password": "whislter",
 "institution":{
   "id":"AU00000"
 }
}
```
