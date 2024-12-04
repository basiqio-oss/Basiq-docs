---
title: Enrich
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
The Enrich resource enables you to retrieve details by passing in a search `query` containing a bank transaction description. 

The service enriches transaction data with multiple attributes, returning a transaction classification and three metadata components.  The transaction classification will first determine if the transaction is of type payment, transfer, cash-withdrawal, bank-fee etc. The engine then derives merchant information, purchase location and prescribes an industry standard categorisation for each payment transaction.

You can subscribe to one or all of the following three core datasets returned depending on your use case.  
[block:parameters]
{
  "data": {
    "h-0": "Data",
    "0-0": "`Merchant`",
    "1-0": "`Location`",
    "0-1": "Details relating to the store or merchant such as business name, website, ABN and contact details",
    "1-1": "Details relating to the location of the entity such as address and geocode location",
    "2-0": "`Category`",
    "2-1": "Industry standard categorisation with a 4 level hierarchy for banking transactions.",
    "3-0": "`Links`",
    "3-1": "Provides direct link to `self` - original query\nProvides links master and thumb merchant logos"
  },
  "cols": 2,
  "rows": 4
}
[/block]
The query will typically be the full textual description of a transaction record, however the partner calling the API may also optionally pass in more details to make the search more relevant (such as an MCC code). 

**Pre-requisties**

• Prior to calling the enrich service, you will need to be authenticated via the Basiq API service.
• The service will only be accessible to partners that have been enabled.

**Request**

You can call the `enrich` endpoint by passing in the following query parameters:
[block:callout]
{
  "type": "info",
  "body": "You will need to ensure that the search query is **url encoded** before calling the resource and must contain at least 3 characters.",
  "title": ""
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Mandatory Arguments",
    "0-0": "**q**\n*string, required*",
    "0-1": "This is the search string that is used to lookup the entity (merchant) information. \n\n`**q=garfish%20MANLY%20NS**&country=AU&institution=AU06703`",
    "2-0": "**institution**\n*string, required*",
    "2-1": "Identifies the institution from where the transaction was derived. \nThis must be a Basiq recognisable institution ID.\n\n`enrich?METRO%20PETROLEUM%20FR%20FORE&country=AU&accountType=transaction&amount=-12.95&**institution=AU04301**`",
    "4-0": "**country**\n*string, required*",
    "4-1": "Specifies the country the search should be narrowed down to. \nPassing in a country value will limit the search to the specified country. \nThe country must be in [ISO 3166 Alpha-2 format] (https://www.iso.org/obp/ui/#search) \n\n`q=garfish%20MANLY%20NS&**country=AU**&institution=AU06703`",
    "0-2": "",
    "2-2": "",
    "4-2": ""
  },
  "cols": 2,
  "rows": 5
}
[/block]
Note: accountType and amount are mandatory arguments for transaction classification. If these arguments are not provided, the query will be treated as a payment transaction and categorised accordingly.
[block:parameters]
{
  "data": {
    "0-0": "**mcc**\n*string, optional*",
    "0-1": "Merchant classification code as defined by Visa and Mastercard\n\n`q=garfish%20MANLY%20NS&country=AU&institution=AU06703&**mcc=3299**`",
    "h-0": "Optional Arguments",
    "2-0": "**accountType**\n*string, optional*",
    "2-1": "The Account type from which the transaction was derived.\n\n`METRO%20PETROLEUM%20FR%20FORE&country=AU&**accountType=transaction**&institution=AU04301**`\n\n \nValid values:\n\n- transaction\n- credit-card\n- savings\n- mortgage\n- loan\n- foreign",
    "4-0": "**amount**\n*string, optional*",
    "4-1": "The dollar/cent amount relevant to the transaction.\n\n`q=garfish%20MANLY%20NS&country=AU&institution=AU06703&**amount=-12.95**`"
  },
  "cols": 2,
  "rows": 5
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "GET /enrich",
      "language": "json",
      "name": "Definition"
    }
  ],
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "GET enrich?q=METRO%20PETROLEUM%20FR%20FORE&country=AU&accountType=transaction&amount=-12.95&institution=AU04301\nHTTP/1.1\nContent-Type: application/json\nAuthorization: Bearer YOUR_ACCESS_TOKEN\n",
      "language": "json",
      "name": "Example Request"
    }
  ],
  "sidebar": true
}
[/block]
**Response**

The `enrich` endpoint will always return a 200 response to the user, along with a set of results for each of the datasets subscribed to: category, entity and location. If no results are found for the search query then an empty result set is returned. If parameter inputs are invalid an error is returned.

