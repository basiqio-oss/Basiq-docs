---
title: Connections
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
Connections are a core feature that securely link your users’ financial institutions to your app, allowing for real-time data synchronization. This guide will walk you through managing connections using the dashboard and API, while offering best practices for developers.

## What is a Connection?

<Accordion title="What is a Connection?" icon="fa-info-circle">
  A **Connection** is created whenever a user links their financial institution with your app. It acts as a secure conduit to fetch and store account holder data (e.g., accounts, transactions, and enrich insights). Connections are tied to the **User Object**.

  > 📘 **Pro Tip:**
  >
  > Interact with accounts and transactions through the **User Object**, not the connection itself, to ensure data integrity.
</Accordion>

***

## Connection States

<Cards columns={4}>
  <Card title="Pre-init" icon="fa-hourglass">
    The connection is initialized but not yet active.
  </Card>

  <Card title="Active" icon="fa-check-circle">
    The connection is successfully established and operational.
  </Card>

  <Card title="Invalid" icon="fa-exclamation-triangle">
    The connection is no longer valid and may require user re-authentication.
  </Card>

  <Card title="Failed" icon="fa-times-circle">
    An error occurred during the connection process.
  </Card>
</Cards>

View connection states in the **Connections** section of the dashboard.

***

<Columns layout="auto">
  <Column>
    ## Actions on a Connection

    Developers can manage connections using the following actions:

    <Accordion title="Refresh Connection" icon="fa-sync">
      Use this action to fetch the latest data from the financial institution without creating a new connection. A `job resource` is triggered asynchronously to update account and transaction data.

      **Steps:**

      * Select the connection.
      * Click **Refresh** to sync data.
      * Track the progress in the **Job History** section.

      > 📘 **Pro Tip:**
      >
      > Regularly refresh connections to keep your data up-to-date.
    </Accordion>

    <Accordion title="Purge Connection" icon="fa-trash-alt">
      Removes **all user data** related to a specific financial institution.

      **When to use:**

      * Before refreshing enriched data to ensure insights are accurate.
      * To securely delete sensitive user data.

      > info
      > Always **purge and refresh connections** to ensure enriched insights reflect the latest data.
    </Accordion>

    <Accordion title="Revoke/Delete Connection" icon="fa-ban">
      Permanently unlinks the financial institution. This action:

      * Does not delete stored account or transaction data.
      * Is irreversible.

      **When to use:** When a user decides to disconnect their institution or when the connection is no longer needed.
    </Accordion>
  </Column>

  <Column>
    ## Connection Profile Overview

    When selecting a connection, the **Connection Profile** displays the following details:

    <Cards columns={1}>
      <Card title="Full Name" icon="fa-user">
        The name of the account holder.
      </Card>

      <Card title="Phone Numbers" icon="fa-phone">
        Partially masked contact numbers.
      </Card>

      <Card title="Email Addresses" icon="fa-envelope">
        User's email addresses.
      </Card>

      <Card title="Physical Addresses" icon="fa-map-marker">
        Associated address details.
      </Card>
    </Cards>

    Actions available in the connection profile:

    * **Refresh Connection**

    * **Purge Connection**

    * **Revoke Connection**

    > 📘 Note:
    >
    > Data fetched from financial institutions includes PII (Personally Identifiable Information), which is partially masked in the dashboard for security.
  </Column>
</Columns>

***

## Example Workflows

<Tabs>
  <Tab title="Refresh Only">
    Refreshing a connection keeps your app in sync with the latest account and transaction data.

    **Steps:**

    1. Select the connection.
    2. Click **Refresh** to fetch the latest data.
    3. Monitor progress in the **Job History** section.
  </Tab>

  <Tab title="Purge and Refresh">
    Always purge and refresh the connection to ensure accurate Enrich insights.

    **Steps:**

    1. Select the connection.
    2. Click **Purge** to remove outdated data.
    3. Click **Refresh** to fetch new data.
    4. Monitor progress in the **Job History** section.
  </Tab>

  <Tab title="Revoke Connection">
    Revoke a connection to permanently disconnect a financial institution.

    **Steps:**

    1. Select the connection.
    2. Click **Revoke** to unlink the institution.
    3. Note: Data will remain unless purged beforehand.
  </Tab>
</Tabs>

***

## API Endpoints for Managing Connections

<Accordion title="Purge Connection" icon="fa-trash-alt">
  Use this endpoint to remove all data related to a specific user connection. Purging is **only applicable** for active connections and is essential for ensuring enriched insights reflect the latest data.

  **Endpoint:**
  POST /connections/:connection\_id/purge

  **Description:**

  * Deletes all user data associated with the connection.
  * Must be done before refreshing connections to update Enrich results.

    > 📘 **Note:**
    >
    > After purging, make sure to refresh the connection to keep your data current.
</Accordion>