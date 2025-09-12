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
## POST `/token`

| Status Code | Response Title/Detail                                                      | Action                                                                                                                                                                      |
| :---------- | :------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400         | `Authorization header parameter is required`                               | Provide a valid key-value pair `{"Authorization" : " Basic YOUR_API_KEY" }` inside request header.                                                                          |
| 400         | `Invalid authorization header`                                             | Provide a valid key-value pair `{"Authorization" : " Basic YOUR_API_KEY" }` inside request header.                                                                          |
| 400         | `Version 0.9 is no longer supported. Please upgrade to the latest version` | Provide a valid `basiq-version` (2.0 - 2.1)                                                                                                                                 |
| 400         | `Basiq-version must be specified in HTTP request header`                   | Provide a valid `basiq-version` (2.0 - 2.1)                                                                                                                                 |
| 403         | `Your account has been disabled. Please contact Basiq support.`            | Get in touch with the Customer Success to enable your account.                                                                                                              |
| 403         | `Invalid request`                                                          | Forbidden. There have been too many requests for the token endpoint within a 5 minute period from a specific IP address.                                                    |
| 404         | `Unable to authenticate. Please, check your API key`                       | Provide a valid authorization header. This can happen if your API key is deleted, or your application is deleted, or if you use API key from dev environment in production. |
| 429         | `Too many requests.`                                                       | Query limit reached. Reduce request frequency and try again later.                                                                                                          |
| 500         | `Internal server error`                                                    | There has been some internal error, possibly within the AWS architecture. You'll have to try again and seek assistance from Customer Success if it continues.               |

## POST `/users`

| Status Code | Response Title/Detail                                         | Action                                                                                                                                                                                                           |
| :---------- | :------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400         | `One of 'email' or 'mobile' is required.`                     | Provide key-value pair `"email" : " your email"` or `"mobile" : "your mobile"` or both inside request body                                                                                                       |
| 400         | `Posted user is not in valid format.`                         | Provide valid key-value pair inside request body                                                                                                                                                                 |
| 400         | `Provided email is in bad format.`                            | Provide correct format of email inside request body                                                                                                                                                              |
| 400         | `Provided mobile is in bad format.`                           | Provide correct format of mobile inside request body                                                                                                                                                             |
| 400         | `Accept type is not supported`                                | Provide a valid accept header                                                                                                                                                                                    |
| 400         | `Business name is required when business number is provided.` | Provide business name                                                                                                                                                                                            |
| 401         | `Invalid authorization token.`                                | Provide a key-value pair `{"authorization" : " Bearer YOUR_ACCESS_TOKEN" }` inside request header and provide key-value pair `"email" : " your email"` or `"mobile" : "your mobile"` or both inside request body |
| 403         | `Token has expired`                                           | Get a new access token on `/token` endpoint                                                                                                                                                                      |
| 403         | `Access to this resource is forbidden`                        | Incorrect/missing scope set for the token you are using, You likely need to supply `scope=SERVER_ACCESS`. Make sure when you provide scope you are setting this in the body and not as a request header.         |
| 503         | `Service is currently unavailable. Please try again later.`   | Try again later, and if problem persists reach out to Customer Success                                                                                                                                           |

## GET `/users/{userId}`

| Status Code | Response Title/Detail                                                  | Action                                                                                            |
| :---------- | :--------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------ |
| 400         | `User ID value is not valid`                                           | Check you are providing a valid `userId` in the URL                                               |
| 400         | `Accept type application/json is not supported on requested endpoint.` | Provide a valid accept type                                                                       |
| 401         | `Invalid authorization token.`                                         | Provide a key-value pair `{"authorization" : " Bearer YOUR_ACCESS_TOKEN" }` inside request header |
| 401         | `You are not authorized to access this resource`                       | Ensure you the token you're using is valid for use with the `userId` in the URL                   |
| 403         | `Token has expired`                                                    | Get a new access token on `/token` endpoint                                                       |
| 404         | `Requested user does not exist.`                                       | `userId` does not exist... Provide correct `userId` in URL                                        |
| 500         | `Internal server error. Please contact support.`                       | Contact Customer Success                                                                          |

## All Endpoints - General Errors

