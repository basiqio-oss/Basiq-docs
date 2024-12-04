---
title: Retrieve an event
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
Use this to retrieve the details of a specific event. This request will return back an event object with the latest data. 
[block:parameters]
{
  "data": {
    "0-0": "**id**\n*string, required*",
    "0-1": "The identifier of the event to be retrieved.",
    "h-0": "Arguments"
  },
  "cols": 2,
  "rows": 1
}
[/block]
**Returns**

Returns an account if a valid event ID was provided. Returns an [error](https://basiq.readme.io/v2.0/reference#errors) otherwise.
[block:code]
{
  "codes": [
    {
      "code": "GET /events/{event.id}\n",
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
      "code": "GET /events/40f8bb39 HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN\n",
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
      "code": "HTTP/1.11.1 200 OK\nContent-Type:application/json\n\n{\n    \"type\": \"event\",\n    \"id\": \"40f8bb39\",\n    \"createdDate\": \"2021-06-23T10:29:15Z\",\n    \"eventType\": \"user.deleted\",\n    \"userId\": \"86d1124d\",\n    \"dataRef\": \"https://au-api.basiq.io/users/86d1124d\",\n    \"data\": {\n        \"email\": \"test@updatemyemail.com\",\n        \"firstName\": \"Joe\",\n        \"id\": \"86d1124d\",\n        \"lastName\": \"Bloggs\",\n        \"links\": {\n            \"self\": \"https://au-api.basiq.io/users/86d1124d\"\n        },\n        \"mobile\": \"+61410777555\",\n        \"type\": \"user\"\n    },\n    \"links\": {\n        \"self\": \"https://au-api.basiq.io/events/40f8bb39\"\n    }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]