---
title: Frequently asked questions
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: platform
      title: Platform
---
<Image align="center" src="https://files.readme.io/6187bf8ac3419d7f0b37f637f292af736f81f1489917d737d444936e52ecf3a8-82119ec-FAQ_Header.jpg" />

When incorporating the Basiq API into your application, it's essential to follow best practices that significantly contribute to the success of any implementation. These practices span various areas, including security considerations, user experience (UX), scalability, and more. They have undergone thorough testing to provide you with the essential tools and guidelines for a successful integration.

Explore the Frequently Asked Questions (FAQs) below for our platform:

<Accordion title="What is OpenBanking?" icon="fa-info-circle">
  <p>
    <strong>Open Banking (CDR):</strong> Open banking, also known as the Consumer Data Right (CDR) in Australia, is a new method for capturing user consent and sharing financial data. Regulated by the Australian federal government, it requires banks to share data via APIs specifically built for this purpose. Unlike DDC, CDR does not require users to share login credentials, is more performant and robust, and banks are mandated to participate.
  </p>
</Accordion>

<Accordion title="What is a DDC Connector?" icon="fa-info-circle">
  <p>
    <strong>DDC Connector:</strong> Digital Data Capture (or "screen scraping") is a well-established method of aggregating financial data. It involves securely sharing login credentials, which are then passed to the bank's internet banking portal. The portal is parsed to extract a user's accounts and transactions. This method can be slow and is susceptible to changes in the bank's portal. DDC has seen a decline, especially after recent data breaches, as banks take measures to prevent bot access to their internet banking portals.
  </p>

  <p>
    <strong>API Versions:</strong> Version 2 of the API supports DDC only. Version 3 supports both DDC and CDR, allowing dynamic switching between the two methods.
  </p>
</Accordion>

<Accordion title="What is a Data Holder (DH) and an Accredited Data Recipient (ADR)?" icon="fa-info-circle">
  <p><strong>A Data Holder</strong> refers to a business that currently holds a consumers’ data, such as a bank. Consumers have the authority to instruct registered Data Holders to share their data with an <strong>Accredited Data Recipient (ADR)</strong>.</p>
  <p>An <strong>ADR</strong> is a business accredited by the Australian Competition and Consumer Commission (ACCC) to receive consumer data from a Data Holder, contingent upon the consumer's explicit consent. The ADR then utilises the data for the specified purpose.</p>
  <p><strong>BASIQ</strong> operates as an ADR within the CDR system, having obtained accreditation by meeting the stringent criteria outlined by the ACCC.</p>
  <p>For a comprehensive list of registered Data Holders, refer to the government's CDR website: <a href="https://www.cdr.gov.au/find-a-provider" target="_blank">[https://www.cdr.gov.au/find-a-provider](https://www.cdr.gov.au/find-a-provider)</a></p>
</Accordion>

<Accordion title="What are Web and Open Banking transaction date/times?" icon="fa-info-circle">
  <h2>Web Connectors:</h2>
  <p>We only get <code>transaction.Date</code> field from the connector (timestamp not available).</p>
  <p>We only store date under user transaction data.</p>
  <p>When compiling <code>user\_transactions\_get</code> response, we add midnight time <code>normalizedDateTime := transaction.Date + utils.RFCMIDNIGHT</code>.</p>
  <p>We set the date for transactions, then <code>00:00:00Z</code> is appended (indicating UTC).</p>
  <h2>OB/CDR Connectors:</h2>
  <p>We get full datetime from the connector, as <code>obTransactionDateTime</code>.</p>
  <p><code>postingDateTime</code> in the case of posted transactions.</p>
  <p><code>executionDateTime</code> in the case of pending transactions.</p>
  <p>We store the date in two fields within user transactions data: <code>date</code> and <code>obTransactionDateTime</code>.</p>
  <p>When compiling <code>user\_transactions\_get</code> response, we normalize the time <code>normalizedDateTime.UTC().Format(time.RFC3339)</code>.</p>
  <p>In case <code>obTransactionDateTime</code> can't be validated, we add midnight to the <code>transaction.Date</code>.</p>
  <h2>Exposing Data via GET /transactions Endpoint:</h2>
  <p>For posted transactions, we return <code>postDate</code>.</p>
  <p>For pending transactions, we return <code>transactionDate</code>.</p>
  <p>We initially save transaction’s <code>dateTime</code> as received from the DH, without any modifications. Per CDR standard, RFC3339 is used for <code>dateTime</code>, meaning all times expressed have a stated relationship (offset) to Coordinated Universal Time (UTC).</p>
  <p>All DHs return data in UTC (plus offset, if there is any), or at least they are obligated to convert to UTC, not just set this timezone.</p>
  <p>Some DHs actually provide the offset to UTC, like ANZ. Example is "<code>2021-11-19T00:00:00+11:00</code>". This represents UTC + 11 hours. In our system, we have a logic where we calculate this offset to provide in standardized format in UTC without the offset so, "<code>2021-11-19T00:00:00+11:00</code>" becomes "<code>2021-11-18T13:00:00Z</code>". We subtracted 11 hours from midnight, and got the previous day at 13:00 hours. This is correct behavior from our side.</p>
  <p>Note: all <code>dateTimes</code> for open banking are in UTC, as this is CDR standard. We cannot convert to local times depending on the time zone, this is impossible for us, and we strive to have a single time zone (UTC is usually the standard).</p>
  <p>Some DHs just append <code>00:00:00Z</code> at the end - now, if they haven’t done conversion to UTC, but just take the date and say it is UTC, this is incorrect behavior from the DH side. In those instances, that transaction within the customer's Internet/Online Banking would show exact times in the local time zone.</p>
  <p>We raise these behaviors in a ticket to the DH via the CDR Portal and, over time, we will see improvements in the accuracy of these time stamps.</p>
