---
title: Create a connection
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
Use this to create a new connection. When a new connection request is made the server will [create a job](https://basiq.readme.io/v1.0/reference#jobs) that will process the following steps:

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

You can [check the status of each step](https://basiq.readme.io/v1.0/reference#retrieve-a-job) by querying the job resource (returned when the connection is created).

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
        **loginId**
        *string, required*
      </td>

      <td style={{ textAlign: "left" }}>
        The users institution login ID
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **password**\
        *string, required*
      </td>

      <td style={{ textAlign: "left" }}>
        The users institution password
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **securityCode**\
        *string, conditional*
      </td>

      <td style={{ textAlign: "left" }}>
        User's institution security code. Mandatory if required by institution's login process
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **secondaryLoginId**\
        *string, conditional*
      </td>

      <td style={{ textAlign: "left" }}>
        User's institution secondary login id. Mandatory if required by institution's login process
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **[institution](https://basiq.readme.io/v1.0/reference#institutions)**\
        *object, required*
      </td>

      <td style={{ textAlign: "left" }}>
        Only the id of the institution is required
      </td>
    </tr>
  </tbody>
</Table>

> 🚧 Note that the time it takes to complete the processes above will vary depending on the volume of data along with the general latency between our servers and the financial institution. As a rough guide this entire process could take anywhere between 3 - 30 secs.

**Returns**

Returns a created job resource, if the operation succeeded. Returns an [error](https://basiq.readme.io/v1.0/reference#errors) if the post failed (e.g. not supplying required properties).

```json Definition
POST /users/{user.id}/connections
```

```json Example Request
POST /users/ea3a81/connections HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json

{
  "loginId": "gavinBelson",
  "password": "hooli2016",
  "institution":{
    "id":"AU00000"
  }
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
