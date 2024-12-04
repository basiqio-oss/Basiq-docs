---
title: Create a statement
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
A user can choose to share their financial data by uploading official pdf bank statements instead of creating a bank connection. Once the statement object is successfully created you can use it to obtain the user's latest financial data extracted from the bank statement i.e. accounts and transactions. 

> 👍 The endpoint also accepts csv files conforming to our file specification.  Contact us directly for more details.

Create a new statement by uploading an official pdf bank statement or csv file statement. When a new statement request is made, the server will [create a job](https://api.basiq.io/v2.1/reference/jobs) that will process the following steps:

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
        The server will verify the file, validate the statement layout and attempt to parse the target statement
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

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

You can [check the status of each step](https://api.basiq.io/v2.1/reference/jobs) by querying the job resource (returned when the statement is created).

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
        **statement**
        *file, required*
      </td>

      <td style={{ textAlign: "left" }}>
        Official PDF bank statement for the specified [institution](ref:retrieve-an-institution) to be uploaded.  Csv files conforming to our file specification are also accepted.
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
        **institutionId**\
        *string, required*
      </td>

      <td style={{ textAlign: "left" }}>
        The identifier of the [institution](ref:retrieve-an-institution) to which the statement relates e.g. "AU01001".  Note that sandbox institutions (i.e. AU00000 **do not** support the file upload option.
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

> 🚧 Note that the time it takes to complete the processes above will vary depending on the volume of data along with the complexity of the bank statement. As a rough guide this entire process could take anywhere between 10 - 30 secs. Upload multiple statements in parallel to provide the best user experience

**Returns**

Returns a created job resource, if the operation succeeded. Returns an [error](https://api.basiq.io/docs/errors-1) if the post failed (e.g. not supplying required properties).

```json Definition
POST /users/{user.id}/statements
```

```json Example Request
POST /users/ea3a81/statements HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: multipart/form-data; boundary=----xxxxxxxx

Content-Disposition: form-data; name="statement"; filename="/Users/DSmith/bankstatement_filename.pdf"

Content-Disposition: form-data; name="institutionId"
AU04301

Content-Disposition: form-data; name="Accept"

multipart/form-data
------xxxxxxxx--
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
