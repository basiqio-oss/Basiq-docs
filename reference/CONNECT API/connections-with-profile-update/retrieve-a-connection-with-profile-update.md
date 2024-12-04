---
title: Retrieve a connection with profile update
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
GET /user/{user.id}/connections/{connection.id}
```

```json Example Request
GET /users/ea3a81/connections/8fce3b HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.1 200 OK
Content-Type: application/json

{
  "type": "connection",
  "id": "8fce3b",
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
