---
title: Authentication
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
When working with Basiq APIs your application will need to complete the authentication process first before you can access any of the available resources.

The process requires you to exchange your API key for a token. Once you obtain the token, you can call any of the available API services by simply including the token in the Authorization header of each request.

**Note: Your token will expire after 60 minutes, so ensure you are caching the token and only generating a new one when necessary. Excessive use of the `/token` endpoint may result in unsuccessful requests.** 

> ❗️ Your API keys carry many privileges, so be sure to keep them secret!
> 
> Do not share your API keys in publicly accessible areas such GitHub, client-side code, etc.

Prior to authenticating your application you will need to complete the following steps:

1. [Sign-up](https://dashboard.basiq.io/) to the Basiq API service
2. Grab your API key for your application (via the [Developer Dashboard](https://dashboard.basiq.io/))

> 📘 Token scope: CLIENT_ACCESS or SERVER_ACCESS
> 
> The scope of a `CLIENT_ACCESS` token is restricted and should be used for all client side requests for security reasons.
> 
> `CLIENT_ACCESS` token only grants access to the following requests:
> 
> - Access the Consent UI (Note: for this request you will need to bind your `userId` to the access token the same way you do the scope).
> 
> `SERVER_ACCESS` tokens can be used for all endpoints and has full access to create resources and retrieve data. They should never be exposed on the client side.