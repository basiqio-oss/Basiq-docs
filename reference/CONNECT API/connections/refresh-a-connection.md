---
title: Refresh a connection
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
Use this to retrieve the latest financial data. Similar to when a connection is first created, the refresh resource will initiate the following series of steps to retrieve the latest financial data from the target institution:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        \#
      </th>

      <th style={{ textAlign: "left" }}>
        Step
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        1
      </td>

      <td style={{ textAlign: "left" }}>
        verify-credentials
      </td>

      <td style={{ textAlign: "left" }}>
        The server will attempt to authenticate with the target institution using the supplied credentials
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        2
      </td>

      <td style={{ textAlign: "left" }}>
        retrieve-accounts
      </td>

      <td style={{ textAlign: "left" }}>
        The server will retrieve the complete list of accounts and their details e.g. account number, name and balances
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        3
      </td>

      <td style={{ textAlign: "left" }}>
        retrieve-transactions
      </td>

      <td style={{ textAlign: "left" }}>
        The server will fetch the associated transactions for each of the accounts
      </td>
    </tr>
  </tbody>
</Table>

You can [check the status of each step](https://basiq.readme.io/v2.1/reference/retrieve-a-job) by querying the job resource (returned when the connection is created).

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
        The identifier of the connection to be refreshed.
      </td>
    </tr>
  </tbody>
</Table>

**Returns**

Returns a created job resource, if the operation succeeded. Returns an [error](https://api.basiq.io/docs/errors-1) if the post failed.

```json Definition
POST /users/{user.id}/connections/{connection.id}/refresh
```

```json Example Request
POST /users/ea3a81/connections/8fce3b/refresh HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.1 202 Accepted
Content-Type: application/json

{
  "type": "job",
  "id": "61724",
  "links": {
    "self": "https://au-api.basiq.io/jobs/61724"
  }
}
```
