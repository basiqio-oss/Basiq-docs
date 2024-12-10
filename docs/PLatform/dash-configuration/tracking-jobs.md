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
# Job History

<br />

The **Job History** section logs activities performed on a connection, helping developers monitor the outcomes of operations like refreshing or purging data. Each job is uniquely identified and displays its status, date, and outcome.


* **Job ID**: A unique identifier for each job.
  * **Status**: Indicates success, failure, or ongoing progress.
    * **Date**: The time the job was executed.
      <br />
      This feature allows developers to track and debug connection-related operations efficiently.
      <br />

## Job Overview

<br />

<Columns layout="auto">
  <Column>
    ### Key Features

    * **Trackable:** Each job is uniquely identifiable by a `job_id`.
    * **Status Indicator:** Quickly identify the outcome of operations (e.g., **Success**, **Failed**).
    * **Historical Logs:** Easily review past actions on a connection for debugging or auditing.
  </Column>

  <Column>
    ### Benefits

    * Ensure reliability by tracking failed operations.
    * Gain insights into task execution times.
    * Use programmatic access for advanced monitoring and integrations.
  </Column>
</Columns>

***

## Examples from Job History

<br />

<Tabs>
  <Tab title="Successful Job">
    <Cards columns={2}>
      <Card title="Job ID" icon="fa-tag">
        `10105886-f806-43c5-9a56-7b672ad24c1d`
      </Card>

      <Card title="Date" icon="fa-calendar">
        10 Dec 2024, 04:33
      </Card>

      <Card title="Status" icon="fa-check-circle">
        **Success**
      </Card>
    </Cards>

    > **Description:**\
    > This job successfully refreshed the connection data from the financial institution. All data is synchronized and available for use.
  </Tab>

  <Tab title="Failed Job">
    <Cards columns={2}>
      <Card title="Job ID" icon="fa-tag">
        `6c869859-8635-4fad-b809-2fe9ef7a0ee7`
      </Card>

      <Card title="Date" icon="fa-calendar">
        10 Dec 2024, 00:46
      </Card>

      <Card title="Status" icon="fa-times-circle">
        **Failed**
      </Card>
    </Cards>

    > **Description:**\
    > This job failed due to an issue during the connection refresh.\
    > **Recommended Actions:**

    1. Check if the user's credentials are still valid.
    2. Verify the network or API endpoint availability.
    3. Use the `job_id` to fetch logs for more details.
  </Tab>
</Tabs>

***

## Quick Reference to Job Statuses

<br />

<Cards columns={3}>
  <Card title="Pending" icon="fa-clock">
    The job is still processing. Wait for the operation to complete.
  </Card>

  <Card title="Success" icon="fa-check-circle">
    The job completed successfully. Data has been updated.
  </Card>

  <Card title="Failed" icon="fa-times-circle">
    The job failed. Review the logs for troubleshooting steps.
  </Card>
</Cards>

***

## Programmatic Access

<br />

Use the Basiq API to retrieve and manage job history programmatically. This is especially useful for building custom monitoring tools or integrating job tracking into your workflows.

