---
title: Errors
excerpt: >-
  Understand Connect API error responses and bank-returned errors surfaced on
  jobs.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
The Connect API uses conventional HTTP response codes to indicate the success or failure of an API request. In general, codes in the `2xx` range indicate success, codes in the `4xx` range indicate an error that failed given the information provided (e.g., a required parameter was omitted, user's credentials are invalid, etc.), and codes in the `5xx` range indicate an error with the Connect API's servers (these are rare).

In addition to returning an appropriate HTTP code the body will also include a JSON formatted error object that provides more details about the specifics of the error. The error object will return the error as an array to indicate multiple errors (where present).

## Consent UI and bank errors

For consent UI flows, any error returned by the bank is surfaced on the Jobs endpoint. Because each bank can return different authorization and consent messages, bank-returned errors are not maintained as a fixed error-code list.

When a job step fails, inspect the failed step's `result` object for the bank-specific error details:

* `code` identifies the error category.
* `title` provides a short summary.
* `detail` contains the bank-returned message, when available.

In this example, the first step, `verify-credentials`, failed because the bank returned `access_denied`:

```json Job with bank-returned error
{
  "type": "job",
  "id": "5c50a2d1-561c-48c4-a186-b763bdf5502a",
  "created": "2024-09-25T04:22:25Z",
  "updated": "2024-09-25T04:22:38Z",
  "jobType": "connection",
  "steps": [
    {
      "title": "verify-credentials",
      "status": "failed",
      "result": {
        "code": "authorization-failed",
        "title": "Authorization failed",
        "detail": "access_denied"
      }
    },
    {
      "title": "retrieve-accounts",
      "status": "pending",
      "result": null
    },
    {
      "title": "retrieve-transactions",
      "status": "pending",
      "result": null
    }
  ],
  "links": {
    "self": "https://au-api.basiq.io/jobs/5c50a2d1-561c-48c4-a186-b763bdf5502a",
    "source": "https://au-api.basiq.io/users/b2afc9cd-0f3c-41f0-9e19-d18482abc9fc/connections/60612323-9c42-478a-8ff2-640445dbe64a"
  }
}
```

## API error response format

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Attributes
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `correlationId`
      </td>

      <td style={{ textAlign: "left" }}>
        a unique identifier for this particular occurrence of the problem.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `code`
      </td>

      <td style={{ textAlign: "left" }}>
        an application-specific [error code](https://api.basiq.io/docs/codes), expressed as a string value.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `title`
      </td>

      <td style={{ textAlign: "left" }}>
        a short, human-readable summary of the problem.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `detail`
      </td>

      <td style={{ textAlign: "left" }}>
        a human-readable explanation specific to this occurrence of the problem.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `source`
      </td>

      <td style={{ textAlign: "left" }}>
        an object containing references to the source of the error, optionally including any of the following members:
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `pointer` the location to the object or attribute that the error relates to

        * `parameter` a string indicating which URI query parameter caused the error.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

```json EXAMPLE ERROR OBJECT
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
  "type": "list",
  "correlationId": "bd1183d9-c9d8-11e7-909a-6789bfc80ac5",
  "data": [
    {
      "type": "error",
      "code": "parameter-not-supplied",
      "title": "Required parameter not supplied",
      "detail": "Institution ID  parameter is required.",
      "source": {
        "pointer": "connection/institution/id",
        "parameter": "id"
      }
    }
  ]
}
```