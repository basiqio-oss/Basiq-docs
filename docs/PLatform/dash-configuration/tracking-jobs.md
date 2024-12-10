---
title: Tracking Jobs
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Job History** section provides a record of all operations performed on a connection, including their outcomes. Each job has a unique `job_id`, a timestamp, and a status (e.g., **Success**, **Failed**). This helps developers monitor the progress of asynchronous tasks such as refreshing or purging data.

<Accordion title="What is a Job?" icon="fa-info-circle">
  A **Job** represents a background task initiated by an action on a connection (e.g., refreshing, purging).

  * Each job logs its ID, status, and the timestamp of the operation.
  * Use the `job_id` to track the task's progress programmatically.
</Accordion>

## Job Details in the Dashboard

<Columns layout="2-1">
  <Column>
    ### Key Fields

    * **Job ID:** Unique identifier for each job.
    * **Date:** The timestamp of when the job was triggered.
    * **Status:** Indicates whether the job was successful, failed, or still processing.
  </Column>

  <Column>
    <Cards columns={2}>
      <Card title="Success" icon="fa-check-circle">
        The operation was completed successfully. No further action is required.
      </Card>

      <Card title="Failed" icon="fa-times-circle">
        The operation encountered an issue. Investigate the logs or retry the action.
      </Card>
    </Cards>
  </Column>
</Columns>

***

## Example Job History from the Dashboard

<Tabs>
  <Tab title="Success Job">
    **Job ID:** `10105886-f806-43c5-9a56-7b672ad24c1d`\
    **Date:** 10 Dec 2024, 04:33\
    **Status:** ✅ Success

    <Accordion title="More Details" icon="fa-info-circle">
      This job successfully refreshed the connection and synchronized the latest data from the financial institution. No further action is needed.
    </Accordion>
  </Tab>

  <Tab title="Failed Job">
    **Job ID:** `6c869859-8635-4fad-b809-2fe9ef7a0ee7`\
    **Date:** 10 Dec 2024, 00:46\
    **Status:** ❌ Failed

    <Accordion title="Troubleshooting Steps" icon="fa-tools">
      1. Check if the user credentials are valid and up to date.
      2. Review the error logs associated with this `job_id` for additional details.
      3. Retry the operation after resolving any issues.
    </Accordion>
  </Tab>
</Tabs>

***

## Managing Job History Programmatically

You can programmatically query job history using the Basiq API. Use the connection's `connection_id` to fetch the associated jobs and track their progress.

\<Accordion title="API Example: Fetch Job History" icon="fa-code">
&#x20; \*\*Endpoint:\*\* \`GET /connections/:connection\_id/jobs\` &#x20;
&#x20; \*\*Response:\*\*
&#x20; \`\`\`json
&#x20; \[
&#x20;   \{
&#x20;     "job\_id": "10105886-f806-43c5-9a56-7b672ad24c1d",
&#x20;     "status": "success",
&#x20;     "date": "2024-12-10T04:33:00Z"
&#x20;   },
&#x20;   \{
&#x20;     "job\_id": "6c869859-8635-4fad-b809-2fe9ef7a0ee7",
&#x20;     "status": "failed",
&#x20;     "date": "2024-12-10T00:46:00Z"
&#x20;   }
&#x20; ]
\</Accordion>