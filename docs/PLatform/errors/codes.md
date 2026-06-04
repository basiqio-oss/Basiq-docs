---
title: Codes
excerpt: >-
  Identify Connect API error codes from the latest error file, including status
  codes, details, source fields, and affected API reference areas.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Use this page to identify Connect API error codes from the latest error file and understand where each error can occur.

The Connect API returns an error object with a `code`, `title`, and `detail`. For endpoint-specific HTTP status mappings, see **HTTP errors per endpoint**.

## Consent UI and bank-returned errors

Consent UI authorization errors returned by banks are surfaced on the Jobs endpoint instead of this fixed code list. Inspect the failed job step's `result` object for the bank-specific `code`, `title`, and `detail`.

Because each bank can return different authorization and consent messages, bank-returned errors are not maintained as a fixed error-code list.

## Error response fields

| Field | Description |
| :--- | :--- |
| `type` | The object type. Error rows use `error`. |
| `code` | The application-specific error code. |
| `title` | A short summary of the error. |
| `detail` | The specific message returned for this occurrence. |
| `source.pointer` | The request object or attribute related to the error, when available. |
| `source.parameter` | The URI, header, or body parameter related to the error, when available. |

## Connect errors

These errors apply to the Connect API reference endpoints, including token, users, consents, auth links, events, jobs, and MFA.

| HTTP status | Code | Title | Detail | Source | Example endpoints |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 400 | `invalid-content` | Invalid request content | Posted user or mobile is not in valid format. | — | `POST /users`, `POST /users/{userId}/auth_link` |
| 400 | `parameter-not-supplied` | Required parameter not supplied | Required user, job, consent, email, mobile, or business parameters were not supplied. | `userId`, `jobId`, `consentId`, email/mobile fields | Users, consents, auth links, jobs |
| 400 | `parameter-not-valid` | Required parameter not valid / Parameter value is not valid | A header, path parameter, email, mobile, user ID, or consent ID value is not valid. | `Authorization`, `userId`, `consentId`, `email`, `mobile` | `/token`, users, consents, auth links, jobs |
| 400 | `resource-not-found` | Requested resource is not found | Requested job does not exist. | — | `GET /jobs/{jobId}` |
| 400 | `unsupported-accept` | Accept type is not supported | The requested endpoint does not support the supplied `Accept` header. | — | Users |
| 401 | `access-denied` | access-denied | Token has expired. | — | `POST /users`, `POST /jobs/{jobId}/mfa` |
| 401 | `invalid-authorization-token` | Invalid authorization token | Empty response detail. | — | Users, jobs MFA |
| 401 | `unauthorised-access` | unauthorised-access | You are not authorized to access this resource. | — | Consents, auth links, events, jobs |
| 403 | `access-denied` | access-denied | Your account has been disabled, or the token has expired. | — | `/token`, users, consents, auth links, events, jobs |
| 403 | `forbidden-access` | forbidden-access | Access to this resource is forbidden. | — | `POST /users` |
| 403 | `request-not-valid` | Invalid request | Missing Authentication Token. | — | `DELETE /users/{userId}` |
| 403 | `Forbidden access` | Forbidden access | Access to this resource is forbidden. | — | `POST /jobs/{jobId}/mfa` |
| 404 | `parameter-not-valid` | We have encountered an error | Unable to authenticate. Check your API key. | `header/Authorization`, `Authorization` | `POST /token` |
| 404 | `resource-not-found` | Requested resource is not found | Requested user or consent does not exist. | — | Users, consents |
| 415 | `unsupported-content-type` | Request content type is not supported | Content type is not supported on requested endpoint. | — | `POST /users/{userId}/auth_link` |
| 500 | `parameter-not-valid` | We have encountered an error | Internal server error. | `Authorization` when returned from `/token`; otherwise — | `/token`, users, consents, auth links, events, jobs |
| 503 | `service-unavailable` | service-unavailable | Service is currently unavailable. Please try again later. | — | Users, jobs MFA |
| 503 | `Service unavailable` | Service unavailable | Service is currently unavailable. Please try again later. | — | Users, consents, auth links, events, jobs |

## Identity errors

