---
title: List all accounts
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
Use this collection to retrieve a list of [accounts](https://api.basiq.io/reference/accounts). Each entry in the array is a separate account object.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>

      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        **[filter](https://api.basiq.io/docs/collections-filters)**
        *string, optional*
      </td>

      <td style={{ textAlign: "left" }}>
        This list can be [filtered](https://api.basiq.io/docs/collections-filters) by the following properties:

        * `account.id`

        * `connection.id`

        * `institution.id`

        Only equals (eq) and not equals (ne) operations are currently supported.
      </td>
    </tr>
  </tbody>
</Table>

**Returns**

Returns a list with a data property that contains an array of accounts. Each entry in the array is a separate object. If no data is returned, the resulting array will be empty. Otherwise, this call returns an [error](https://api.basiq.io/docs/errors-1) in the event of a failure.

```json Definition
GET /users/{user.id}/accounts
```

```json Example Request
GET  /users/ea3a81/accounts  HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.1 200 OK
Content-Type: application/json

{
  "type": "list",
  "data": [
    {
      "type": "account",
      "id": "2682e4bf",
      "accountNo": "12345612345678",
      "name": "Mortgage 746833",
      "currency": "AUD",
      "class": {
        "type": "mortgage",
        "product": "Hooli Home Loan",
        "meta": {
          "accountNumber": "12345612345678",
          "availableRedraw": "200.00",
          "endDate": "2040-01-13T08:00:00.000Z",
          "fee": "300.00",
          "instalmentAmount": null,
          "interestRate": null,
          "interestType": "variable",
          "nextInstalmentDate": "2021-02-01T00:00:00.000Z",
          "offsetAccountNumber": "12-999-000",
          "repaymentFrequency": "monthly",
          "repaymentType": "interest and principal"
        }
      },
      "balance": "-367576.75",
      "availableFunds": "32423.25",
      "lastUpdated": "2021-01-19T04:17:17Z",
      "transactionIntervals": [
        {
          "from": "2019-04-30",
          "to": "2021-01-19"
        }
      ],
      "institution": "AU00000",
      "accountHolder": "Max Wentworth-Smith & Paul Wentworth-Smith",
      "connection": "575f762e",
      "status": "available",
      "links": {
        "self": "https://au-api.basiq.io/users/bf3399fg0/accounts/2682e4bf",
        "transactions": "https://au-api.basiq.io/users/bf3399fg0/transactions?filter=account.id.eq('2682e4bf)",
        "connection": null,
        "institution": "https://au-api.basiq.io/institutions/AU00000"
      }
    },
    {
      "type": "account",
      "id": "99bd6065",
      "accountNo": "23456723456789",
      "name": "Credit Card 13000",
      "currency": "AUD",
      "class": {
        "type": "credit-card",
        "product": "Hooli Visa"
      },
      "balance": "10260.81",
      "availableFunds": "30260.81",
      "lastUpdated": "2021-01-19T04:17:17Z",
      "transactionIntervals": [
        {
          "from": "2019-05-13",
          "to": "2021-01-19"
        }
      ],
      "institution": "AU00000",
      "accountHolder": "Max Wentworth-Smith",
      "connection": "575f762e",
      "status": "available",
      "links": {
        "self": "https://au-api.basiq.io/users/bf3399fg0/accounts/99bd6065",
        "transactions": "https://au-api.basiq.io/users/bf3399fg0/transactions?filter=account.id.eq('99bd6065')",
        "connection": null,
        "institution": "https://au-api.basiq.io/institutions/AU00000"
      }
    }
  ],
  "links": {
    "self": "https://au-api.basiq.io/users/bf3399fg0/accounts"
  }
}
```
