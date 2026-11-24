---
title: HTTP errors per endpoint
excerpt: >-
  Troubleshoot HTTP error responses by endpoint, status code, response message,
  and recommended action.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
Find the error response for your endpoint and follow the action to troubleshoot your request.

Response messages below preserve the API wording, including any grammatical errors. Replace `YOUR_API_KEY` and `YOUR_ACCESS_TOKEN` with your own credentials when setting request headers; these labels are not credentials.

## POST `/token`

| Status code | Response title/detail | Action |
| --- | --- | --- |
| 403 | `Your account has been disabled. Please contact Basiq support.` | Contact Customer Success to enable your account. |
| 500 | `Internal server error` | Try again. If the error persists, contact Customer Success. |
| 400 | `Authorization header parameter is required` | Set the request header to `Authorization: Basic YOUR_API_KEY`. |
| 400 | `Version 0.9 is no longer supported. Please upgrade to the latest version` | Set the `basiq-version` request header to `2.0` or `2.1`. |
| 400 | `Basiq-version must be specified in HTTP request header` | Set the `basiq-version` request header to `2.0` or `2.1`. |
| 404 | `Unable to authenticate. Please, check your API key` | Check that your API key and application still exist. Use an API key from the same environment as your request. |
| 400 | `Invalid authorization header` | Set the request header to `Authorization: Basic YOUR_API_KEY`. |
| 403 | `Invalid request` | Your IP address has exceeded the token request limit within a five-minute period. Reduce requests to `/token`. |

## POST `/users`

| Status code | Response title/detail | Action |
| --- | --- | --- |
| 401 | `Invalid authorization token.` | Set the request header to `Authorization: Bearer YOUR_ACCESS_TOKEN`. |
| 400 | `Posted user is not in valid format.` | Check the request body. Include an `email` value, a `mobile` value, or both. |
| 400 | `One of 'email' or 'mobile' is required.` | Include an `email` value, a `mobile` value, or both in the request body. |
| 400 | `Provided email is in bad format.` | Check the `email` value in the request body for formatting errors. |
| 400 | `Provided mobile is in bad format.` | Check the `mobile` value in the request body for formatting errors. |
| 403 | `Token has expired` | Get a new access token from `POST /token`. |
| 403 | `Access to this resource is forbidden` | Check your token's scope (its access permissions). You may need `scope=SERVER_ACCESS` in the token request body, not a request header. |
| 400 | `Accept type is not supported` | Check the `Accept` request header against the endpoint's supported response media types. |
| 400 | `Business name is required when business number is provided.` | Include the business name in the request body when you supply a business number. |
| 503 | `Service is currently unavailable. Please try again later.` | Try again later. If the error persists, contact Customer Success. |

## GET `/users/{userId}`

| Status code | Response title/detail | Action |
| --- | --- | --- |
| 401 | `Invalid authorization token.` | Set the request header to `Authorization: Bearer YOUR_ACCESS_TOKEN`. |
| 400 | `User ID value is not valid` | Check the format of `userId` in the URL. |
| 404 | `Requested user does not exist.` | Set `userId` in the URL to the ID of an existing user. |
| 403 | `Token has expired` | Get a new access token from `POST /token`. |
| 400 | `Accept type application/json is not supported on requested endpoint.` | Check the `Accept` request header against the endpoint's supported response media types. |
| 401 | `You are not authorized to access this resource` | Check that your token grants access to the `userId` in the URL. |
| 500 | `Internal server error. Please contact support.` | Contact Customer Success. |

## POST `/users/{userId}`

