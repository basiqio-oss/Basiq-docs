---
title: Events
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Events mark changes or behaviour in entities and can be used to trigger actions in your application.

## Entities and their events

| Entity       | Event Type             | Description                                                                                                                                                                                                                                                       | Webhook Available |
| ------------ | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| Connection   | connection.created     | When a connection is created                                                                                                                                                                                                                                      | ✅                 |
| Connection   | connection.updated     | When a connection is updated                                                                                                                                                                                                                                      | ❌                 |
| Connection   | connection.deleted     | When a connection is deleted                                                                                                                                                                                                                                      | ✅                 |
| Connection   | connection.invalidated | When a connection status changes from active to invalid due to user-related errors. The specific user-related errors that should trigger this event for web and OB connections are as follows:                                                                    | ✅                 |
|              |                        | **Web Connections:** user-action-required, invalid-username-or-password, invalid-connection, locked-account, multifactor-required                                                                                                                                 |                   |
|              |                        | **OB Connections:** expired CDR arrangement - user didn’t re-authorize, any issue occurred during user re-authorization                                                                                                                                           |                   |
| Connection   | connection.activated   | when a connection is activated                                                                                                                                                                                                                                    | ✅                 |
| Account      | account.updated        | When an account is updated or a change is made to existing account attributes                                                                                                                                                                                     | ✅                 |
| Transactions | transactions.updated   | When a new transaction is added for a user through various scenarios: creating a new connection (web, Open Banking, or CSV/PDF) whether or not previous transactions exist, updating an existing connection, or refreshing a connection manually, via a scheduler | ✅                 |
| Consent      | consent.created        | When a consent is created                                                                                                                                                                                                                                         | ✅                 |
| Consent      | consent.expired        | When a consent is expired                                                                                                                                                                                                                                         | ✅                 |
| Consent      | consent.reminder       | When a consent has been active for 90 days since the last update                                                                                                                                                                                                  | ✅                 |
| Consent      | consent.revoked        | When a consent is revoked                                                                                                                                                                                                                                         | ✅                 |
| Consent      | consent.updated        | When a consent is updated                                                                                                                                                                                                                                         | ✅                 |
| Consent      | consent.warning        | When a consent is about to expire                                                                                                                                                                                                                                 | ✅                 |
| User         | user.created           | When a user is created                                                                                                                                                                                                                                            | ✅                 |
| User         | user.deleted           | When a user is deleted                                                                                                                                                                                                                                            | ✅                 |
| User         | user.updated           | When a user is updated                                                                                                                                                                                                                                            | ✅                 |

> 📘 Consent events
> 
> Any events around consent must be monitored if your application is using Open Banking data. For more information please read our documentation on [data governance events](https://api.basiq.io/docs/data-governance).