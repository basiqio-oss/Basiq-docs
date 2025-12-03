---
title: Generate an auth token
excerpt: >-
  Use this endpoint to retrieve a token that will be passed as authorization
  header for Basiq API
api:
  file: core.json
  operationId: postToken
hidden: false
---
<Callout icon="❗️" theme="error">
  **Access Tokens**

  The response will contain an access token which will allow you to make secure calls to the Basiq API. They expire every 60 minutes, so we recommend you store it globally and refresh 2-3 times an hour.
</Callout>
