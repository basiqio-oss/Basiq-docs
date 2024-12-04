---
title: Upgrading to v2.1
excerpt: Things to consider when making the the move
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
When upgrading to v2.1 of the Basiq API, the following new features and their implementation need to be taken into consideration. 

# Support for MFA

- **MFA support means that there is a new job flow** that needs to be managed slightly differently. You’ll be able to tell if you are met with an MFA challenge by checking the number of steps in the job process (an MFA challenge  job process has 4 steps. We recommend you check this and manage the flow accordingly. Read the implementation details  and what the new flow looks like [here](https://api.basiq.io/reference/retrieve-a-job).
- **MFA jobs are not automatically refreshed**, because the user needs to be present to provide the additional authentication parameters. In this case, to get updated data you will need to handle this on your end and prompt a customer when they log in or open your application so they can then post the MFA challenge themselves.
- **MFA support for Bendigo Bank** involves a new job flow that must be managed slightly differently from the standard process. To determine if you are encountering an MFA challenge, you can check the number of steps in the job process. An MFA challenge job process typically consists of four steps. We recommend that you verify this and adjust your flow accordingly. For Bendigo Bank, if you do not utilise our user interface (UI). In such cases, you should return "confirmed" (as a string) as an MFA response to indicate that your end user has opened an app. We rely on this response when establishing a connection with Bendigo Bank. The MFA response for Bendigo Bank is as follows:

```json POST Create MFA Response Bendigo
POST /jobs/61723/mfa HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json

{
  "mfa-response": ["confirmed"]
}
```

MFA Challenge: 

```json Example job response for MFA challenge
{
  "type": "job",
  "id": "61723",
  "created": "2021-06-08T09:10:32.000Z",
  "updated": "2021-06-08T09:14:28.000Z",
  "steps": [
    {
      "title": "verify-credentials",
      "status": "success",
      "result": [...]
    },
    {
      "title": "mfa-challenge",
      "status": "in-progress",
      "result": [
        {
          "type": "mfa",
          "method": "token",
          "description": "A SMS code has been sent to your device, please enter valid number",
          "input": [
            "OTP Password"
          ],
          "expiryMs": 3600,
          "links": {
            "response": "/jobs/61723/mfa"
          }
        }
      ]
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

# Connection retry mechanism

- Previously, **when using v2.0** of the API, if you made a `POST` or `UPDATE` request to the connections endpoint (in order to set up an initial connection to an institution or to update the login credentials on an existing one) and the associated institution was unavailable, the API would return a response that this job has failed, and from there it is up to your application to initiate a retry.
- **With v2.1** of the API comes a new retry mechanism to handle these failed jobs. A failed `POST` or `UPDATE` request to the connections endpoint (due to failure in either the financial institution or the Basiq Connector), will result in a that request being placed in a paused jobs queue for up to 7 days. 
- After the request is queued, an attempt will be initiated every 2 hours. If the institution has subsequently come available (operational, under-maintenance or degraded-performance condition) at the moment of the retry, the job will be executed. If the institution is still unavailable, attempting to execute the job will be delayed for another 2 hours.

```json New job response with connection retry
"steps": [
       {
           "title": "verify-credentials",
           "status": "pending",
           "result": {
               "code": "temporary-unavailable-queued",
               "title": "Institution temporary unavailable, retry pending",
               "detail": "3rd party service temporary unavailable. Job queued, retry in 2 hours."
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
```

## Updates to the application flow

This scenario used to be a terminal state. The user would be asked to try again or come back later. Now the user experience can be improved as the Retry is in the Basiq platform.

Reattempting to execute queued jobs is done automatically on Basiq side and any additional automated refresh attempts from the partner side can only slow down overall execution time. This is also true for automated refresh of all existing connections, especially in a short time frame.

### New application flow after a failed `POST` or `UPDATE` to the `/connections` endpoint

- Inform the user of the outage of the institution connection and that them their details will have arrived once their institution connection is back up 

- You can continue to monitor the status of the queued request using the jobId, the response will remain the same until the status changes to either `success` or `failed`.

- A job reaches `failed` status when it has expired (after 7 days or over 84 retries)

```json Example expired failed job
{
  "title": "verify-credentials",
  "status": "failed",
  "result": {
      "code": "temporary-unavailable",
      "title": "Institution temporary unavailable",
      "detail": "3rd party service temporary unavailable. Please try again later."
}
```