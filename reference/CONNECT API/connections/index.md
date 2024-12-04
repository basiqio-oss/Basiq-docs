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
The connection object is created whenever a user links their financial institution with your app. Connections act as conduits that retrieve account holders' data (i.e. accounts and transactions) from the institution and store it against the User object. Connections can be deleted and recreated so it is recommended that apps access accounts via the User object rather than the connection.

After a connection is successfully established, you can fetch data created after this point by refreshing the connection. This process ensures on-demand data synchronization between your system and Institution itself. Basiq recommends using the Smart Cache to ensure you always have access to the latest data.

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
        * `pending` the connection is in this status briefly until credentials are verified

        * `active` the connection is valid (is working!) and the credentials have been verified (the jobs steps will continue)

        * `invalid` the connection is no longer valid and requires the user to update their logon details.  Invalid connections cannot refreshed until the password is updated.
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
        `createdDate`
      </td>

      <td style={{ textAlign: "left" }}>
        UTC Date and Time the connection was created, in RFC 3339 format.
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
        UTC Date and Time the connection was last used, in RFC 3339 format.
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
        `mfaEnabled`
      </td>

      <td style={{ textAlign: "left" }}>
        * \*[new]\*\* Indicates whether MFA (multi factor authentication) is enabled for this connection. Where the value is `true` then expect an additional step in the [Jobs](ref:jobs) response. Otherwise value is `false`.
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
        Available profile data for the logged in user or data sharer.  Where no data is available the attribute is "null". This attribute contains the following properties and will return "null" for data that is unavailable:
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
        * `fullName`

        * `firstName`

        * `lastName`

        * `middleName`

        * `phoneNumbers` - a collection of phone numbers

        * `emailAddresses` - a collection of email addresses

        * `physicalAddresses` - a collection of addresses\
                 \- `addressLine1`\
                 \- `addressLine2`\
                 \- `addressLine3`\
                 \- `postcode`\
                 \- `city`\
                 \- `state`\
                 \- `country`\
                 \- `countryCode`\
                 \- `formattedAddress` - full address as a string
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
        [**institution**](https://basiq.readme.io/v2.0/reference/institutions)
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
        **[accounts](https://basiq.readme.io/v2.0/reference/accounts)**
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

```json Example Connection Object
HTTP/1.1 200 OK
Content-Type: application/json
{
    "type": "connection",
    "id": "c7231718",
    "status": "active",
    "createdDate": "2020-12-02T02:20:49Z",
    "lastUsed": "2020-12-02T02:20:59Z",
    "mfaEnabled": false,
    "profile": {
        "fullName": "Max Wentworth-Smith",
        "firstName": "Max",
        "lastName": "Wentworth-Smith",
        "middleName": "",
        "phoneNumbers": [
            "040534555 ### 991"
        ],
        "emailAddresses": [
            "maxsmith@gmail.com"
        ],
        "physicalAddresses": [
            {
                "addressLine1": "91 Fisher Road",
                "addressLine2": null,
                "addressLine3": null,
                "postcode": "2099",
                "city": "Dee Why",
                "state": "NSW",
                "country": "Australia",
                "countryCode": "AU",
                "formattedAddress": "13/91 Fisher Rd, Dee Why NSW 2099, Australia"
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
                "id": "29a1e18b",
                "accountNo": "2",
                "name": "Transaction 14000",
                "currency": "AUD",
                "class": {
                    "type": "transaction",
                    "product": "Hooli Transaction"
                },
                "balance": "49084.34",
                "availableFunds": "49084.34",
                "lastUpdated": "2020-12-02T02:21:01Z",
                "status": "available",
                "links": {
                    "self": "https://au-api.basiq.io/users/9ac25c19/accounts/29a1e18b",
                    "transactions": "https://au-api.basiq.io/users/9ac25c19/transactions?filter=account.id.eq('29a1e18b')"
                }
            }
        ]
    },
    "links": {
        "self": "https://au-api.basiq.io/users/9ac25c19/connections/c7231718",
        "user": "https://au-api.basiq.io/users/9ac25c19",
        "accounts": "https://au-api.basiq.io/users/9ac25c19/accounts?filter=institution.id.eq('AU00000')",
        "transactions": "https://au-api.basiq.io/users/9ac25c19/transactions?filter=institution.id.eq('AU00000')"
    }
}
```
