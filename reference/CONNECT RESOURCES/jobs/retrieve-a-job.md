---
title: Retrieve a job
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
Retrieves the details of an existing job. You need only supply the unique job identifier that was returned upon job creation.

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
        *required*
      </td>

      <td style={{ textAlign: "left" }}>
        The identifier of the job to be retrieved.
      </td>
    </tr>
  </tbody>
</Table>

Returns\
Returns a job if a valid job ID was provided. Returns an[ error](https://basiq.readme.io/v1.0/reference#errors) otherwise.

```json Definition
GET /jobs/{job.id}
```

```json Example Request
GET /jobs/61723 HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.1 200 OK
Content-Type: application/json

{
  "type": "job",
  "id": "61723",
  "created": "2016-06-08T09:10:32.000Z",
  "updated": "2016-06-08T09:14:28.000Z",
  "steps": [
    {
      "title": "verify-credentials",
      "status": "success",
      "result": [
        {
          "type": "link",
          "url": "/users/ea3a81/connections/8fce3b"
        }
      ]
    },
    {
      "title": "retrieve-accounts",
        "status": "in-progress",
        "result": null
    },
    {
      "title": "retrieve-transactions",
      "status": "pending",
      "result": null
    }
  ],
  "links": {
    "self": "/jobs/61723",
    "source": "/users/ea3a81/connections/8fce3b"
  }
}
```