| Status Code | Response Title/Detail    | Action                                                                                                               |
| :---------- | :----------------------- | :------------------------------------------------------------------------------------------------------------------- |
| 400         | `Bad Request`            | The request could not be understood by the server due to malformed syntax. Check your request format and parameters. |
| 400         | `Invalid request format` | Ensure your request body is properly formatted JSON and contains all required fields.                                |
| 401         | `Unauthorized`           | Authentication credentials are missing or invalid. Provide valid authorization header.                               |
| 403         | `Forbidden`              | You don't have permission to access this resource. Check your API key permissions and scopes.                        |
| 404         | `Not Found`              | The requested resource could not be found. Verify the endpoint URL and resource ID.                                  |
| 405         | `Method Not Allowed`     | The HTTP method is not supported for this endpoint. Check the API documentation for allowed methods.                 |
| 409         | `Conflict`               | The request conflicts with the current state of the resource. Check for duplicate entries or conflicting operations. |
| 422         | `Unprocessable Entity`   | The request was well-formed but contains semantic errors. Validate your input data.                                  |
| 429         | `Too Many Requests`      | Rate limit exceeded. Wait before making additional requests or contact support to increase limits.                   |
| 500         | `Internal Server Error`  | An unexpected error occurred on the server. Try again later or contact Customer Success if the issue persists.       |
| 502         | `Bad Gateway`            | The server received an invalid response from an upstream server. Try again later.                                    |
| 503         | `Service Unavailable`    | The service is temporarily unavailable. Try again later or check the status page.                                    |
| 504         | `Gateway Timeout`        | The server did not receive a timely response from an upstream server. Try again later.                               |

## Enrich Endpoints

| Status Code | Response Title/Detail            | Action                                                                                            |
| :---------- | :------------------------------- | :------------------------------------------------------------------------------------------------ |
| 400         | `Invalid enrichment parameters`  | Check that all required parameters for enrichment are provided and properly formatted.            |
| 400         | `Enrichment data not available`  | The requested enrichment data is not available for this transaction or account.                   |
| 403         | `Enrichment feature not enabled` | Contact Customer Success to enable enrichment features for your account.                          |
| 429         | `Enrichment rate limit exceeded` | You have exceeded the rate limit for enrichment requests. Wait before making additional requests. |

## Affordability Endpoints

| Status Code | Response Title/Detail                                               | Action                                                                                                                                                              |
| :---------- | :------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 400         | `Dates not in valid format. Date has to be in yyyy-mm-dd format`    | Provide a valid dates format in yyyy-mm-dd format                                                                                                                   |
| 400         | `fromDate not in valid format. Date has to be in yyyy-mm-dd format` | Provide a valid dates format in yyyy-mm-dd format                                                                                                                   |
| 400         | `toDate not in valid format. Date has to be in yyyy-mm-dd format`   | Provide a valid toDate format in yyyy-mm-dd format                                                                                                                  |
| 400         | `toDate must be be after or equal to fromDate`                      | Ensure you are sending a valid date range where toDate is after or equal to fromDate                                                                                |
| 400         | `User's accounts contains mixed currencies`                         | User's accounts contains mixed currencies which is causing issues with aggregation. Remove these accounts                                                           |
| 403         | `Please contact us to have your API key enabled for Affordability.` | You are not enabled for this feature. Please contact Customer Success to have this enabled.                                                                         |
| 404         | `Requested resource is not found`                                   | These accounts are unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications. |

## Income Endpoints

| Status Code | Response Title/Detail                                                | Action                                                                                                                                                            |
| :---------- | :------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400         | `Dates not in valid format. Date has to be in yyyy-mm-dd format`     | Provide a valid dates format in yyyy-mm-dd format                                                                                                                 |
| 400         | `fromDate not in valid format. Date has to be in yyyy-mm-dd format`  | Provide a valid dates format in yyyy-mm-dd format                                                                                                                 |
| 400         | `toDate not in valid format. Date has to be in yyyy-mm-dd format`    | Provide a valid toDate format in yyyy-mm-dd format                                                                                                                |
| 400         | `User's accounts contains mixed currencies`                          | User's accounts contains mixed currencies which is causing issues with aggregation. Remove these accounts                                                         |
| 403         | `Please contact us to have your API key enabled for Income Summary.` | You are not enabled for this feature. Please contact Customer Success to have this enabled.                                                                       |
| 404         | `Requested resource is not found`                                    | This resource is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications. |

## Expenses Endpoints

| Status Code | Response Title/Detail                                               | Action                                                                                                    |
| :---------- | :------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------- |
| 400         | `Dates not in valid format. Date has to be in yyyy-mm-dd format`    | Provide a valid dates format in yyyy-mm-dd format                                                         |
| 400         | `fromDate not in valid format. Date has to be in yyyy-mm-dd format` | Provide a valid dates format in yyyy-mm-dd format                                                         |
| 400         | `toDate not in valid format. Date has to be in yyyy-mm-dd format`   | Provide a valid toDate format in yyyy-mm-dd format                                                        |
| 400         | `User's accounts contains mixed currencies`                         | User's accounts contains mixed currencies which is causing issues with aggregation. Remove these accounts |
| 400         | `Invalid expenses snapshot ID provided`                             | Invalid snapshotId, please check the value you are providing                                              |
| 403         | `Please contact us to have your API key enabled for Expenses.`      | You are not enabled for this feature. Please contact Customer Success to have this enabled.               |
| 404         | `User doesn't have any accounts`                                    | User does not have any accounts connected                                                                 |
