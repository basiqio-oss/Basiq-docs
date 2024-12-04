---
title: Events
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
The event object represents an event that has occurred via another endpoint such as create user, update account or  failed job.  This feature is in `alpha` and this first release provides support for [user](ref:users) event types: `user.created`, `user.updated`, `user.deleted`.
[block:parameters]
{
  "data": {
    "0-0": "`type`",
    "h-0": "Attributes",
    "0-1": "Value is \"event\".",
    "1-0": "`id`",
    "1-1": "Uniquely identifies the event.",
    "2-0": "`createdDate`",
    "2-1": "Timestamp of event creation, UTC, RFC 3339 format e.g. \"2021-06-23T10:29:15Z\",",
    "3-0": "`eventType`",
    "3-1": "Identifies enum relating to the event type e.g `user.deleted`",
    "4-0": "`userId`",
    "4-1": "The id of the [user](ref:users) resource the event is created for.",
    "5-0": "`dataRef`",
    "5-1": "A URI reference to the data relating to the event e.g. link to the [account object](ref:retrieve-an-account)",
    "6-0": "`data`",
    "6-1": "The payload that relates to the event. Note that all event types should include the same object type schema as defined in the API e.g. if an event of type user.created occurs, then the [user](ref:users)  schema is included within the event.",
    "7-0": "`links`",
    "7-1": "A links object contains:\n\n- `self` link to the requested event"
  },
  "cols": 2,
  "rows": 8
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"type\": \"event\",\n    \"id\": \"40f8bb39\",\n    \"createdDate\": \"2021-06-23T10:29:15Z\",\n    \"eventType\": \"user.deleted\",\n    \"userId\": \"86d1124d\",\n    \"dataRef\": \"https://au-api.basiq.io/users/86d1124d\",\n    \"data\": {\n        \"email\": \"test@updatemyemail.com\",\n        \"firstName\": \"Joe\",\n        \"id\": \"86d1124d\",\n        \"lastName\": \"Bloggs\",\n        \"links\": {\n            \"self\": \"https://au-api.basiq.io/users/86d1124d\"\n        },\n        \"mobile\": \"+61410777555\",\n        \"type\": \"user\"\n    },\n    \"links\": {\n        \"self\": \"https://au-api.basiq.io/events/40f8bb39\"\n    }\n}",
      "language": "json",
      "name": "Example Event Object"
    }
  ],
  "sidebar": true
}
[/block]