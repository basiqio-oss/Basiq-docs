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

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Entity
      </th>

      <th style={{ textAlign: "left" }}>
        Event Type
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>

      <th style={{ textAlign: "left" }}>
        Webhook Available
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Connection
      </td>

      <td style={{ textAlign: "left" }}>
        connection.created
      </td>

      <td style={{ textAlign: "left" }}>
        When a connection is created
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Connection
      </td>

      <td style={{ textAlign: "left" }}>
        connection.updated
      </td>

      <td style={{ textAlign: "left" }}>
        When a connection is updated
      </td>

      <td style={{ textAlign: "left" }}>
        ❌
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Connection
      </td>

      <td style={{ textAlign: "left" }}>
        connection.deleted
      </td>

      <td style={{ textAlign: "left" }}>
        When a connection is deleted
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Connection
      </td>

      <td style={{ textAlign: "left" }}>
        connection.invalidated
      </td>

      <td style={{ textAlign: "left" }}>
        When a connection status changes from active to invalid due to user-related errors. The specific user-related errors that should trigger this event for web and OB connections are as follows:
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        **Web Connections:**

        user-action-required, invalid-username-or-password, invalid-connection, locked-account, multifactor-required
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        **OB Connections:**

        expired CDR arrangement - user didn’t re-authorize, any issue occurred during user re-authorization
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Connection
      </td>

      <td style={{ textAlign: "left" }}>
        connection.activated
      </td>

      <td style={{ textAlign: "left" }}>
        when a connection is activated (only available for Open banking connections)
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Account
      </td>

      <td style={{ textAlign: "left" }}>
        account.updated
      </td>

      <td style={{ textAlign: "left" }}>
        When an account is updated or a change is made to existing account attributes
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Transactions
      </td>

      <td style={{ textAlign: "left" }}>
        transactions.updated
      </td>

      <td style={{ textAlign: "left" }}>
        When a new transaction is added for a user through various scenarios: creating a new connection (web, Open Banking, or CSV/PDF) whether or not previous transactions exist, updating an existing connection, or refreshing a connection manually, via a scheduler
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Consent
      </td>

      <td style={{ textAlign: "left" }}>
        consent.created
      </td>

      <td style={{ textAlign: "left" }}>
        When a consent is created
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Consent
      </td>

      <td style={{ textAlign: "left" }}>
        consent.expired
      </td>

      <td style={{ textAlign: "left" }}>
        When a consent is expired
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Consent
      </td>

      <td style={{ textAlign: "left" }}>
        consent.reminder
      </td>

      <td style={{ textAlign: "left" }}>
        When a consent has been active for 90 days since the last update
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Consent
      </td>

      <td style={{ textAlign: "left" }}>
        consent.revoked
      </td>

      <td style={{ textAlign: "left" }}>
        When a consent is revoked
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Consent
      </td>

      <td style={{ textAlign: "left" }}>
        consent.updated
      </td>

      <td style={{ textAlign: "left" }}>
        When a consent is updated
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Consent
      </td>

      <td style={{ textAlign: "left" }}>
        consent.warning
      </td>

      <td style={{ textAlign: "left" }}>
        When a consent is about to expire
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        User
      </td>

      <td style={{ textAlign: "left" }}>
        user.created
      </td>

      <td style={{ textAlign: "left" }}>
        When a user is created
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        User
      </td>

      <td style={{ textAlign: "left" }}>
        user.deleted
      </td>

      <td style={{ textAlign: "left" }}>
        When a user is deleted
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        User
      </td>

      <td style={{ textAlign: "left" }}>
        user.updated
      </td>

      <td style={{ textAlign: "left" }}>
        When a user is updated
      </td>

      <td style={{ textAlign: "left" }}>
        ✅
      </td>
    </tr>
  </tbody>
</Table>

> 🚧 Note:
>
> The `consent.warning` event is triggered daily when a consent is set to expire in 7 days or less. This event continues to fire each day until the consent either expires or is extended.
>
> ## Consent Events:
>
> Any events around consent must be monitored if your application is using Open Banking data. For more information please read our documentation on [data governance events](https://api.basiq.io/docs/data-governance).
