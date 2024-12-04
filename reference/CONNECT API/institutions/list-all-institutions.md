---
title: List all institutions
excerpt: ''
deprecated: true
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Use this collection to retrieve a list of [institutions](https://basiq.readme.io/v2.0/reference#institutions). Each entry in the array is a separate institution object.

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
        **[filter](https://api.basiq.io/docs/collections-filters)**
        *optional*
      </td>

      <td style={{ textAlign: "left" }}>
        This list can be [filtered](https://api.basiq.io/docs/collections-filters) by the following properties:

        * `country`

        * `tier`

        * `serviceType`

        * `institutionType`

        * `stage`

        Only equals (eq) and not equals (ne) operations are currently supported.
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
  "totalCount": 56,
  "data": [
    {
      "type": "institution",
      "id": "AU00000",
      "name": "Hooli Bank",
      "shortName": "Hooli",
      "institutionType": "Test Bank",
      "country": "Australia",
      "serviceName": "Personal Online Banking",
      "serviceType": "Personal Banking",
      "loginIdCaption": "Login",
      "passwordCaption": "Password",
      "tier": "4",
      "authorization": "user",
      "features": {
        "login":[
           "web"
         ],
        "accounts": {
          "accountNo": [
            "web"
          ],
          "name": [
            "web"
          ],
          ...
        },
        "transactions": {
          "status": [
            "web"
          ],
          "description": [
            "web"
          ],
          ...
        },
        "profile": {
          "fullName": [
            "web"
          ],
          "firstName": [
            "web"
          ],
          ...
        }
      },
      "forgottenPasswordUrl": "https://hooli.com.au/forgotten...",
      "stage": "beta",
      "status": "under-maintenance",
      "stats": {
        "averageDurationMs": {
          "verifyCredentials": 3600,
          "retrieveAccounts": 4500,
          "retrieveTransactions": 2300,
          "retrieveMeta": 1200,
          "total": 11600
        }
      },
      "logo": {
        "type": "image",
        "colors": null,
        "links": {
          "square": "https://d388vpyfrt4zrj.cloudfront.net/AU00000.svg",
          "full": "https://d388vpyfrt4zrj.cloudfront.net/AU00000-full.svg"
        }
      },
      "links": {
        "self": "https://au-api.basiq.io/institutions/AU00000"
      }
    },
 }
```
