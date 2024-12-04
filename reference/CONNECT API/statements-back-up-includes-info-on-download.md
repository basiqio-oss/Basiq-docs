---
title: Statements - back up - includes info on download
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
The statement object represents an official bank statement for an account or accounts held with a financial institution (e.g. a savings account). You can use this object to **retrieve** official bank statements downloaded from a financial institution for which you have created a connection.  Alternatively, you can **create** a statement object by uploading official pdf bank statements which are parsed to extract and expose the user's latest account and transaction data. 

> 📘 Download Bank Statements from Created Connection
>
> When a new Connection request is made, the server will [create a job](https://basiq.readme.io/v2.0/reference#jobs) that will process an additional step to download the most recent bank statement for each account held by the user.

> 📘 Upload Official Bank Statements by Creating a Statement resource
>
> When a new Statement request is made, the server will [create a job](https://basiq.readme.io/v2.0/reference#jobs) that will processes 3 steps verify the file, retrieve accounts and transactions

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
        Value is "statement".
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
        A string that uniquely identifies the statement.
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
        **links**
      </td>

      <td style={{ textAlign: "left" }}>
        A links object containing the following members for this statement:
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
        * `self` link to the this **single** bank statement
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
        * **[accounts](https://basiq.readme.io/v2.0/reference#accounts)**  All accounts or a single user account extracted from this statement.
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
        **links**
      </td>

      <td style={{ textAlign: "left" }}>
        A links object containing the following members:
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
        * `self` link to the list of **all** statements for this user
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

```json Example Statements Object
{
    "type": "list",
    "data": [
        {
            "type": "statement",
            "id": "1a73e",
            "links": {
                "self": "/users/ea3a81/statements/1a73e",
                "account": "/users/ea3a81/accounts/e40f6"
            }
        }
    ],
    "links": {
        "self": "/users/ea3a81/statements"
    }
}
```
