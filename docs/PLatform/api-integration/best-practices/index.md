---
title: Basiq best practices
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
When integrating with the Basiq API, there are some best practices that play a crucial role in any applications success. These practices cover areas such as security considerations, UX, scalability etc. and have been tried and tested to ensure that you have all the necessary tools and guidelines for success.

## **When authenticating:**

The token you receive will expire after one hour (3600 seconds). You should cache this token for global use: do not re-authenticate separately for each user or connection, etc., as this will cause trouble as your app scales.

## **When configuring your application**

**Ensure you have carefully considered your consent policy:** any changes to your consent policy, such as additional data scope, will only be applied to new user consents. Users under the previous consent policy will either be restricted to the original policy, or need to re-consent. 

**Be specific and demonstrate value in your applications purpose:** it is crucial to outline *why* you are requesting your users consent. The **purpose** you define in your consent policy will be displayed to users before they give consent so it is important they understand the value your application will provide to them.

## **When refreshing a Connection:**

**Keep these ad hoc refreshes to a minimum:** These requests put extra load on the banks' websites and if used excessively are liable to trigger action from the bank: your user may be locked out of their account, or the bank may even try to block Basiq.

**Use job steps to follow the progress of a connection:** If you attempt to create a new connection with the same credentials when a connection is already in progress then the new connection will automatically be paused for 6 minutes in order to avoid account lock-out issues, due to credentials already being in use.

**Avoid bulk refreshes, e.g., cron jobs:** If you refresh thousands of connections at the same time, this will put load on the banks' websites which may cause problems. Let the smart cache handle this for you, and use the Refresh Connection request only after confirming that Basiq has not recently refreshed.

**Before refreshing, check when the connection was last refreshed:** Check the user's jobs for a complete view of when the connection was last refreshed and the result, or for a more lightweight option, check the `connection.lastUsed` attribute to see when the connection was last refreshed. It's essential to ensure that the connection is active before attempting a refresh, as refreshing will not work for inactive connections.

### *Use the smart cache instead*

**For ongoing daily refreshed data,** ask the Basiq team to enable your application for background refreshes (the "smart cache" feature). This is a much more efficient way to refresh data than initiating a Refresh Connection request yourself each day. 

**Note:** OpenBanking connections are limited to 20 connection refreshes per day.

## **Handling jobs: for ongoing access to data**

### *Handling jobs correctly is essential to your applications UX*

Providing your users with a simple, intuitive and informed experience is key to good UX, and handling jobs correctly is a key to achieving this. 

To help keep you and your users informed we provide both the job status and error messages. These are for you and our support team to troubleshoot issues and pass directly onto the user (i.e. new login credentials).

To do this, you can use the `/job` endpoint, checking on the status of recent jobs to see if there were any failures.

### *Check the users jobs regularly.*

A common cadence is once a day and then every time they login, giving you the opportunity to handle any unresolved errors that have occurred. See our resources on how to effectively handle jobs. 

For example, the user may have initially connected their banks without issues, but Basiq has since had trouble refreshing their data. The user may have changed their login credentials, or the bank may be presenting a popup requiring the user to acknowledge new T\&Cs, etc.

There is more to read on our job processes and how to handle it, including why and where jobs may fail and how to test your applications handling of these scenarios [here](doc:handling-jobs). 

## Purging Connection Data

In addition to using our [API](https://api.basiq.io/reference/purgeconnectiondata), you can now purge connection data directly from the Dashboard. This is useful for dashboard users who need to manage user connections without the need for direct API calls.

### How to Purge Data from the Dashboard:

**Navigate to the User's Connections:** From the main dashboard, go to the specific user's profile and access their connections list.

**Identify the Connection:** Each connection will have a unique Connection ID. Locate the connection that you wish to purge.

**Initiate the Purge:** Click on the "Purge" button next to the relevant connection. 

**Confirm the Purge:** You will be asked to confirm the purge action. Once confirmed, all user data associated with that particular connection will be removed from our systems. Please note that the connectionID will remain intact. You can refresh the connection using that connectionID to refetch new financial data.

> 🚧 Please note that this action is irreversible and should be performed with caution. The purge functionality via the Dashboard respects the same permissions and security protocols as the API endpoint.

### API Endpoint Reference

For reference, the API endpoint for purging connection data is as follows:

```asp Purge
POST /users/{userId}/connections/{connectionId}/purge
```

This endpoint requires the user's identifier `userId` and the connection's identifier `connectionId`. Please refer to our [API documentation](https://api.basiq.io/reference/purgeconnectiondata) for detailed information on request parameters and expected responses.

# Error resolution

## Using the `/connectors` endpoint

You can use the connectors endpoint to fetch the current status and stage of each connector we offer. This is especially useful if you encounter any issues when refreshing connections because you can then dynamically determine if there are any issues currently, and proceed accordingly. E.g. if a refresh fails, and you can see using the /connectors endpoint that a specific connector is currently down, you now know the issue is on their end and to try connecting again when they are operational. This can all be done without having to log any issues with Basiq's support team, meaning the whole process can be automated.

## *Error logging*

When logging any errors you encounter in production, it is important that you include the `userId`, `connectionId`, and `jobId`. Having a record of these when you reach out to our support team means that we are able to better investigate and help you debug.