| HTTP status | Code | Title | Detail | Source | Example endpoints |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 400 | `parameter-not-supplied` | Required parameter not supplied | User ID not supplied. | `userId` | `GET /users/{userId}/identities`, `GET /users/{userId}/identities/{identityId}` |
| 400 | `parameter-not-valid` | Parameter value is not valid | User ID value is not valid. | `userId` | Identity endpoints |
| 401 | `unauthorised-access` | unauthorised-access | You are not authorized to access this resource. | — | Identity endpoints |
| 403 | `access-denied` | access-denied | Token has expired. | — | Identity endpoints |
| 404 | `resource-not-found` | Requested resource is not found | Requested identity does not exist. | — | `GET /users/{userId}/identities/{identityId}` |
| 500 | `parameter-not-valid` | We have encountered an error | Internal server error. | — | Identity endpoints |
| 503 | `Service unavailable` | Service unavailable | Service is currently unavailable. Please try again later. | — | Identity endpoints |

## Reports errors

| HTTP status | Code | Title | Detail | Source | Example endpoints |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 400 | `invalid-content` | Invalid request content | Invalid accounts. | — | `POST /reports` |
| 401 | `Invalid authorization token` | Invalid authorization token | Empty response detail. | — | `GET /reports`, report transactions, report types |
| 404 | `resource-not-found` | Requested resource is not found | Requested user, report, or report type does not exist. | — | Reports endpoints |
| 500 | `Internal server error` | Internal server error | Internal server error. | — | Reports endpoints |

## Data errors

| HTTP status | Code | Title | Detail | Source | Example endpoints |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 400 | `parameter-not-valid` | Parameter value is not valid | User ID, account ID, transaction ID, or connection ID value is not valid. | `userId`, `accountId`, `transactionId`, `connectionId` | Accounts, transactions, connections |
| 400 | `unsupported-accept` | Accept type is not supported | Accept type `application/jsons` is not supported on requested endpoint. | — | Accounts, transactions, connections, connectors |
| 401 | `invalid-authorization-token` | invalid-authorization-token | Empty response detail. | — | Accounts, transactions, connections, connectors |
| 404 | `resource-not-found` | Requested resource is not found | Requested connector does not exist. | — | `GET /connectors/{connectorId}/method` |
| 500 | `parameter-not-valid` | We have encountered an error | Internal server error. | — | Accounts, transactions, connections, connectors |
| 503 | `Service unavailable` | Service unavailable | Service is currently unavailable. Please try again later. | — | Accounts, transactions, connections |

## Affordability errors

| HTTP status | Code | Title | Detail | Source | Example endpoints |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 400 | `parameter-not-valid` | Parameter value is not valid | User ID or limit value is not valid. | `userId`, `limit` | Affordability, expense, income endpoints |
| 400 | `path-parameter-not-valid` | Parameter value is not valid | Snapshot ID value is not valid. | `snapshotId` | Expense and income snapshot endpoints |
| 400 | `unsupported-accept` | Accept type is not supported | Accept type `application/jsons` is not supported on requested endpoint. | — | Affordability, expense, income endpoints |
| 401 | `invalid-authorization-token` | invalid-authorization-token | Empty response detail. | — | Affordability, expense, income endpoints |
| 404 | `resource-not-found` | Requested resource is not found | Requested user or snapshot does not exist, or the user does not have any accounts. | — | Affordability snapshot and transaction endpoints |
| 500 | `parameter-not-valid` | We have encountered an error | Internal server error. | — | Affordability, expense, income endpoints |
| 503 | `Service unavailable` | Service unavailable | Service is currently unavailable. Please try again later. | — | Affordability, expense, income endpoints |

## Enrich errors

| HTTP status | Code | Title | Detail | Source | Example endpoints |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 429 | `too-many-requests` | Too many requests. | Query limit reached. | — | All endpoints |

## HTTP status summary

| HTTP status | Meaning | What to check |
| :--- | :--- | :--- |
| 400 | The request is invalid. | Check required parameters, path parameters, request body format, and supported headers. |
| 401 | The request is not authorized. | Check the bearer token and whether it is valid for the requested resource. |
| 403 | Access is denied. | Check token expiry, account status, API key enablement, and required scopes. |
| 404 | The requested resource was not found. | Check resource IDs and whether the resource belongs to the application environment you are using. |
| 415 | The content type is not supported. | Send a supported `Content-Type` for the endpoint. |
| 429 | Too many requests were sent. | Reduce request volume and retry after the limit resets. |
| 500 | The API returned an internal server error. | Retry the request and contact Customer Success if the issue persists. |
| 503 | The service is temporarily unavailable. | Retry later and contact Customer Success if the issue persists. |
