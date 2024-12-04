---
title: List all events
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
Use this collection to retrieve a paginated list of events. The events are returned sorted by created date descending order. Events are paginated in chunks of 500. Absence of `next` link means that there are no more pages to retrieve.
[block:parameters]
{
  "data": {
    "0-0": "**limit**\n*string, optional*",
    "0-1": "This represents the maximum number of items that may be included in the response (maximum of 500). Note that by default 500 items are returned if this value is not specified.",
    "2-0": "**next**\n*string, optional*",
    "1-0": "**[filter](https://basiq.readme.io/v2.0/reference#events)**\n*string, optional*",
    "1-1": "This list can be [filtered](https://basiq.readme.io/v2.0/reference#filters) by the following properties:\n\n- `user.id`\n\nOnly equals (eq) and not equals (ne) operations are currently supported.",
    "2-1": "Use this to retrieve the next page when a link to `next` is returned in the response."
  },
  "cols": 2,
  "rows": 3
}
[/block]
**Returns**

Returns a list with a data property that contains an array of events for the past 30 days. Each entry in the array is a separate object. If no data is returned, the resulting array will be empty. Otherwise, this call returns an [error](https://basiq.readme.io/v2.0/reference#errors) in the event of a failure.
[block:code]
{
  "codes": [
    {
      "code": "GET /events",
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
      "code": "GET  /events  HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
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
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n{\n    \"type\": \"list\",\n    \"count\": 3,\n    \"data\": [\n        {\n            \"type\": \"event\",\n            \"id\": \"40f8bb39\",\n            \"createdDate\": \"2021-06-23T10:29:15Z\",\n            \"eventType\": \"user.deleted\",\n            \"userId\": \"86d1124d-77e4-460a-8b3e-c67d50ee177f\",\n            \"dataRef\": \"https://au-api.basiq.io/users/86d1124d\",\n            \"data\": {\n                \"email\": \"test@updatemyemail.com\",\n                \"firstName\": \"Joe\",\n                \"id\": \"86d1124d-77e4-460a-8b3e-c67d50ee177f\",\n                \"lastName\": \"Bloggs\",\n                \"links\": {\n                    \"self\": \"https://au-api.basiq.io/users/86d1124d\"\n                },\n                \"mobile\": \"+61410777555\",\n                \"type\": \"user\"\n            },\n            \"links\": {\n                \"self\": \"https://au-api.basiq.io/events/40f8bb39\"\n            }\n        },\n        {\n            \"type\": \"event\",\n            \"id\": \"8ef41015-cd6f-4a34-b8f3-b83e59526648\",\n            \"createdDate\": \"2021-06-23T10:29:04Z\",\n            \"eventType\": \"user.updated\",\n            \"userId\": \"86d1124d\",\n            \"dataRef\": \"https://au-api.basiq.io/users/86d1124d-77e4-460a-8b3e-c67d50ee177f\",\n            \"data\": {\n                \"email\": \"test@updatemyemail.com\",\n                \"firstName\": \"Joe\",\n                \"id\": \"86d1124d\",\n                \"lastName\": \"Bloggs\",\n                \"links\": {\n                    \"self\": \"https://au-api.basiq.io/users/86d1124d\"\n                },\n                \"mobile\": \"+61410777555\",\n                \"type\": \"user\"\n            },\n            \"links\": {\n                \"self\": \"https://au-api.basiq.io/events/8ef41015\"\n            }\n        },\n        {\n            \"type\": \"event\",\n            \"id\": \"10f94af8-71df-44fe-a1b0-6e74318e52d2\",\n            \"createdDate\": \"2021-06-21T04:42:06Z\",\n            \"eventType\": \"user.created\",\n            \"userId\": \"3e554d6e\",\n            \"dataRef\": \"https://au-api.basiq.io/users/3e554d6e\",\n            \"data\": {\n                \"email\": \"test@test.com\",\n                \"firstName\": \"Joe\",\n                \"id\": \"3e554d6e\",\n                \"lastName\": \"Bloggs\",\n                \"links\": {\n                    \"self\": \"https://au-api.basiq.io/users/3e554d6e\"\n                },\n                \"mobile\": \"+61410777555\",\n                \"type\": \"user\"\n            },\n            \"links\": {\n                \"self\": \"https://au-api.basiq.io/events/10f94af8\"\n            }\n        }\n    ],\n    \"links\": {\n        \"self\": \"https://au-api.basiq.io/events\"\n    }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]