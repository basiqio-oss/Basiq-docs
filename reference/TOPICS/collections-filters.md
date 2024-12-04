---
title: Collections & Filters
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
## Collections

Collection resources provide access to information about a list of objects of the same type. For example, you can use a collection resource to access information about a list of users. Collection resources are paged and may be sorted and filtered (depending on availability) - and will always return an object of type list.

## Filters
Some collections support the ability to filter the results. Filtering a collection resource is conducted via the `filter` query parameter using the following notation:

**`?filter=[property].[condition]([value])`** 
[block:callout]
{
  "type": "info",
  "body": "All filter values should be URL encoded: `?filter=URLEncode(*)`"
}
[/block]
**Accessing Properties**

Properties are accessed using the following notation `object.property`.

**Supported Conditions** 
[block:parameters]
{
  "data": {
    "0-0": "eq",
    "1-0": "bt",
    "2-0": "gt",
    "3-0": "gteq",
    "4-0": "lt",
    "5-0": "lteq",
    "0-1": "Equals \n`?filter=account.id.eq('s55bf3')`",
    "1-1": "Between two values - used for date range filtering. \n`?filter=transaction.postDate.bt('2017-09-28','2018-01-30'). Values are inclusive.`",
    "2-1": "Greater than \n`?filter=transaction.postDate.gt('2018-01-28')`",
    "3-1": "Greater than or equal to \n`?filter=transaction.postDate.gteq('2018-01-28')`",
    "4-1": "Less than \n`?filter=transaction.postDate.lt('2018-01-28')`",
    "5-1": "Less than or equal to \n`?filter=transaction.postDate.lteq('2018-01-28')`",
    "6-0": "ne",
    "6-1": "Not equals (only currently for [Institutions](https://api.basiq.io/v2.1/reference/institutions) endpoint)\n`?filter=institution.institutionType.ne('Test Bank')`"
  },
  "cols": 2,
  "rows": 7
}
[/block]
Where available, you can apply multiple filters to a collection by separating them with a comma.

`?filter=transaction.postDate.bt('2018-01-28','2018-02-27'),account.id.eq('aef3g')`

Multiple filters are treated as an **and (&)** operation example:
[block:callout]
{
  "type": "warning",
  "body": "Note the examples above have not url encoded the filters. You will need to ensure that the filter values are url encoded before calling the resource."
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "GET /users/ea3a81/transactions?filter=transaction.postDate.bt('2018-01-01','2018-02-26') HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
      "language": "json",
      "name": "Example Request"
    }
  ],
  "sidebar": true
}
[/block]