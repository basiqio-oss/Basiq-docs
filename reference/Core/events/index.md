---
title: Events
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
Events mark changes or behaviour in entities and can be used to trigger actions in your application.

## Entities and their events

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        entity
      </th>

      <th style={{ textAlign: "left" }}>
        eventType
      </th>

      <th style={{ textAlign: "left" }}>
        when does this occur
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `connection`
      </td>

      <td style={{ textAlign: "left" }}>
        `created`
      </td>

      <td style={{ textAlign: "left" }}>
        When a connection is created.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        `updated`
      </td>

      <td style={{ textAlign: "left" }}>
        When a connection is updated.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        `deleted`
      </td>

      <td style={{ textAlign: "left" }}>
        When a connection is deleted.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `consent`
      </td>

      <td style={{ textAlign: "left" }}>
        `created`
      </td>

      <td style={{ textAlign: "left" }}>
        A user has agreed to an applications consent policy which in turn creates a consent policy against the user.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        `reminder`
      </td>

      <td style={{ textAlign: "left" }}>
        It's time for a consent reminder.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        `updated`
      </td>

      <td style={{ textAlign: "left" }}>
        A user has agreed to an updated consent policy.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        `revoked`
      </td>

      <td style={{ textAlign: "left" }}>
        A user has decided to withdraw consent to share data with an application.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        `warning`
      </td>

      <td style={{ textAlign: "left" }}>
        It's time for a consent warning.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `Payout`
      </td>

      <td style={{ textAlign: "left" }}>
        `created`
      </td>

      <td style={{ textAlign: "left" }}>
        When a payout is created.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        `failed`
      </td>

      <td style={{ textAlign: "left" }}>
        When a payout is failed.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        `in-progress`
      </td>

      <td style={{ textAlign: "left" }}>
        When a payout is in-progress.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        `successful`
      </td>

      <td style={{ textAlign: "left" }}>
        When a payout is successful.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `Payrequest`
      </td>

      <td style={{ textAlign: "left" }}>
        `created`
      </td>

      <td style={{ textAlign: "left" }}>
        When a payrequest is created.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        `failed`
      </td>

      <td style={{ textAlign: "left" }}>
        When a payrequest is failed.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        `in-progress`
      </td>

      <td style={{ textAlign: "left" }}>
        When a payrequest is in-progress.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        `successful`
      </td>

      <td style={{ textAlign: "left" }}>
        When a payrequest is successful.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `user`
      </td>

      <td style={{ textAlign: "left" }}>
        `created`
      </td>

      <td style={{ textAlign: "left" }}>
        A user has been created.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        `updated`
      </td>

      <td style={{ textAlign: "left" }}>
        A user has been updated.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        `deleted`
      </td>

      <td style={{ textAlign: "left" }}>
        A user has been deleted.
      </td>
    </tr>
  </tbody>
</Table>

> 📘 Consent events
>
> Any events around consent must be monitored if your application is using Open Banking data. For more information please read our documentation on [data governance events](ref:data-governance#data-governance-events).
