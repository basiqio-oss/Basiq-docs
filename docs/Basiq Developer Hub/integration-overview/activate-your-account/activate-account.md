---
title: Activate Account
deprecated: false
hidden: true
metadata:
  robots: index
---
\{const userId = "userId"}

\<Accordion title="When authenticating" icon="fa-info-circle">
&#x20; The token you receive will expire after one hour (3600 seconds). You should cache this token for global use: \*\*do not\*\* re-authenticate separately for each user or connection, as this will cause trouble as your app scales.
\</Accordion>

\<Accordion title="When configuring your application" icon="fa-cogs">
&#x20; \<ul>
&#x20;   \<li>
&#x20;     \<strong>Ensure you have carefully considered your consent policy:\</strong> Changes to your consent policy, such as additional data scope, will only be applied to new user consents.
&#x20;   \</li>

&#x20;   \<li>
&#x20;     \<strong>Be specific and demonstrate value in your application's purpose:\</strong> Clearly outline \*why\* you are requesting users' consent. The purpose defined in your consent policy will be displayed to users before they give consent.
&#x20;   \</li>
&#x20; \</ul>
\</Accordion>

\<Cards columns=\{2}>
&#x20; \<Card title="Refreshing a Connection" icon="fa-refresh">
&#x20;   \<ul>
&#x20;     \<li>\<strong>Keep ad hoc refreshes to a minimum:\</strong> Excessive refresh requests can put extra load on the banks' websites and cause issues like user lockouts.\</li>
&#x20;     \<li>\<strong>Use job steps to follow the progress of a connection:\</strong> When a connection is in progress, new requests will automatically be paused to avoid account lock-outs.\</li>
&#x20;   \</ul>
&#x20; \</Card>

&#x20; \<Card title="Handling Jobs" icon="fa-tasks">
&#x20;   \<ul>
&#x20;     \<li>\<strong>Check the user's jobs regularly:\</strong> Regular checks, such as once a day and after each login, will help you handle unresolved errors promptly.\</li>
&#x20;     \<li>\<strong>Use the /job endpoint:\</strong> The \`/job\` endpoint can be used to check the status of recent jobs and troubleshoot issues like login credentials errors or new T\\\&Cs popups.\</li>
&#x20;   \</ul>
&#x20; \</Card>
\</Cards>

\<Columns layout="auto">
&#x20; \<Column>
&#x20;   \<h3>Purging Connection Data\</h3>
&#x20;   \<p>In addition to using the API, you can purge connection data directly from the Dashboard, making it easier for users to manage their connections without API calls.\</p>
&#x20; \</Column>

&#x20; \<Column>
&#x20;   \<h3>API Endpoint Reference\</h3>

&#x20;   \<pre>
&#x20;     POST /users/\{userId}/connections/\{connectionId}/purge
&#x20;   \</pre>

&#x20;   \<p>For more details, please refer to the \[API documentation]\(https\://api.basiq.io/reference/purgeconnectiondata).\</p>
&#x20; \</Column>

&#x20; \<Column>
&#x20;   \<h3>Error Resolution\</h3>
&#x20;   \<p>You can use the \`/connectors\` endpoint to fetch the status and stage of each connector we offer. This helps you identify if any issues are caused by connector downtime and allows you to proceed accordingly.\</p>
&#x20; \</Column>
\</Columns>

\<Tabs>
&#x20; \<Tab title="Error Logging">
&#x20;   When logging errors in production, it's important to include the \`userId\`, \`connectionId\`, and \`jobId\`. This will help our support team investigate and assist you with debugging.
&#x20; \</Tab>

&#x20; \<Tab title="Data Storage Best Practices">
&#x20;   Partners should have a secure data storage system for necessary information. API calls should be made only when required to obtain updated information. Note that Basiq is not an information storage service.
&#x20; \</Tab>
\</Tabs>