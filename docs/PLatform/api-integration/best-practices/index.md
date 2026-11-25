---
title: Basiq best practices
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Apply these practices to manage authentication, consent, connection refreshes, and user data in your Basiq API integration.

<Tabs>
  <Tab title="Authentication">
    <div className="doc-section">
      <h2>Cache your authentication token</h2>
    <p className="doc-highlight">
    The token you receive expires after one hour (3600 seconds).<br /><strong>Cache this token for global use.</strong> Reuse it across users and connections. Authenticating separately for each user or connection causes scaling issues.<br />  </p>
     </div>
  </Tab>

  <Tab title="Configuring Your Application">
    <div className="doc-section">
      <h2>Configure your consent policy</h2>
      <p className="doc-highlight">
        <strong>Review your consent policy before making changes.</strong> Changes apply only to new user consents. This includes adding data scopes (permissions to access specific types of data). Existing users either keep their original consent policy or need to consent again.
      </p>

      <p>
        <strong>Explain why you request consent.</strong> Your consent policy shows users the <strong>purpose</strong> you define. Describe how your application uses their data and the value they receive.
      </p>
    </div>
  </Tab>

  <Tab title="Refreshing Connections">
    <div className="doc-section">
      <h2>Manage connection refreshes</h2>
      <ul className="doc-list">
        <li>
          <strong>Minimize ad hoc (on-demand) refreshes:</strong> Excessive requests can overload bank websites, causing account lockouts or action from the bank.
        </li>

        <li>
          <strong>Use job steps to monitor progress.</strong> If you create another connection with the same credentials while one is in progress, Basiq pauses the new connection for 6 minutes. This pause helps prevent account lockouts.
        </li>

        <li>
          <strong>Avoid bulk refreshes.</strong> Large-scale refreshes can overload bank websites. This includes refreshes from cron jobs (scheduled tasks). Use Smart Cache (a background data refresh mechanism) instead. Before requesting a refresh yourself, check when the connection last refreshed.
        </li>

        <li>
          <strong>Check the last refresh time:</strong> Use <code>connection.lastUsed</code> (the connection's last refresh time) or the user's job records. Check job records for the refresh result. Ensure the connection is active before refreshing; attempts to refresh inactive connections fail.
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
    <h2>Use Smart Cache</h2>

    <p>
      Ask the Basiq team to enable <strong>Smart Cache</strong> for daily data refreshes.
      This feature refreshes data in the background, so you can avoid initiating daily Refresh Connection requests.
    </p>

    <p>
      <strong>Note:</strong> Open Banking (bank data sharing with user consent) allows up to
      <span className="highlight">20 refreshes per connection per day</span>.
    </p>
  </Column>

  <Column>
    <h2>Handle jobs for ongoing data access</h2>
    <h3>Respond to job statuses and errors</h3>

    <p>
      Check job statuses and error messages to identify failures. Tell users what action to take, such as updating their login credentials.
    </p>

    <p>
      Use the <code>/job</code> endpoint to monitor the status of recent jobs and address failures promptly.
    </p>

    <h3>Check jobs regularly</h3>

    <p>
      A typical cadence includes daily checks and checks during user login. This allows for timely resolution of errors. For instance:
    </p>

    <ul>
      <li>Users might need to update credentials.</li>
      <li>Banks may require acknowledging new terms or popup messages.</li>
    </ul>

    <p>
      For more details, read <a href="/docs/handling-jobs">Handling jobs</a>.
    </p>
  </Column>

  <Column>
    <h2>Purge connection data</h2>

    <p>
      Purge (permanently delete) connection data from the Dashboard or through the <a href="https://api.basiq.io/reference/purgeconnectiondata">Purge Connection Data API</a>.
      Use the Dashboard to purge data without making API calls.
    </p>

    <h3>Purge data from the Dashboard</h3>

    <ol>
      <li>
        <strong>Navigate to user connections:</strong> Open the user's profile and locate the connections list.
      </li>

      <li>
        <strong>Identify the connection:</strong> Find the connection by its unique connection ID.
      </li>

      <li>
        <strong>Initiate the purge:</strong> Select the "Purge" button next to the connection.
      </li>

      <li>
        <strong>Confirm the purge:</strong> Approve the action to permanently delete the connection's data.
        <span className="highlight">The connection ID stays the same.</span> You can refresh the connection again later.
      </li>
    </ol>
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

<blockquote className="warning">
  🚧 <strong>Important:</strong> Purging is irreversible. Proceed with caution. The Dashboard feature adheres to the same permissions and security protocols as the API endpoint.
</blockquote>

<p> </p>

<Columns layout="auto" className="documentation-columns">
  <Column>
    <div className="interactive-card">
      <div className="card-content">
        <div className="card-icon" aria-hidden="true">
          <i className="fa fa-plug" />
        </div>

        <h2 className="card-title">Connectors endpoint</h2>

        <p className="card-description">
          Fetch the current status and stage of all connectors to dynamically resolve connection issues.
        </p>
      </div>
    </div>
  </Column>

  <Column>
    <div className="interactive-card">
      <div className="card-content">
        <div className="card-icon" aria-hidden="true">
          <i className="fa fa-exclamation-triangle" />
        </div>

        <h2 className="card-title">Error logging</h2>

        <p className="card-description">
          Log <code>userId</code>, <code>connectionId</code>, and <code>jobId</code> so support teams can investigate the affected user, connection, and job.
        </p>
      </div>
    </div>
  </Column>

  <Column>
    <div className="interactive-card">
      <div className="card-content">
        <div className="card-icon" aria-hidden="true">
          <i className="fa fa-database" />
        </div>

        <h2 className="card-title">Secure data storage</h2>

        <p className="card-description">
          Store only the user information you need. Encrypt it and restrict access to authorized users.
        </p>
      </div>
    </div>
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

## Contact support

Contact [Basiq support](mailto:support@basiq.io) if you encounter issues.