---
title: Transactions
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
A transaction object is created whenever money is debited or credited from a particular account. We have extended transaction object with enriched data. 

> 📘 Get more Enriched data via Transactions endpoint
>
> Added ability to retrieve fully enriched data via Transactions endpoint for **partners enabled for Enrich API** . This means, no extra round trip to Enrich endpoint for each transaction.  For partners not enabled for Enrich then the attribute will return null.

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
        `enrich`
      </td>

      <td style={{ textAlign: "left" }}>
        * `merchant`  - details relating to the store or merchant such as business name, website and contact details

        * `location` - details relating to the location of the entity such as address and geocode location

        * `category` - industry standard categorisation with a 4 level hierarchy for banking transactions.

        * `merchant.logoMaster` & `merchant.logoThumb` - links to the merchant logos

        Example JSON provided, also see [Enrich API](https://api.basiq.io/reference/get_enrich) for full details on attributes returned.

        * \*For partners not enabled for Enrich API then this attribute returns null\*\* -   `"enrich": null`
      </td>
    </tr>
  </tbody>
</Table>

```json Enrich enabled transaction object
HTTP/1.1 200 OK
Content-Type: application/json

{
    "type": "transaction",
    "id": "3733ed4c-1edc-477d-ba78-84eae16ab8cf",
    "status": "posted",
    "description": "MCDONALDS HEATHERTON HEATHERTON VICAU",
    "amount": "-124.69",
    "account": "55002a88-d4e9-4814-bdc4-a2aa0ab1db75",
    "balance": "0.00",
    "direction": "debit",
    "class": "payment",
    "institution": "AU04301",
    "connection": "0987220d-6353-40ea-b0bd-6d68dc51601a",
    "transactionDate": "",
    "postDate": "2022-12-23T00:00:00Z",
    "subClass": {
        "title": "Cafes, Restaurants and Takeaway Food Services",
        "code": "451"
    },
    "enrich": {
        "cleanDescription": "MCDONALDS HEATHERTON HEATHERTON VIC",
        "tags": [],
        "merchant": {
            "id": "daf5235c-9748-4a2a-8497-186376004029",
            "businessName": "McDonald's",
            "website": "https://mcdonalds.com.au/?utm_medium=local&utm_source=google%20my%20business&utm_campaign=local%20search&utm_content=vic&utm_term=mcdonalds%20heatherton",
            "abn": "43008496928",
            "logoMaster": "https://enrich-enrichmerchantslogobucket-6or17iuhdvs9.s3-ap-southeast-2.amazonaws.com/mcdonalds-master.svg",
            "logoThumb": "https://enrich-enrichmerchantslogobucket-6or17iuhdvs9.s3-ap-southeast-2.amazonaws.com/mcdonalds-thumb.svg",
            "phoneNumber": {
                "local": "(03) 9551 2918",
                "international": "+61 3 9551 2918"
            }
        },
        "location": {
            "routeNo": "414",
            "route": "Warrigal Road",
            "postalCode": "3202",
            "suburb": "Heatherton",
            "state": "VIC",
            "country": "Australia",
            "formattedAddress": "414 Warrigal Rd, Heatherton VIC 3202, Australia",
            "geometry": {
                "lat": "-37.9517179",
                "lng": "145.0780503"
            }
        },
        "category": {
            "anzsic": {
                "division": {
                    "code": "H",
                    "title": "Accommodation and  Food Services"
                },
                "subdivision": {
                    "code": "45",
                    "title": "Food and Beverage Services"
                },
                "group": {
                    "code": "451",
                    "title": "Cafes, Restaurants and Takeaway Food Services"
                },
                "class": {
                    "code": "4512",
                    "title": "Takeaway Food Services"
                },
                "subclass": {
                    "code": "451200",
                    "title": "Takeaway Food Services"
                }
            }
        }
    },
    "links": {
        "self": "https://au-api.basiq.io/users/fa48b8da-ddae-4f09-8de9-70dd9520d523/transactions/3733ed4c-1edc-477d-ba78-84eae16ab8cf",
        "account": "https://au-api.basiq.io/users/fa48b8da-ddae-4f09-8de9-70dd9520d523/accounts/55002a88-d4e9-4814-bdc4-a2aa0ab1db75",
        "institution": "https://au-api.basiq.io/institutions/AU04301",
        "connection": null
    }
}
```
```json Enrich disabled
HTTP/1.1 200 OK
Content-Type: application/json

{
    "type": "transaction",
    "id": "3733ed4c-1edc-477d-ba78-84eae16ab8cf",
    "status": "posted",
    "description": "MCDONALDS HEATHERTON HEATHERTON VICAU",
    "amount": "-124.69",
    "account": "55002a88-d4e9-4814-bdc4-a2aa0ab1db75",
    "balance": "0.00",
    "direction": "debit",
    "class": "payment",
    "institution": "AU04301",
    "connection": "0987220d-6353-40ea-b0bd-6d68dc51601a",
    "transactionDate": "",
    "postDate": "2022-12-23T00:00:00Z",
    "subClass": {
        "title": "Cafes, Restaurants and Takeaway Food Services",
        "code": "451"
    },
    "enrich": null,
    "links": {
        "self": "https://au-api.basiq.io/users/fa48b8da-ddae-4f09-8de9-70dd9520d523/transactions/3733ed4c-1edc-477d-ba78-84eae16ab8cf",
        "account": "https://au-api.basiq.io/users/fa48b8da-ddae-4f09-8de9-70dd9520d523/accounts/55002a88-d4e9-4814-bdc4-a2aa0ab1db75",
        "institution": "https://au-api.basiq.io/institutions/AU04301",
        "connection": null
    }
}
```
