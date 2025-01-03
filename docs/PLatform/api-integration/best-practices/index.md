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

\<Tabs>
&#x20; \<Tab title="Authentication Best Practices">
&#x20;   \<div className="doc-section">
&#x20;     \<h2>Authentication\</h2>

&#x20;     \<p className="doc-highlight">
&#x20;       🔑 The token you receive will expire after one hour (3600 seconds).
&#x20;       \<strong>Cache this token for global use\</strong>: avoid re-authenticating separately for each user or connection, as this will cause scaling issues in your application.
&#x20;     \</p>
&#x20;   \</div>
&#x20; \</Tab>

&#x20; \<Tab title="Configuring Your Application">
&#x20;   \<div className="doc-section">
&#x20;     \<h2>Configuring Your Application\</h2>

&#x20;     \<p className="doc-highlight">
&#x20;       📜 \<strong>Consider your consent policy carefully:\</strong> Any changes to your consent policy (e.g., adding new data scopes) will only apply to new user consents. Existing users will either be restricted to the original policy or need to re-consent.
&#x20;     \</p>

&#x20;     \<p>
&#x20;       🎯 \<strong>Be specific and show value:\</strong> Clearly outline \<em>why\</em> you are requesting user consent. The \<strong>purpose\</strong> defined in your consent policy will be displayed to users, so ensure it communicates the value your application provides.
&#x20;     \</p>
&#x20;   \</div>
&#x20; \</Tab>

&#x20; \<Tab title="Refreshing Connections">
&#x20;   \<div className="doc-section">
&#x20;     \<h2>Refreshing Connections\</h2>

&#x20;     \<ul className="doc-list">
&#x20;       \<li>
&#x20;         ⚠️ \<strong>Minimize ad hoc refreshes:\</strong> Excessive requests can overload bank websites, causing account lockouts or action from the bank.
&#x20;       \</li>

&#x20;       \<li>
&#x20;         🕒 \<strong>Use job steps to monitor progress:\</strong> Creating a new connection with the same credentials while one is already in progress will pause the new connection for 6 minutes to prevent account lockout issues.
&#x20;       \</li>

&#x20;       \<li>
&#x20;         🚫 \<strong>Avoid bulk refreshes:\</strong> Large-scale refreshes (e.g., via cron jobs) can overload bank websites. Instead, rely on the smart cache or confirm a connection has not recently been refreshed before initiating a new request.
&#x20;       \</li>

&#x20;       \<li>
&#x20;         🔍 \<strong>Check the last refresh time:\</strong> Use the \`connection.lastUsed\` attribute or the user’s jobs to determine the last refresh time and result. Ensure the connection is active before refreshing, as refreshing inactive connections will fail.
&#x20;       \</li>
&#x20;     \</ul>
&#x20;   \</div>
&#x20; \</Tab>
\</Tabs>

\<style jsx>
&#x20; \{\`
&#x20;                 .doc-section \{
&#x20;                   padding: 20px;
&#x20;                   background: #f9f9f9;
&#x20;                   border-radius: 8px;
&#x20;                   box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
&#x20;                   margin: 10px 0;
&#x20;                 }

&#x20;                 .doc-highlight \{
&#x20;                   font-size: 1.1em;
&#x20;                   color: #333;
&#x20;                   background: #eef7fe;
&#x20;                   padding: 10px;
&#x20;                   border-radius: 6px;
&#x20;                   margin-bottom: 16px;
&#x20;                 }

&#x20;                 .doc-list \{
&#x20;                   list-style: none;
&#x20;                   padding-left: 0;
&#x20;                   margin: 0;
&#x20;                 }

&#x20;                 .doc-list li \{
&#x20;                   font-size: 1em;
&#x20;                   color: #555;
&#x20;                   padding: 8px 0;
&#x20;                   border-bottom: 1px solid #eee;
&#x20;                 }

&#x20;                 .doc-list li:last-child \{
&#x20;                   border-bottom: none;
&#x20;                 }

&#x20;                 .doc-list strong \{
&#x20;                   color: #0073e6;
&#x20;                 }
&#x20;               \`}
\</style>

\<Columns layout="auto" className="documentation-columns">
&#x20; \<Column>
&#x20;   \<h3>🚀 Use the Smart Cache\</h3>

&#x20;   \<p>
&#x20;     For ongoing daily refreshed data, request the Basiq team to enable the
&#x20;     \<strong>smart cache feature\</strong>. This background refresh mechanism is far more efficient than initiating daily Refresh Connection requests.
&#x20;   \</p>

&#x20;   \<p>
&#x20;     \<strong>Note:\</strong> OpenBanking connections are limited to
&#x20;     \<span className="highlight">20 refreshes per day\</span>.
&#x20;   \</p>
&#x20; \</Column>

&#x20; \<Column>
&#x20;   \<h3>🛠️ Handling Jobs for Ongoing Data Access\</h3>
&#x20;   \<h4>Handling jobs correctly is essential for good UX\</h4>

