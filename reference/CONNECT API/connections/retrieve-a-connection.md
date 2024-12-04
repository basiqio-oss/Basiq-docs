---
title: Retrieve a connection
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
Use this to retrieve details of a specific connection. This request will return back a connection object with most of the fields that were submitted when the connection was first created. The connection object will also return a list of URLs to the associated account, transaction and institution objects.

The status property of the connection object identifies the state of the connection. Use this to work out if the connection is still valid, or whether to take further action (e.g. if the connection credentials are no longer valid you may ask the user to re-submit their details).

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
        **id**
        *required*
      </td>

      <td style={{ textAlign: "left" }}>
        The identifier of the connection to be retrieved.
      </td>
    </tr>
  </tbody>
</Table>

> 📘 Note that due to security the loginId, password, securityCode are never returned.

**Returns**

Returns a connection if a valid connection ID was provided. Returns an [error](https://basiq.readme.io/v2.0/reference#errors) otherwise.

```json
GET /users/{user.id}/connections/{connection.id}
```

```json Example Request
GET /users/ea3a81/connections/8fce3b HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

> 🚧 Profile data
>
> Profile data represents the name, phone, email and address of the logged in user or data sharer.  Only data made available by institution can be returned. An institution may offer the option for a customer to hide all personal data or add 2FA to access the data - in this case no data would be returned for all data points.  Note, that when a Connection is deleted - the profile data will also be deleted. If a phone number or email address is masked by the institution - the string will be shown exactly as it is provided by the institution.

```json Example Response
HTTP/1.1 200 OK
Content-Type: application/json

{
  "type": "connection",
  "id": "8fce3b",
  "status": "active",
  "createdDate": "2020-10-02T05:53:05Z",
  "lastUsed": "2020-12-02T02:21:02Z",
  "profile": {
    "fullName": "Max James",
    "firstName": "Max",
    "lastName": "James",
    "middleName": "",
    "phoneNumbers": [
      "XXXX 888 991"
    ],
    "emailAddresses": [
      "XXXXames@hotmail.com"
    ],
    "physicalAddresses": [
      {
        "addressLine1": "13/91 Fisher Rd",
        "addressLine2": null,
        "addressLine3": null,
        "postcode": "2099",
        "city": null,
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
          "transactions": "https://au-api.basiq.io/users/ea3a81/transactions?filter=account.id.eq('s55bf3')"
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
