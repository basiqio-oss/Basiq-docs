---
title: Connections
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
The connection object is created whenever a user links their financial institution with your app. Once a connection is successfully created - you can use it to obtain the user's latest financial data i.e. accounts and transactions.\
After a connection is successfully established, you can fetch data created after this point by [refreshing](https://basiq.readme.io/v1.0/reference#refresh-a-connection) the connection. This process ensures on-demand data syncronization between your system and Institution itself.

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
        **type**
        *string, read-only*
      </td>

      <td style={{ textAlign: "left" }}>
        Value is "connection".
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **id**\
        *string, read-only*
      </td>

      <td style={{ textAlign: "left" }}>
        A string that uniquely identifies the user connection.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **loginId**\
        *string, required*
      </td>

      <td style={{ textAlign: "left" }}>
        User's institution login ID. This value cannot be read.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **password**\
        *string, required*
      </td>

      <td style={{ textAlign: "left" }}>
        User's institution password. This value cannot be read.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **securityCode**\
        *string, conditional*
      </td>

      <td style={{ textAlign: "left" }}>
        User's institution security code. This value cannot be read.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **secondaryLoginId**\
        *string, conditional*
      </td>

      <td style={{ textAlign: "left" }}>
        User's institution secondary login id. This value cannot be read.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **status**\
        *enum, read-only* 
      </td>

      <td style={{ textAlign: "left" }}>
        Indicates the connection status. Possible values include:

        * `active` the connection is valid (is working!)
        * `invalid` the connection is no longer valid and requires the user to update their logon details
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **lastUsed**\
        *string, optional*
      </td>

      <td style={{ textAlign: "left" }}>
        UTC Date and Time of when the connection was last used, in RFC 3339 format.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [**institution**](https://basiq.readme.io/v1.0/reference#institutions)\
        *object, read-only*
      </td>

      <td style={{ textAlign: "left" }}>
        The institution the connection relates to.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **[accounts](https://basiq.readme.io/v1.0/reference#accounts)**\
        *list of objects, read-only*
      </td>

      <td style={{ textAlign: "left" }}>
        User's accounts in this institution.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **links**\
        *object, read-only*
      </td>

      <td style={{ textAlign: "left" }}>
        A links object containing the following members:

        * `self` link to the requested connection
        * `accounts` link to the accounts associated with this connection
        * `transactions` link to the transactions associated with this connection
      </td>
    </tr>
  </tbody>
</Table>

> 📘 To minimise the exposure of credential details, loginId, password and securityCode are omitted from all server responses.

```json Example Connection Object
{
  "type": "connection",
  "id": "8fce3b",
  "loginId": ...,
  "password": ...,
  "status": "active",
  "lastUsed": "2017-09-28T11:15:09Z",
  "institution": {
    "type": "institution",
    "id": "AU00000",
    "links": {
      "self": "https://au-api.basiq.io/institutions/AU00000"
    }
  },
  "accounts": {
    "type": "list",
    "data": [
      {
        "type": "account",
        "id": "s55bf3",
        "accountNo": "105148119695",
        "name": "Business account",
        "currency": "AUD",
        "balance": "10.00",
        "availableFunds": "0.00",
        "lastUpdated": "2017-09-28T11:15:09.756Z",
        "class": {
            "type": "savings",
            "product": "Saver"
        },
        "status": "available",
        "links": {
          "self": "https://au-api.basiq.io/users/ea3a81/accounts/s55bf3",
          "transactions": "https://au-api.basiq.io/users/ea3a81/transactions?filter=account.id.eq('s55bf3')'"
        }
      },
      {
        "type": "account",
        "id": "ar36y2",
        "accountNo": "533705985043",
        "name": "Choice Account",
        "currency": "AUD",
        "balance": "-10.09",
        "availableFunds": "0.00",
        "lastUpdated": "2017-09-28T11:15:09.756Z",
        "class": {
            "type": "savings",
            "product": "Saver"
        },
        "status": "available",
        "links": {
          "self": "https://au-api.basiq.io/users/ea3a81/accounts/ar36y2",
          "transactions": "https://au-api.basiq.io/users/ea3a81/transactions?filter=account.id.eq('ar36y2')"
        }
      }
    ]
  },
  "links": {
    "self": "https://au-api.basiq.io/users/ea3a81/connections/8fce3b",
    "accounts": "https://au-api.basiq.io/users/ea3a81/accounts?filter=connection.id.eq('8fce3b')",
    "transactions": "https://au-api.basiq.io/users/ea3a81/transactions?filter=connection.id.eq('8fce3b')"
  }
}
```