| Status code | Response title/detail | Action |
| --- | --- | --- |
| 400 | `One of 'email' or 'mobile' is required.` | Include an `email` or `mobile` value in the request body. |
| 400 | `"Provided mobile is in bad format."` | Check the `mobile` value in the request body for formatting errors. |
| 400 | `Provided email is in bad format.` | Check the `email` value in the request body for formatting errors. |
| 401 | `Invalid authorization token.` | Set the request header to `Authorization: Bearer YOUR_ACCESS_TOKEN`. |
| 400 | `User ID value is not valid` | Check the format of `userId` in the URL. |
| 403 | `Token has expired` | Get a new access token from `POST /token`. |
| 403 | `Access to this resource is forbidden` | Check your token's scope (its access permissions). You may need `scope=SERVER_ACCESS` in the token request body, not a request header. |
| 400 | `Accept type application/json is not supported on requested endpoint.` | Check the `Accept` request header against the endpoint's supported response media types. |
| 400 | `User ID not supplied` | Include `userId` in the URL. |
| 400 | `Posted user is not in valid format.` | Check the request body for formatting errors. |
| 404 | `Requested user does not exist.` | Check that the user still exists and belongs to the application associated with your API key. |
| 500 | `Internal server error. Please contact support.` | Contact Customer Success. |
| 503 | `Service is currently unavailable. Please try again later.` | Try again. If the error persists, contact Customer Success. |

## DELETE `/users/{userId}`

| Status code | Response title/detail | Action |
| --- | --- | --- |
| 403 | `Missing Authentication Token` | Set the request header to `Authorization: Bearer YOUR_ACCESS_TOKEN`. |
| 404 | `Requested user does not exist.` | Check that the user still exists and belongs to the application associated with your API key. |
| 400 | `User ID value is not valid` | Check the format of `userId` in the URL. |
| 401 | `Invalid authorization token.` | Set the request header to `Authorization: Bearer YOUR_ACCESS_TOKEN`. |
| 403 | `Token has expired` | Get a new access token from `POST /token`. |
| 400 | `Accept type application/json is not supported on requested endpoint.` | Check the `Accept` request header against the endpoint's supported response media types. |
| 400 | `User ID not supplied` | Include `userId` in the URL. |
| 500 | `Internal server error. Please contact support.` | Contact Customer Success. |
| 503 | `Service is currently unavailable. Please try again later.` | Wait five minutes and try again. If the error persists, contact Customer Success. |

## POST `/users/{userId}/connections`

| Status code | Response title/detail | Action |
| --- | --- | --- |
| 401 | `Invalid authorization token.` | Set the request header to `Authorization: Bearer YOUR_ACCESS_TOKEN`. |
| 400 | `Login ID parameter is required.` | Include the `loginId` field and its value in the request body. |
| 400 | `Password parameter is required.` | Include the `password` field and its value in the request body. |
| 400 | `Institution ID  parameter is required.` | Include the `institutionId` field and its value in the request body. |
| 400 | `Posted connection is not in valid format.` | Send a nonempty request body and check it for formatting errors. |
| 415 | `Content type application/json is not supported on requested endpoint.` | Check the `Content-Type` request header against the endpoint's supported request media types. |
| 403 | `Token has expired` | Get a new access token from `POST /token`. |
| 400 | `Requested institution does not exist.` | Set `institutionId` to the ID of an existing institution. |
| 400 | `Accept type application/json is not supported on requested endpoint.` | Check the `Accept` request header against the endpoint's supported response media types. |
| 401 | `Unauthorized access` | Check that your token grants access to the `userId` in the URL. |
| 400 | `User ID value is not valid` | Check the format of `userId` in the URL. |
| 403 | `Please contact us to have your API key enabled for Connections.` | Contact Customer Support to enable live data for your sandbox account before connecting to real institutions. |
| 404 | `Requested resource is not found` | Check that the user still exists and belongs to the application associated with your API key. |
| 400 | `The institution you are trying to connect to is currently disabled. Our developers have been notified and are working to have the issue resolved.` | Check the institution's status on the status page in your dashboard. |
| 503 | `Service is currently unavailable. Please try again later.` | Wait five minutes and try again. If the error persists, contact Customer Success. |
| 500 | `Internal server error. Please contact support.` | Wait five minutes and try again. If the error persists, contact Customer Success. |
| 403 | `Limit reached for sandbox connections.` | Contact Customer Success to request a higher sandbox connection limit. |

## GET `/users/{userId}/connections`

| Status code | Response title/detail | Action |
| --- | --- | --- |
| 403 | `Access to this resource is forbidden` | Check your token's scope (its access permissions). You may need `scope=SERVER_ACCESS` in the token request body, not a request header. |
| 400 | `Accept type application/json is not supported on requested endpoint.` | Check the `Accept` request header against the endpoint's supported response media types. |
| 400 | `User ID not supplied` | Include `userId` in the URL. |
| 400 | `User ID value is not valid` | Check the format of `userId` in the URL. |
| 404 | `Requested user does not exist.` | Check that the user still exists and belongs to the application associated with your API key. |
| 503 | `Service is currently unavailable. Please try again later.` | Wait five minutes and try again. If the error persists, contact Customer Success. |
| 500 | `Internal server error. Please contact support.` | Contact Customer Success. |

