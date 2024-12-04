---
title: Jobs
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
Some of the services provided by Basiq are quite resource intensive, and may take a little time to process. To ensure that we provide a pleasant experience to you and your end-users, and that we avoid timeouts of long running connections to our server - we will handle these processes (jobs) asynchronously.

Asynchronous operations are great as they enable us to return an immediate result when an endpoint is queried, and also enable us to scale the requests optimally behind the scenes.

When an asynchronous operation is initiated (e.g. refreshing a connection) the Basiq server will create a job resource and return a status code of 202 - Accepted along with the job details (in the body). You can then query the job url to track its progress.

**Tracking the status of a job**

Every step of the job has a status property that depicts its current state. The possible status values for each step are as follows:

* `pending` - The job has been created and is waiting to be started.
* `in-progress` - The job has started and is currently processing.
* `success` - The job has successfully completed.
* `failed` - The job has failed.

**Find out what steps have been completed**

Depending on the job being executed, some jobs will have multiple steps which need to be executed, for e.g. refreshing a connection requires the following steps to be completed:

1. Establish successful authentication with institution
2. Fetch latest list of accounts
3. Fetch latest list of transactions

You can keep track of the steps that have been completed by observing the results array property. As each step is successfully completed, its status will be updated and a result object with the link to the affected resource will be present. In the event that a step has failed, the result object will contain an embedded `error` object.

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
        `type`
      </td>

      <td style={{ textAlign: "left" }}>
        Value is "job".
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
        `id`
      </td>

      <td style={{ textAlign: "left" }}>
        A string that uniquely identifies the job.
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
        `created`
      </td>

      <td style={{ textAlign: "left" }}>
        The date time when the job was created.
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
        `updated`
      </td>

      <td style={{ textAlign: "left" }}>
        The date time when the job was last updated.
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
        `steps`
      </td>

      <td style={{ textAlign: "left" }}>
        List of steps that need to be completed. With the following properties:
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
        * `title` - Name of the step the job needs to complete.

        * `status` - Step status: `pending`, `in-progress`, `success`, `failed`.

        * `result` - Object containing updated (or created) resources. Otherwise if a step `failed` contains an [error](https://api.basiq.io/docs/errors-1) response
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
        `links`
      </td>

      <td style={{ textAlign: "left" }}>
        Links to the following resources:
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
        * `self` - URL of job resource

        * `source` - Resource that initiated creation of this Job. For example, for operations on [Connection](https://api.basiq.io/reference/connections), this is a Connection URL.  This is only returned for Connection jobs and not for Statement jobs.
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

![708](https://files.readme.io/e8ecae5-job.png "job.png")

```json Example Job Object
{
  "type": "job",
  "id": "61723",
  "created": "2016-06-08T09:10:32.000Z",
  "updated": "2016-06-08T09:14:28.000Z",
  "steps": [
    {
      "title": "verify-credentials",
      "status": "success",
      "result": 
        {
          "type": "link",
          "url": "/users/ea3a81/connections/8fce3b"
        }
    },
    {
      "title": "retrieve-accounts",
      "status": "success",
      "result": 
        {
          "type": "link",
          "url": "/users/ea3a81/accounts?filter=institution.id.eq('AU00000')"
        }
    },
    {
      "title": "retrieve-transactions",
      "status": "in-progress",
      "result": null
    }
  ],
  "links": {
    "self": "/jobs/61723",
    "source": "/users/ea3a81/connections/8fce3b"
  }
}
```