You can subscribe one or all of the following three datasets depending on your use case.  The datasets are described below.
[block:code]
{
  "codes": [
    {
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n    \"type\": \"enrich\",\n    \"direction\": \"debit\",\n    \"class\": \"payment\",\n    \"data\": {\n        \"merchant\": {\n            \"id\": \"15e83d60-7332-4cec-96ab-06cfc4e3d710\",\n            \"businessName\": \"Metro Petroleum\",\n            \"website\": \"http://www.metropetroleum.com.au/\",\n            \"abn\": \"12345767657\"\n            \"phoneNumber\": {\n                \"local\": \"(03) 9471 0283\",\n                \"international\": \"+61 3 9471 0283\"\n            }\n        },\n        \"location\": {\n            \"routeNo\": \"145\",\n            \"route\": \"Spring St\",\n            \"postalCode\": \"3073\",\n            \"suburb\": \"Reservoir\",\n            \"state\": \"VIC\",\n            \"country\": \"Australia\",\n            \"formattedAddress\": \"139/145 Spring St, Reservoir VIC 3073\",\n            \"geometry\": {\n                \"lat\": \"-37.7263016\",\n                \"lng\": \"145.0009305\"\n            }\n        },\n        \"category\": {\n            \"anzsic\": {\n                \"division\": {\n                    \"code\": \"G\",\n                    \"title\": \"Retail Trade\"\n                },\n                \"subdivision\": {\n                    \"code\": \"40\",\n                    \"title\": \"Fuel Retailing\"\n                },\n                \"group\": {\n                    \"code\": \"400\",\n                    \"title\": \"Fuel Retailing\"\n                },\n                \"class\": {\n                    \"code\": \"4000\",\n                    \"title\": \"Fuel Retailing\"\n                }\n            }\n        }\n    },\n    \"links\": {\n        \"self\": \"https://au-api.basiq.io/enrich?country=AU&institution=AU04301&q=METRO+PETROLEUM+FR+FORE\",\n        \"logo-master\": \"https://enrich-enrichmerchantslogobucket-6or17iuhdvs9.s3-ap-southeast-2.amazonaws.com/metro_petroleum-master.png\",\n        \"logo-thumb\": \"https://enrich-enrichmerchantslogobucket-6or17iuhdvs9.s3-ap-southeast-2.amazonaws.com/metro_petroleum-thumb.png\"\n    }\n}\n",
      "language": "json",
      "name": "Example Response: result found"
    }
  ],
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n    \"type\": \"enrich\",\n    \"direction\": \"debit\",\n    \"class\": \"payment\",\n    \"data\": {\n        \"merchant\": null,\n        \"location\": null,\n        \"category\": null\n    },\n    \"links\": {\n        \"self\": \"https://au-api.basiq.io/enrich?accountType=transaction&amount=-12.95&country=AU&institution=AU06703&q=sfdsdfsd\",\n        \"logo-master\": null,\n        \"logo-thumb\": null\n    }\n}\n\n",
      "language": "json",
      "name": "Example Response: no result found"
    }
  ],
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "HTTP/1.1 400 Bad Request\nContent-Type: application/json\n{\n    \"type\": \"list\",\n    \"correlationId\": \"923788f1-72de-11e9-9a9f-a7c155f44712\",\n    \"data\": [\n        {\n            \"type\": \"error\",\n            \"code\": \"parameter-not-valid\",\n            \"title\": \"Parameter value is not valid\",\n            \"detail\": \"accountType is not valid Basiq account type value\",\n            \"source\": {\n                \"parameter\": \"accountType\"\n            }\n        }\n    ]\n}",
      "language": "json"
    }
  ],
  "sidebar": true
}
[/block]
**Attributes**
[block:parameters]
{
  "data": {
    "0-0": "`type`",
    "0-1": "Value is \"enrich\"",
    "2-1": "Debit or Credit transaction",
    "2-0": "`direction`",
    "4-0": "`class`",
    "4-1": "Describes the type of transaction: payment, transfer, cash-withdrawal, bank-fee, interest, refund etc.",
    "h-0": "Enrich"
  },
  "cols": 2,
  "rows": 6
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Merchant",
    "4-0": "`website`",
    "4-1": "The merchant website.",
    "6-0": "`phoneNumber`",
    "6-1": "Provides the `local` and `international` telephone numbers of the merchant.",
    "0-0": "`id`",
    "0-1": "The merchant id.",
    "7-0": "`ABN`",
    "7-1": "Provides the Australian Business Number.",
    "2-0": "`businessName`",
    "2-1": "The merchant business name."
  },
  "cols": 2,
  "rows": 9
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Location",
    "0-0": "`routeNo`",
    "2-0": "`route`",
    "4-0": "`postalCode`",
    "6-0": "`suburb`",
    "0-1": "The street number of the merchant location.",
    "2-1": "The street name of the merchant location.",
    "4-1": "The post code of the merchant location.",
    "6-1": "The suburb of the merchant location.",
    "8-0": "`state`",
    "8-1": "The state of the merchant location.",
    "10-0": "`country`",
    "12-0": "`formattedAddress`",
    "14-0": "`geometry`",
    "10-1": "The country of the merchant location.",
    "12-1": "The full address for the merchant location",
    "14-1": "Contains the `lat` and `lng` coordinates of the merchant location."
  },
  "cols": 2,
  "rows": 16
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Category",
    "0-0": "`class`",
    "2-0": "`group`",
    "4-0": "`subdivision`",
    "6-0": "`division`",
    "6-1": "Details the `code` and `title` of the merchant ANZSIC division.",
    "4-1": "Details the `code` and `title` of the merchant ANZSIC subdivision.",
    "2-1": "Details the `code` and `title` of the merchant ANZSIC group.",
    "0-1": "Details the `code` and `title` of the merchant ANZSIC class."
  },
  "cols": 2,
  "rows": 8
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Links",
    "0-0": "`self`",
    "0-1": "Provides a reference link to the original query.",
    "2-0": "`logo-master`",
    "4-0": "`logo-thumb`",
    "2-1": "Provides link to master logo. Logos are provided in a variety of formats: .svg, .png, .jpg, jpeg, gif. Where null no merchant logo is available.",
    "4-1": "Provides link to thumb logo (where no thumb available master logo is returned for both).  Logos are provided in a variety of formats: .svg, .png, .jpg, jpeg, gif. Where null no merchant logo is available."
  },
  "cols": 2,
  "rows": 6
}
[/block]