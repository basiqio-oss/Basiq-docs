---
title: Data governance
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
# Overview
Within the Basiq platform we have introduced new concepts regarding the management of user data. These include: 

Consent **Policy** - A set of rules defined by the partner that outline how the partner will engage with the consumer. Specifically these cover things such as duration of the consent, the data they wish to collect, the intended businesses purposes and more. The policy is used to render the consent screens (UI) that are presented to the consumer.

User **Consent** - The final accepted set-of terms that the user agreed to. The consent is constructed by presenting the policy to the user, and capturing users preferences. The final product of this process is the consent itself. The consent dictates when the user's consent expires, and what the user has approved (or not). The consent defines all the data handling rules in relation to the specific user.

Providing partners with the ability to configure their policy, and users with the ability to configure their preferences ensures that Basiq provides an environment where both parties can engage in a mutual way. It is therefore equally important that the rules concerning the handling and management of the user's consent is respected accordingly. This process is called “**data governance**”.

The scope of the data governance that the Basiq platform handles is inclusive of the data located within the Basiq platform and data that resides within the Partners environment. This means, that the scope of the data governance that Basiq provides is both internal and external. 

This is important to note, as data by nature is likely to leave the Basiq platform e.g. the partner may have their own database which will store and persist the users data for purposes of rendering, analytics and supply to other systems. By providing a data governance management solution that is inclusive of local and external storage (of CDR data), and a consent management framework - Basiq ensures that the partner is fully compliant with their regulatory requirements and that the consumers privacy is respected.
 
When a user accepts the consent requirements of an application, a snapshot of that consent is stored alongside their user record. This will then define their individual preferences around the data management, and will dictate the governance imposed on the data persisted by Basiq. 

Basiq will monitor for triggered actions in these consent policies. Partners will need to provide a web hook to receive and act on these events. This can be done using the [dashboard](https://api.basiq.io/v3.0/docs/dash-configuration).

## Data governance events

The consent [events](https://api.basiq.io/reference/events-1) act as the primary trigger to initiate services that are responsible for ensuring compliance to the consent that has been granted. These events can be triggered by multiple parties e.g. (partner) application archives all consents, user revokes / updates a granted consent or the system expiring the event as its data has lapsed.
[block:parameters]
{
  "data": {
    "h-0": "Event",
    "h-1": "Cause",
    "0-0": "`consent.revoked`",
    "0-1": "When **the user **explicitly revokes the consent.",
    "1-0": "`consent.expired`",
    "1-1": "The time period specified for this users consent has lapsed.",
    "2-0": "`consent.updated`",
    "2-1": "**The user** has made a change to their consent.",
    "0-2": "Delete/de-identify data received for that user by both Basiq and the partner.",
    "1-2": "Delete/de-identify data received for that user by both Basiq and the partner.",
    "2-2": "*For first release this will be handled as a revoke/new consent flow* ",
    "h-2": "Action",
    "3-0": "`consent.created`",
    "4-0": "`consent.archived`",
    "3-1": "When a consent object has been created for a specific **user**.",
    "4-1": "When **the partner** archives the consent."
  },
  "cols": 3,
  "rows": 5
}
[/block]
The process of raising and managing events is handled by the Basiq Platform. This includes:

### Notification Services

Notifications services are critical to ensuring that all the parties (Basiq and Partners) adhere to and respect the users consent. To assist parties in adhering to the granted consent - Basiq will provide a series of notification services that will inform partners when there is a change of state within the consent object. These changes, will be delivered in the form of events (see consent events above) and will be delivered to partners via the event web-hook provided in the Application configuration.

### Data Management

One of the primary requirements concerning the management of consent is the handling and management of data. Users have the ability to define for how long data can be accessed, retained and what happens to the data once the consent is no longer valid. To ensure that these rules are implemented according to the consent requirements, the Basiq platform supports the following capability:

 * Auto expiry of consent. Each consent that is granted has a defined expiry period, which once reached requires us to archive / destroy / anonymise data. 

 * Data Anonymisation. This is the process of de-identifying and anonymising the collected data so that it cannot be identified as belonging to the user.

 * Deleting Data. This is the process of deleting data that has been collected from the financial institutions (external sources).

[block:callout]
{
  "type": "info",
  "body": "The above events may trigger actions in multiple places. E.g. By Basiq and partner application."
}
[/block]