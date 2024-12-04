---
title: Events
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
Events mark changes or behaviour in entities and can be used to trigger actions in your application.

## Entities and their events 
[block:parameters]
{
  "data": {
    "h-0": "entity",
    "h-1": "eventType",
    "h-2": "when does this occur",
    "3-0": "`consent`",
    "3-1": "`created`",
    "3-2": "A user has agreed to an applications consent policy which in turn creates a consent policy against the user.",
    "5-0": "",
    "5-1": "`updated`",
    "6-1": "`revoked`",
    "8-0": "`Payout`",
    "16-0": "`user`",
    "16-1": "`created`",
    "8-1": "`created`",
    "9-1": "`failed`",
    "18-1": "`deleted`",
    "5-2": "A user has agreed to an updated consent policy.",
    "6-2": "A user has decided to withdraw consent to share data with an application.",
    "8-2": "When a payout is created.",
    "9-2": "When a payout is failed.",
    "16-2": "A user has been created.",
    "18-2": "A user has been deleted.",
    "17-1": "`updated`",
    "17-2": "A user has been updated.",
    "10-1": "`in-progress`",
    "10-2": "When a payout is in-progress.",
    "0-0": "`connection`",
    "0-1": "`created`",
    "1-1": "`updated`",
    "2-1": "`deleted`",
    "0-2": "When a connection is created.",
    "2-2": "When a connection is deleted.",
    "1-2": "When a connection is updated.",
    "4-1": "`reminder`",
    "4-2": "It's time for a consent reminder.",
    "7-1": "`warning`",
    "7-2": "It's time for a consent warning.",
    "11-1": "`successful`",
    "11-2": "When a payout is successful.",
    "12-0": "`Payrequest`",
    "12-1": "`created`",
    "12-2": "When a payrequest is created.",
    "13-1": "`failed`",
    "14-1": "`in-progress`",
    "15-1": "`successful`",
    "13-2": "When a payrequest is failed.",
    "14-2": "When a payrequest is in-progress.",
    "15-2": "When a payrequest is successful."
  },
  "cols": 3,
  "rows": 19
}
[/block]

[block:callout]
{
  "type": "info",
  "title": "Consent events",
  "body": "Any events around consent must be monitored if your application is using Open Banking data. For more information please read our documentation on [data governance events](ref:data-governance#data-governance-events)."
}
[/block]