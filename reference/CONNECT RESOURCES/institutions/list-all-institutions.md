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
Use this collection to retrieve a list of [institutions](https://basiq.readme.io/v1.0/reference#institutions). Each entry in the array is a separate institution object.

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
        **[filter](https://basiq.readme.io/v1.0/reference#filters)**
        *optional*
      </td>

      <td style={{ textAlign: "left" }}>
        This list can be [filtered](https://basiq.readme.io/v1.0/reference#filters) by the following properties:

        * institution.country
        * institution.tier
        * institution.serviceType
        * institution.institutionType

        Only equality operation is currently supported.
      </td>
    </tr>
  </tbody>
</Table>

```json Definition
GET /institutions
```

```json Example Request
GET /institutions HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.11.1 200 OK
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
            "tier": "4",
            "logo": {
                "type": "image",
                "colors": {
                    "primary": "#000000"
                },
                "links": {
                    "square": "https://s3-ap-southeast-2.amazonaws.com/basiq-institutions/AU00000.svg",
                    "full": "https://s3-ap-southeast-2.amazonaws.com/basiq-institutions/AU00000-full.svg"
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