## POST `/users/{userId}/connections/refresh`

| Status code | Response title/detail | Action |
| --- | --- | --- |
| 401 | `Invalid authorization token.` | Set the request header to `Authorization: Bearer YOUR_ACCESS_TOKEN`. |
| 400 | `Accept type application/json is not supported on requested endpoint.` | Check the `Accept` request header against the endpoint's supported response media types. |
| 400 | `User ID not supplied` | Include `userId` in the URL. |
| 403 | `Access to this resource is forbidden` | Check your token's scope (its access permissions). You may need `scope=SERVER_ACCESS` in the token request body, not a request header. |
| 400 | `User ID value is not valid` | Check the format of `userId` in the URL. |
| 404 | `Requested user does not exist.` | Check that the user still exists and belongs to the application associated with your API key. |
| 500 | `Internal server error. Please contact support.` | Contact support. |

## GET `/jobs/{jobId}`

| Status code | Response title/detail | Action |
| --- | --- | --- |
| 401 | `Invalid authorization token.` | Set the request header to `Authorization: Bearer YOUR_ACCESS_TOKEN`. |
| 403 | `Token has expired` | Get a new access token from `POST /token`. |
| 400 | `Job ID value is not valid` | Check the format of `jobId` in the URL. |
| 404 | `Requested resource is not found` | Check that the job still exists and belongs to the application associated with your API key. |
| 400 | `Accept type application/json is not supported on requested endpoint.` | Check the `Accept` request header against the endpoint's supported response media types. |
| 400 | `Job ID not supplied` | Include `jobId` in the URL. |
| 404 | `Requested user does not exist.` | Check that the user still exists and belongs to the application associated with your API key. |
| 500 | `Internal server error. Please contact support.` | Contact Customer Success. |
| 403 | `Access to this resource is forbidden` | Check your token's scope (its access permissions). You may need `scope=SERVER_ACCESS` in the token request body, not a request header. |

## GET `/users/{userId}/jobs`

| Status code | Response title/detail | Action |
| --- | --- | --- |
| 401 | `Invalid authorization token.` | Set the request header to `Authorization: Bearer YOUR_ACCESS_TOKEN`. |
| 400 | `User ID value is not valid` | Check the format of `userId` in the URL. |
| 403 | `Token has expired` | Get a new access token from `POST /token`. |
| 403 | `Access to this resource is forbidden` | Check your token's scope (its access permissions). You may need `scope=SERVER_ACCESS` in the token request body, not a request header. |
| 400 | `Accept type application/json is not supported on requested endpoint.` | Check the `Accept` request header against the endpoint's supported response media types. |
| 404 | `Requested user does not exist.` | Check that the user still exists and belongs to the application associated with your API key. |
| 404 | `Route not found for this API version.` | Check that your API version supports this endpoint. |

## POST `/users/{userId}/connections/{connectionId}`

| Status code | Response title/detail | Action |
| --- | --- | --- |
| 400 | `User ID value is not valid` | Check the format of `userId` in the URL. |
| 401 | `Invalid authorization token.` | Set the request header to `Authorization: Bearer YOUR_ACCESS_TOKEN`. |
| 403 | `Token has expired` | Get a new access token from `POST /token`. |
| 403 | `Invalid request` | Include `userId` in the URL. A path such as `/users//connections/connectionId` omits the user ID. |
| 400 | `Connection ID value is not valid` | Check the format of `connectionId` in the URL. |
| 403 | `Access to this resource is forbidden` | Check your token's scope (its access permissions). You may need `scope=SERVER_ACCESS` in the token request body, not a request header. |
| 400 | `Accept type application/json is not supported on requested endpoint.` | Check the `Accept` request header against the endpoint's supported response media types. |
| 415 | `Content type invalid-content-type is not supported on requested endpoint.` | Check the `Content-Type` request header against the endpoint's supported request media types. |
| 401 | `Unauthorized access` | Check that your token grants access to the resources in the URL. |
| 400 | `Posted connection is not in valid format.` | Send a nonempty request body and check it for formatting errors. |
| 400 | `Password value is not valid` | Check the `password` value in the request body for formatting errors. |
| 404 | `Requested resource is not found` | Check that the connection and other requested resources still exist and belong to the application associated with your API key. |
| 400 | `Connection type is not Web` | Use a connection with type `web` for this operation. |
| 400 | `Requested resource is not found` | Check that the requested resource still exists and belongs to the application associated with your API key. |
| 400 | `The institution you are trying to connect to is currently disabled. Our developers have been notified and are working to have the issue resolved.` | Check the institution's status on the status page in your dashboard. |
| 500 | `Internal server error. Please contact support.` | Contact Customer Success. |
| 503 | `Service is currently unavailable. Please try again later.` | Try again. If the error persists, contact Customer Success. |

