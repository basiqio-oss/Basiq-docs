---
title: Consent Events
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
## Consent Events

The consent events act as the primary trigger to initiate services that are responsible for ensuring compliance to the consent that has been granted. These events can be triggered by multiple parties e.g. (partner) application archives all consents, user revokes / updates a granted consent or the system expiring the event as its data has lapsed.

| Event              | Cause                                                                  | Action                                                                        |
| :----------------- | :--------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| `consent.revoked`  | When **the user **explicitly revokes the consent.                      | Delete/de-identify data received for that user by both Basiq and the partner. |
| `consent.expired`  | The time period specified for this users consent has lapsed.           | Delete/de-identify data received for that user by both Basiq and the partner. |
| `consent.updated`  | **The user** has made a change to their consent.                       | _For first release this will be handled as a revoke/new consent flow_         |
| `consent.warning`  | When a consent is close to its expiration date (7 days before expiry). | Notify the user about the upcoming expiration date.                           |
| `consent.created`  | When a consent object has been created for a specific **user**.        |                                                                               |
| `consent.archived` | When **the partner** archives the consent.                             |                                                                               |