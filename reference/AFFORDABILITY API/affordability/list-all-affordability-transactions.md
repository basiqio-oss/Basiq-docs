---
title: List all affordability transactions
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
Use this collection to retrieve a paginated list of [transactions](https://basiq.readme.io/v2.1/reference/transactions). The transactions are returned sorted by account and then posted date descending order - with pending transactions appearing first. Transactions are paginated in chunks of 500. Absence of `next` link means that there are no more pages to retrieve.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Arguments
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        **limit**
        *string, optional*
      </td>

      <td style={{ textAlign: "left" }}>
        This represents the maximum number of items that may be included in the response (maximum of 500). Note that by default 500 items are returned if this value is not specified.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **[filter](https://api.basiq.io/docs/collections-filters)**\
        *string, optional*
      </td>

      <td style={{ textAlign: "left" }}>
        This list can be [filtered](https://api.basiq.io/docs/collections-filters) by the following properties:  

        * `transaction.class`  

             

         \
        **Note**: this filter applies only to JSON structure, due to the difference in CSV formatting\*
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

**Returns**

Returns a paginated list with a data property that contains an array of transactions from the affordability snapshot. Each entry in the array is a separate object. If no data is returned, the resulting array will be empty. Otherwise, this call returns an [error](https://api.basiq.io/docs/errors-1) in the event of a failure.

> 📘 Affordability Transactions
>
> The array of transactions used to generate Affordability insights is the full snapshot of transactions as per the [transactions](https://basiq.readme.io/v2.1/reference/transactions) resource where the following attributes are specific to Affordability:
>
> * there is no link to self
> * `class`: enums specific to affordability provide more granularity around transfer transactions - detailed in the table 
> * `subClass`: attribute returns HEC class for payments by default or alternatively the custom class configured for a partner account

Each affordability transaction contains the same attributes however the data extends the  [transactions](https://basiq.readme.io/v2.1/reference/transactions) resource as follows:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Attributes
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `class`
      </td>

      <td style={{ textAlign: "left" }}>
        Describes the class(type) of transaction. Possible values depend on the `direction` field, and include:
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        **Debit Classes:**
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `bank-fee` - a fee incurred by the user from their bank e.g. ATM withdrawal fee.  
        * `payment` - payment made to a merchant.  
        * `cash-withdrawal` - funds withdrawn via atm facility.  
        * `internal-transfer` - funds transferred between shared accounts. **[affordability only]**  
        * `external-transfer` - funds transferred to an external account (not included in accounts shared) **[affordability only]**  
        * `loan-interest` - interest charged on a loan account.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        **Credit Classes:**
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `refund` - funds returned due to refund.  
        * `direct-credit` - funds deposited into an account.  
        * `interest` - interest earned.  
        * `internal-transfer` - funds transferred between shared accounts. **[affordability only]**  
        * `external-transfer` - funds transferred from an external account (not included in accounts shared) **[affordability only]**  
        * `loan-repayment` - loan repayment credited to a loan account.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `subClass`
      </td>

      <td style={{ textAlign: "left" }}>
        Attribute includes a `code` and `title` property. The `subClass` attribute will only return values for payment transactions (i.e. will be empty for all others) ( **[affordability only]** - HEC classification class is returned by default **or** custom class is returned if configured - ask us about custom category mapping)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `links`
      </td>

      <td style={{ textAlign: "left" }}>
        A links object containing the following members:
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `account` link to the account  

        * `institution` link to institution  

        (note: no link to self)
      </td>
    </tr>
  </tbody>
</Table>

```json Definition
GET /users/{user.id}/affordability/{affordability.id}/transactions
```

```json Example Request
GET /users/115dc708/affordability/9dedbb28/transactions HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.1 200 OK
Content-Type: application/json

{
  "type": "list",
  "count": 500,
  "size": 4434,
  "data": [
    {
      "type": "transaction",
      "id": "8272d3cb",
      "status": "posted",
      "description": "DDEBIT Only About Children Seaforth",
      "amount": "-114.88",
      "account": "5b45bd2e",
      "balance": "-114.34",
      "direction": "debit",
      "class": "payment",
      "institution": "AU00000",
      "transactionDate": "",
      "postDate": "2017-06-12T00:00:00Z",
      "subClass": {
        "title": "Formal child care services nec",
        "code": "0801050199"
      },
      "links": {
        "account": "https://au-api.basiq.io/users/115dc708/accounts/5b45bd2e",
        "institution": "https://au-api.basiq.io/institutions/AU00000"
      }
    },
    {
      "type": "transaction",
      "id": "4258e66b",
      "status": "posted",
      "description": "TFR Acc14000 TO 12389",
      "amount": "-500.00",
      "account": "5b45bd2e",
      "balance": "7895.00",
      "direction": "debit",
      "class": "internal-transfer",
      "institution": "AU00000",
      "transactionDate": "",
      "postDate": "2017-06-13T00:00:00Z",
      "subClass": null,
      "links": {
        "account": "https://au-api.basiq.io/users/115dc708/accounts/5b45bd2e",
        "institution": "https://au-api.basiq.io/institutions/AU00000"
      }
    },
  ],
  "links": {
    "self": "https://au-api.basiq.io/users/115dc708/affordability/9dedbb28/transactions",
    "next": "https://au-api.basiq.io/users/115dc708/affordability/9dedbb28/transactions?next=9b7d9a64"
  }
}
```
