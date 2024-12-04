---
title: Transactions
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
A transaction object is created whenever money is debited or credited from a particular account.

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
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Value is "transaction".
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **id**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Uniquely identifies the transaction for this connection.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **status**\
        *enum, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Identifies if a transaction is `pending` or `posted`. A pending transaction is an approved debit or credit transaction that has not been fully processed yet (i.e. has not been posted). Find out more about [pending transaction and how to deal with them within your app.](http://docs.basiq.io/the-basiq-platform/what-is-a-pending-transaction)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **description**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        The transaction description as submitted by the institution.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **postDate**\
        *string, readonly* 
      </td>

      <td style={{ textAlign: "left" }}>
        Date the transaction was posted (this is the same date that appears on a bank statement). This value is null if the record is pending.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **transactionDate**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Date that the user executed the transaction. Note that not all transactions provide this value (varies by institution).
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **amount**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction amount. Outgoing funds are expressed as negative values.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **balance**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Value of the account balance at time the transaction was completed.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **bankCategory**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Category as defined by the institution itself. Note that not all institutions define this category.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **class**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Identifies if the transaction is of debit or credit type. This object contains a list of the following types of subclasses: 

        **Debit Subclasses:**

        * `bank-fee` - a fee incurred by the user from their bank e.g. ATM withdrawal fee.
        * `direct-debit` - funds directly debited from the user’s bank account.
        * `payment` - payment made to a merchant.
        * `cash-withdrawal` - funds withdrawn via atm facility.
        * `internal-transfer` - funds transferred to an account (within the same connection).
        * `external-transfer` - funds transferred to an account (outside of the connection).

        **Credit Subclasses:**

        * `refund` - funds returned due to refund.
        * `direct-credit` - funds deposited into an account.
        * `interest` - interest earned.
        * `internal-transfer` - funds received from an account (within the same connection)
        * `external-transfer` - funds received from an account (outside of the same connection)

        **Notes:**

        * Note that some transactions may be classified into multiple subclasses of the same class, for e.g. when a customer pays a merchant and withdraws cash from the same facility.\
          -Debit transactions with a subclass of type `payment` may also include details of the `merchant` through which the payment took place. Merchant details may change over time (e.g. businesses may change address) - Basiq retains copies of these changes, and will ensure that the correct details are returned with each transaction record to indicate the validity at the date the payment took place.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **[account](https://basiq.readme.io/v0.9/reference#accounts)**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        User's accounts in this institution.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **[institution](https://basiq.readme.io/v0.9/reference#institutions)**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        The institution this transaction relates to.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **[connection](https://basiq.readme.io/v0.9/reference#connections)**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        The connection this transaction relates to.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **links**\
        *object, read-only*
      </td>

      <td style={{ textAlign: "left" }}>
        A links object containing the following members:

        * `self` link to the requested transaction
      </td>
    </tr>
  </tbody>
</Table>

```json Example Transaction Object
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
              "saturday": [                
              ],
              "sunday": [              
              ]
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
