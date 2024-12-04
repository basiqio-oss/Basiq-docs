---
title: List all transactions
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
Use this collection to retrieve a list of [transactions](https://basiq.readme.io/v0.9/reference#transactions). The transactions are returned sorted by posted date descending order.
[block:parameters]
{
  "data": {
    "0-0": "**filter[x.y]**\n*string, optional*",
    "h-0": "Arguments",
    "0-1": "Filters transaction collection by given filter. Syntax is: `?filter[property.id]=value` Possible filters include:\n- `filter[account.id]` filters transactions by [account](https://basiq.readme.io/v0.9/reference#accounts) ID. For example: filter[account.id]=1",
    "1-0": "**fromDate**\n*string, optional*",
    "1-1": "Request transactions with `postDate` value from given date and upwards. Can be combined with `toDate` argument. Format is YYYY-MM-DD.",
    "2-0": "**toDate**\n*string, optional*",
    "2-1": "Request transactions with `postDate` up to given date. Can be combined with `fromDate` argument. Format is YYYY-MM-DD."
  },
  "cols": 2,
  "rows": 3
}
[/block]
Returns
Returns a list of transaction resources, or an [error](https://basiq.readme.io/v0.9/reference#errors).
[block:code]
{
  "codes": [
    {
      "code": "GET /connections/{connection.id}/transactions",
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
      "code": "GET /connections/1/transactions HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
      "language": "json",
      "name": "Example Request"
    }
  ],
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"list\",\n  \"data\": [\n    {\n      \"type\": \"transaction\",\n      \"id\": \"fx789e\",\n      \"status\": \"posted\",\n      \"description\": \"FLIGHT CENTRE CO    BRISB    QL\",\n      \"postDate\": \"2016-01-01\",\n      \"transactionDate\": \"\",\n      \"amount\": \"-139.98\",\n      \"balance\": \"356.50\",\n      \"bankCategory\": \"\",\n      \"class\": {\n        \"type\": \"debit\",\n        \"subclass\": [\n          {\n            \"type\": \"payment\",\n            \"merchant\": {\n              \"type\": \"merchant\",\n              \"id\": \"88ab27\",\n              \"created\": \"2015-09-27T16:23:02Z\",\n              \"updated\": \"2015-09-27T16:23:02Z\",\n              \"identity\": {\n                \"entityName\": \"FLIGHT CENTRE TRAVEL GROUP LIMITED\",\n                \"businessName\": \"FLIGHT CENTRE\",\n                \"businessNumber\": \"25003377188\",\n                \"status\": \"active\",\n                \"phoneNumber\": {\n                  \"local\": \"(07) 3221 4821\",\n                  \"international\": \"+61 7 3221 4821\"\n                },\n                \"website\": \"https://www.flightcentre.com.au/\",\n                \"operatingHours\": {\n                  \"monday\": [\n                    {\n                      \"begin\": \"09:00\",\n                      \"end\": \"17:30\"\n                    }\n                  ],\n                  \"tuesday\": [\n                    {\n                      \"begin\": \"09:00\",\n                      \"end\": \"17:30\"\n                    }\n                  ],\n                  \"wednesday\": [\n                    {\n                      \"begin\": \"09:00\",\n                      \"end\": \"17:30\"\n                    }\n                  ],\n                  \"thursday\": [\n                    {\n                      \"begin\": \"09:00\",\n                      \"end\": \"17:30\"\n                    }\n                  ],\n                  \"friday\": [\n                    {\n                      \"begin\": \"09:00\",\n                      \"end\": \"12:00\"\n                    },\n                    {\n                      \"begin\": \"12:30\",\n                      \"end\": \"17:30\"\n                    }\n                  ],\n                  \"saturday\": [],\n                  \"sunday\": []\n                }\n              },\n              \"location\": {\n                \"routeNo\": \"327\",\n                \"route\": \"George Street\",\n                \"postalCode\": \"4000\",\n                \"locality\": {\n                  \"longName\": \"Brisbane City\",\n                  \"shortName\": \"Brisbane\"\n                },\n                \"administrativeArea2\": {\n                  \"longName\": \"Brisbane City\",\n                  \"shortName\": \"Brisbane City\"\n                },\n                \"administrativeArea1\": {\n                  \"longName\": \"Queensland\",\n                  \"shortName\": \"QLD\"\n                },\n                \"country\": {\n                  \"name\": \"Australia\",\n                  \"code\": \"AU\"\n                },\n                \"formattedAddress\": \"327 George St Brisbane City QLD 4000 Australia\",\n                \"geometry\": {\n                  \"lat\": \"-27.4687768\",\n                  \"lng\": \"153.0216079\"\n                }\n              },\n              \"classification\": {\n                \"mcc\": {\n                  \"code\": \"4722\",\n                  \"title\": \"Travel Agencies and Tour Operations\"\n                },\n                \"anzsic\": {\n                  \"division\": {\n                    \"code\": \"N\",\n                    \"title\": \"Administrative and Support Services\"\n                  },\n                  \"subdivision\": {\n                    \"code\": \"72\",\n                    \"title\": \"Administrative Services\"\n                  },\n                  \"group\": {\n                    \"code\": \"722\",\n                    \"title\": \"Travel Agency and Tour Arrangement Services\"\n                  },\n                  \"class\": {\n                    \"code\": \"7220\",\n                    \"title\": \"Travel Agency and Tour Arrangement Services\"\n                  }\n                }\n              }\n            }\n          }\n        ]\n      },\n      \"institution\": {\n        \"type\": \"institution\",\n        \"id\": \"AU00101\",\n        \"links\": {\n          \"self\": \"https://au-api.basiq.io/institutions/AU00101\"\n        }\n      },\n      \"connection\": {\n        \"type\": \"connection\",\n        \"id\": \"8fce3b\",\n        \"links\": {\n          \"self\": \"https://au-api.basiq.io/connections/8fce3b\"\n        }\n      },\n      \"account\": {\n        \"type\": \"account\",\n        \"id\": \"s55bf3\",\n        \"links\": {\n          \"self\": \"https://au-api.basiq.io/connections/8fce3b/accounts/s55bf3\"\n        }\n      },\n      \"links\": {\n        \"self\": \"https://au-api.basiq.io/connections/8fce3b/transactions/fx789e\"\n      }\n    }\n  ],\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/connections/8fce3b/transactions\"\n  }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]