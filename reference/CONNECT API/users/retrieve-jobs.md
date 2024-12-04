---
title: Retrieve jobs
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
Retrieves the job details for an existing user for all jobs performed against that user over the previous 7 days. You need only supply the unique user identifier that was returned upon user creation. Jobs are returned in descending order of the *updated* field

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
        **[filter](https://api.basiq.io/docs/collections-filters)**
        *optional*
      </td>

      <td style={{ textAlign: "left" }}>
        This list can be [filtered](https://api.basiq.io/docs/collections-filters) by the following property: `connection.id`.
      </td>
    </tr>
  </tbody>
</Table>

**Returns**\
Returns an array of jobs if a valid user ID was provided. Returns an [error](https://api.basiq.io/docs/errors-1) otherwise.

```http Defintion
GET /users/{user.id}/jobs
```
```curl
$ curl \
-s https://api.intercom.io/users/5714dd359a3fd47136000001 \
-H 'Authorization:Bearer <Your access token>' \
-H 'Accept:application/json'
```
```http HTTP Request
POST /users/ea3a81 HTTP/1.1
Content-Type: application/json
Authorization: Bearer YOUR_ACCESS_TOKEN

{
  "email": "gavin@hooli.xyz"
}
```

```json Example Request
GET /users/ea3a81/jobs HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.1 200 OK
Content-Type: application/json

{
  "type": "list",
  "size": 2,
  "data": [
    {
      "type": "job",
      "id": "3d7827b4",
      "created": "2019-11-19T02:29:19Z",
      "updated": "2019-11-19T02:29:21Z",
      "institution": {
        "type": "institution",
        "id": "AU00000",
        "links": {
          "self": "https://au-api.basiq.io/institutions/AU00000"
        }
      },
      "steps": [
        {
          "title": "verify-credentials",
          "status": "success",
          "result": {
            "type": "link",
            "url": "/users/55bfd18/connections/5f84ff2"
          }
        },
        {
          "title": "retrieve-accounts",
          "status": "success",
          "result": {
            "type": "link",
            "url": "/users/55bfd18/accounts?filter=institution.id.eq('AU00000')"
          }
        },
        {
          "title": "retrieve-transactions",
          "status": "in-progress",
          "result": null
        }
      ],
      "links": {
        "self": "https://au-api.basiq.io/jobs/3d7827b4",
        "source": "https://au-api.basiq.io/users/55bfd18/connections/5f84ff"
      }
    },
    {
      "type": "job",
      "id": "ac85c3f",
      "created": "2019-11-19T02:26:01Z",
      "updated": "2019-11-19T02:27:50Z",
      "institution": {
        "type": "institution",
        "id": "AU00000",
        "links": {
          "self": "https://au-api.basiq.io/institutions/AU00000"
        }
      },
      "steps": [
        {
          "title": "verify-credentials",
          "status": "success",
          "result": {
            "type": "link",
            "url": "/users/55bfd18/connections/c148bbb"
          }
        },
        {
          "title": "retrieve-accounts",
          "status": "success",
          "result": {
            "type": "link",
            "url": "/users/55bfd18/accounts?filter=institution.id.eq('AU00000')"
          }
        },
        {
          "title": "retrieve-transactions",
          "status": "success",
          "result": {
            "type": "link",
            "url": "/users/55bfd18/transactions?filter=institution.id.eq('AU00000')"
          }
        }
      ],
      "links": {
        "self": "https://au-api.basiq.io/jobs/ac85c3f",
        "source": "https://au-api.basiq.io/users/55bfd18/connections/c148bbb"
      }
    }
  ],
  "links": {
    "self": "https://au-api.basiq.io/users/55bfd18/jobs"
  }
}
```
