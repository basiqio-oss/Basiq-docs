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
        gavinBelson
      </td>

      <td style={{ textAlign: "left" }}>
        hooli2016
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        jared
      </td>

      <td style={{ textAlign: "left" }}>
        django
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        richard
      </td>

      <td style={{ textAlign: "left" }}>
        tabsnotspaces
      </td>
    </tr>
  </tbody>
</Table>

```json Create Connection (using test account)
POST /users/ea3a81/connections HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN                                           
Content-Type: application/json

{
  "loginId": "gavinBelson",
  "password": "hooli2016",   
  "institution":{
    "id":"AU00000"
  }
}
```
