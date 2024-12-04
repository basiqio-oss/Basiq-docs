---
title: Error codes
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
Below you will find details for our various response codes.
[block:parameters]
{
  "data": {
    "h-0": "Code",
    "h-1": "Description",
    "0-0": "**invalid-credentials** ",
    "0-1": "**Invalid Attribute **\nCannot login to target institution using supplied credentials. Please check credentials and try again.",
    "1-1": "**Invalid Attribute **\nRequested resource is not found. Check details message.",
    "1-0": "**resource-not-found** ",
    "2-1": "**Invalid Attribute **\nResource already exists. Check details message.",
    "2-0": "**resource-already-exists** ",
    "3-0": "**unsupported-content-type** ",
    "3-1": "**Invalid Attribute **\nRequested content type is not supported.",
    "4-0": "**unsupported-accept** ",
    "4-1": "**Invalid Attribute **\nAccept type is not supported.",
    "5-0": "**invalid-content** ",
    "5-1": "**Invalid Attribute **\nInvalid request content. Check details message.",
    "6-0": "**parameter-not-supplied** ",
    "6-1": "**Missing Attribute **\nRequired parameter not supplied. Check details and source message.",
    "7-0": "**parameter-not-valid** ",
    "7-1": "**Invalid Attribute **\nParameter value is not valid. Check details and source message.",
    "8-0": "**internal-server-error** ",
    "8-1": "**Server Error **\nInternal server error. Please contact support.",
    "9-0": "**service-unavailable** ",
    "9-1": "**Service Unavailable **\nService is currently unavailable. Please try again later.",
    "10-1": "**Service Unavailable **\nRequest rate limit per connection reached. Follow detail message for futher instructions.",
    "10-0": "**too-many-requests** ",
    "11-0": "**method-not-allowed** ",
    "11-1": "**Not Allowed **\nRequested method is not allowed.",
    "12-0": "**unauthorized-access** ",
    "12-1": "**Unauthorized **\nUnauthorized access.",
    "13-0": "**invalid-authorization-token** ",
    "13-1": "**Unauthorized **\nInvalid authorization token. Check details message.",
    "14-0": "**invalid-authorization-request** ",
    "14-1": "**Unauthorized **\nInvalid authorization request. Check details message.",
    "15-0": "**no-production-access** ",
    "15-1": "**Unauthorized **\nPartner has permission to access Sandbox data only. For accessing live Institution data, please contact us via Intercom or email.",
    "16-0": "**account-not-accessible-requires-user-action** ",
    "16-1": "**Not Accesible **\nAn action is required from end-user before account details can be returned.",
    "17-0": "**maintenance-error** ",
    "17-1": "**Not Accessible **\nRequested resource is currently unavailable due to maintenance on Institution's side."
  },
  "cols": 2,
  "rows": 18
}
[/block]