---
title: Codes
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
    "0-0": "too-many-sandbox-connections",
    "0-1": "**Limit reached for sandbox connections**\n You have reached the limit for sandbox connections. Reach out to  support@basiq.io to reset your account.",
    "22-0": "unsupported-content-type",
    "22-1": "**Invalid Attribute **\nRequested content type is not supported.",
    "24-0": "unsupported-accept",
    "24-1": "**Invalid Attribute **\nAccept type is not supported.",
    "26-0": "service-unavailable",
    "26-1": "**Service Unavailable **\nService is currently unavailable. Please try again later.",
    "28-1": "**Service Unavailable **\nRequest rate limit per connection reached. Follow detail message for futher instructions.",
    "28-0": "too-many-requests",
    "30-0": "method-not-allowed",
    "30-1": "**Not Allowed **\nRequested method is not allowed.",
    "32-0": "unauthorized-access",
    "32-1": "**Unauthorized **\nUnauthorized access.",
    "34-0": "invalid-authorization-request",
    "34-1": "**Unauthorized **\nInvalid authorization request. Check details message.",
    "38-0": "no-production-access",
    "38-1": "**Unauthorized **\nPartner has permission to access Sandbox data only. For accessing live Institution data, please contact us via Intercom or email.",
    "40-0": "account-not-accessible-requires-user-action",
    "40-1": "**Not Accessible **\nAn action is required from end-user before account details can be returned.",
    "42-0": "maintenance-error",
    "42-1": "**Not Accessible **\nRequested resource is currently unavailable due to maintenance on Institution's side.",
    "44-0": "forbidden-access",
    "44-1": "**Forbidden access**\nAccess to this resource is forbidden",
    "46-0": "institution-not-supported",
    "46-1": "**Institution is not supported**\ne.g. Institution AU00000 is not supported on this endpoint",
    "50-0": "bank-statement-new-product",
    "50-1": "**PDF Bank statement new product**\n`title` : \"New product requires config.\"\n`detail`:  \"Unable to recognise statement product name.\"",
    "53-0": "bank-statement-parsing-error",
    "53-1": "**PDF Bank statement parsing error**\n`title` : \"Unable to parse statement.\"\n`detail`:  \"Error parsing statement due to new statement layout for this product.\"",
    "55-0": "bank-statement-not-supported",
    "55-1": "**PDF bank statement not supported**\n`title` : \"Statement not supported.\"\n`detail` : \"Statement is not currently supported for this institution - check statement uploaded against correct bank.\"",
    "59-0": "missing-required-field",
    "59-1": "**CSV missing required field**\nCSV header does not contain required field",
    "61-1": "**CSV missing required field value**\nCSV row does not contain value for required field",
    "61-0": "missing-required-field-value",
    "63-0": "invalid-field-value",
    "63-1": "**CSV invalid field value**\nField value is not valid",
    "65-0": "account-data-differs",
    "65-1": "**CSV account data differs**\nData for single account differs across rows",
    "67-1": "**CSV empty file**\nCSV file has no data rows",
    "67-0": "empty-file",
    "69-1": "**CSV row count exceeded**\nCSV row count is above limit",
    "69-0": "row-count-exceeded",
    "71-0": "invalid-request-content",
    "71-1": "**PDF/CSV invalid request content (file type)**\nStatement is not valid",
    "12-0": "parameter-not-supplied",
    "14-0": "parameter-not-valid",
    "12-1": "**Missing Attribute **\nRequired parameter not supplied. Check details and source message.\ne.g. One of 'email' or 'mobile' is required.",
    "14-1": "**Invalid Attribute **\nParameter value is not valid. Check details and source message.\ne.g. Provided mobile is in bad format.\nUser ID value is not valid",
    "8-0": "access-denied",
    "8-1": "**Access denied**\nToken has expired",
    "10-1": "**Unauthorized **\nInvalid authorization token. Check details message.",
    "10-0": "invalid-authorization-token",
    "16-0": "resource-not-found",
    "16-1": "**Invalid Attribute **\nRequested resource is not found. Check details message.",
    "18-0": "resource-already-exists",
    "18-1": "**Invalid Attribute **\nResource already exists. Check details message.",
    "20-1": "**Invalid Attribute**\nInvalid request content. Check details message.\ne.g. empty request body",
    "20-0": "invalid-content",
    "6-1": "**Server Error **\nInternal server error\nAll endpoints",
    "6-0": "internal-server-error",
    "73-0": "request-not-valid",
    "73-1": "**PDF/CSV Invalid request**\nRequest too long",
    "36-1": "**Unauthorized **\nPlease contct us to have your API key enabled for Connections.",
    "36-0": "access-denied",
    "2-0": "invalid-credentials",
    "2-1": "**Invalid Attribute **\nCannot login to target institution using supplied credentials. Please check credentials and try again.",
    "4-1": "Introduced new granularity for invalid-credentials code.  These are the possible `title` and `detail` scenarios for invalid-credentials - see JSON examples\n\n*  invalid-credentials  - existing generic title and detail message,  fallback where no cases match from below\n\n* **[new]**  title and detail message for: **invalid-username-or-password** \n\n* **[new]**  title and detail message for: **locked-account** \n\n* **[new]**  title and detail message for: **multi-factor-authentication**",
    "57-0": "bank-statement-invalid",
    "57-1": "**PDF bank statement invalid**\n`title` : \"Invalid bank statement.\"\n`detail` : \"File uploaded is not an official PDF bank statement.\"",
    "51-1": "*note: requires configuration of product name to account type mapping is missing*",
    "48-1": "**Request not valid** (403)\nThere have been too many requests for the token endpoint within a 5 minute period from a specific IP address.",
    "48-0": "request-not-valid"
  },
  "cols": 2,
  "rows": 74
}
[/block]

