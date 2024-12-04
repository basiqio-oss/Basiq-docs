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

In order to gain access to the API, you need to pass the appropriate version in HTTP header basiq-version, when[ exchanging ](https://api.basiq.io/reference/authentication)your API key for a token. 

You don't need to pass basiq-version header in any subsequent requests. 

**Latest version: 2.1** 
**Stable version: 3.0**
[block:code]
{
  "codes": [
    {
      "code": "POST /token HTTP/1.1\nAuthorization: Basic YOUR_API_KEY\nContent-Type: application/x-www-form-urlencoded\nbasiq-version: 3.0",
      "language": "json",
      "name": "Example Request"
    }
  ],
  "sidebar": true
}
[/block]