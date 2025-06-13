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
## Response Code Reference

Below you will find details for our various response codes.

| Code                                          | Description                                                                                                                                                                          |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `too-many-sandbox-connections`                | **Limit Reached for Sandbox Connections**<br />You have reached the limit for sandbox connections. Please contact [support@basiq.io](mailto:support@basiq.io) to reset your account. |
| `unsupported-content-type`                    | **Invalid Attribute**<br />Requested content type is not supported.                                                                                                                  |
| `unsupported-accept`                          | **Invalid Attribute**<br />Accept type is not supported.                                                                                                                             |
| `service-unavailable`                         | **Service Unavailable**<br />Service is currently unavailable. Please try again later.                                                                                               |
| `too-many-requests`                           | **Service Unavailable**<br />Request rate limit per connection reached. Follow detail message for further instructions.                                                              |
| `method-not-allowed`                          | **Not Allowed**<br />Requested method is not allowed.                                                                                                                                |
| `unauthorized-access`                         | **Unauthorized**<br />Unauthorized access.                                                                                                                                           |
| `invalid-authorization-request`               | **Unauthorized**<br />Invalid authorization request. Check details message.                                                                                                          |
| `no-production-access`                        | **Unauthorized**<br />Partner can access Sandbox data only. Contact us via Intercom or email for live data access.                                                                   |
| `account-not-accessible-requires-user-action` | **Not Accessible**<br />User action required before account details can be returned.                                                                                                 |
| `maintenance-error`                           | **Not Accessible**<br />Institution resource is under maintenance.                                                                                                                   |
| `forbidden-access`                            | **Forbidden Access**<br />Access to this resource is forbidden.                                                                                                                      |
| `institution-not-supported`                   | **Institution Not Supported**<br />e.g. Institution AU00000 is not supported on this endpoint.                                                                                       |
| `bank-statement-new-product`                  | **PDF Bank Statement New Product**<br />`title`: "New product requires config."<br />`detail`: "Unable to recognise statement product name."                                         |
| `bank-statement-parsing-error`                | **PDF Bank Statement Parsing Error**<br />`title`: "Unable to parse statement."<br />`detail`: "New layout not supported."                                                           |
| `bank-statement-not-supported`                | **PDF Bank Statement Not Supported**<br />`title`: "Statement not supported."<br />`detail`: "Unsupported institution statement."                                                    |
| `missing-required-field`                      | **CSV Missing Required Field**<br />CSV header does not contain required field.                                                                                                      |
| `missing-required-field-value`                | **CSV Missing Required Field Value**<br />CSV row does not contain value for required field.                                                                                         |
| `invalid-field-value`                         | **CSV Invalid Field Value**<br />Field value is not valid.                                                                                                                           |
| `account-data-differs`                        | **CSV Account Data Differs**<br />Data for a single account differs across rows.                                                                                                     |
| `empty-file`                                  | **CSV Empty File**<br />CSV file has no data rows.                                                                                                                                   |
| `row-count-exceeded`                          | **CSV Row Count Exceeded**<br />Row count exceeds limit.                                                                                                                             |
| `invalid-request-content`                     | **PDF/CSV Invalid Request Content**<br />Statement file is not valid.                                                                                                                |
| `request-not-valid`                           | **Request Not Valid**<br />Request too long or too frequent (403 for token endpoint).                                                                                                |
| `bank-statement-invalid`                      | **PDF Bank Statement Invalid**<br />`title`: "Invalid bank statement."<br />`detail`: "File is not an official PDF bank statement."                                                  |
| `invalid-credentials`                         | **Invalid Attribute**<br />Cannot login to institution using supplied credentials.                                                                                                   |

***

## Handling Invalid Credentials

### locked-account

```json
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

### invalid-username-or-password

```json JSON
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

### multi-factor-authentication

```json
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