## DELETE `/users/{userId}/connections/{connectionId}`

| Status code | Response title/detail | Action |
| :---: | --- | --- |
| 400 | `User ID value is not valid` | Check the format of `userId` in the URL. |
| 401 | `Invalid authorization token.` | Set the request header to `Authorization: Bearer YOUR_ACCESS_TOKEN`. |
| 403 | `Token has expired` | Get a new access token from `POST /token`. |
| 403 | `Invalid request` | Include `userId` in the URL and check its value. |
| 400 | `Connection ID value is not valid` | Check the format of `connectionId` in the URL. |
| 403 | `Access to this resource is forbidden` | Check your token's scope (its access permissions). You may need `scope=SERVER_ACCESS` in the token request body, not a request header. |
| 400 | `Connection ID not supplied` | Include `connectionId` in the URL. |
| 404 | `Requested resource is not found` | Check that the requested resource still exists and belongs to the application associated with your API key. |
| 404 | `Requested user does not exist.` | Check that the user still exists and belongs to the application associated with your API key. |
| 500 | `Internal server error. Please contact support.` | Contact Customer Success. |
| 503 | `Service is currently unavailable. Please try again later.` | Try again. If the error persists, contact Customer Success. |

## GET `/users/{userId}/connections/{connectionId}`

| Status code | Response title/detail | Action |
| --- | --- | --- |
| 401 | `Invalid authorization token.` | Set the request header to `Authorization: Bearer YOUR_ACCESS_TOKEN`. |
| 400 | `User ID value is not valid` | Check the format of `userId` in the URL. |
| 400 | `Connection ID value is not valid` | Check the format of `connectionId` in the URL. |
| 404 | `Requested resource is not found` | Check that the requested resource still exists and belongs to the application associated with your API key. |
| 403 | `Token has expired` | Get a new access token from `POST /token`. |
| 403 | `Access to this resource is forbidden` | Check your token's scope (its access permissions). You may need `scope=SERVER_ACCESS` in the token request body, not a request header. |
| 400 | `Accept type application/json is not supported on requested endpoint.` | Check the `Accept` request header against the endpoint's supported response media types. |
| 401 | `Unauthorized access` | Check that your token grants access to the resources in the URL. |
| 400 | `Connection ID not supplied` | Include `connectionId` in the URL. |
| 500 | `Internal server error. Please contact support.` | Contact Customer Success. |
| 503 | `Service is currently unavailable. Please try again later.` | Try again. If the error persists, contact Customer Success. |

## POST `/users/{userId}/connections/{connectionId}/refresh`

