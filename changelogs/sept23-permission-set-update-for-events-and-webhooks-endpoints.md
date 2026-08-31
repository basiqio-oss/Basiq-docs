---
title: Sept'23 - Permission Set Update for Events and Webhooks Endpoints
author: Ashman Malik
hidden: false
published_at: '2023-09-19T03:53:25.063Z'
type: improved
---
# Improvements :tada:

We have enhanced the Permission Sets to support Events and Webhooks Endpoints. Several new endpoints have been added to the list of permissions to provide more comprehensive control and access to these features.

## **Action Required:**

If you are a partner with custom permission sets, you can update them via our [BASIQ dashboard](https://dashboard.basiq.io/settings/permissionSets). It is essential to update them to include the following endpoints to ensure uninterrupted access to Webhooks and Events features:

## **Webhooks Endpoints:**

* **POST /notifications/webhooks** - Create a new webhook.
* **GET /notifications/webhooks** - Retrieve a list of webhooks.
* **POST /notifications/webhooks/\{id}** - Update an existing webhook.
* **GET /notifications/webhooks/\{id}** - Retrieve details of a specific webhook.
* **DELETE /notifications/webhooks/\{id}** - Delete a webhook.
* **GET /notifications/webhooks/\{id}/messages** - Retrieve messages for a specific webhook.
* **GET /notifications/webhooks/\{id}/messages/\{id}** - Retrieve a specific message for a webhook.
* **POST /notifications/messages/test** - Send a test message.

## **Events Endpoints:**

* **GET /events** - Retrieve a list of events.
* **GET /events/types** - Retrieve event types.
* **GET /events/types/\{id}** - Retrieve details of a specific event type.

By updating your custom permission sets to include these endpoints, you can take full advantage of our enhanced Events and Webhooks functionality. 

If you have any questions or require further assistance, please don't hesitate to reach out to our support team.