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

<Table>
  <thead>
    <tr>
      <th>
        Entity
      </th>

      <th>
        Event Type
      </th>

      <th>
        Description
      </th>

      <th>
        Webhook Available
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Connection
      </td>

      <td>
        connection.created
      </td>

      <td>
        When a connection is created
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        Connection
      </td>

      <td>
        connection.updated
      </td>

      <td>
        When a connection is updated
      </td>

      <td>
        ❌
      </td>
    </tr>

    <tr>
      <td>
        Connection
      </td>

      <td>
        connection.deleted
      </td>

      <td>
        When a connection is deleted
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        Connection
      </td>

      <td>
        connection.invalidated
      </td>

      <td>
        When a connection status changes from active to invalid due to user-related errors. The specific user-related errors that should trigger this event for web and OB connections are as follows:
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>
        **Web Connections:**

         user-action-required, invalid-username-or-password, invalid-connection, locked-account, multifactor-required
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>
        **OB Connections:**

         expired CDR arrangement - user didn’t re-authorize, any issue occurred during user re-authorization
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        Connection
      </td>

      <td>
        connection.activated
      </td>

      <td>
        when a connection is activated
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        Account
      </td>

      <td>
        account.updated
      </td>

      <td>
        When an account is updated or a change is made to existing account attributes
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        Transactions
      </td>

      <td>
        transactions.updated
      </td>

      <td>
        When a new transaction is added for a user through various scenarios: creating a new connection (web, Open Banking, or CSV/PDF) whether or not previous transactions exist, updating an existing connection, or refreshing a connection manually, via a scheduler
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        Consent
      </td>

      <td>
        consent.created
      </td>

      <td>
        When a consent is created
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        Consent
      </td>

      <td>
        consent.expired
      </td>

      <td>
        When a consent is expired
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        Consent
      </td>

      <td>
        consent.reminder
      </td>

      <td>
        When a consent has been active for 90 days since the last update
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        Consent
      </td>

      <td>
        consent.revoked
      </td>

      <td>
        When a consent is revoked
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        Consent
      </td>

      <td>
        consent.updated
      </td>

      <td>
        When a consent is updated
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        Consent
      </td>

      <td>
        consent.warning
      </td>

      <td>
        When a consent is about to expire
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        User
      </td>

      <td>
        user.created
      </td>

      <td>
        When a user is created
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        User
      </td>

      <td>
        user.deleted
      </td>

      <td>
        When a user is deleted
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        User
      </td>

      <td>
        user.updated
      </td>

      <td>
        When a user is updated
      </td>

      <td>
        ✅
      </td>
    </tr>
  </tbody>
</Table>

> 📘 Consent events
>
> Any events around consent must be monitored if your application is using Open Banking data. For more information please read our documentation on [data governance events](https://api.basiq.io/docs/data-governance).
