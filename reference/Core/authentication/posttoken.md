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
[block:callout]
{
  "type": "danger",
  "title": "Your API keys carry many privileges, so be sure to keep them secret! Do not share your API keys in publicly accessible areas such GitHub, client-side code, etc.",
  "body": ""
}
[/block]
## Prerequisites

Prior to authenticating your application you will need to complete the following steps:

1. [Sign-up](https://dashboard.basiq.io/) to the Basiq API service
2. Grab an API key for your application (via the [Developer Dashboard](https://dashboard.basiq.io/))

## Steps to authenticate

Pass the API key in the Authorization header and Basiq API version you intend to use, as well as the scope of access you need. The server will validate the key and if everything is successful will issue an access token.
[block:callout]
{
  "type": "success",
  "body": "The scope of a `CLIENT_ACCESS` token is restricted and should be used when making any calls directly from the client side. \n\nA `SERVER_ACCESS` token can be used for all endpoints and has full access to create resources and retrieve data. **Never** expose a server access token on your client side!",
  "title": "Token scopes"
}
[/block]

[block:callout]
{
  "type": "warning",
  "title": "CLIENT_ACCESS tokens must be bound to a userId",
  "body": "Any token generated with a `CLIENT_ACCESS` scope must be bound to a `userId`\n\nYou will get this `userId` by calling [Create a user Endpoint](https://api.basiq.io/reference/createuser)."
}
[/block]

[block:html]
{
  "html": "<script src=\"https://code.jquery.com/jquery-3.5.0.js\"></script>\n<script>\n  setTimeout(() => {    \n    const toolTip =  \"<p class='toolTip'>&#8505;&#65039; &nbsp; Populate your request using the input fields provided <br/><br/> Once a token is generated, please copy the token to use it on other service calls</p>\";\n    $(toolTip).insertAfter($('.rm-PlaygroundRequest'));\n\t}, 100)\n//  setTimeout(() => {    \n //   const toolTi =  \"<p class='Info-infoBadge3luOwOnjfNiR Info-infoBadge_tooltip24vnuq69qR2X'> Please add required fields. </p>\";\n //   $(toolTi).insertAfter($('.headline-container-article-info2GaOf2jMpV0r'));\n//\t}, 100)\n  \n</script>"
}
[/block]