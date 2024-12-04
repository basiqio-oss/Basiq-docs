---
title: Basiq best practices
excerpt: Best practices, tips & tricks to follow when you're building your app.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: >-
    We've summarised they key areas of focus into a "Go live" checklist, to
    ensure you've got everything covered before hitting production.
  pages:
    - type: basic
      slug: go-live-checklist-1
      title: Go live checklist
---
When integrating with the Basiq API, there are some best practices that play a crucial role in any applications success. These practices cover areas such as security considerations, UX, scalability etc. and have been tried and tested to ensure that you have all the necessary tools and guidelines for success.

## **When authenticating:**

The token you receive will expire after one hour (3600 seconds). You should cache this token for global use: do not re-authenticate separately for each user or connection, etc., as this will cause trouble as your app scales.

## **When connecting financial institutions:**

You should always use a `CLIENT_ACCESS` scope token for this request, regardless of whether you're using the UI Control or your own bank picker. The `CLIENT_ACCESS` scope restricts access and does not grant access to your users' data.

### *If you’re using the Basiq Simple UI Component for connections*

* If you are using the BasiqConnect UI Component, it will make the request on your behalf so the scope is handled for you.

* As you are not making the connection request, you won't get the response with the job details, and instead you will need to listen for the jobCreated event which will pass you the jobId. When you have this jobId you will be able poll the job endpoint to check the progress of syncing the user's data. See how to handle jobs. 

### *If you’re building your own bank picker*

* If you are building your own UI, under no circumstance should you store your customers credentials anywhere in your application. Instead post them directly to the Basiq API.  

* As you are making the connection request directly, you will get an asynchronous job resource in the response: you should poll this job to check the progress of syncing the user's data. See how to handle jobs.

## **When refreshing a Connection:**

**Keep these ad hoc refreshes to a minimum:** these requests put extra load on the banks' websites and if used excessively are liable to trigger action from the bank: your user may be locked out of their account, or the bank may even try to block Basiq.

**Use job steps to follow the progress of a connection:** if you attempt to create a new connection with the same credentials when a connection is already in progress then the new connection will automatically be paused for 6 minutes in order to avoid account lock-out issues, due to credentials already being in use.

**Avoid bulk refreshes, e.g., cron jobs:** if you refresh thousands of connections at the same time, this will put load on the banks' websites which may cause problems. Let the smart cache handle this for you, and use the Refresh Connection request only after confirming that Basiq has not recently refreshed.

**Before refreshing, check when the connection was last refreshed:** check the user's jobs for a complete view of when the connection was last refreshed and the result, or for a more lightweight option check the connection.lastUsed attribute to see when the connection was last refreshed.

### *Use the smart cache instead*

**For ongoing daily refreshed data,** ask the Basiq team to enable your application for background refreshes (the "smart cache" feature). This is a much more efficient way to refresh data than initiating a Refresh Connection request yourself each day. 

### *Check the users jobs regularly.*

A common cadence is once a day and then every time they login, giving you the opportunity to handle any unresolved errors that have occurred. See our resources on how to effectively handle jobs. 

For example, the user may have initially connected their banks without issues, but Basiq has since had trouble refreshing their data. The user may have changed their login credentials, or the bank may be presenting a popup requiring the user to acknowledge new T\&Cs, etc.

## **Handling jobs**

### *Handling jobs correctly is essential to your applications UX*

Providing your users with a simple, intuitive and informed experience is key to good UX, and handling jobs correctly is a key to achieving this. 

 To help keep you and your users informed we provide both the job status and error messages. These are for you and our support team to troubleshoot issues and pass directly onto the user (i.e. in cases of invalid credentials).

To do this, you can poll the `/job` endpoint, checking on the status of each step until the job has either

* successfully completed the relevant step/s;
* failed at any of the steps.

If you are building your own UI, you should keep your user engaged until the first (`verify-credentials`) step is complete: it's not a good experience to let the user go and then have to drag them back if the credentials didn't work.

As soon as the credentials step is complete you should release the user to continue with your onboarding journey while Basiq fetches their accounts and transactions: there is no sense in keeping them hanging around watching a spinning wheel.

There is more to read on our job processes and how to handle it, including why and where jobs may fail and how to test your applications handling of these scenarios [here](https://api.basiq.io/docs/handling-jobs). 

# Error resolution

## Using the `/institutions` endpoint

You can use the institutions endpoint to fetch the current status and stage of each institution we offer. This is especially useful if you encounter any issues when connecting/refreshing connections because you can then dynamically determine if there are any issues currently, and proceed accordingly. E.g. if a connection fails, and you can see using the `/institutions` endpoint that bank is currently down, you now know the issue is on their end and to try connect when they are operational again. This can all be done without having to log any issues with Basiq's support team, meaning the whole process can be automated. 

## *Error logging*

When logging any errors you encounter in production, it is important that you include the `userId`, `connectionId`, and `jobId`. Having a record of these when you reach out to our support team means that we are able to better investigate and help you debug.
