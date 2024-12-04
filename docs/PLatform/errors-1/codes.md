---
title: Codes
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
Below you will find details for our various response codes.

[block:parameters]
{
  "data": {
    "h-0": "Code",
    "h-1": "Description",
    "0-0": "too-many-sandbox-connections",
    "0-1": "**Limit reached for sandbox connections**  \n You have reached the limit for sandbox connections. Reach out to  [support@basiq.io](mailto:support@basiq.io) to reset your account.",
    "1-0": "",
    "1-1": "",
    "2-0": "invalid-credentials",
    "2-1": "**Invalid Attribute **  \nCannot login to target institution using supplied credentials. Please check credentials and try again.",
    "3-0": "",
    "3-1": "",
    "4-0": "",
    "4-1": "Introduced new granularity for invalid-credentials code.  These are the possible `title` and `detail` scenarios for invalid-credentials - see JSON examples  \n  \n\\_  invalid-credentials  - existing generic title and detail message,  fallback where no cases match from below  \n  \n\\_ **[new]**  title and detail message for: **invalid-username-or-password**  \n  \n\\_ **[new]**  title and detail message for: **locked-account**  \n  \n\\_ **[new]**  title and detail message for: **multi-factor-authentication**",
    "5-0": "",
    "5-1": "",
    "6-0": "internal-server-error",
    "6-1": "**Server Error **  \nInternal server error  \nAll endpoints",
    "7-0": "",
    "7-1": "",
    "8-0": "access-denied",
    "8-1": "**Access denied**  \nToken has expired",
    "9-0": "",
    "9-1": "",
    "10-0": "invalid-authorization-token",
    "10-1": "**Unauthorized **  \nInvalid authorization token. Check details message.",
    "11-0": "",
    "11-1": "",
    "12-0": "parameter-not-supplied",
    "12-1": "**Missing Attribute **  \nRequired parameter not supplied. Check details and source message.  \ne.g. One of 'email' or 'mobile' is required.",
    "13-0": "",
    "13-1": "",
    "14-0": "parameter-not-valid",
    "14-1": "**Invalid Attribute **  \nParameter value is not valid. Check details and source message.  \ne.g. Provided mobile is in bad format.  \nUser ID value is not valid",
    "15-0": "",
    "15-1": "",
    "16-0": "resource-not-found",
    "16-1": "**Invalid Attribute **  \nRequested resource is not found. Check details message.",
    "17-0": "",
    "17-1": "",
    "18-0": "resource-already-exists",
    "18-1": "**Invalid Attribute **  \nResource already exists. Check details message.",
    "19-0": "",
    "19-1": "",
    "20-0": "invalid-content",
    "20-1": "**Invalid Attribute**  \nInvalid request content. Check details message.  \ne.g. empty request body",
    "21-0": "",
    "21-1": "",
    "22-0": "unsupported-content-type",
    "22-1": "**Invalid Attribute **  \nRequested content type is not supported.",
    "23-0": "",
    "23-1": "",
    "24-0": "unsupported-accept",
    "24-1": "**Invalid Attribute **  \nAccept type is not supported.",
    "25-0": "",
    "25-1": "",
    "26-0": "service-unavailable",
    "26-1": "**Service Unavailable **  \nService is currently unavailable. Please try again later.",
    "27-0": "",
    "27-1": "",
    "28-0": "too-many-requests",
    "28-1": "**Service Unavailable **  \nRequest rate limit per connection reached. Follow detail message for futher instructions.",
    "29-0": "",
    "29-1": "",
    "30-0": "method-not-allowed",
    "30-1": "**Not Allowed **  \nRequested method is not allowed.",
    "31-0": "",
    "31-1": "",
    "32-0": "unauthorized-access",
    "32-1": "**Unauthorized **  \nUnauthorized access.",
    "33-0": "",
    "33-1": "",
    "34-0": "invalid-authorization-request",
    "34-1": "**Unauthorized **  \nInvalid authorization request. Check details message.",
    "35-0": "",
    "35-1": "",
    "36-0": "access-denied",
    "36-1": "**Unauthorized **  \nPlease contact us to have your API key enabled for Connections.",
    "37-0": "",
    "37-1": "",
    "38-0": "no-production-access",
    "38-1": "**Unauthorized **  \nPartner has permission to access Sandbox data only. For accessing live Institution data, please contact us via Intercom or email.",
    "39-0": "",
    "39-1": "",
    "40-0": "account-not-accessible-requires-user-action",
    "40-1": "**Not Accessible **  \nAn action is required from end-user before account details can be returned.",
    "41-0": "",
    "41-1": "",
    "42-0": "maintenance-error",
    "42-1": "**Not Accessible **  \nRequested resource is currently unavailable due to maintenance on Institution's side.",
    "43-0": "",
    "43-1": "",
    "44-0": "forbidden-access",
    "44-1": "**Forbidden access**  \nAccess to this resource is forbidden",
    "45-0": "",
    "45-1": "",
    "46-0": "institution-not-supported",
    "46-1": "**Institution is not supported**  \ne.g. Institution AU00000 is not supported on this endpoint",
    "47-0": "",
    "47-1": "",
    "48-0": "request-not-valid",
    "48-1": "**Request not valid** (403)  \nThere have been too many requests for the token endpoint within a 5 minute period from a specific IP address.",
    "49-0": "",
    "49-1": "",
    "50-0": "bank-statement-new-product",
    "50-1": "**PDF Bank statement new product**  \n`title` : \"New product requires config.\"  \n`detail`:  \"Unable to recognise statement product name.\"",
    "51-0": "",
    "51-1": "_note: requires configuration of product name to account type mapping is missing_",
    "52-0": "",
    "52-1": "",
    "53-0": "bank-statement-parsing-error",
    "53-1": "**PDF Bank statement parsing error**  \n`title` : \"Unable to parse statement.\"  \n`detail`:  \"Error parsing statement due to new statement layout for this product.\"",
    "54-0": "",
    "54-1": "",
    "55-0": "bank-statement-not-supported",
    "55-1": "**PDF bank statement not supported**  \n`title` : \"Statement not supported.\"  \n`detail` : \"Statement is not currently supported for this institution - check statement uploaded against correct bank.\"",
    "56-0": "",
    "56-1": "",
    "57-0": "bank-statement-invalid",
    "57-1": "**PDF bank statement invalid**  \n`title` : \"Invalid bank statement.\"  \n`detail` : \"File uploaded is not an official PDF bank statement.\"",
    "58-0": "",
    "58-1": "",
    "59-0": "missing-required-field",
    "59-1": "**CSV missing required field**  \nCSV header does not contain required field",
    "60-0": "",
    "60-1": "",
    "61-0": "missing-required-field-value",
    "61-1": "**CSV missing required field value**  \nCSV row does not contain value for required field",
    "62-0": "",
    "62-1": "",
    "63-0": "invalid-field-value",
    "63-1": "**CSV invalid field value**  \nField value is not valid",
    "64-0": "",
    "64-1": "",
    "65-0": "account-data-differs",
    "65-1": "**CSV account data differs**  \nData for single account differs across rows",
    "66-0": "",
    "66-1": "",
    "67-0": "empty-file",
    "67-1": "**CSV empty file**  \nCSV file has no data rows",
    "68-0": "",
    "68-1": "",
    "69-0": "row-count-exceeded",
    "69-1": "**CSV row count exceeded**  \nCSV row count is above limit",
    "70-0": "",
    "70-1": "",
    "71-0": "invalid-request-content",
    "71-1": "**PDF/CSV invalid request content (file type)**  \nStatement is not valid",
    "72-0": "",
    "72-1": "",
    "73-0": "request-not-valid",
    "73-1": "**PDF/CSV Invalid request**  \nRequest too long"
  },
  "cols": 2,
  "rows": 74,
  "align": [
    "left",
    "left"
  ]
}
[/block]


