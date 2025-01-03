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

<Columns layout="auto" className="documentation-columns">
  <Column>
    <h3>🚀 Use the Smart Cache</h3>

    <p>
      For ongoing daily refreshed data, request the Basiq team to enable the
      <strong>smart cache feature</strong>. This background refresh mechanism is far more efficient than initiating daily Refresh Connection requests.
    </p>

    <p>
      <strong>Note:</strong> OpenBanking connections are limited to
      <span className="highlight">20 refreshes per day</span>.
    </p>
  </Column>

  <Column>
    <h3>🛠️ Handling Jobs for Ongoing Data Access</h3>
    <h4>Handling jobs correctly is essential for good UX</h4>

    <p>
      Providing users with a simple, intuitive experience requires proper handling of job statuses and error messages. These help you troubleshoot issues and communicate them effectively to users (e.g., new login credentials needed).
    </p>

    <p>
      Use the <code>/job</code> endpoint to monitor the status of recent jobs and address failures promptly.
    </p>

    <h4>Check jobs regularly</h4>

    <p>
      A typical cadence includes daily checks and checks during user login. This allows for timely resolution of errors. For instance:
    </p>

    <ul>
      <li>Users might need to update credentials.</li>
      <li>Banks may require acknowledging new terms or popup messages.</li>
    </ul>

    <p>
      For more details, refer to our resources on <a href="doc:handling-jobs">handling jobs effectively</a>.
    </p>
  </Column>

  <Column>
    <h3>🧹 Purging Connection Data</h3>

    <p>
      In addition to using our <a href="https://api.basiq.io/reference/purgeconnectiondata">API</a>,
      connection data can be purged directly from the Dashboard. This feature allows you to manage user connections without direct API calls.
    </p>

    <h4>Steps to Purge Data from the Dashboard:</h4>

    <ul>
      <li>
        <strong>Navigate to User Connections:</strong> Access the user's profile and locate the connections list.
      </li>

      <li>
        <strong>Identify the Connection:</strong> Find the connection with the unique Connection ID.
      </li>

      <li>
        <strong>Initiate the Purge:</strong> Click on the "Purge" button next to the relevant connection.
      </li>

      <li>
        <strong>Confirm the Purge:</strong> Approve the action to remove associated data.
        <span className="highlight">The Connection ID remains intact</span>, allowing future refreshes.
      </li>
    </ul>

    <blockquote className="warning">
      🚧 <strong>Important:</strong> Purging is irreversible. Proceed with caution. The Dashboard feature adheres to the same permissions and security protocols as the API endpoint.
    </blockquote>
  </Column>
</Columns>

<style jsx>
  {`
                                          .documentation-columns {
                                            gap: 20px;
                                          }

                                          .highlight {
                                            color: #0073e6;
                                            font-weight: bold;
                                          }

                                          .warning {
                                            background: #ffefef;
                                            border-left: 5px solid #f44336;
                                            padding: 10px;
                                            margin: 10px 0;
                                          }

                                          h3, h4 {
                                            margin-top: 0;
                                          }

                                          ul {
                                            list-style: disc;
                                            padding-left: 20px;
                                          }

                                          p {
                                            margin: 0 0 10px;
                                          }
                                        `}
</style>

<p />

<Columns layout="auto" className="documentation-columns">
  <Column>
    <div className="interactive-card">
      <div className="card-content">
        <div className="card-icon">
          <i className="fa fa-plug" />
        </div>

        <h3 className="card-title">Connectors Endpoint</h3>

        <p className="card-description">
          Fetch the current status and stage of all connectors to dynamically resolve connection issues.
        </p>
      </div>
    </div>
  </Column>

  <Column>
    <div className="interactive-card">
      <div className="card-content">
        <div className="card-icon">
          <i className="fa fa-exclamation-triangle" />
        </div>

        <h3 className="card-title">Error Logging</h3>

        <p className="card-description">
          Log key details like <code>userId</code>, <code>connectionId</code>, and <code>jobId</code>. This allows support teams to investigate issues effectively and provide better assistance.
        </p>
      </div>
    </div>
  </Column>

  <Column>
    <Tab title="Data Storage Best Practices">
      <div className="interactive-card">
        <div className="card-content">
          <div className="card-icon">
            <i className="fa fa-database" />
          </div>

          <h3 className="card-title">Secure Data Storage</h3>

          <p className="card-description">
            Partners should implement a secure data storage system to store necessary user information, with encryption and restricted access for authorized users only.
          </p>
        </div>
      </div>
    </Tab>
  </Column>
</Columns>

<style jsx>
  {`
                                    .documentation-columns {
                                      gap: 20px;
                                      margin-top: 30px;
                                    }

                                    .interactive-card {
                                      max-width: 360px;
                                      margin: 0 auto;
                                      padding: 20px;
                                      background-color: #ffffff;
                                      border-radius: 12px;
                                      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
                                      transition: transform 0.3s ease;
                                      cursor: pointer;
                                    }

                                    .interactive-card:hover {
                                      transform: translateY(-10px);
                                    }

                                    .card-content {
                                      text-align: center;
                                    }

                                    .card-icon {
                                      font-size: 48px;
                                      color: #0073e6;
                                      margin-bottom: 20px;
                                    }

                                    .card-title {
                                      font-size: 1.4em;
                                      color: #333;
                                      margin-bottom: 16px;
                                      font-weight: bold;
                                    }

                                    .card-description {
                                      font-size: 1em;
                                      color: #666;
                                      line-height: 1.5;
                                      margin-bottom: 20px;
                                    }

                                    .learn-more-button {
                                      padding: 10px 20px;
                                      background-color: #0073e6;
                                      color: white;
                                      font-size: 1em;
                                      border: none;
                                      border-radius: 30px;
                                      cursor: pointer;
                                      transition: background-color 0.3s ease;
                                    }

                                    .learn-more-button:hover {
                                      background-color: #005bb5;
                                    }
                                  `}
</style>