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

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Event
      </th>

      <th style={{ textAlign: "left" }}>
        Cause
      </th>

      <th style={{ textAlign: "left" }}>
        Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `consent.revoked`
      </td>

      <td style={{ textAlign: "left" }}>
        When 

        **the user**

         

        explicitly revokes the consent.
      </td>

      <td style={{ textAlign: "left" }}>
        Delete/de-identify data received for that user by both Basiq and the partner.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `consent.expired`
      </td>

      <td style={{ textAlign: "left" }}>
        The time period specified for this users consent has lapsed.
      </td>

      <td style={{ textAlign: "left" }}>
        Delete/de-identify data received for that user by both Basiq and the partner.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `consent.updated`
      </td>

      <td style={{ textAlign: "left" }}>
        **The user**

         has made a change to their consent.
      </td>

      <td style={{ textAlign: "left" }}>
        *For first release this will be handled as a revoke/new consent flow*
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `consent.warning`
      </td>

      <td style={{ textAlign: "left" }}>
        When a consent is close to its expiration date (7 days before expiry).
      </td>

      <td style={{ textAlign: "left" }}>
        Notify the user about the upcoming expiration date.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `consent.created`
      </td>

      <td style={{ textAlign: "left" }}>
        When a consent object has been created for a specific 

        **user**

        .
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `consent.archived`
      </td>

      <td style={{ textAlign: "left" }}>
        When 

        **the partner**

         archives the consent.
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>