| Status code | Response title/detail | Action |
| --- | --- | --- |
| 401 | `Invalid authorization token.` | Set the request header to `Authorization: Bearer YOUR_ACCESS_TOKEN`. |
| 403 | `Token has expired` | Get a new access token from `POST /token`. |
| 400 | `User ID value is not valid` | Check the format of `userId` in the URL. |
| 404 | `Requested user does not exist.` | Check that the user still exists and belongs to the application associated with your API key. |
| 400 | `Connection ID not supplied` | Include `connectionId` in the URL. |
| 400 | `Connection ID value is not valid` | Check the format of `connectionId` in the URL. |
| 400 | `Accept type application/json is not supported on requested endpoint.` | Check the `Accept` request header against the endpoint's supported response media types. |
| 403 | `Access to this resource is forbidden` | Check your token's scope (its access permissions). You may need `scope=SERVER_ACCESS` in the token request body, not a request header. |
| 404 | `Requested resource is not found` | Check that the requested resource still exists and belongs to the application associated with your API key. |
| 400 | `Connection type is not Web` | Use a connection with type `web` for this operation. |
| 400 | `Cannot login to target institution using supplied credentials. Please check credentials and try again.` | Ask the user to check their institution credentials and provide their current credentials. Their password may have changed. |
| 403 | `Please contact us to have your API key enabled for Connections.` | Contact Customer Support to enable live data for your sandbox account before connecting to real institutions. |
| 500 | `Internal server error. Please contact support.` | Contact Customer Success. |
| 503 | `Service is currently unavailable. Please try again later.` | Try again. If the error persists, contact Customer Success. |

## GET `/users/{userId}/accounts`

| Status code | Response title/detail | Action |
| --- | --- | --- |
| 403 | `Token has expired` | Get a new access token from `POST /token`. |
| 401 | `Invalid authorization token.` | Set the request header to `Authorization: Bearer YOUR_ACCESS_TOKEN`. |
| 400 | `User ID value is not valid` | Check the format of `userId` in the URL. |
| 404 | `Requested user does not exist.` | Check that the user still exists and belongs to the application associated with your API key. |
| 403 | `Access to this resource is forbidden` | Check your token's scope (its access permissions). You may need `scope=SERVER_ACCESS` in the token request body, not a request header. |
| 400 | `Accept type application/json is not supported on requested endpoint.` | Check the `Accept` request header against the endpoint's supported response media types. |
| 404 | `Requested resource is not found` | Check that the requested resource still exists and belongs to the application associated with your API key. |
| 400 | `Requested connection does not exist.` | Check the connection type. This error can occur when the type is not `web`. |
| 500 | `Internal server error. Please contact support.` | Contact Customer Success. |

## GET `/users/{userId}/accounts/{accountId}`

| Status code | Response title/detail | Action |
| --- | --- | --- |
| 403 | `Token has expired` | Get a new access token from `POST /token`. |
| 401 | `Invalid authorization token.` | Set the request header to `Authorization: Bearer YOUR_ACCESS_TOKEN`. |
| 400 | `Account ID value is not valid` | Check the format of `accountId` in the URL. |
| 404 | `Requested resource is not found` | Check that the requested resource still exists and belongs to the application associated with your API key. |
| 400 | `User ID value is not valid` | Check the format of `userId` in the URL. |
| 403 | `Access to this resource is forbidden` | Check your token's scope (its access permissions). You may need `scope=SERVER_ACCESS` in the token request body, not a request header. |
| 400 | `Accept type application/json is not supported on requested endpoint.` | Check the `Accept` request header against the endpoint's supported response media types. |
| 400 | `Account ID not supplied` | Include `accountId` in the URL. |
| 404 | `Requested user does not exist.` | Check that the user still exists and belongs to the application associated with your API key. |
| 500 | `Internal server error. Please contact support.` | Contact Customer Success. |

## GET `/users/{userId}/transactions`

| Status code | Response title/detail | Action |
| --- | --- | --- |
| 403 | `Token has expired` | Get a new access token from `POST /token`. |
| 401 | `Invalid authorization token.` | Set the request header to `Authorization: Bearer YOUR_ACCESS_TOKEN`. |
| 400 | `User ID value is not valid` | Check the format of `userId` in the URL. |
| 404 | `Requested user does not exist.` | Check that the user still exists and belongs to the application associated with your API key. |
| 403 | `Access to this resource is forbidden` | Check your token's scope (its access permissions). You may need `scope=SERVER_ACCESS` in the token request body, not a request header. |
| 400 | `Accept type application/json is not supported on requested endpoint.` | Check the `Accept` request header against the endpoint's supported response media types. |
| 400 | `Next value is not valid` | Check the `next` parameter in the URL. |
| 400 | `Limit value is not valid` | Check the `limit` parameter in the URL. |
| 400 | `Maximum limit allowed is 500` | Set `limit` to a value no greater than `500`. |
| 400 | `PostDate is not valid` | Check the format of the `PostDate` parameter. |
| 500 | `Internal server error. Please contact support.` | Contact Customer Success. |

