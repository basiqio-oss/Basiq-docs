---
title: API Rate Limiting
excerpt: >-
  Learn about Basiq's API rate limiting policies and guidelines to ensure stable
  platform access and avoid potential errors or account suspension.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Basiq platform access limits and restrictions

The Basiq platform contains access limits and restrictions designed to protect the stability of the platform. Partners who approach or exceed these limits, for example by sending an excessive amount of requests in quick succession, large volumes of requests per day or running many concurrent processes may see error responses from the APIs, including 429 or 403 errors. Note that additional charges may apply if you exceed our limits.

Basiq has a number of generic limits that apply platform wide, based on expected partner behaviour.

Basiq also has explicit and externally published limits applied to specific parts of the platform, designed to protect the stability of the platform:

| Product        | Component                       | Reference                                                                             | Limit                                                                                                                              |
| -------------- | ------------------------------- | ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Authentication | Generate an auth token          | [Generate an auth token](https://api.basiq.io/reference/posttoken)                    | 1,500 requests per 5 minute period. Auth tokens should be reused as much as possible and not recreated for each request.           |
| Enrich         | Enrich                          | [Enrich](https://api.basiq.io/reference/enrich-1)                                     | Sandbox users can run 100 requests per month.                                                                                      |
| Affordability  | Create an affordability summary | [Create an affordability summaries](https://api.basiq.io/reference/postaffordability) | The lesser of the number of users created per day or 1,000 total per day (including affordability, income and expenses summaries). |
| Income         | Create an income summary        | [Create an income summary](https://api.basiq.io/reference/postincome)                 | As Above.                                                                                                                          |
| Expenses       | Create an expense summary       | [Create an expense summary](https://api.basiq.io/reference/postexpenses)              | As Above.                                                                                                                          |
| Reports        | Create a report                 | [Create a report](https://api.basiq.io/reference/post_reports)                        | The lesser of the number of users created per day or 1,000 total per day.                                                          |

These limits should be treated as maximums - do not generate unnecessary load. Generating excessive or unnecessary load may lead to your account being suspended to terminated.

We may reduce limits to prevent abuse, or increase limits to enable high-traffic applications. To request an increased rate limit, please [contact Basiq support](https://basiq.atlassian.net/servicedesk/customer/portal/3/group/8) so we can discuss how we can better serve your use case.
