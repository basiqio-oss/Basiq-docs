---
title: Codes
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
<Columns layout="auto">
<Column>
<strong>Error Code</strong>

too-many-sandbox-connections

invalid-credentials

internal-server-error

parameter-not-supplied

resource-not-found

</Column>

<Column>
<strong>Description</strong>

Limit reached for sandbox connections. Reach out to support@basiq.io to reset your account.

Cannot login to target institution using supplied credentials. Check credentials and try again.

Generic server error affecting all endpoints.

Required parameter not supplied. Check details and source message.

Requested resource not found. Check details message.

</Column>

<Column>
<strong>Additional Details</strong>

- Sandbox connections limit exceeded.

- Subtypes: invalid-username-or-password, locked-account, multi-factor-authentication.

- Server-side issue.

- Missing required parameters like 'email' or 'mobile'.

- Resource could not be located; verify request data.

</Column>
</Columns>