&#x20;   \<p>
&#x20;     Providing users with a simple, intuitive experience requires proper handling of job statuses and error messages. These help you troubleshoot issues and communicate them effectively to users (e.g., new login credentials needed).
&#x20;   \</p>

&#x20;   \<p>
&#x20;     Use the \<code>/job\</code> endpoint to monitor the status of recent jobs and address failures promptly.
&#x20;   \</p>

&#x20;   \<h4>Check jobs regularly\</h4>

&#x20;   \<p>
&#x20;     A typical cadence includes daily checks and checks during user login. This allows for timely resolution of errors. For instance:
&#x20;   \</p>

&#x20;   \<ul>
&#x20;     \<li>Users might need to update credentials.\</li>
&#x20;     \<li>Banks may require acknowledging new terms or popup messages.\</li>
&#x20;   \</ul>

&#x20;   \<p>
&#x20;     For more details, refer to our resources on \<a href="doc:handling-jobs">handling jobs effectively\</a>.
&#x20;   \</p>
&#x20; \</Column>

&#x20; \<Column>
&#x20;   \<h3>🧹 Purging Connection Data\</h3>

&#x20;   \<p>
&#x20;     In addition to using our \<a href="https\://api.basiq.io/reference/purgeconnectiondata">API\</a>,
&#x20;     connection data can be purged directly from the Dashboard. This feature allows you to manage user connections without direct API calls.
&#x20;   \</p>

&#x20;   \<h4>Steps to Purge Data from the Dashboard:\</h4>

&#x20;   \<ul>
&#x20;     \<li>
&#x20;       \<strong>Navigate to User Connections:\</strong> Access the user's profile and locate the connections list.
&#x20;     \</li>

&#x20;     \<li>
&#x20;       \<strong>Identify the Connection:\</strong> Find the connection with the unique Connection ID.
&#x20;     \</li>

&#x20;     \<li>
&#x20;       \<strong>Initiate the Purge:\</strong> Click on the "Purge" button next to the relevant connection.
&#x20;     \</li>

&#x20;     \<li>
&#x20;       \<strong>Confirm the Purge:\</strong> Approve the action to remove associated data.
&#x20;       \<span className="highlight">The Connection ID remains intact\</span>, allowing future refreshes.
&#x20;     \</li>
&#x20;   \</ul>

&#x20;   \<blockquote className="warning">
&#x20;     🚧 \<strong>Important:\</strong> Purging is irreversible. Proceed with caution. The Dashboard feature adheres to the same permissions and security protocols as the API endpoint.
&#x20;   \</blockquote>
&#x20; \</Column>
\</Columns>

\<style jsx>
&#x20; \{\`
&#x20;               .documentation-columns \{
&#x20;                 gap: 20px;
&#x20;               }

&#x20;               .highlight \{
&#x20;                 color: #0073e6;
&#x20;                 font-weight: bold;
&#x20;               }

&#x20;               .warning \{
&#x20;                 background: #ffefef;
&#x20;                 border-left: 5px solid #f44336;
&#x20;                 padding: 10px;
&#x20;                 margin: 10px 0;
&#x20;               }

&#x20;               h3, h4 \{
&#x20;                 margin-top: 0;
&#x20;               }

&#x20;               ul \{
&#x20;                 list-style: disc;
&#x20;                 padding-left: 20px;
&#x20;               }

&#x20;               p \{
&#x20;                 margin: 0 0 10px;
&#x20;               }
&#x20;             \`}
\</style>

\<Accordion title="API Endpoint Reference">
&#x20; \<div className="accordion-content">
&#x20;   \<h3>Purge Connection Data Endpoint\</h3>
&#x20;   \<p>
&#x20;     Use the following endpoint to purge connection data:
&#x20;   \</p>
&#x20;   \<pre className="code-block">
&#x20;     \<code>
POST /users/\{userId}/connections/\{connectionId}/purge
&#x20;     \</code>
&#x20;   \</pre>
&#x20;   \<p>
&#x20;     This endpoint requires:
&#x20;   \</p>
&#x20;   \<ul>
&#x20;     \<li>\<strong>userId\</strong>: The identifier for the user.\</li>
&#x20;     \<li>\<strong>connectionId\</strong>: The identifier for the connection.\</li>
&#x20;   \</ul>
&#x20;   \<p>
&#x20;     For detailed information on request parameters and expected responses, refer to our\{" "}
&#x20;     \<a href="https\://api.basiq.io/reference/purgeconnectiondata" target="\_blank" rel="noopener noreferrer">
&#x20;       API Documentation
&#x20;     \</a>.
&#x20;   \</p>
&#x20; \</div>
\</Accordion>

