---
title: Authentication
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
When working with Basiq APIs your application will need to complete the authentication process first before you can access any of the available resources.

The authentication process is fairly straight forward, and simply requires you to exchange your API key for a token. Once you obtain the token, you can call any of the available API services by simply including the token in the Authorization header of each request.
[block:callout]
{
  "type": "danger",
  "body": "**Your API keys carry many privileges, so be sure to keep them secret! Do not share your API keys in publicly accessible areas such GitHub, client-side code, etc.**"
}
[/block]

**Prerequisites**

Prior to authenticating your application you will need to complete the following steps:

1. [Sign-up](https://dashboard.basiq.io/login) to the Basiq API service
2. Grab your API key for your application (via the [Developer Dashboard](https://dashboard.basiq.io/))


**Steps to authenticate**

1. Call /token passing in the API key in the Authorization header of the request and Basiq API version you intent to use
2. The server will validate the key and if everything is successful will issue an access token along with the following properties:
[block:parameters]
{
  "data": {
    "h-0": "Property",
    "h-1": "Description",
    "0-0": "**access_token**\n*string, readonly* ",
    "0-1": "The generated access token.",
    "2-0": "**token_type**\n*string, readonly* ",
    "2-1": "This value will always be `Bearer`.",
    "4-0": "**expires_in**\n*number, readonly* ",
    "4-1": "The number of seconds left before the token becomes invalid."
  },
  "cols": 2,
  "rows": 6
}
[/block]
This access token is the key to making successful requests to the Basiq API. From here on you will need to include this access token in the header when requesting any of the secured resources as follows: 

`Authorization: Bearer [access_token]`
[block:callout]
{
  "type": "warning",
  "body": "Note that tokens have a short lifespan and as such should not be stored permanently. Once a token has expired your application will need to reauthenticate."
}
[/block]
**Possible Errors**

In the event that something goes wrong a valid HTTP status code and error object will be returned in the body of the response.
[block:parameters]
{
  "data": {
    "0-0": "invalid-request",
    "0-1": "**Status 400 Bad Request**\nThe request is missing a required parameter, includes an unsupported parameter value (other than grant type) or is otherwise malformed.",
    "6-1": "**Status 403 Forbidden**\nAccess to the requested resource is forbidden.  This will be returned when a Basiq partner account is temporarily disabled.",
    "6-0": "access-denied",
    "8-0": "parameter-not-valid",
    "8-1": "**Status 404 Not Found**\nResource not found.  This will be returned once a Basiq partner account has been deleted.",
    "10-0": "internal-server-error",
    "10-1": "**Status 500 Internal Server Error**\nA generic HTTP error message, an unexpected condition was encountered.",
    "12-0": "invalid-grant",
    "14-0": "unauthorized-client",
    "12-1": "**Status 400 Bad Request**\nThe provided Authorization grant (e.g. apiKey) or token is invalid, expired or has been revoked.\n\nError status no longer returned and to be removed from docs from Aug 21",
    "14-1": "**Status 400 Bad Request**\nThe authenticated application is not authorized to use this Authorization grant type.\n\nError status no longer returned and to be removed from docs from Aug 21",
    "2-0": "parameter-not-valid",
    "2-1": "**Status 400 Bad Request**\nAuthorization header parameter is required/invalid or the older version is no longer supported",
    "4-1": "**Status 400 Bad Request**\nThe Authorization grant type is not supported.",
    "4-0": "unsupported-grant-type",
    "16-0": "invalid-client",
    "16-1": "**Status 401 Unauthorized**\nApplication authentication failed (e.g., unknown application, no authentication included, or unsupported authentication method).\n\nError status no longer returned and to be removed from docs from Aug 21"
  },
  "cols": 2,
  "rows": 18
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "POST /token",
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
      "code": "POST /token HTTP/1.1\nAuthorization: Basic YOUR_API_KEY\nContent-Type: application/x-www-form-urlencoded\nbasiq-version: 2.1\n\nscope=SERVER_ACCESS",
      "language": "json",
      "name": "Example Request (to acquire token with the full access scope (with the full access scope the scope parameter is optional))"
    }
  ],
  "sidebar": true
}
[/block]

[block:callout]
{
  "type": "success",
  "body": "The scope of a CLIENT_ACCESS token is restricted and should be used on your client application to pass user credentials when creating a connection.  This means that user credentials are passed straight through to Basiq and do not ever hit your server.\n\nCLIENT_ACCESS token only grants access to the following requests:\n* [Retrieve or list all institutions](https://api.basiq.io/reference#retrieve-an-institution) \n* [Create a connection](https://api.basiq.io/reference#create-a-connection)\n* [Update a connection](https://api.basiq.io/reference#update-a-connection)\n* [Check job status](https://api.basiq.io/reference#retrieve-a-job) \n\nSERVER_ACCESS token can be used for all endpoints and has full access to create resources and retrieve data",
  "title": "Token scope: CLIENT_ACCESS or SERVER_ACCESS"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "POST /token HTTP/1.1\nAuthorization: Basic YOUR_API_KEY\nContent-Type: application/x-www-form-urlencoded\nbasiq-version: 2.1\n\nscope=CLIENT_ACCESS",
      "language": "json",
      "name": "Example Request (to acquire token with the restricted access scope)"
    }
  ],
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n    \"access_token\":\"YOUR_ACCESS_TOKEN\",\n    \"token_type\":\"Bearer\",\n    \"expires_in\":3600\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "GET /users/ea3a81/accounts HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN\nContent-Type: application/json",
      "language": "json",
      "name": "Example Request (using token)"
    }
  ],
  "sidebar": true
}
[/block]