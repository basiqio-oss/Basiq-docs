---
title: Create MFA response
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
Use this to create a new MFA challenge response to job step: `mfa-challenge`

> 🚧 Authorization
>
> Ensure that you generate an authentication token with 
>
> * `scope= CLIENT_ACCESS` and 
> * `basiq-version = 2.1` 
>
> to create this resource

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
        **mfa-response**
        *array of strings*
      </td>

      <td style={{ textAlign: "left" }}>
        One time password or answer to a security question/s e.g.  ["1234"]
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

```json Definition
POST /jobs/{job.id}/mfa
```

**Returns**

Returns a job if MFA response was correct. Returns an[ error](https://api.basiq.io/docs/errors-1) otherwise.

```json Example Request: OTP
POST /jobs/61723/mfa HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json

{
  "mfa-response": ["1234"]
}
```
```json Example Request: Question/s
POST /jobs/61723/mfa HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json

{
  "mfa-response": ["Basiq", "AU00002"]
}
```
```json Example: MFA Bendigo
POST /jobs/61723/mfa HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json

{
  "mfa-response": ["confirmed"]
}
```

```json Example Response
HTTP/1.1 202 Accepted
Content-Type: application/json
{
  "type": "job",
  "id": "61723",
  "links": {
    "self": "https://au-api.basiq.io/jobs/61723"
  }
}
```