\<style jsx>
&#x20; \{\`
&#x20;   .accordion-content \{
&#x20;     padding: 16px;
&#x20;     background-color: #f9f9f9;
&#x20;     border-radius: 8px;
&#x20;     margin-top: 8px;
&#x20;   }

&#x20;   .accordion-content h3 \{
&#x20;     font-size: 1.2em;
&#x20;     color: #333;
&#x20;     margin-bottom: 8px;
&#x20;     font-weight: bold;
&#x20;   }

&#x20;   .accordion-content p \{
&#x20;     font-size: 1em;
&#x20;     color: #666;
&#x20;     line-height: 1.5;
&#x20;   }

&#x20;   .code-block \{
&#x20;     background-color: #272822;
&#x20;     color: #f8f8f2;
&#x20;     padding: 12px;
&#x20;     border-radius: 8px;
&#x20;     font-family: 'Courier New', Courier, monospace;
&#x20;     overflow-x: auto;
&#x20;     margin: 12px 0;
&#x20;   }

&#x20;   .code-block code \{
&#x20;     white-space: pre-wrap;
&#x20;   }

&#x20;   a \{
&#x20;     color: #0073e6;
&#x20;     text-decoration: none;
&#x20;   }

&#x20;   a:hover \{
&#x20;     text-decoration: underline;
&#x20;   }

&#x20;   ul \{
&#x20;     margin: 8px 0 16px;
&#x20;     padding-left: 20px;
&#x20;   }

&#x20;   li \{
&#x20;     font-size: 1em;
&#x20;     color: #555;
&#x20;     margin-bottom: 4px;
&#x20;   }
&#x20; \`}
\</style>
.

\<Columns layout="auto" className="documentation-columns">
&#x20; \<Column>
&#x20;   \<div className="interactive-card">
&#x20;     \<div className="card-content">
&#x20;       \<div className="card-icon">
&#x20;         \<i className="fa fa-plug" />
&#x20;       \</div>

&#x20;       \<h3 className="card-title">Using the Connectors Endpoint\</h3>

&#x20;       \<p className="card-description">
&#x20;         Fetch the current status and stage of all connectors to dynamically resolve connection issues. Automate your workflows by determining the cause of issues without contacting support.
&#x20;       \</p>

&#x20;       \<button className="learn-more-button">Learn More\</button>
&#x20;     \</div>
&#x20;   \</div>
&#x20; \</Column>

&#x20; \<Column>
&#x20;   \<div className="interactive-card">
&#x20;     \<div className="card-content">
&#x20;       \<div className="card-icon">
&#x20;         \<i className="fa fa-exclamation-triangle" />
&#x20;       \</div>

&#x20;       \<h3 className="card-title">Error Logging\</h3>

&#x20;       \<p className="card-description">
&#x20;         Log key details like \<code>userId\</code>, \<code>connectionId\</code>, and \<code>jobId\</code>. This allows support teams to investigate issues effectively and provide better assistance.
&#x20;       \</p>

&#x20;       \<button className="learn-more-button">Learn More\</button>
&#x20;     \</div>
&#x20;   \</div>
&#x20; \</Column>
\</Columns>

\<style jsx>
&#x20; \{\`
&#x20;         .documentation-columns \{
&#x20;           gap: 20px;
&#x20;           margin-top: 30px;
&#x20;         }

&#x20;         .interactive-card \{
&#x20;           max-width: 360px;
&#x20;           margin: 0 auto;
&#x20;           padding: 20px;
&#x20;           background-color: #ffffff;
&#x20;           border-radius: 12px;
&#x20;           box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
&#x20;           transition: transform 0.3s ease;
&#x20;           cursor: pointer;
&#x20;         }

&#x20;         .interactive-card:hover \{
&#x20;           transform: translateY(-10px);
&#x20;         }

&#x20;         .card-content \{
&#x20;           text-align: center;
&#x20;         }

&#x20;         .card-icon \{
&#x20;           font-size: 48px;
&#x20;           color: #0073e6;
&#x20;           margin-bottom: 20px;
&#x20;         }

&#x20;         .card-title \{
&#x20;           font-size: 1.4em;
&#x20;           color: #333;
&#x20;           margin-bottom: 16px;
&#x20;           font-weight: bold;
&#x20;         }

&#x20;         .card-description \{
&#x20;           font-size: 1em;
&#x20;           color: #666;
&#x20;           line-height: 1.5;
&#x20;           margin-bottom: 20px;
&#x20;         }

&#x20;         .learn-more-button \{
&#x20;           padding: 10px 20px;
&#x20;           background-color: #0073e6;
&#x20;           color: white;
&#x20;           font-size: 1em;
&#x20;           border: none;
&#x20;           border-radius: 30px;
&#x20;           cursor: pointer;
&#x20;           transition: background-color 0.3s ease;
&#x20;         }

&#x20;         .learn-more-button:hover \{
&#x20;           background-color: #005bb5;
&#x20;         }
&#x20;       \`}
\</style>