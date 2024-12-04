---
title: Retrieve a transaction
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
Retrieves the details of an existing transaction. You need only supply the unique transaction identifier.

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
        *string, required*
      </td>

      <td style={{ textAlign: "left" }}>
        The identifier of the transaction to be retrieved.
      </td>
    </tr>
  </tbody>
</Table>

**Returns**

Returns a transaction if a valid transaction ID was provided. Returns an [error](https://basiq.readme.io/v0.9/reference#errors) otherwise.

```json Definition
GET /connections/{connection.id}/transactions/{transaction.id}
```

```json Example Request
GET /connections/1/transactions/1 HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.1 200 OK
Content-Type: application/json

{
  "type": "transaction",
  "id": "fx789e",
  "status": "posted",
  "description": "FLIGHT CENTRE CO    BRISB    QL",
  "postDate": "2016-01-01",
  "transactionDate": "",
  "amount": "-139.98",
  "balance": "356.50",
  "bankCategory": "",
  "class": {
    "type": "debit",
    "subclass": [
      {
        "type": "payment",
        "merchant": {
          "type": "merchant",
          "id": "88ab27",
          "created": "2015-09-27T16:23:02Z",
          "updated": "2015-09-27T16:23:02Z",
          "identity": {
            "entityName": "FLIGHT CENTRE TRAVEL GROUP LIMITED",
            "businessName": "FLIGHT CENTRE",
            "businessNumber": "25003377188",
            "status": "active",
            "phoneNumber": {
              "local": "(07) 3221 4821",
              "international": "+61 7 3221 4821"
            },
            "website": "https://www.flightcentre.com.au/",
            "operatingHours": {
              "monday": [
                {
                  "begin": "09:00",
                  "end": "17:30"
                }
              ],
              "tuesday": [
                {
                  "begin": "09:00",
                  "end": "17:30"
                }
              ],
              "wednesday": [
                {
                  "begin": "09:00",
                  "end": "17:30"
                }
              ],
              "thursday": [
                {
                  "begin": "09:00",
                  "end": "17:30"
                }
              ],
              "friday": [
                {
                  "begin": "09:00",
                  "end": "12:00"
                },
                {
                  "begin": "12:30",
                  "end": "17:30"
                }
              ],
              "saturday": [],
              "sunday": []
            }
          },
          "location": {
            "routeNo": "327",
            "route": "George Street",
            "postalCode": "4000",
            "locality": {
              "longName": "Brisbane City",
              "shortName": "Brisbane"
            },
            "administrativeArea2": {
              "longName": "Brisbane City",
              "shortName": "Brisbane City"
            },
            "administrativeArea1": {
              "longName": "Queensland",
              "shortName": "QLD"
            },
            "country": {
              "name": "Australia",
              "code": "AU"
            },
            "formattedAddress": "327 George St Brisbane City QLD 4000 Australia",
            "geometry": {
              "lat": "-27.4687768",
              "lng": "153.0216079"
            }
          },
          "classification": {
            "mcc": {
              "code": "4722",
              "title": "Travel Agencies and Tour Operations"
            },
            "anzsic": {
              "division": {
                "code": "N",
                "title": "Administrative and Support Services"
              },
              "subdivision": {
                "code": "72",
                "title": "Administrative Services"
              },
              "group": {
                "code": "722",
                "title": "Travel Agency and Tour Arrangement Services"
              },
              "class": {
                "code": "7220",
                "title": "Travel Agency and Tour Arrangement Services"
              }
            }
          }
        }
      }
    ]
  },
  "institution": {
    "type": "institution",
    "id": "AU00101",
    "links": {
      "self": "https://au-api.basiq.io/institutions/AU00101"
    }
  },
  "connection": {
    "type": "connection",
    "id": "8fce3b",
    "links": {
      "self": "https://au-api.basiq.io/connections/8fce3b"
    }
  },
  "account": {
    "type": "account",
    "id": "s55bf3",
    "links": {
      "self": "https://au-api.basiq.io/connections/8fce3b/accounts/s55bf3"
    }
  },
  "links": {
    "self": "https://au-api.basiq.io/connections/8fce3b/transactions/fx789e"
  }
}
```