</Accordion>

<Accordion title="Job error 'Service is currently unavailable. Please try again later.'" icon="fa-info-circle">
  <p>No, this error does not indicate any problem with Basiq. The error indicates that there was a problem retrieving your user's data from their bank, and as the Basiq job relates closely to your user interaction, we provide a range of actionable error codes to help you to provide the best possible user experience in those cases where the bank fails to return data.</p>
  <p>You can read more about these scenarios and recommended actions and user comms <a href="https://api.basiq.io/docs/handling-jobs" target="_blank">here</a>:</p>
  <p>The service-unavailable error code is our way to tell you (so that you can tell your user) that their bank was unable to return data in response to a request.</p>
</Accordion>

<Accordion title="Why do I have a 'missing bank data' error in my job output?" icon="fa-info-circle">
  <p>The output can show missing data because your user’s bank failed to provide the requested information. This can happen for various reasons, including:</p>

  <ul>
    <li>The bank's response to our API is incomplete or contains missing data.</li>
    <li>Your user’s online banking session expired or was terminated unexpectedly.</li>
    <li>The bank's technical infrastructure is experiencing downtime or disruptions.</li>
  </ul>

  <p>Further details are available in the <a href="https://api.basiq.io/docs/error-codes#incomplete-job" target="_blank">error code documentation</a>.</p>
</Accordion>

<Accordion title="What should I do if my request returns an error?" icon="fa-info-circle">
  <p>If your request returns an error, review the error code and the accompanying message carefully to understand the issue. Our <a href="https://api.basiq.io/docs/error-codes" target="_blank">error code documentation</a> provides detailed explanations for each error code and how you should handle them. Common issues include authentication errors, incorrect request formats, or temporary issues with the bank’s API.</p>
  <p>Ensure your implementation follows Basiq's guidelines for error handling and data retrieval to improve user experience and service reliability.</p>
</Accordion>

<Accordion title="How do I test my integration with Basiq?" icon="fa-info-circle">
  <p>To test your integration with Basiq, use our sandbox environment. The sandbox allows you to simulate user interactions and API calls to test your implementation without impacting real user data. Detailed documentation on how to access and use the sandbox is available on our <a href="https://api.basiq.io/docs/sandbox" target="_blank">sandbox page</a>.</p>
  <p>Use the sandbox to verify data flows, simulate various scenarios, and ensure your application responds appropriately to different API responses.</p>
</Accordion>

<Accordion title="What data does Basiq retrieve from users' bank accounts?" icon="fa-info-circle">
  <p>Basiq can retrieve various types of financial data from users' bank accounts, including:</p>

  <ul>
    <li>Account information such as account type, number, and balance</li>
    <li>Transaction history with details such as date, description, and amount</li>
    <li>Pending and posted transactions</li>
  </ul>

  <p>All data retrieval is done securely and with the explicit consent of the user, following the CDR standards and data privacy regulations. For a full breakdown of the data Basiq retrieves, refer to our <a href="https://api.basiq.io/docs/data-structure" target="_blank">data structure documentation</a>.</p>
</Accordion>

<br />

\<p>
&#x20; If you have any questions, please reach out to our\{" "}
&#x20; \<a href="#" onClick=\{() => Intercom('showNewMessage', 'Feedback on the new feature:')}>
&#x20;   support team
&#x20; \</a>.
\</p>