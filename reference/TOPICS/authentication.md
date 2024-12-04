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

> ❗️ **Your API keys carry many privileges, so be sure to keep them secret! Do not share your API keys in publicly accessible areas such GitHub, client-side code, etc.**

**Prerequisites**

Prior to authenticating your application you will need to complete the following steps:

1. [Sign-up](https://dashboard.basiq.io/login) to the Basiq API service
2. Grab your API key for your application (via the [Developer Dashboard](https://dashboard.basiq.io/))

**Steps to authenticate**

1. Call /token passing in the API key in the Authorization header of the request and Basiq API version you intent to use
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

      </td>

      <td style={{ textAlign: "left" }}>

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

      </td>

      <td style={{ textAlign: "left" }}>

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

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

This access token is the key to making successful requests to the Basiq API. From here on you will need to include this access token in the header when requesting any of the secured resources as follows: 

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
        invalid-request
      </td>

      <td style={{ textAlign: "left" }}>
        **Status 400 Bad Request**\
        The request is missing a required parameter, includes an unsupported parameter value (other than grant type) or is otherwise malformed.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        parameter-not-valid
      </td>

      <td style={{ textAlign: "left" }}>
        **Status 400 Bad Request**\
        Authorization header parameter is required/invalid or the older version is no longer supported
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        unsupported-grant-type
      </td>

      <td style={{ textAlign: "left" }}>
        **Status 400 Bad Request**\
        The Authorization grant type is not supported.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        access-denied
      </td>

      <td style={{ textAlign: "left" }}>
        **Status 403 Forbidden**\
        Access to the requested resource is forbidden.  This will be returned when a Basiq partner account is temporarily disabled.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        parameter-not-valid
      </td>

      <td style={{ textAlign: "left" }}>
        **Status 404 Not Found**\
        Resource not found.  This will be returned once a Basiq partner account has been deleted.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        internal-server-error
      </td>

      <td style={{ textAlign: "left" }}>
        **Status 500 Internal Server Error**\
        A generic HTTP error message, an unexpected condition was encountered.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        invalid-grant
      </td>

      <td style={{ textAlign: "left" }}>
        **Status 400 Bad Request**\
        The provided Authorization grant (e.g. apiKey) or token is invalid, expired or has been revoked.

        Error status no longer returned and to be removed from docs from Aug 21
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        unauthorized-client
      </td>

      <td style={{ textAlign: "left" }}>
        **Status 400 Bad Request**\
        The authenticated application is not authorized to use this Authorization grant type.

        Error status no longer returned and to be removed from docs from Aug 21
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        invalid-client
      </td>

      <td style={{ textAlign: "left" }}>
        **Status 401 Unauthorized**\
        Application authentication failed (e.g., unknown application, no authentication included, or unsupported authentication method).

        Error status no longer returned and to be removed from docs from Aug 21
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

```json Definition
POST /token
```

```json Example Request (to acquire token with the full access scope (with the full access scope the scope parameter is optional))
POST /token HTTP/1.1
Authorization: Basic YOUR_API_KEY
Content-Type: application/x-www-form-urlencoded
basiq-version: 2.1

scope=SERVER_ACCESS
```

> 👍 Token scope: CLIENT\_ACCESS or SERVER\_ACCESS
>
> The scope of a CLIENT\_ACCESS token is restricted and should be used on your client application to pass user credentials when creating a connection.  This means that user credentials are passed straight through to Basiq and do not ever hit your server.
>
> CLIENT\_ACCESS token only grants access to the following requests:
>
> * [Retrieve or list all institutions](https://api.basiq.io/reference#retrieve-an-institution) 
> * [Create a connection](https://api.basiq.io/reference#create-a-connection)
> * [Update a connection](https://api.basiq.io/reference#update-a-connection)
> * [Check job status](https://api.basiq.io/reference#retrieve-a-job) 
>
> SERVER\_ACCESS token can be used for all endpoints and has full access to create resources and retrieve data

```json Example Request (to acquire token with the restricted access scope)
POST /token HTTP/1.1
Authorization: Basic YOUR_API_KEY
Content-Type: application/x-www-form-urlencoded
basiq-version: 2.1

scope=CLIENT_ACCESS
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
GET /users/ea3a81/accounts HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json
```
