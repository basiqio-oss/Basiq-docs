---
title: Filters
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
Some collections support the ability to filter the results. Filtering a collection resource is conducted via the `filter` query parameter using the following notation:

**`?filter=[property].[condition]([value])`** 

> 📘 All filter values should be URL encoded: `?filter=URLEncode(*)`

**Accessing Properties**

Properties are accessed using the following notation `object.property`.

**Supported Conditions** 

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>

      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        eq
      </td>

      <td style={{ textAlign: "left" }}>
        Equals\
        `?filter=account.id.eq("s55bf3")`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        bt
      </td>

      <td style={{ textAlign: "left" }}>
        Between two values - used for date range filtering.\
        `?filter=transaction.postDate.bt('2017-09-28','2018-01-30'). Values are inclusive.`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        gt
      </td>

      <td style={{ textAlign: "left" }}>
        Greater than\
        `?filter=transaction.postDate.gt('2018-01-28')`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        gteq
      </td>

      <td style={{ textAlign: "left" }}>
        Greater than or equal to\
        `?filter=transaction.postDate.gteq('2018-01-28')`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        lt
      </td>

      <td style={{ textAlign: "left" }}>
        Less than\
        `?filter=transaction.postDate.lt('2018-01-28')`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        lteq
      </td>

      <td style={{ textAlign: "left" }}>
        Less than or equal to\
        `?filter=transaction.postDate.lteq('2018-01-28')`
      </td>
    </tr>
  </tbody>
</Table>

Where available, you can apply multiple filters to a collection by separating them with a comma.

`?filter=transaction.postDate.bt('2018-01-28','2018-02-27'),account.id.eq('aef3g')`

Multiple filters are treated as an **and (&)** operation example:

> 🚧 Note the examples above have not url encoded the filters. You will need to ensure that the filter values are url encoded before calling the resource.

```json Example Request
GET /users/ea3a81/transactions?filter=transaction.postDate.bt('2018-01-01','2018-02-26') HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```
