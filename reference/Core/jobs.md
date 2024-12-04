---
title: Jobs
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Due to differences in banking portals there can sometimes be inconsistencies with durations when creating or refreshing connections. For this reason we run this process asynchronously, and break it into three steps. This allows partners to perform other tasks while waiting for the tasks to be complete.
 
&nbsp;
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e8ecae5-job.png",
        "job.png",
        708,
        731,
        "#9faea0"
      ],
      "sizing": "80"
    }
  ],
  "sidebar": true
}
[/block]

When an asynchronous operation is initiated (e.g. refreshing a connection) the Basiq server will create a job resource and return a status code of 202 - Accepted **along with the job details (in the body)**. You can then query the job url to track its progress.

**Tracking the status of a job**

Every step of the job has a status property that depicts its current state. The possible status values for each step are as follows:

- `pending` - The job has been created and is waiting to be started.
- `in-progress` - The job has started and is currently processing.
- `success` - The job has successfully completed.
- `failed` - The job has failed.

**Find out what steps have been completed**

Depending on the job being executed, some jobs will have multiple steps which need to be executed, for e.g. refreshing a connection requires the following steps to be completed:

  1.  Establish successful authentication with institution
  2. Fetch latest list of accounts
  3. Fetch latest list of transactions

You can keep track of the steps that have been completed by observing the results array property. As each step is successfully completed, its status will be updated and a result object with the link to the affected resource will be present. In the event that a step has failed, the result object will contain an embedded `error` object.