## GET `/users/{userId}/transactions/{transactionId}`

| Status code | Response title/detail | Action |
| --- | --- | --- |
| 403 | `Token has expired` | Get a new access token from `POST /token`. |
| 401 | `Invalid authorization token.` | Set the request header to `Authorization: Bearer YOUR_ACCESS_TOKEN`. |
| 400 | `User ID not supplied` | Include `userId` in the URL. |
| 400 | `User ID value is not valid` | Check the format of `userId` in the URL. |
| 404 | `Requested user does not exist.` | Check that the user still exists and belongs to the application associated with your API key. |
| 400 | `Transaction ID value is not valid` | Check the format of `transactionId` in the URL. |
| 404 | `Requested resource is not found` | Check that the requested resource still exists and belongs to the application associated with your API key. |
| 403 | `Access to this resource is forbidden` | Check your token's scope (its access permissions). You may need `scope=SERVER_ACCESS` in the token request body, not a request header. |
| 400 | `Accept type application/json is not supported on requested endpoint.` | Check the `Accept` request header against the endpoint's supported response media types. |
| 400 | `Transaction ID not supplied` | Include `transactionId` in the URL. |
| 503 | `Service is currently unavailable. Please try again later.` | Try again. If the error persists, contact Customer Success. |
| 500 | `Internal server error. Please contact support.` | Contact Customer Success. |

## POST `/users/{userId}/affordability`

| Status code | Response title/detail | Action |
| --- | --- | --- |
| 401 | `Invalid authorization token.` | Set the request header to `Authorization: Bearer YOUR_ACCESS_TOKEN`. |
| 403 | `Token has expired` | Get a new access token from `POST /token`. |
| 400 | `User ID value is not valid` | Check the format of `userId` in the URL. |
| 404 | `Requested resource is not found` | Check that the accounts still exist and belong to the application associated with your API key. |
| 400 | `Accept type application/json is not supported on requested endpoint.` | Check the `Accept` request header against the endpoint's supported response media types. |
| 403 | `Access to this resource is forbidden` | Check your token's scope (its access permissions). You may need `scope=SERVER_ACCESS` in the token request body, not a request header. |
| 401 | `Unauthorized access` | Check that your token grants access to the resources in the URL. |
| 400 | `Dates not in valid format. Date has to be in yyyy-mm-dd format` | Format dates as `yyyy-mm-dd` (year-month-day). |
| 400 | `fromDate not in valid format. Date has to be in yyyy-mm-dd format` | Format `fromDate` as `yyyy-mm-dd` (year-month-day). |
| 400 | `toDate not in valid format. Date has to be in yyyy-mm-dd format` | Format `toDate` as `yyyy-mm-dd` (year-month-day). |
| 400 | `toDate must be be after or equal to fromDate` | Set `toDate` to the same date as `fromDate` or a later date. |
| 404 | `Requested user does not exist.` | Check that the user still exists and belongs to the application associated with your API key. |
| 500 | `Internal server error. Please contact support.` | Contact Customer Success. |
| 400 | `User's accounts contains mixed currencies` | The user's accounts contain different currencies, which prevents aggregation. Contact Customer Success before removing accounts to resolve the currency mismatch. |

## GET `/users/{userId}/affordability/{snapshotId}`

| Status code | Response title/detail | Action |
| --- | --- | --- |
| 401 | `Invalid authorization token.` | Set the request header to `Authorization: Bearer YOUR_ACCESS_TOKEN`. |
| 403 | `Token has expired` | Get a new access token from `POST /token`. |
| 400 | `User ID value is not valid` | Check the format of `userId` in the URL. |
| 400 | `Snapshot ID value is not valid` | Check the format of `snapshotId` in the URL. |
| 400 | `Accept type is not supported` | Check the `Accept` request header against the endpoint's supported response media types. |
| 403 | `Access to this resource is forbidden` | Check your token's scope (its access permissions). You may need `scope=SERVER_ACCESS` in the token request body, not a request header. |
| 401 | `Unauthorized access` | Check that your token grants access to the resources in the URL. |
| 400 | `Snapshot ID value is not supplied` | Include `snapshotId` in the URL. |
| 404 | `Requested user does not exist.` | Check that the user still exists and belongs to the application associated with your API key. |
| 500 | `Internal server error. Please contact support.` | Contact Customer Success. |
| 403 | `Please contact us to have your API key enabled for Income Summary.` | Contact Customer Success to enable access to the feature. |
| 503 | `Service is currently unavailable. Please try again later.` | Try again. If the error persists, contact Customer Success. |

