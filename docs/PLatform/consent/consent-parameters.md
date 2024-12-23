---
title: Consent Parameters
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
## State Parameter

### Overview

The state parameter is a versatile tool provided by Basiq to enhance the flexibility and user experience of the frontend flow. When launching the Basiq Consent UI, partners can pass a unique state value which will be returned to the partner's application when the user is redirected back after completing their interaction with the Consent UI. This allows the partner to maintain state across the user's journey and manage navigation or context upon return.

### URL Structure

```python URL
https://consent.basiq.io/home?token=${token}&action=${action}&state={yourState}
```

### Parameter: `state`

**Usage**: This parameter can be used to encode the user's return point or any other contextual data needed after the consent flow. Ensure the state is URL encoded if it contains special characters or spaces.

***

## Institution Parameters

### Overview

When partners know in advance which financial institution the user intends to connect with, they can streamline the process by specifying an `institutionId`. This bypasses the need for users to select their institution from a list, making the process quicker and more user-friendly.

### URL Structure

```python URL
https://consent.basiq.io/home?token=${token}&action=${action}&state={yourState}&institutionId={institutionId}
```

### Parameter: `institutionId`

**Usage**: Useful for predefined user journeys where the institution is already known. This parameter can be used in various consent flows such as creating consent, connecting institutions, or updating consent.

***

## ConnectionId Parameter

### Overview

The `connectionId` parameter is important for managing existing banking connections, particularly for reauthorisation and updating credentials in Web connections and Open Banking connections.

### URL Structure

```python URL
https://consent.basiq.io/home?token=${token}&connectionId=${connectionId}
```

### Parameter: `connectionId`

#### For Web Connections

**Existing Behavior:** It is used primarily for initiating a credential update flow through the Consent UI.

**Usage:** When a partner passes a `connectionId` using web source, the Consent UI triggers a workflow to update credentials.

#### For Open Banking Connections

**New Behavior:** The `connectionId` parameter now also supports OB connections.

**Reauthorisation Support:** For OB connections, if a partner includes a `connectionId` in the URL, it'll kick-start the reauthorisation process. This includes handling via API calls or by using the `action=reauthorise`

**Account Selection:** This parameter is particularly useful when a user is already connected with the Data Holder and wants to re-elect the account(s) that are sharing data.

***

## JobIds Parameter

### Overview

The jobIds parameter allows tracking multiple connection attempts within the same user session, especially useful when the 'Allow multiple connections' feature is enabled.

### Example Redirect URL

```python URL
http://www.your-redirect-url.com/?jobIds=123,456,789
```

### Parameter: `jobIds`

**Usage**: Retrieve all job IDs from connection attempts to monitor progress and manage multiple connections more effectively.

***

<Tabs>
  <Tab title="State Parameter">
    <Accordion title="Overview" icon="fa-info-circle">
      The `state` parameter is a versatile tool provided by Basiq to enhance the flexibility and user experience of the frontend flow. When launching the Basiq Consent UI, partners can pass a unique state value which will be returned to the partner's application when the user is redirected back after completing their interaction with the Consent UI. This allows the partner to maintain state across the user's journey and manage navigation or context upon return.
    </Accordion>

    <Accordion title="URL Structure" icon="fa-link">
      ```javascript
      https://consent.basiq.io/home?token=${token}&action=${action}&state={yourState}
      ```
    </Accordion>

    <Accordion title="Parameter: state" icon="fa-flag">
      <ul>
        <li><strong>Usage</strong>: This parameter can be used to encode the user's return point or any other contextual data needed after the consent flow. Ensure the state is URL encoded if it contains special characters or spaces.</li>
      </ul>
    </Accordion>
  </Tab>

  <Tab title="Institution Parameters">
    <Accordion title="Overview" icon="fa-info-circle">
      When partners know in advance which financial institution the user intends to connect with, they can streamline the process by specifying an `institutionId`. This bypasses the need for users to select their institution from a list, making the process quicker and more user-friendly.
    </Accordion>

    <Accordion title="URL Structure" icon="fa-link">
      ```javascript
      https://consent.basiq.io/home?token=${token}&action=${action}&state={yourState}&institutionId={institutionId}
      ```
    </Accordion>

    <Accordion title="Parameter: institutionId" icon="fa-bank">
      <ul>
        <li><strong>Usage</strong>: Useful for predefined user journeys where the institution is already known. This parameter can be used in various consent flows such as creating consent, connecting institutions, or updating consent.</li>
      </ul>
    </Accordion>
  </Tab>

  <Tab title="ConnectionId Parameter">
    <Accordion title="Overview" icon="fa-info-circle">
      The `connectionId` parameter is important for managing existing banking connections, particularly for reauthorisation and updating credentials in Web connections and Open Banking connections.
    </Accordion>

    <Cards columns={2}>
      <Card title="URL Structure" icon="fa-link">
        ```javascript
        https://consent.basiq.io/home?token=${token}&connectionId=${connectionId}
        ```
      </Card>

      <Card title="Parameter Details" icon="fa-cogs">
        <Columns layout="auto">
          <Column>
            <strong>Web Connections:</strong> Used primarily for initiating a credential update flow through the Consent UI.
          </Column>

          <Column>
            <strong>Open Banking Connections:</strong> Supports reauthorisation via `connectionId` and can include `action=reauthorise`.
          </Column>
        </Columns>
      </Card>
    </Cards>
  </Tab>

  <Tab title="JobIds Parameter">
    <Accordion title="Overview" icon="fa-info-circle">
      The `jobIds` parameter allows tracking multiple connection attempts within the same user session, especially useful when the 'Allow multiple connections' feature is enabled.
    </Accordion>

    <Accordion title="Example Redirect URL" icon="fa-link">
      ```javascript
      http://www.your-redirect-url.com/?jobIds=123,456,789
      ```
    </Accordion>

    <Accordion title="Parameter: jobIds" icon="fa-tasks">
      <ul>
        <li><strong>Usage</strong>: Retrieve all job IDs from connection attempts to monitor progress and manage multiple connections more effectively.</li>
      </ul>
    </Accordion>
  </Tab>
</Tabs>