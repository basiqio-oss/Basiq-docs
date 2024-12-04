---
title: Versioning
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
Your API version controls the API behaviour you see e.g. what properties you see in responses, what parameters you’re permitted to send in requests etc.

In order to gain access to the API, you need to pass the appropriate version in HTTP header basiq-version, when[ exchanging ](https://basiq.readme.io/v1.0/reference#authentication)your API key for a token.\
You don't need to pass basiq-version header in any subsequent requests.

You can check the list of API changes via the API [Changelog](https://basiq.readme.io/v1.0/reference#changelog).

```json Example Request
POST /token HTTP/1.1
Authorization: Basic YOUR_API_KEY
Content-Type: application/x-www-form-urlencoded
basiq-version: 1.0
```