[block:textarea]
{
  "text": "##  Handling Invalid Credentials\n\ninvalid-credentials  - existing generic title and detail for fallback, where no cases match from below",
  "sidebar": true
}
[/block]


```json invalid credentials (generic fallback message)
{
  "title": "verify-credentials",
  "status": "failed",
  "result": {
    "code": "invalid-credentials",
    "title": "Cannot login to target institution, check credentials.",
    "detail": "Cannot login to target institution using supplied credentials. Please check credentials and try again."
  }
}
```

[block:textarea]
{
  "text": "invalid-credentials - title and detail for scenario: **invalid-username-or-password** ",
  "sidebar": true
}
[/block]


```json invalid username or password message
{
  "title": "verify-credentials",
  "status": "failed",
  "result": {
    "code": "invalid-credentials",
    "title": "Cannot login to target institution: invalid username or password.",
    "detail": "Cannot login to target institution: invalid username or password. Please check credentials and try again."
  }
}
```

[block:textarea]
{
  "text": "invalid-credentials - title and detail for scenario: **locked-account** ",
  "sidebar": true
}
[/block]


```json locked account message
{
  "title": "verify-credentials",
  "status": "failed",
  "result": {
    "code": "invalid-credentials",
    "title": "Cannot login to target institution: this account is locked.",
    "detail": "Cannot login to target institution: this account is locked. Please contact institution directly."
  }
}
```

[block:textarea]
{
  "text": "invalid-credentials - title and detail for scenario: **multi-factor-authentication** ",
  "sidebar": true
}
[/block]


```json multi factor authentication message
{
  "title": "verify-credentials",
  "status": "failed",
  "result": {
    "code": "invalid-credentials",
    "title": "Cannot login to target institution: multi-factor authentication is not supported.",
    "detail": "Cannot login to target institution: multi-factor authentication is not supported. Please check if multi-factor authentication is enabled on login."
  }
}
```