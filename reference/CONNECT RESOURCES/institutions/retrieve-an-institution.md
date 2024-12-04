---
title: Retrieve an institution
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
Retrieves the details of an existing institution. You need only supply the institutions unique identifier.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Arguments
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        **id**
        *string, required*
      </td>

      <td style={{ textAlign: "left" }}>
        The identifier of the institution to be retrieved.
      </td>
    </tr>
  </tbody>
</Table>

**Returns**

Returns an institution if a valid ID was provided. Returns an [error](https://basiq.readme.io/v1.0/reference#errors) otherwise.

```json Definition
GET /institutions/{institution.id}
```

```json Example Request
GET /institutions/AU00000 HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.1 200 OK
Content-Type: application/json

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
}
```
