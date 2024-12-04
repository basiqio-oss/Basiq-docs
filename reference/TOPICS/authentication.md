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

> ❗️ **Your API keys carry many privileges, so be sure to keep them secret! Do not share your API keys in publicly accessible areas such GitHub, client-side code, etc.** 

**Prerequisites**

1. Prior to authenticating your application you will need to complete the following steps:

2. [Sign-up](https://dashboard.basiq.io/login) to the Basiq API service\
   Grab your api key for your application (via the [Developer Dashboard](https://dashboard.basiq.io/))

**Steps to authenticate**

1. Call `/oauth2/token` passing in the api key in the `Authorization` header of the request
2. The server will validate the key and if everything is successful will issue an access token along with the following properties:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Property
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        **access\_token**
        *string, readonly* 
      </td>

      <td style={{ textAlign: "left" }}>
        The generated access token.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **token\_type**\
        *string, readonly* 
      </td>

      <td style={{ textAlign: "left" }}>
        This value will always be `Bearer`.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **expires\_in**\
        *number, readonly* 
      </td>

      <td style={{ textAlign: "left" }}>
        The number of seconds left before the token becomes invalid.
      </td>
    </tr>
  </tbody>
</Table>

This access token is the key to making successful requests to the Basiq API. From here on you will need to include this access token in the header when requesting any of the secured resources as follows:\
`Authorization: Bearer [access_token]`

> 🚧 Note that tokens have a short lifespan and as such should not be stored permanently. Once a token has expired your application will need to reauthenticate.

**Possible Errors**

In the event that something goes wrong a valid HTTP status code and error object will be returned in the body of the response.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>

      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        **invalid\_request** 
      </td>

      <td style={{ textAlign: "left" }}>
        The request is missing a required parameter, includes an unsupported parameter value (other than grant type) or is otherwise malformed.\
        `Http 400 Bad Request`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **invalid\_client** 
      </td>

      <td style={{ textAlign: "left" }}>
        Application authentication failed (e.g., unknown application, no authentication included, or unsupported authentication method).\
        `Status 401 Unauthorized`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **invalid\_grant** 
      </td>

      <td style={{ textAlign: "left" }}>
        The provided Authorization grant (e.g. apiKey) or token is invalid, expired or has been revoked.\
        `Status 400 Bad Request`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **unauthorized\_client** 
      </td>

      <td style={{ textAlign: "left" }}>
        The authenticated application is not authorized to use this Authorization grant type.\
        `Status 400 Bad Request`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **unsupported\_grant\_type** 
      </td>

      <td style={{ textAlign: "left" }}>
        The Authorization grant type is not supported.\
        `Status 400 Bad Request`
      </td>
    </tr>
  </tbody>
</Table>

```json Definition
POST /oauth2/token
```

```json Example Request (to acquire token)
POST /oauth2/token HTTP/1.1
Authorization: Basic YOUR_API_KEY
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials
```

```json Example Response
HTTP/1.1 200 OK
Content-Type: application/json

{
    "access_token":"YOUR_ACCESS_TOKEN",
    "token_type":"Bearer",
    "expires_in":3600
}
```

```json Example Request (using token)
GET /connections HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json
```
