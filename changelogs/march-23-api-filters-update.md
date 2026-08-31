---
title: March '23 - API Filters Improvements
author: Ashman Malik
hidden: false
published_at: '2023-03-22T23:18:51.218Z'
type: improved
---
# March '23 :sunny:

## :star2: What's Coming?

## Slick new API Filters Improvements

 \
We are excited to announce that we are updating all of our API filters. With this update, we will be returning more helpful error messages when invalid filters are used. Previously, our filters were failing silently, which made it difficult for developers to identify and resolve issues.

## What does this mean for you?

With more accurate error messages, you will be able to quickly identify and fix any issues that may arise from using incorrect filters on our Endpoints. This improvement will undoubtedly enhance the development and usage of our API and improve the overall performance and reliability of our platform and your integration.

Stay tuned for the upcoming release of this improvement!

```json
{
    "type": "list",
    "correlationId": "82038bb2-9fb4-9fb4-9fb4-9ca60b3a7555",
    "data": [
        {
            "type": "error",
            "code": "parameter-not-valid",
            "title": "Parameter value is not valid",
            "detail": "The provided filter parameter is in invalid format or unsupported",
            "source": {
                "parameter": "filter"
            }
        }
    ]
}
```