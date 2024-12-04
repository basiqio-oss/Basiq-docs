---
title: Retrieve an institution
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

Returns an institution if a valid ID was provided. Returns an [error](https://api.basiq.io/docs/errors-1) otherwise.

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
        "mfaChallenge": [],
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
