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
[block:callout]
{
  "type": "info",
  "body": "Added ability to retrieve fully enriched data via Transactions endpoint for **partners enabled for Enrich API **. This means, no extra round trip to Enrich endpoint for each transaction.  For partners not enabled for Enrich then the attribute will return null.",
  "title": "Get more Enriched data via Transactions endpoint"
}
[/block]

[block:parameters]
{
  "data": {
    "0-1": "- `merchant`  - details relating to the store or merchant such as business name, website and contact details\n\n-  `location` - details relating to the location of the entity such as address and geocode location\n\n-  `category` - industry standard categorisation with a 4 level hierarchy for banking transactions.\n\n- `merchant.logoMaster` & `merchant.logoThumb` - links to the merchant logos\n\nExample JSON provided, also see [Enrich API](https://api.basiq.io/reference/get_enrich) for full details on attributes returned.\n\n**For partners not enabled for Enrich API then this attribute returns null** -   `\"enrich\": null`",
    "0-0": "`enrich`",
    "h-0": "Attributes"
  },
  "cols": 2,
  "rows": 1
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n    \"type\": \"transaction\",\n    \"id\": \"3733ed4c-1edc-477d-ba78-84eae16ab8cf\",\n    \"status\": \"posted\",\n    \"description\": \"MCDONALDS HEATHERTON HEATHERTON VICAU\",\n    \"amount\": \"-124.69\",\n    \"account\": \"55002a88-d4e9-4814-bdc4-a2aa0ab1db75\",\n    \"balance\": \"0.00\",\n    \"direction\": \"debit\",\n    \"class\": \"payment\",\n    \"institution\": \"AU04301\",\n    \"connection\": \"0987220d-6353-40ea-b0bd-6d68dc51601a\",\n    \"transactionDate\": \"\",\n    \"postDate\": \"2022-12-23T00:00:00Z\",\n    \"subClass\": {\n        \"title\": \"Cafes, Restaurants and Takeaway Food Services\",\n        \"code\": \"451\"\n    },\n    \"enrich\": {\n        \"cleanDescription\": \"MCDONALDS HEATHERTON HEATHERTON VIC\",\n        \"tags\": [],\n        \"merchant\": {\n            \"id\": \"daf5235c-9748-4a2a-8497-186376004029\",\n            \"businessName\": \"McDonald's\",\n            \"website\": \"https://mcdonalds.com.au/?utm_medium=local&utm_source=google%20my%20business&utm_campaign=local%20search&utm_content=vic&utm_term=mcdonalds%20heatherton\",\n            \"abn\": \"43008496928\",\n            \"logoMaster\": \"https://enrich-enrichmerchantslogobucket-6or17iuhdvs9.s3-ap-southeast-2.amazonaws.com/mcdonalds-master.svg\",\n            \"logoThumb\": \"https://enrich-enrichmerchantslogobucket-6or17iuhdvs9.s3-ap-southeast-2.amazonaws.com/mcdonalds-thumb.svg\",\n            \"phoneNumber\": {\n                \"local\": \"(03) 9551 2918\",\n                \"international\": \"+61 3 9551 2918\"\n            }\n        },\n        \"location\": {\n            \"routeNo\": \"414\",\n            \"route\": \"Warrigal Road\",\n            \"postalCode\": \"3202\",\n            \"suburb\": \"Heatherton\",\n            \"state\": \"VIC\",\n            \"country\": \"Australia\",\n            \"formattedAddress\": \"414 Warrigal Rd, Heatherton VIC 3202, Australia\",\n            \"geometry\": {\n                \"lat\": \"-37.9517179\",\n                \"lng\": \"145.0780503\"\n            }\n        },\n        \"category\": {\n            \"anzsic\": {\n                \"division\": {\n                    \"code\": \"H\",\n                    \"title\": \"Accommodation and  Food Services\"\n                },\n                \"subdivision\": {\n                    \"code\": \"45\",\n                    \"title\": \"Food and Beverage Services\"\n                },\n                \"group\": {\n                    \"code\": \"451\",\n                    \"title\": \"Cafes, Restaurants and Takeaway Food Services\"\n                },\n                \"class\": {\n                    \"code\": \"4512\",\n                    \"title\": \"Takeaway Food Services\"\n                },\n                \"subclass\": {\n                    \"code\": \"451200\",\n                    \"title\": \"Takeaway Food Services\"\n                }\n            }\n        }\n    },\n    \"links\": {\n        \"self\": \"https://au-api.basiq.io/users/fa48b8da-ddae-4f09-8de9-70dd9520d523/transactions/3733ed4c-1edc-477d-ba78-84eae16ab8cf\",\n        \"account\": \"https://au-api.basiq.io/users/fa48b8da-ddae-4f09-8de9-70dd9520d523/accounts/55002a88-d4e9-4814-bdc4-a2aa0ab1db75\",\n        \"institution\": \"https://au-api.basiq.io/institutions/AU04301\",\n        \"connection\": null\n    }\n}",
      "language": "json",
      "name": "Enrich enabled transaction object"
    },
    {
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n    \"type\": \"transaction\",\n    \"id\": \"3733ed4c-1edc-477d-ba78-84eae16ab8cf\",\n    \"status\": \"posted\",\n    \"description\": \"MCDONALDS HEATHERTON HEATHERTON VICAU\",\n    \"amount\": \"-124.69\",\n    \"account\": \"55002a88-d4e9-4814-bdc4-a2aa0ab1db75\",\n    \"balance\": \"0.00\",\n    \"direction\": \"debit\",\n    \"class\": \"payment\",\n    \"institution\": \"AU04301\",\n    \"connection\": \"0987220d-6353-40ea-b0bd-6d68dc51601a\",\n    \"transactionDate\": \"\",\n    \"postDate\": \"2022-12-23T00:00:00Z\",\n    \"subClass\": {\n        \"title\": \"Cafes, Restaurants and Takeaway Food Services\",\n        \"code\": \"451\"\n    },\n    \"enrich\": null,\n    \"links\": {\n        \"self\": \"https://au-api.basiq.io/users/fa48b8da-ddae-4f09-8de9-70dd9520d523/transactions/3733ed4c-1edc-477d-ba78-84eae16ab8cf\",\n        \"account\": \"https://au-api.basiq.io/users/fa48b8da-ddae-4f09-8de9-70dd9520d523/accounts/55002a88-d4e9-4814-bdc4-a2aa0ab1db75\",\n        \"institution\": \"https://au-api.basiq.io/institutions/AU04301\",\n        \"connection\": null\n    }\n}",
      "language": "json",
      "name": "Enrich disabled"
    }
  ]
}
[/block]