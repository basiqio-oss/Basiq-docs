---
title: Generate an auth token
excerpt: >-
  Use this endpoint to retrieve a token that will be passed as authorization
  header for Basiq API
api:
  file: core.json
  operationId: postToken
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> ❗️ Your API keys carry many privileges, so be sure to keep them secret! Do not share your API keys in publicly accessible areas such GitHub, client-side code, etc.

## Prerequisites

Prior to authenticating your application you will need to complete the following steps:

1. [Sign-up](https://dashboard.basiq.io/) to the Basiq API service
2. Grab an API key for your application (via the [Developer Dashboard](https://dashboard.basiq.io/))

## Steps to authenticate

Pass the API key in the Authorization header and Basiq API version you intend to use, as well as the scope of access you need. The server will validate the key and if everything is successful will issue an access token.

> 👍 Token scopes
>
> The scope of a `CLIENT_ACCESS` token is restricted and should be used when making any calls directly from the client side. 
>
> A `SERVER_ACCESS` token can be used for all endpoints and has full access to create resources and retrieve data. **Never** expose a server access token on your client side!

> 🚧 CLIENT\_ACCESS tokens must be bound to a userId
>
> Any token generated with a `CLIENT_ACCESS` scope must be bound to a `userId`
>
> You will get this `userId` by calling [Create a user Endpoint](https://api.basiq.io/reference/createuser).

<HTMLBlock>{`
<script src="https://code.jquery.com/jquery-3.5.0.js"></script>
<script>
  setTimeout(() => {    
    const toolTip =  "<p class='toolTip'>&#8505;&#65039; &nbsp; Populate your request using the input fields provided <br/><br/> Once a token is generated, please copy the token to use it on other service calls</p>";
    $(toolTip).insertAfter($('.rm-PlaygroundRequest'));
	}, 100)
//  setTimeout(() => {    
 //   const toolTi =  "<p class='Info-infoBadge3luOwOnjfNiR Info-infoBadge_tooltip24vnuq69qR2X'> Please add required fields. </p>";
 //   $(toolTi).insertAfter($('.headline-container-article-info2GaOf2jMpV0r'));
//	}, 100)
  
</script>
`}</HTMLBlock>
