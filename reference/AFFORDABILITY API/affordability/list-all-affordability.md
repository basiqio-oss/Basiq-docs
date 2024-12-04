---
title: List all affordability summaries
excerpt: List all affordability snapshots generated for this user
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
Use this collection to retrieve a list of [Affordability](https://api.basiq.io/reference/affordability) resources generated.  The list provides a short form on the affordability resource responses with a link to the full response.  The collection is ordered by generated date in descending order.

**Returns**

Returns a list with a data property that contains an array of affordability resources. Each entry in the array is a separate object. If no data is returned, the resulting array will be empty. Otherwise, this call returns an error in the event of a failure.

```json Definition
GET /users/{user.id}/affordability
```

```json Example Request
GET users/ea3a81/affordability HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.1 200 OK
Content-Type: application/json
{
    "type": "list",
    "data": [
        {
            "type": "affordability",
            "id": "b35f967b",
            "fromMonth": "2019-10",
            "toMonth": "2020-10",
            "coverageDays": 393,
            "generatedDate": "2021-02-17T09:12:25",
            "institutions": [
                "AU00000"
            ],
            "links": {
                "self": "https://au-api.basiq.io/users/e9a95456/affordability/b35f967b",
                "income": "https://au-api.basiq.io/users/e9a95456/income/b35f967b",
                "expenses": "au-api.basiq.io/users/e9a95456/expenses/b35f967b"
            }
        }
    ],
    "links": {
        "self": "https://au-api.basiq.io/users/e9a95456/affordability"
    }
}
```
