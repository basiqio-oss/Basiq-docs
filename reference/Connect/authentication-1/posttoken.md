---
api:
  file: connect.json
  operationId: postToken
hidden: false
---
<br />

<Callout icon="❗️" theme="error">
  **Access Tokens**

  The response will contain an access token which will allow you to make secure calls to the Basiq API. They expire every 60 minutes, so we recommend you store it globally and refresh 2-3 times an hour.
</Callout>

<Callout icon="🚧" theme="warn">
  **API key format — do not Base64-encode**

  Unlike standard HTTP Basic Auth, the Basiq API key is passed **verbatim** as the header value. The correct header is:

  `Authorization: Basic <your-api-key-as-issued>`

  Base64-encoding the key (as the HTTP spec normally requires for `user:password` credentials) will produce a `400` error. Use the key exactly as issued from the dashboard.
</Callout>