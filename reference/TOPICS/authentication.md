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

The authentication process is fairly straight forward, and simply requires you to exchange your API key for a token. Once you obtain the token, you can call any of the available API services by simply including the token in the `Authorization` header of each request.
[block:callout]
{
  "type": "danger",
  "body": "**Your API keys carry many privileges, so be sure to keep them secret! Do not share your API keys in publicly accessible areas such GitHub, client-side code, etc.** "
}
[/block]
**Prerequisites**

1. Prior to authenticating your application you will need to complete the following steps:

2. [Sign-up](https://dashboard.basiq.io/login) to the Basiq API service
Grab your api key for your application (via the [Developer Dashboard](https://dashboard.basiq.io/))


**Steps to authenticate**

1. Call `/oauth2/token` passing in the api key in the `Authorization` header of the request
2. The server will validate the key and if everything is successful will issue an access token along with the following properties:
[block:parameters]
{
  "data": {
    "h-0": "Property",
    "h-1": "Description",
    "0-0": "**access_token**\n*string, readonly* ",
    "0-1": "The generated access token.",
    "1-0": "**token_type**\n*string, readonly* ",
    "1-1": "This value will always be `Bearer`.",
    "2-0": "**expires_in**\n*number, readonly* ",
    "2-1": "The number of seconds left before the token becomes invalid."
  },
  "cols": 2,
  "rows": 3
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
    "0-0": "**invalid_request** ",
    "0-1": "The request is missing a required parameter, includes an unsupported parameter value (other than grant type) or is otherwise malformed. \n`Http 400 Bad Request`",
    "1-0": "**invalid_client** ",
    "1-1": "Application authentication failed (e.g., unknown application, no authentication included, or unsupported authentication method). \n`Status 401 Unauthorized`",
    "2-0": "**invalid_grant** ",
    "2-1": "The provided Authorization grant (e.g. apiKey) or token is invalid, expired or has been revoked. \n`Status 400 Bad Request`",
    "3-0": "**unauthorized_client** ",
    "3-1": "The authenticated application is not authorized to use this Authorization grant type. \n`Status 400 Bad Request`",
    "4-0": "**unsupported_grant_type** ",
    "4-1": "The Authorization grant type is not supported. \n`Status 400 Bad Request`"
  },
  "cols": 2,
  "rows": 5
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "POST /oauth2/token",
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
      "code": "POST /oauth2/token HTTP/1.1\nAuthorization: Basic YOUR_API_KEY\nContent-Type: application/x-www-form-urlencoded\n\ngrant_type=client_credentials\n",
      "language": "json",
      "name": "Example Request (to acquire token)"
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
      "code": "GET /connections HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN\nContent-Type: application/json",
      "language": "json",
      "name": "Example Request (using token)"
    }
  ],
  "sidebar": true
}
[/block]