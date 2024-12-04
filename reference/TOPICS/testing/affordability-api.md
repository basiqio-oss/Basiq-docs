---
title: Affordability API
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
The test data that we provide for the Affordability API service has been designed to mimic a real life user. This means that just a like a real user would spend and receive funds throughout the day - our test accounts have been designed to do the same thing. Therefore you should expect to see new transaction records being created throughout the day, and the account balances adjusted accordingly.

> 🚧 You can use our sandbox environment for free - contact us (via the "help" icon at the bottom of the page) to have your API key activated for Affordability.

> 📘 Ensure that you pass the institution code AU00000 when using the test accounts

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        loginId
      </th>

      <th style={{ textAlign: "left" }}>
        password
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
    </tr>
  </tbody>
</Table>

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

> 👍 Once you have created a test connection you can access the Affordability, Income and Expense endpoints for this user.  The Affordability endpoint returns links to Income and Expense resources or you can use these endpoints independently without Affordability.

```json Definitions
POST /users/{user.id}/affordability HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json
```