## POST `/users/{userId}/income`

| Status code | Response title/detail | Action |
| --- | --- | --- |
| 401 | `Invalid authorization token.` | Set the request header to `Authorization: Bearer YOUR_ACCESS_TOKEN`. |
| 403 | `Token has expired` | Get a new access token from `POST /token`. |
| 400 | `User ID value is not valid` | Check the format of `userId` in the URL. |
| 400 | `Accept type application/json is not supported on requested endpoint.` | Check the `Accept` request header against the endpoint's supported response media types. |
| 403 | `Access to this resource is forbidden` | Check your token's scope (its access permissions). You may need `scope=SERVER_ACCESS` in the token request body, not a request header. |
| 401 | `Unauthorized access` | Check that your token grants access to the resources in the URL. |
| 400 | `Dates not in valid format. Date has to be in yyyy-mm-dd format` | Format dates as `yyyy-mm-dd` (year-month-day). |
| 400 | `fromDate not in valid format. Date has to be in yyyy-mm-dd format` | Format `fromDate` as `yyyy-mm-dd` (year-month-day). |
| 400 | `toDate not in valid format. Date has to be in yyyy-mm-dd format` | Format `toDate` as `yyyy-mm-dd` (year-month-day). |
| 404 | `Requested user does not exist.` | Check that the user still exists and belongs to the application associated with your API key. |
| 404 | `Requested resource is not found` | Check that the requested resource still exists and belongs to the application associated with your API key. |
| 403 | `Please contact us to have your API key enabled for Income Summary.` | Contact Customer Success to enable access to the feature. |
| 400 | `User's accounts contains mixed currencies` | The user's accounts contain different currencies, which prevents aggregation. Contact Customer Success before removing accounts to resolve the currency mismatch. |
| 500 | `Internal server error. Please contact support.` | Contact Customer Success. |

## GET `/users/{userId}/income/{snapshotId}`

| Status code | Response title/detail | Action |
| --- | --- | --- |
| 401 | `Invalid authorization token.` | Set the request header to `Authorization: Bearer YOUR_ACCESS_TOKEN`. |
| 403 | `Token has expired` | Get a new access token from `POST /token`. |
| 400 | `User ID value is not valid` | Check the format of `userId` in the URL. |
| 400 | `Snapshot ID value is not valid` | Check the format of `snapshotId` in the URL. |
| 400 | `Accept type application/json is not supported on requested endpoint.` | Check the `Accept` request header against the endpoint's supported response media types. |
| 403 | `Access to this resource is forbidden` | Check your token's scope (its access permissions). You may need `scope=SERVER_ACCESS` in the token request body, not a request header. |
| 401 | `Unauthorized access` | Check that your token grants access to the resources in the URL. |
| 400 | `Snapshot ID value is not supplied` | Include `snapshotId` in the URL. |
| 404 | `Requested user does not exist.` | Check that the user still exists and belongs to the application associated with your API key. |
| 404 | `Requested resource is not found` | Check that the user has connected accounts. This error occurs when the user has no accounts. |
| 403 | `Please contact us to have your API key enabled for Income Summary.` | Contact Customer Success to enable access to the feature. |
| 500 | `Internal server error. Please contact support.` | Contact Customer Success. |

## POST `/users/{userId}/expenses`

