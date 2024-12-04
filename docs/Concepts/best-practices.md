---
title: Consent Management
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
When integrating with the Basiq API, there are some best practices that play a crucial role in any applications success. These practices cover areas such as security considerations, UX, scalability etc. and have been tried and tested to ensure that you have all the necessary tools and guidelines for success.

## **When authenticating:**

The token you receive will expire after one hour (3600 seconds). You should cache this token for global use: do not re-authenticate separately for each user or connection, etc., as this will cause trouble as your app scales.

## **When configuring your application**

**Ensure you have carefully considered your consent policy:** any changes to your consent policy, such as additional data scope, will only be applied to new user consents. Users under the previous consent policy will either be restricted to the original policy, or need to re-consent. 

**Be specific and demonstrate value in your applications purpose:** it is crucial to outline *why* you are requesting your users consent. The **purpose** you define in your consent policy will be displayed to users before they give consent so it is important they understand the value your application will provide to them.

## **When refreshing a Connection:**

**Keep these ad hoc refreshes to a minimum:** these requests put extra load on the banks' websites and if used excessively are liable to trigger action from the bank: your user may be locked out of their account, or the bank may even try to block Basiq.

**Use job steps to follow the progress of a connection:** if you attempt to create a new connection with the same credentials when a connection is already in progress then the new connection will automatically be paused for 6 minutes in order to avoid account lock-out issues, due to credentials already being in use.

**Avoid bulk refreshes, e.g., cron jobs:** if you refresh thousands of connections at the same time, this will put load on the banks' websites which may cause problems. Let the smart cache handle this for you, and use the Refresh Connection request only after confirming that Basiq has not recently refreshed.

**Before refreshing, check when the connection was last refreshed:** check the user's jobs for a complete view of when the connection was last refreshed and the result, or for a more lightweight option check the connection.lastUsed attribute to see when the connection was last refreshed.

### *Use the smart cache instead*

**For ongoing daily refreshed data,** ask the Basiq team to enable your application for background refreshes (the "smart cache" feature). This is a much more efficient way to refresh data than initiating a Refresh Connection request yourself each day. 

## **Handling jobs: for ongoing access to data**

### *Handling jobs correctly is essential to your applications UX*

Providing your users with a simple, intuitive and informed experience is key to good UX, and handling jobs correctly is a key to achieving this. 

To help keep you and your users informed we provide both the job status and error messages. These are for you and our support team to troubleshoot issues and pass directly onto the user (i.e. new login credentials).

To do this, you can use the `/job` endpoint, checking on the status of recent jobs to see if there were any failures.

### *Check the users jobs regularly. *

A common cadence is once a day and then every time they login, giving you the opportunity to handle any unresolved errors that have occurred. See our resources on how to effectively handle jobs. 

For example, the user may have initially connected their banks without issues, but Basiq has since had trouble refreshing their data. The user may have changed their login credentials, or the bank may be presenting a popup requiring the user to acknowledge new T&Cs, etc.

There is more to read on our job processes and how to handle it, including why and where jobs may fail and how to test your applications handling of these scenarios [here](#handling-failed-jobs). 

# Error resolution

## Using the `/institutions` endpoint 
You can use the institutions endpoint to fetch the current status and stage of each institution we offer. This is especially useful if you encounter any issues when refreshing connections because you can then dynamically determine if there are any issues currently, and proceed accordingly. E.g. if a refresh fails, and you can see using the `/institutions` endpoint that bank is currently down, you now know the issue is on their end and to try connect when they are operational again. This can all be done without having to log any issues with Basiq's support team, meaning the whole process can be automated. 

## *Error logging*

When logging any errors you encounter in production, it is important that you include the `userId`, `connectionId`, and `jobId`. Having a record of these when you reach out to our support team means that we are able to better investigate and help you debug.