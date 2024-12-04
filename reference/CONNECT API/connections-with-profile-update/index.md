---
title: Connections with profile update
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
The connection object is created whenever a user links their financial institution with your app. Connections act as conduits that retrieve account holders' data (i.e. accounts and transactions) from the institution and store it against the User object. Connections can be deleted and recreated so it is recommended that apps access accounts via the User object rather than the connection.

After a connection is successfully established, you can fetch data created after this point by refreshing the connection. This process ensures on-demand data synchronization between your system and Institution itself. Basiq recommends using the Scheduler if connections are to be refreshed multiple times per day.

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
        `type`
      </td>

      <td style={{ textAlign: "left" }}>
        Value is "connection".
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
        `id`
      </td>

      <td style={{ textAlign: "left" }}>
        A string that uniquely identifies the user connection.
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
        `loginId`
      </td>

      <td style={{ textAlign: "left" }}>
        User's institution login ID. This value cannot be read.  *required*
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
        `password`
      </td>

      <td style={{ textAlign: "left" }}>
        User's institution password. This value cannot be read. *required*
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
        `securityCode`
      </td>

      <td style={{ textAlign: "left" }}>
        User's institution security code. This value cannot be read. *conditional*
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
        `secondaryLoginId`
      </td>

      <td style={{ textAlign: "left" }}>
        User's institution secondary login id. This value cannot be read. *conditional*
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
        `status`
      </td>

      <td style={{ textAlign: "left" }}>
        Indicates the connection status. Possible values include:
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
        * `active` the connection is valid (is working!)

        * `invalid` the connection is no longer valid and requires the user to update their logon details
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
        `lastUsed`
      </td>

      <td style={{ textAlign: "left" }}>
        UTC Date and Time of when the connection was last used, in RFC 3339 format.
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
        `profile`
      </td>

      <td style={{ textAlign: "left" }}>
        Profile data relating to the login used to access the institution. Does not apply to PDF or CSV upload connections
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
        [**institution**](https://basiq.readme.io/v2.0/reference#institutions)
      </td>

      <td style={{ textAlign: "left" }}>
        The institution the connection relates to.
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
        **[accounts](https://basiq.readme.io/v2.0/reference#accounts)**
      </td>

      <td style={{ textAlign: "left" }}>
        User's accounts in this institution.
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
        **links**
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
        * `self` link to the requested connection

        * `accounts` link to the accounts associated with this connection

        * `transactions` link to the transactions associated with this connection
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

> 📘 To minimise the exposure of credential details, loginId, password and securityCode are omitted from all server responses.

> 📘 profile data
>
> The profile attribute is not populated for all institutions. This data is exposed only when available from the institution. Applies only to direct connections to institutions and not to statement uploads.

```json Example Connection Object
{
  "type": "connection",
  "id": "8fce3b",
  "loginId": ...,
  "password": ...,
  "status": "active",
  "lastUsed": "2017-09-28T11:15:09Z",
  "profile": {
        "fullName": "Test User",
        "firstName": "Test",
        "lastName": "User",
        "middleName": "",
        "phoneNumbers": [],
        "emailAddresses": [],
        "physicalAddresses": [
            {
                "addressLine1": "1 SMITH STREET, Sydney, NSW, 2000",
                "addressLine2": null,
                "addressLine3": null,
                "postcode": "2000",
                "city": "Sydney",
                "state": "NSW",
                "country": "Australia",
                "countryCode": "AU",
                "formattedAddress": "1 Smith Street, Sydney NSW 2000, Australia"
            }
        ]
  },
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
    "accounts": "https://au-api.basiq.io/users/ea3a81/accounts?filter=institution.id.eq('AU00000')",
    "transactions": "https://au-api.basiq.io/users/ea3a81/transactions?filter=institution.id.eq('AU00000')"
  }
}
```