| Status code | Response title/detail | Action |
| --- | --- | --- |
| 401 | `Invalid authorization token.` | Set the request header to `Authorization: Bearer YOUR_ACCESS_TOKEN`. |
| 403 | `Token has expired` | Get a new access token from `POST /token`. |
| 400 | `User ID value is not valid` | Check the format of `userId` in the URL. |
| 400 | `Accept type is not supported` | Check the `Accept` request header against the endpoint's supported response media types. |
| 403 | `Access to this resource is forbidden` | Check your token's scope (its access permissions). You may need `scope=SERVER_ACCESS` in the token request body, not a request header. |
| 401 | `Unauthorized access` | Check that your token grants access to the resources in the URL. |
| 400 | `Dates not in valid format. Date has to be in yyyy-mm-dd format` | Format dates as `yyyy-mm-dd` (year-month-day). |
| 400 | `fromDate not in valid format. Date has to be in yyyy-mm-dd format` | Format `fromDate` as `yyyy-mm-dd` (year-month-day). |
| 400 | `toDate not in valid format. Date has to be in yyyy-mm-dd format` | Format `toDate` as `yyyy-mm-dd` (year-month-day). |
| 404 | `Requested resource is not found` | Check that the user has connected accounts. This error occurs when the user has no accounts. |
| 403 | `Please contact us to have your API key enabled for Income Summary.` | Contact Customer Success to enable access to the feature. |
| 400 | `User's accounts contains mixed currencies` | The user's accounts contain different currencies, which prevents aggregation. Contact Customer Success before removing accounts to resolve the currency mismatch. |
| 500 | `Internal server error. Please contact support.` | Contact Customer Success. |

## GET `/users/{userId}/expenses/{snapshotId}`

| Status code | Response title/detail | Action |
| --- | --- | --- |
| 401 | `Invalid authorization token.` | Set the request header to `Authorization: Bearer YOUR_ACCESS_TOKEN`. |
| 403 | `Token has expired` | Get a new access token from `POST /token`. |
| 400 | `User ID value is not valid` | Check the format of `userId` in the URL. |
| 400 | `Snapshot ID value is not valid` | Check the format of `snapshotId` in the URL. |
| 400 | `Accept type application/json is not supported on requested endpoint.` | Check the `Accept` request header against the endpoint's supported response media types. |
| 403 | `Access to this resource is forbidden` | Check your token's scope (its access permissions). You may need `scope=SERVER_ACCESS` in the token request body, not a request header. |
| 401 | `Unauthorized access` | Check that your token grants access to the resources in the URL. |
| 400 | `Snapshot ID value is not supplied` | Include `snapshotId` in the URL. |
| 500 | `Internal server error. Please contact support.` | Contact Customer Success. |
| 404 | `Requested user does not exist.` | Check that the user still exists and belongs to the application associated with your API key. |
| 400 | `Invalid expenses snapshot ID provided` | Check that `snapshotId` identifies the expenses snapshot you want to retrieve. |
| 404 | `User doesn't have any accounts` | Check that the user has connected accounts. |
| 403 | `Please contact us to have your API key enabled for Income Summary.` | Contact Customer Success to enable access to the feature. |

## POST `/users/{userId}/statements`

| Status code | Response title/detail | Action |
| --- | --- | --- |
| 401 | `Invalid authorization token.` | Set the request header to `Authorization: Bearer YOUR_ACCESS_TOKEN`. |
| 403 | `Token has expired` | Get a new access token from `POST /token`. |
| 400 | `User ID value is not valid` | Check the format of `userId` in the URL. |
| 400 | `Statement is not valid` | Check that your request includes a valid statement file or an `institutionId`. |
| 413 | `Request Too Long` | Upload a smaller statement file. |
| 400 | `Institution AU00000 is not supported on this endpoint` | Choose an institution that supports statement uploads. |
| 400 | `Accept type application/json is not supported on requested endpoint.` | Check the `Accept` request header against the endpoint's supported response media types. |
| 403 | `Access to this resource is forbidden` | Check your token's scope (its access permissions). You may need `scope=SERVER_ACCESS` in the token request body, not a request header. |
| 401 | `Unauthorized access` | Check that your token grants access to the resources in the URL. |
| 404 | `Requested user does not exist.` | Check that the user still exists and belongs to the application associated with your API key. |
| 403 | `Please contact us to have your API key enabled for Income Summary.` | Contact Customer Success to enable access to the feature. |
| 400 | `User's accounts contains mixed currencies` | The user's accounts contain different currencies, which prevents aggregation. Contact Customer Success before removing accounts to resolve the currency mismatch. |
| 500 | `Internal server error. Please contact support.` | Contact Customer Success. |
| 503 | `Service is currently unavailable. Please try again later.` | Try again. If the error persists, contact Customer Success. |
