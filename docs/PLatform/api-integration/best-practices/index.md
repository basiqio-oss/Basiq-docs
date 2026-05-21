---
title: Basiq best practices
excerpt: >-
  Best practices for building secure, reliable, and scalable integrations with
  the Basiq API.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Use these best practices to build a secure, reliable, and scalable integration with the Basiq API.

These recommendations cover authentication, consent, connection refreshes, job handling, data purging, troubleshooting, and secure data storage.

## Core integration practices

<Tabs>
  <Tab title="Authentication">

The access token expires after one hour, or 3600 seconds.

Cache the token for global use instead of re-authenticating for each user or connection. Re-authenticating too often can create scaling issues in your application.

  </Tab>

  <Tab title="Consent policy">

Plan your consent policy before users connect their accounts. Changes to your consent policy, such as adding new data scopes, only apply to new user consents.

Existing users are either restricted to the original policy or need to re-consent.

Clearly explain why you are requesting user consent. The `purpose` defined in your consent policy is displayed to users, so it should describe the value your application provides.

  </Tab>

  <Tab title="Connection refreshes">

Minimize ad hoc refreshes. Excessive refresh requests can overload bank websites, cause account lockouts, or trigger action from the bank.

Follow these practices when refreshing connections:

- Use job steps to monitor progress.
- Avoid creating a new connection with the same credentials while another connection is already in progress. The new connection is paused for 6 minutes to prevent account lockout issues.
- Avoid bulk refreshes, such as cron jobs that refresh every connection at once.
- Use Smart Cache where possible, or confirm that a connection has not been refreshed recently before starting a new request.
- Check the `connection.lastUsed` attribute or the user's jobs to determine the last refresh time and result.
- Confirm that the connection is active before refreshing it. Refreshing inactive connections fails.

  </Tab>
</Tabs>

## Use Smart Cache for ongoing data access

For ongoing daily refreshed data, request the Basiq team to enable Smart Cache. Smart Cache refreshes data in the background and is more efficient than initiating daily Refresh Connection requests.

<Callout icon="circle-info" theme="info">
OpenBanking connections are limited to 20 refreshes per day.
</Callout>

## Handle jobs correctly

Handling jobs correctly improves user experience and helps you troubleshoot connection issues.

Use the `/job` endpoint to monitor recent job statuses and address failures promptly. Check jobs regularly, including during user login, so users can resolve issues while they are already in your application.

Common issues include:

- The user needs to update their credentials.
- The bank requires the user to acknowledge new terms or popup messages.

For more details, see [handling jobs effectively](doc:handling-jobs).

## Purge connection data

You can purge connection data with the [Purge Connection Data API](https://api.basiq.io/reference/purgeconnectiondata) or from the Dashboard.

To purge connection data from the Dashboard:

1. Open the user's profile.
2. Locate the user's connections list.
3. Find the connection using its unique Connection ID.
4. Click **Purge** next to the relevant connection.
5. Confirm the action to remove the associated data.

The Connection ID remains intact, which allows future refreshes.

<Callout icon="triangle-exclamation" theme="warning">
Purging is irreversible. The Dashboard feature follows the same permissions and security protocols as the API endpoint.
</Callout>

## Troubleshoot connection issues

<Columns layout="auto">
  <Column>

### Check connector status

Use the connectors endpoint to fetch the current status and stage of all connectors. This helps you identify and resolve connection issues dynamically.

  </Column>

  <Column>

### Log useful identifiers

Log key details such as `userId`, `connectionId`, and `jobId`. These identifiers help support teams investigate issues and provide better assistance.

  </Column>

  <Column>

### Store data securely

Implement secure data storage for required user information. Encrypt stored data and restrict access to authorized users only.

  </Column>
</Columns>

<Callout icon="life-ring" theme="info">
If you have issues, contact the Basiq support team.
</Callout>