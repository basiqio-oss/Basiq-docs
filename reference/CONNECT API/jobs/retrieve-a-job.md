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
        *string, required*
      </td>

      <td style={{ textAlign: "left" }}>
        The identifier of the job to be retrieved.
      </td>
    </tr>
  </tbody>
</Table>

**Returns**

Returns a job if a valid job ID was provided. Returns an[ error](https://api.basiq.io/docs/errors-1) otherwise.

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

> 🚧 Jobs with an MFA Challenge
>
> When a user is presented with an MFA challenge, the job flow changes, and there is an additional step to consider; 
>
> 1. `verify-credentials`
> 2. `mfa-challenge` : **only appears in MFA challenge flow**
> 3. `retrieve-accounts`
> 4. `retrieve-transactions`
>
> . See below for the expected flow and how to handle this.

The `mfa-challenge` step will go through a number of statuses before reaching sucess/failure: 

**Step 1: MFA challenge pending**: When job first starts, the `mfa-challenge` state will be set to `pending` with null result.

```json STEP 1: MFA challenge pending
HTTP/1.1 200 OK
Content-Type: application/json

{
  "type": "job",
  "id": "61723",
  "created": "2021-06-08T09:10:32.000Z",
  "updated": "2021-06-08T09:14:28.000Z",
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
      "title": "mfa-challenge",
      "status": "pending",
      "result": null
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
    "self": "/jobs/61723",
    "source": "/users/ea3a81/connections/8fce3b"
  }
}
```

**Step 2: MFA challenge request**: When a job reaches the `mfa-challenge` step, the status will progress to `in-progress` and the result object with instructions on how to handle MFA will be present.

```json STEP 2: MFA challenge: OTP
{
  "title": "mfa-challenge",
  "status": "in-progress",
 	"result": {
      "type": "mfa",
      "method": "token",
      "description": "A SMS code has been sent to your device, please enter valid number",
      "input": [
        "OTP Password"
      ],
      "expiryMs": 120000,
      "links": {
        "response": "/jobs/61723/mfa"
      }
    }
}
```
```json STEP 2: MFA challenge: Question/s
{
  "title": "mfa-challenge",
  "status": "in-progress",
  "result": {
    "type": "mfa",
    "method": "security-questions",
    "description": "security-questions",
    "input": [
      "What's your favourite company?",
      "What's the ID of this institution?"
    ],
    "expiryMs": 120000,
    "links": {
      "response": "https://au-api.basiq.io/jobs/61723/mfa"
    }
  }
}
```

**The client application should render visually the input for the MFA challenge** so that the end-user can supply a value - details on how to render this can be obtained from the result object. Once a value has been captured it should be posted to the URL supplied in the results attribute i.e. `/jobs/{job.id}/mfa`. See [MFA response](https://api.basiq.io/v2.1/reference/create-mfa-challenge-response). 

**Step 2: MFA skipped (*alternate* flow)**: In the event that an MFA challenge was not encountered, `mfa-challenge` will be present, with a status of skipped. No action is required, the flow will continue to retrieve accounts/transactions for that user. 

```json STEP 2: MFA skipped (alternate flow)
{
  "title": "mfa-challenege",
  "status": "skipped",
  "result": null
}
```

**Step 3: MFA challenge in progress**: Once an MFA challenge response has been supplied, the `mfa-challenge` state will remain in the in-progress state. This state implies that the connector is carrying out its work, and no further action by the application client is required. The client application should continue to monitor the status of the job to handle future state changes.

```json STEP 3: MFA challenge in progress
{
   "title": "mfa-challenge",
   "status": "in-progress",
   "result": null
},
```

**Step 4: MFA failed (*alternate* flow - no retry)**

```json STEP 4: MFA failed (alternate flow - no retry)
{
   "title": "mfa-challenge",
   "status": "failed",
   "result": null
},
```

**Step 5: MFA challenge succeeded**: The MFA challenge has successfully completed so the job has progressed to next step to retrieve accounts and complete the job.

```json STEP 5: MFA challenge succeeded
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
      "title": "mfa-challenge",
      "status": "success",
      "result": null
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
