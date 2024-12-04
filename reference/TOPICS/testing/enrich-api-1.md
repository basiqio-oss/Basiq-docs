---
title: Enrich API
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
The Enrich API returns merchant metadata regarding name, location and category.

This service can be tested using bank transaction data that you provide.  You can use real bank transaction data and the Enrich API will return enriched records for those transactions. Note that the same endpoint is utilised for both testing and production users, however a limit of 100 queries is set for testing users. 

[block:callout]
{
  "type": "warning",
  "body": "Contact us (via the \"help\" icon at the bottom of the page) to have your Enrich access enabled."
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "You will need to ensure that the search query is **url encoded** before calling the resource and must contain at least 3 characters.\n\nExample queries:\nq=garfish%20MANLY%20NS&country=AU&institution=AU06703&accountType=transaction&amount=-12.95\nq=garfish%20MANLY%20NS&institution= AU13601"
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Example Queries",
    "h-1": "",
    "0-0": "1. `GARFISH MANLY NS`",
    "0-1": "hooli2016",
    "2-0": "3. `HARVEY NORMAN AV/IT BALGOWLAH AU`",
    "2-1": "django",
    "4-0": "5. `KMART 1055 WARRIEWOOD AU`",
    "4-1": "tabsnotspaces",
    "5-0": "6. `KAKADU LODGE & CARAV JABIRU AU`",
    "3-0": "4. `CALTEX ALDINGA BEACH ALDINGA BEACHAU`",
    "1-0": "2. `12 VOLT DIRECT PTY L LONSDALE AU`"
  },
  "cols": 1,
  "rows": 6
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "GET enrich?q=garfish%20MANLY%20NS&country=AU&institution=AU06703&accountType=transaction&amount=-12.95 HTTP/1.1\nContent-Type: application/json\nAuthorization: Bearer YOUR_ACCESS_TOKEN\n",
      "language": "json"
    }
  ],
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n    \"type\": \"enrich\",\n    \"direction\": \"debit\",\n    \"class\": \"payment\",\n    \"data\": {\n        \"merchant\": {\n            \"businessName\": \"Garfish Manly\",\n            \"website\": \"http://garfish.com.au/garfish-manly/\",\n            \"phoneNumber\": {\n                \"local\": \"(02) 9977 0707\",\n                \"international\": \"+61 2 9977 0707\"\n            }\n        },\n        \"location\": {\n            \"routeNo\": \"39\",\n            \"route\": \"E Esplanade\",\n            \"postalCode\": \"2095\",\n            \"suburb\": \"Manly\",\n            \"state\": \"NSW\",\n            \"country\": \"Australia\",\n            \"formattedAddress\": \"1/39 E Esplanade, Manly NSW 2095\",\n            \"geometry\": {\n                \"lat\": \"-33.79988520000001\",\n                \"lng\": \"151.2858021\"\n            }\n        },\n        \"category\": {\n            \"anzsic\": {\n                \"division\": {\n                    \"code\": \"H\",\n                    \"title\": \"Accommodation and  Food Services\"\n                },\n                \"subdivision\": {\n                    \"code\": \"45\",\n                    \"title\": \"Food and Beverage Services\"\n                },\n                \"group\": {\n                    \"code\": \"451\",\n                    \"title\": \"Cafes, Restaurants and Takeaway Food Services\"\n                },\n                \"class\": {\n                    \"code\": \"4511\",\n                    \"title\": \"Cafes and Restaurants\"\n                }\n            }\n        }\n    },\n    \"links\": {\n        \"self\": \"https://au-api.basiq.io/enrich?country=AU&institution=AU06703&q=garfish+MANLY+NS\"\n    }\n}",
      "language": "json",
      "name": "Returns merchant, category, location"
    }
  ],
  "sidebar": true
}
[/block]