---
title: List all institutions
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
Use this collection to retrieve a list of [institutions](https://basiq.readme.io/v0.9/reference#institutions). Each entry in the array is a separate institution object.

```json Definition
GET /institutions
```

```json Example Request
GET /institutions HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTPHTTP//1.11.1  200200  OKOK
 Content-TypeContent-Type::  application/jsonapplication/json

{
  "type": "list",
  "size": 89,
  "data": [
    {
      "type": "institution",
      "id": "AU00000",
      "name": "Basiq Test Bank",
      "shortName": "Basiq Test Bank",
      "institutionType": "Test Bank",
      "country": "Australia",
      "serviceName": "Personal Online Banking",
      "serviceType": "Test",
      "loginIdCaption": "Login",
      "passwordCaption": "Password",
      "logo": {
        "type": "image",
        "links": {
          "self": "https://s3-ap-southeast-2.amazonaws.com/basiq-institutions/AU00000.png"
        }
      },
      "links": {
        "self": "https://au-api.basiq.io/institutions/AU00000"
      }
    },
    null
  ],
  "links": {
    "self": "https://au-api.basiq.io/institutions"
  }
}
```
