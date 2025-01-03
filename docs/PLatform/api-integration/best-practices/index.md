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

<Tabs>
  <Tab title="Authentication Best Practices">
    <div className="doc-section">
      <h2>Authentication</h2>

      <p className="doc-highlight">
        🔑 The token you receive will expire after one hour (3600 seconds).
        <strong>Cache this token for global use</strong>: avoid re-authenticating separately for each user or connection, as this will cause scaling issues in your application.
      </p>
    </div>
  </Tab>

  <Tab title="Configuring Your Application">
    <div className="doc-section">
      <h2>Configuring Your Application</h2>

      <p className="doc-highlight">
        📜 <strong>Consider your consent policy carefully:</strong> Any changes to your consent policy (e.g., adding new data scopes) will only apply to new user consents. Existing users will either be restricted to the original policy or need to re-consent.
      </p>

      <p>
        🎯 <strong>Be specific and show value:</strong> Clearly outline <em>why</em> you are requesting user consent. The <strong>purpose</strong> defined in your consent policy will be displayed to users, so ensure it communicates the value your application provides.
      </p>
    </div>
  </Tab>

  <Tab title="Refreshing Connections">
    <div className="doc-section">
      <h2>Refreshing Connections</h2>

      <ul className="doc-list">
        <li>
          ⚠️ <strong>Minimize ad hoc refreshes:</strong> Excessive requests can overload bank websites, causing account lockouts or action from the bank.
        </li>

        <li>
          🕒 <strong>Use job steps to monitor progress:</strong> Creating a new connection with the same credentials while one is already in progress will pause the new connection for 6 minutes to prevent account lockout issues.
        </li>

        <li>
          🚫 <strong>Avoid bulk refreshes:</strong> Large-scale refreshes (e.g., via cron jobs) can overload bank websites. Instead, rely on the smart cache or confirm a connection has not recently been refreshed before initiating a new request.
        </li>

        <li>
          🔍 <strong>Check the last refresh time:</strong> Use the `connection.lastUsed` attribute or the user’s jobs to determine the last refresh time and result. Ensure the connection is active before refreshing, as refreshing inactive connections will fail.
        </li>
      </ul>
    </div>
  </Tab>
</Tabs>

<style jsx>
  {`
    .doc-section {
      padding: 20px;
      background: #f9f9f9;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      margin: 10px 0;
    }

    .doc-highlight {
      font-size: 1.1em;
      color: #333;
      background: #eef7fe;
      padding: 10px;
      border-radius: 6px;
      margin-bottom: 16px;
    }

    .doc-list {
      list-style: none;
      padding-left: 0;
      margin: 0;
    }

    .doc-list li {
      font-size: 1em;
      color: #555;
      padding: 8px 0;
      border-bottom: 1px solid #eee;
    }

    .doc-list li:last-child {
      border-bottom: none;
    }

    .doc-list strong {
      color: #0073e6;
    }
  `}
</style>

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