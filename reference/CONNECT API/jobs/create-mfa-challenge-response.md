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
> - `scope= CLIENT_ACCESS` and 
> - `basiq-version = 2.1` 
> 
> to create this resource

[block:parameters]
{
  "data": {
    "h-0": "Arguments",
    "h-1": "",
    "0-0": "**mfa-response**  \n_array of strings_",
    "0-1": "One time password or answer to a security question/s e.g.  [\"1234\"]",
    "1-0": "",
    "1-1": ""
  },
  "cols": 2,
  "rows": 2,
  "align": [
    "left",
    "left"
  ]
}
[/block]


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