[block:textarea]
{
  "text": "## Handling Invalid Credentials\n\ninvalid-credentials  - existing generic title and detail for fallback, where no cases match from below",
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"title\": \"verify-credentials\",\n  \"status\": \"failed\",\n  \"result\": {\n    \"code\": \"invalid-credentials\",\n    \"title\": \"Cannot login to target institution, check credentials.\",\n    \"detail\": \"Cannot login to target institution using supplied credentials. Please check credentials and try again.\"\n  }\n}",
      "language": "json",
      "name": "invalid credentials (generic fallback message)"
    }
  ],
  "sidebar": true
}
[/block]

[block:textarea]
{
  "text": "invalid-credentials - title and detail for scenario: **invalid-username-or-password** ",
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"title\": \"verify-credentials\",\n  \"status\": \"failed\",\n  \"result\": {\n    \"code\": \"invalid-credentials\",\n    \"title\": \"Cannot login to target institution: invalid username or password.\",\n    \"detail\": \"Cannot login to target institution: invalid username or password. Please check credentials and try again.\"\n  }\n}",
      "language": "json",
      "name": "invalid username or password message"
    }
  ],
  "sidebar": true
}
[/block]

[block:textarea]
{
  "text": "invalid-credentials - title and detail for scenario: **locked-account** ",
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"title\": \"verify-credentials\",\n  \"status\": \"failed\",\n  \"result\": {\n    \"code\": \"invalid-credentials\",\n    \"title\": \"Cannot login to target institution: this account is locked.\",\n    \"detail\": \"Cannot login to target institution: this account is locked. Please contact institution directly.\"\n  }\n}",
      "language": "json",
      "name": "locked account message"
    }
  ],
  "sidebar": true
}
[/block]

[block:textarea]
{
  "text": "invalid-credentials - title and detail for scenario: **multi-factor-authentication** ",
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"title\": \"verify-credentials\",\n  \"status\": \"failed\",\n  \"result\": {\n    \"code\": \"invalid-credentials\",\n    \"title\": \"Cannot login to target institution: multi-factor authentication is not supported.\",\n    \"detail\": \"Cannot login to target institution: multi-factor authentication is not supported. Please check if multi-factor authentication is enabled on login.\"\n  }\n}",
      "language": "json",
      "name": "multi factor authentication message"
    }
  ],
  "sidebar": true
}
[/block]