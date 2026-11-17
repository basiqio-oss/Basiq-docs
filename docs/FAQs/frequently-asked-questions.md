---
title: Frequently asked questions
excerpt: ''
deprecated: false
hidden: false
icon: fad fa-comment-question
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
  pages:
    - slug: platform
      title: Platform
      type: basic
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
    <strong>DDC Connector:</strong> Digital Data Capture is a well-established method of aggregating financial data. It involves securely sharing login credentials, which are then passed to the bank's internet banking portal. The portal is parsed to extract a user's accounts and transactions. This method can be slow and is susceptible to changes in the bank's portal. DDC has seen a decline, especially after recent data breaches, as banks take measures to prevent bot access to their internet banking portals.
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

<Accordion title="How does the Open Banking consent process work?" icon="fa-info-circle">
  <p>Open Banking allows consumers to authorise an Accredited Data Recipient (ADR) to access their financial data through the Consumer Data Right (CDR) framework.</p>

  <p>When connecting an account through Basiq:</p>

  <ul>
    <li>The consumer selects their financial institution.</li>
    <li>The consumer is redirected to their bank's authentication experience.</li>
    <li>The consumer authenticates directly with their bank.</li>
    <li>The consumer reviews and authorises the requested data sharing permissions.</li>
    <li>Once consent is successfully established, Basiq can retrieve the authorised data through the institution's CDR APIs.</li>
  </ul>

  <p>The authentication and consent experience is managed by the Data Holder. Basiq does not control the bank's individual authentication requirements or user interface.</p>
</Accordion>

<Accordion title="What is the difference between collection consent and disclosure consent?" icon="fa-info-circle">
    <p><strong>Collection consent:</strong> Allows an Accredited Data Recipient (ADR) to collect a consumer's data from a Data Holder under the Consumer Data Right (CDR) framework.</p>

    <p><strong>Disclosure consent:</strong> Relates to the consumer authorising the disclosure of their CDR data by an ADR to another recipient, where the relevant CDR disclosure arrangements apply.</p>

    <p>These are separate consent arrangements with different purposes and obligations. The applicable consent requirements depend on the data-sharing arrangement and the role of each participant.</p>

    <p>For further information, refer to the <a href="https://www.cdr.gov.au/" target="_blank">Consumer Data Right website</a>.</p>
</Accordion>

<Accordion title="How long does an Open Banking consent remain active?" icon="fa-info-circle">
    <p>Open Banking consents are subject to the consent duration and expiry requirements under the Consumer Data Right (CDR) Rules.</p>

    <p>The applicable duration depends on the type of consent and the relevant regulatory requirements.</p>

    <p>Consumers may be required to renew their consent before it expires to maintain ongoing access to their financial data.</p>

    <p>Applications integrating Basiq should monitor consent status and expiry information and provide appropriate notifications to consumers where required.</p>

    <p>For further information, refer to the <a href="https://www.cdr.gov.au/" target="_blank">CDR Rules and regulatory guidance</a>.</p>
</Accordion>

<Accordion title="Can a consumer revoke their Open Banking consent?" icon="fa-info-circle">
    <p>Yes. Consumers can withdraw their CDR consent through the applicable consent management process.</p>

    <p>When consent is withdrawn, the ADR must cease collecting data under that consent in accordance with the applicable CDR requirements.</p>

    <p>Revocation may also trigger obligations relating to the handling, deletion or de-identification of previously collected data, depending on the applicable regulatory requirements and circumstances.</p>

    <p>Applications should ensure that consumers have a clear way to manage their consents and understand the impact of withdrawing access.</p>
</Accordion>

<Accordion title="What happens when an Open Banking consent expires?" icon="fa-info-circle">
    <p>When a CDR consent expires, the ADR can no longer rely on that expired consent to continue collecting data.</p>

    <p>The consumer may need to complete a new consent process to re-establish access to their financial information.</p>

    <p>Applications should monitor consent expiry and communicate any required actions to consumers before access is interrupted.</p>
</Accordion>

<Accordion title="Can a consumer connect multiple bank accounts?" icon="fa-info-circle">
    <p>Yes. Consumers can connect multiple eligible accounts through Basiq, subject to the accounts and permissions made available by their financial institution.</p>

    <p>Account availability depends on the Data Holder, the account types supported and the permissions authorised by the consumer.</p>

    <p>When implementing multiple account connections, applications should ensure that each connection and its associated consent are managed appropriately.</p>
</Accordion>

<Accordion title="Can consumers connect joint bank accounts?" icon="fa-info-circle">
    <p>Joint account access is subject to the Data Holder's CDR implementation and the applicable consumer authorisation requirements.</p>

    <p>The availability of a joint account may depend on the account structure, the institution's supported functionality and the consumer's eligibility to authorise data sharing.</p>

    <p>Not all joint accounts are necessarily available through every financial institution.</p>
</Accordion>

<Accordion title="Does Basiq support business bank accounts?" icon="fa-info-circle">
    <p>Basiq supports financial data aggregation through the available connection methods and institution capabilities.</p>

    <p>Business account availability through CDR depends on the Data Holder, the account holder's eligibility and the applicable CDR requirements.</p>

    <p>For business account integrations, check the relevant institution's supported account types and connection capabilities before implementing your customer journey.</p>
</Accordion>

<Accordion title="Which banks and financial institutions does Basiq support?" icon="fa-info-circle">
    <p>Basiq provides connectivity to financial institutions through its supported Web and Open Banking (CDR) connectors.</p>

    <p>The available institutions and connection methods may differ depending on the institution and the type of account being connected.</p>

    <p>For the latest information about registered CDR participants, refer to the government's <a href="https://www.cdr.gov.au/find-a-provider" target="_blank">CDR provider directory</a>.</p>

    <p>For institution-specific Basiq connectivity and availability, contact <a href="mailto:support@basiq.io">Basiq Support</a>.</p>
</Accordion>

<Accordion title="Why can't I find my bank in the institution list?" icon="fa-info-circle">
  <p>If a financial institution is not appearing in the available institution list, there may be several reasons:</p>

  <ul>
    <li>The institution is not currently supported through the selected connection method.</li>
    <li>The institution may not provide the required CDR functionality.</li>
    <li>The institution may be undergoing changes or maintenance.</li>
    <li>The institution may not support the account type being connected.</li>
  </ul>

  <p>Check the available institution list and connection method in your Basiq integration. If the institution should be available but cannot be found, contact Basiq Support for assistance.</p>
</Accordion>

<Accordion title="Why is my financial institution showing as unavailable?" icon="fa-info-circle">
  <p>An institution may temporarily become unavailable due to technical issues, scheduled maintenance or disruptions within the Data Holder's infrastructure.</p>

  <p>Basiq relies on financial institutions to respond to data requests. If an institution cannot process a request, the connection or data retrieval process may fail.</p>

  <p>We recommend:</p>

  <ul>
    <li>Checking whether the institution is experiencing an outage.</li>
    <li>Reviewing the API response and associated error code.</li>
    <li>Retrying the request when the institution becomes available.</li>
    <li>Providing clear communication to the end user.</li>
  </ul>

  <p>For further information, refer to our <a href="https://api.basiq.io/docs/error-codes" target="_blank">error code documentation</a>.</p>
</Accordion>

<Accordion title="How frequently does Basiq retrieve financial data?" icon="fa-info-circle">
    <p>Data retrieval frequency depends on the connection method, the Data Holder's capabilities, applicable CDR requirements and the integration's data retrieval process.</p>

    <p>For Open Banking, Basiq retrieves data through the institution's CDR APIs when a permitted data retrieval request is made.</p>

    <p>Data availability and freshness depend on the information provided by the Data Holder. Basiq cannot guarantee that every institution will return updated information at the same frequency.</p>

    <p>Applications should account for potential differences in data freshness when displaying account and transaction information.</p>
</Accordion>

<Accordion title="Why hasn't my account information been updated?" icon="fa-info-circle">
  <p>Account information may not reflect the latest information available through internet banking for several reasons:</p>

  <ul>
    <li>The Data Holder has not yet provided updated account information.</li>
    <li>The latest data retrieval request has not completed successfully.</li>
    <li>The institution is experiencing a temporary service disruption.</li>
    <li>The account information returned by the institution has not changed.</li>
  </ul>

  <p>Review the latest connection and job status to determine whether the data retrieval request completed successfully.</p>

  <p>For more information, refer to our <a href="https://api.basiq.io/docs/handling-jobs" target="_blank">job handling documentation</a>.</p>
</Accordion>

<Accordion title="How far back can Basiq retrieve transaction history?" icon="fa-info-circle">
    <p>The available transaction history depends on the financial institution, account type, connection method and the historical data made available by the Data Holder.</p>

    <p>Different institutions may provide different transaction history periods. As a result, the amount of historical data available may vary between accounts.</p>

    <p>Applications should not assume that all institutions provide the same historical transaction coverage.</p>

    <p>For information about the transaction fields returned by Basiq, refer to our <a href="https://api.basiq.io/docs/data-structure" target="_blank">data structure documentation</a>.</p>
</Accordion>

<Accordion title="What is the difference between pending and posted transactions?" icon="fa-info-circle">
    <p><strong>Pending transactions:</strong> Transactions that have been initiated or authorised but have not yet been fully processed by the financial institution.</p>

    <p><strong>Posted transactions:</strong> Transactions that have been processed and recorded against the account by the financial institution.</p>

    <p>Pending transactions may change, disappear or be replaced by posted transactions as the bank completes processing.</p>

    <p>The availability and representation of pending and posted transactions depend on the information provided by the Data Holder.</p>
</Accordion>

<Accordion title="Why are some transactions missing from my account?" icon="fa-info-circle">
  <p>Missing transactions can occur for several reasons:</p>

  <ul>
    <li>The Data Holder has not included the transactions in its API response.</li>
    <li>The requested historical date range does not include the missing transactions.</li>
    <li>The transactions are still pending or have not been processed by the institution.</li>
    <li>The institution has experienced a temporary issue retrieving transaction information.</li>
    <li>The account or connection does not provide the requested transaction information.</li>
  </ul>

  <p>Review the API response and transaction date range to identify whether the missing information is related to the Data Holder or the request.</p>

  <p>For further assistance, contact Basiq Support with the relevant user ID, connection ID and job ID.</p>
</Accordion>

<Accordion title="Why are my account balances different from internet banking?" icon="fa-info-circle">
  <p>Account balances returned through Basiq are sourced from the financial institution.</p>

  <p>Differences between the balance displayed in an application and internet banking may occur because of:</p>

  <ul>
    <li>Differences between available and current balances.</li>
    <li>Pending transactions that have not yet been posted.</li>
    <li>Timing differences between the latest data retrieval and the institution's online banking platform.</li>
    <li>Differences in how the institution reports account balance information.</li>
  </ul>

  <p>For accurate interpretation, refer to the balance fields and their definitions in the <a href="https://api.basiq.io/docs/data-structure" target="_blank">Basiq data structure documentation</a>.</p>
</Accordion>

<Accordion title="Why do pending transactions disappear or change?" icon="fa-info-circle">
    <p>Pending transactions are not necessarily finalised transactions. The financial institution may update, remove or replace a pending transaction when it processes the transaction.</p>

    <p>For example, a pending transaction may be replaced by a posted transaction once the merchant completes processing.</p>

    <p>Applications should account for changes to pending transactions and avoid treating them as permanently settled transactions.</p>
</Accordion>

<Accordion title="Why do I need to authenticate with my bank again?" icon="fa-info-circle">
    <p>Additional authentication may be required depending on the connection method and the financial institution's requirements.</p>

    <p>For CDR connections, authentication and consent are managed through the Data Holder's authorisation experience.</p>

    <p>For Web (DDC) connections, changes to the bank's authentication process, expired sessions or additional security requirements may require the consumer to reconnect their account.</p>

    <p>The authentication experience and requirements are determined by the financial institution.</p>
</Accordion>

<Accordion title="Why am I not receiving an OTP from my bank?" icon="fa-info-circle">
  <p>One-time passwords (OTPs) are issued and managed by the financial institution as part of its authentication process.</p>

  <p>If an OTP is not received, the consumer should:</p>

  <ul>
    <li>Confirm that their registered mobile number or authentication method is correct.</li>
    <li>Check whether the bank provides OTPs through SMS, an authentication application or another method.</li>
    <li>Check for any bank notifications or authentication requests.</li>
    <li>Contact their financial institution if the issue continues.</li>
  </ul>

  <p>Basiq does not control the delivery of OTPs or the bank's authentication systems.</p>
</Accordion>

<Accordion title="Why is my Basiq job still pending?" icon="fa-info-circle">
  <p>A Basiq job may remain pending while the data retrieval process is being completed.</p>

  <p>This can occur when:</p>

  <ul>
    <li>The financial institution is taking longer than expected to respond.</li>
    <li>The Data Holder is experiencing temporary technical issues.</li>
    <li>The requested data is still being processed.</li>
  </ul>

  <p>Applications should monitor the job status and wait for the relevant completion or failure response before assuming that data retrieval has finished.</p>

  <p>For recommended implementation behaviour, refer to <a href="https://api.basiq.io/docs/handling-jobs" target="_blank">Handling Jobs</a>.</p>
</Accordion>

<Accordion title="How does Basiq protect consumer financial data?" icon="fa-info-circle">
    <p>Basiq operates within the Australian Consumer Data Right (CDR) framework and is subject to applicable regulatory obligations for Accredited Data Recipients.</p>

    <p>Financial data access is governed by consumer consent and the applicable CDR requirements.</p>

    <p>Basiq applies security and privacy controls to protect consumer information and support secure data handling across its platform.</p>

    <p>For further information about Basiq's security and privacy practices, refer to the relevant security and privacy documentation or contact Basiq.</p>
</Accordion>

<Accordion title="Does Basiq store consumers' bank login credentials?" icon="fa-info-circle">
    <p>The answer depends on the connection method.</p>

    <p><strong>Open Banking (CDR):</strong> Consumers authenticate directly with their financial institution through its authorisation experience. Basiq does not require consumers to provide their internet banking credentials to Basiq for this CDR authentication process.</p>

    <p><strong>Digital Data Capture (DDC):</strong> This connection method uses the credentials and authentication process associated with the bank's internet banking service.</p>

    <p>For more information, refer to our documentation on <a href="https://api.basiq.io/docs/" target="_blank">Basiq API connectivity</a>.</p>
</Accordion>

<Accordion title="What happens to consumer data when consent is withdrawn?" icon="fa-info-circle">
    <p>When a consumer withdraws their CDR consent, the ADR must cease collecting data under that consent in accordance with the applicable CDR requirements.</p>

    <p>Previously collected data may be subject to deletion, de-identification or other permitted retention requirements depending on the applicable circumstances.</p>

    <p>Revoking consent and deleting previously collected data are separate processes and should not be treated as the same action.</p>

    <p>Applications integrating Basiq should ensure that their data handling processes align with the relevant CDR obligations and Basiq's applicable requirements.</p>
</Accordion>

<Accordion title="What information should I provide when contacting Basiq Support?" icon="fa-info-circle">
  <p>When raising a technical support request, providing relevant diagnostic information helps our team investigate the issue more efficiently.</p>

  <p>Where applicable, include:</p>

  <ul>
    <li>Basiq user ID.</li>
    <li>Connection ID.</li>
    <li>Job ID.</li>
    <li>Financial institution name.</li>
    <li>API endpoint and HTTP response status.</li>
    <li>Error code and response message.</li>
    <li>Date and time the issue occurred, including timezone.</li>
    <li>Relevant request and response details, with sensitive information and credentials removed.</li>
  </ul>

  <p>Never include passwords, authentication credentials, access tokens or other sensitive consumer information in a support request.</p>

  <p>You can contact our team through the Developer Hub support channel.</p>
</Accordion>

## Open Banking, Consent and Privacy

<Accordion title="What is the difference between data collection consent and data disclosure consent?" icon="fa-info-circle">
    <p><strong>Data collection consent</strong> allows an Accredited Data Recipient (ADR) to collect a consumer's data from a Data Holder, such as a bank.</p>

    <p><strong>Data disclosure consent</strong> relates to sharing consumer data with another eligible recipient for an authorised purpose. The disclosure process has its own consent and regulatory requirements.</p>

    <p>The type of consent required depends on how the data is being accessed and used within the application.</p>

    <p>For more information, refer to the <a href="https://www.cdr.gov.au/" target="_blank">Consumer Data Right website</a>.</p>
</Accordion>

<Accordion title="How does Basiq obtain and manage consumer consent?" icon="fa-info-circle">
    <p>Basiq facilitates the Open Banking consent process through the Consumer Data Right (CDR) framework.</p>

    <p>Consumers are directed through an authorisation journey with their selected financial institution, where they authenticate and approve the requested data sharing permissions.</p>

    <p>Once authorised, Basiq can retrieve the permitted financial data in accordance with the consent provided.</p>

    <p>For implementation details, refer to the <a href="https://api.basiq.io/docs" target="_blank">Basiq API documentation</a>.</p>
</Accordion>

<Accordion title="How can a consumer revoke their Open Banking consent?" icon="fa-info-circle">
    <p>Consumers can revoke their consent through the relevant consent management process. This stops the ADR from continuing to access data under that consent.</p>

    <p>Revocation and the subsequent handling of previously collected data are subject to the applicable CDR requirements.</p>

    <p>For more information, refer to the <a href="https://www.cdr.gov.au/" target="_blank">CDR website</a>.</p>
</Accordion>

<Accordion title="What happens when a consumer's consent expires?" icon="fa-info-circle">
    <p>When a consent expires, the associated data access permission is no longer active.</p>

    <p>A consumer may need to complete a new authorisation journey to continue sharing their financial data.</p>

    <p>Your application should handle expired consent states and guide the consumer through the appropriate reconnection process.</p>

    <p>Refer to the <a href="https://api.basiq.io/docs" target="_blank">Basiq API documentation</a> for consent status and management details.</p>
</Accordion>

<Accordion title="Can a consumer renew or extend their consent?" icon="fa-info-circle">
    <p>Consent renewal depends on the applicable CDR requirements and the current consent status.</p>

    <p>Where a new authorisation is required, the consumer must complete the relevant process with their financial institution.</p>

    <p>Applications should monitor consent expiry and provide consumers with a clear way to reconnect when required.</p>

    {/* VALIDATE: Confirm Basiq-supported consent extension and renewal operations, eligibility and API behaviour before publishing. */}
</Accordion>

<Accordion title="Can consumers choose which bank accounts they share?" icon="fa-info-circle">
    <p>The accounts and data a consumer can share depend on the permissions and account-selection options presented during the financial institution's authorisation journey.</p>

    <p>Data access is limited to the accounts and data types authorised by the consumer.</p>

    <p>Available options may vary between financial institutions.</p>
</Accordion>

<Accordion title="Who can access a consumer's financial data?" icon="fa-info-circle">
    <p>Financial data accessed through Open Banking is subject to the consumer's consent and the applicable CDR requirements.</p>

    <p>Access is restricted to authorised parties and permitted purposes under the CDR framework.</p>

    <p>Organisations integrating with Basiq are responsible for ensuring their use of consumer data complies with their applicable legal and regulatory obligations.</p>

    <p>For more information, refer to the <a href="https://www.cdr.gov.au/" target="_blank">CDR website</a>.</p>
</Accordion>

<Accordion title="Does Basiq share consumer financial data with third parties?" icon="fa-info-circle">
    <p>Data sharing is governed by the consumer's consent, the applicable CDR requirements and Basiq's contractual and privacy obligations.</p>

    <p>Where an application uses Basiq to access financial data, the organisation integrating with Basiq must ensure that data is handled and used only for authorised purposes.</p>

    <p>For further information, refer to Basiq's privacy and legal documentation.</p>

    {/* VALIDATE: Confirm current subprocessors, service providers, disclosure arrangements and approved privacy policy links. */}
</Accordion>

<Accordion title="What personal information does Basiq collect from financial institutions?" icon="fa-info-circle">
    <p>The information available through Basiq depends on the data types authorised by the consumer and supported by their financial institution.</p>

    <p>This may include account information, balances, transaction history and other permitted financial data.</p>

    <p>For a detailed breakdown of available data fields, refer to the <a href="https://api.basiq.io/docs/data-structure" target="_blank">Basiq data structure documentation</a>.</p>
</Accordion>

<Accordion title="What happens to collected data when consent is revoked?" icon="fa-info-circle">
    <p>Revoking consent stops further data access under the revoked consent.</p>

    <p>The handling of data that was previously collected is subject to applicable CDR data deletion and retention requirements, including any permitted exceptions.</p>

    <p>Organisations using Basiq should ensure their data handling processes comply with these obligations.</p>

    {/* VALIDATE: Compliance to confirm deletion triggers, retention exceptions, timelines and Basiq's responsibilities versus ADR customer responsibilities. */}
</Accordion>

## Institutions, Accounts and Transactions

<Accordion title="Which financial institutions does Basiq support?" icon="fa-info-circle">
    <p>Basiq supports a range of Australian financial institutions through its available Open Banking and other connector integrations.</p>

    <p>Institution availability and supported data types can vary depending on the connection method and the institution.</p>

    <p>For the latest supported institutions, refer to the <a href="https://api.basiq.io/docs" target="_blank">Basiq API documentation</a> and the institution list available through the API.</p>

    {/* VALIDATE: Add the approved live institution directory link and clarify whether the list includes Open Banking and DDC connectors. */}
</Accordion>

<Accordion title="Can users connect business bank accounts?" icon="fa-info-circle">
    <p>Basiq supports access to financial data where the relevant financial institution and account type are available through the supported connection methods.</p>

    <p>Business account access may depend on the institution's CDR support, account eligibility and the authority of the person completing the authorisation process.</p>

    <p>Not all business account types or institutions necessarily provide the same data coverage.</p>
</Accordion>

<Accordion title="Can users connect joint bank accounts?" icon="fa-info-circle">
    <p>Joint account access depends on the financial institution's Open Banking implementation and the eligibility of the account holder completing the authorisation process.</p>

    <p>The institution determines which accounts can be selected and shared during the authorisation journey.</p>

    {/* VALIDATE: Confirm current Basiq and Data Holder support for joint account scenarios. */}
</Accordion>

<Accordion title="Can users connect trust accounts?" icon="fa-info-circle">
    <p>Trust account availability depends on the financial institution, the account structure and the supported CDR account types.</p>

    <p>Where an account is not available through the institution's authorisation journey, it may not be accessible through Basiq.</p>

    {/* VALIDATE: Confirm supported trust account scenarios and any known institution limitations. */}
</Accordion>

<Accordion title="Can users connect Buy Now Pay Later (BNPL) accounts?" icon="fa-info-circle">
    <p>BNPL data availability depends on whether the relevant provider participates in the applicable data-sharing framework and whether the required data is supported.</p>

    <p>Not all BNPL providers or account types are necessarily available through Basiq.</p>

    {/* VALIDATE: Confirm supported BNPL providers and whether access is through CDR, DDC or another integration. */}
</Accordion>

<Accordion title="Can users access data from closed bank accounts?" icon="fa-info-circle">
    <p>Access to historical information from a closed account depends on the financial institution and the data it makes available through the connection.</p>

    <p>If the institution does not return the closed account or its historical transactions, Basiq cannot independently retrieve that information from the institution.</p>
</Accordion>

<Accordion title="Can users connect multiple banks?" icon="fa-info-circle">
    <p>Yes. An application can support connections to multiple financial institutions, subject to the available institutions and the relevant authorisation requirements.</p>

    <p>Each institution connection may require a separate authorisation journey.</p>

    <p>Your application should manage each connection and its consent status independently.</p>
</Accordion>

<Accordion title="Can users add another bank account after their initial connection?" icon="fa-info-circle">
    <p>Users can initiate an additional institution connection where the application supports the relevant connection flow.</p>

    <p>The user may need to authenticate with the additional financial institution and provide the required consent before data can be accessed.</p>

    <p>Refer to the <a href="https://api.basiq.io/docs" target="_blank">Basiq API documentation</a> for connection implementation details.</p>
</Accordion>

<Accordion title="What happens when a bank is unavailable?" icon="fa-info-circle">
    <p>A financial institution may become temporarily unavailable due to maintenance, service disruptions or technical issues.</p>

    <p>In these situations, a connection or data retrieval job may fail or remain incomplete.</p>

    <p>Basiq provides job statuses and error information to help applications identify and handle these scenarios.</p>

    <p>Refer to the <a href="https://api.basiq.io/docs/handling-jobs" target="_blank">handling jobs documentation</a>.</p>
</Accordion>

<Accordion title="Why might certain bank accounts or account details be missing?" icon="fa-info-circle">
  <p>Missing accounts or account details can occur for several reasons, including:</p>

  <ul>
    <li>The financial institution does not provide the account through its supported API.</li>
    <li>The account type is not eligible for the selected connection method.</li>
    <li>The consumer did not authorise access to the relevant account.</li>
    <li>The institution returned incomplete information.</li>
  </ul>

  <p>Where information is not provided by the financial institution, Basiq cannot guarantee that it will be available in the API response.</p>
</Accordion>

## Connections, Troubleshooting and Data Quality

<Accordion title="How frequently does Basiq retrieve financial data?" icon="fa-info-circle">
    <p>Data retrieval frequency depends on the connection method, the financial institution, the available consent and the application's integration configuration.</p>

    <p>Applications can request data retrieval through the relevant Basiq API operations, subject to applicable restrictions and institution availability.</p>

    <p>Data availability should not be interpreted as a guarantee that every institution will return updated information on every request.</p>

    {/* VALIDATE: Add specific refresh limits, Smart Cache behaviour and any institution-specific restrictions. */}
</Accordion>

<Accordion title="How can I refresh a user's financial data?" icon="fa-info-circle">
    <p>Applications can initiate data retrieval using the relevant Basiq API operations.</p>

    <p>The returned data depends on the connection status, consent permissions, institution availability and applicable refresh behaviour.</p>

    <p>Refer to the <a href="https://api.basiq.io/docs" target="_blank">Basiq API documentation</a> for the relevant endpoints and implementation guidance.</p>
</Accordion>

<Accordion title="What is Smart Cache?" icon="fa-info-circle">
    <p>Smart Cache relates to Basiq's data retrieval and caching behaviour, helping manage the availability of previously retrieved data and requests for updated information.</p>

    <p>Applications should understand the freshness of returned data and avoid assuming that every API request triggers a new retrieval from the financial institution.</p>

    {/* VALIDATE: Insert the approved explanation of Smart Cache, cache expiry, refresh behaviour and relevant API parameters. */}
</Accordion>

<Accordion title="Why are some transactions missing?" icon="fa-info-circle">
  <p>Missing transactions can occur when the financial institution does not return the complete transaction history or when the requested data is not available through the connection.</p>

  <p>Possible causes include:</p>

  <ul>
    <li>Institution-side delays or incomplete responses.</li>
    <li>Historical data limitations imposed by the institution.</li>
    <li>Transactions that have not yet been posted.</li>
    <li>Temporary connection or retrieval issues.</li>
  </ul>

  <p>For more information, refer to the <a href="https://api.basiq.io/docs/handling-jobs" target="_blank">handling jobs documentation</a>.</p>
</Accordion>

<Accordion title="Why are account balances different from internet banking?" icon="fa-info-circle">
    <p>Balances returned through Basiq may differ from the balance currently displayed in internet banking.</p>

    <p>This can happen because of differences in data refresh timing, pending transactions, institution processing delays or the balance type being returned.</p>

    <p>Applications should consider the balance type and the timestamp of the retrieved data when displaying balances to users.</p>

    {/* VALIDATE: Confirm available balance fields and the approved explanation of balance types in Basiq's data model. */}
</Accordion>

<Accordion title="Why do some transactions appear as pending?" icon="fa-info-circle">
    <p>Pending transactions are transactions that have been initiated but have not yet been fully processed or posted by the financial institution.</p>

    <p>Depending on the institution, pending transactions may later be updated, replaced by posted transactions or removed.</p>

    <p>The transaction status and available date fields may differ depending on the connection method and the information supplied by the institution.</p>
</Accordion>

<Accordion title="Why does a connection become invalid?" icon="fa-info-circle">
  <p>A connection may become invalid when the financial institution requires the user to authenticate again or when the existing authorisation can no longer be used.</p>

  <p>Possible reasons include:</p>

  <ul>
    <li>Expired or revoked consent.</li>
    <li>Changes to the user's online banking access.</li>
    <li>Institution-side security requirements.</li>
    <li>Changes to the connection or authentication process.</li>
  </ul>

  <p>Applications should handle invalid connection states and guide users through the appropriate reconnection process.</p>
</Accordion>

<Accordion title="What happens when a user abandons the bank authorisation process?" icon="fa-info-circle">
    <p>If a user leaves or cancels the authorisation journey before completing it, the required consent may not be established.</p>

    <p>In that case, the application may not be able to retrieve the requested financial data.</p>

    <p>Your application should handle incomplete or unsuccessful connection attempts and allow the user to try again where appropriate.</p>
</Accordion>

<Accordion title="Why does a bank require the user to reauthenticate?" icon="fa-info-circle">
    <p>Financial institutions may require users to authenticate again as part of their security and consent management processes.</p>

    <p>This may happen when consent expires, access is revoked or the institution requires additional verification.</p>

    <p>The user must complete the required authorisation process before data access can continue.</p>
</Accordion>

<Accordion title="How do I troubleshoot a failed connection?" icon="fa-info-circle">
  <p>When a connection fails, first review the connection status, job response and associated error information.</p>

  <p>Common causes include:</p>

  <ul>
    <li>Temporary financial institution outages.</li>
    <li>Authentication or authorisation failures.</li>
    <li>Expired or revoked consent.</li>
    <li>Incomplete responses from the financial institution.</li>
    <li>Unsupported account types or institution limitations.</li>
  </ul>

  <p>Refer to Basiq's <a href="https://api.basiq.io/docs/error-codes" target="_blank">error codes</a> and <a href="https://api.basiq.io/docs/handling-jobs" target="_blank">handling jobs documentation</a>.</p>
</Accordion>

## API, Integrations, Reporting and Platform Management

<Accordion title="How do I configure Basiq's Consent UI?" icon="fa-info-circle">
    <p>Basiq provides integration options to support the consumer authorisation and connection experience.</p>

    <p>The configuration required depends on the integration approach and the Basiq products enabled for your organisation.</p>

    <p>Refer to the <a href="https://api.basiq.io/docs" target="_blank">Basiq Developer Hub</a> for implementation guidance.</p>

    {/* VALIDATE: Add the exact Consent UI configuration guide and supported integration options. */}
</Accordion>

<Accordion title="Can I customise the consent experience with my own branding?" icon="fa-info-circle">
    <p>Branding and customisation options depend on the Basiq integration method and the components used in the connection journey.</p>

    <p>Any customisation must continue to meet applicable CDR requirements and financial institution authorisation standards.</p>

    {/* VALIDATE: Confirm available branding controls, supported UI components and restrictions. */}
</Accordion>

<Accordion title="How do I configure available financial institutions?" icon="fa-info-circle">
    <p>Available institutions depend on the connection methods and products enabled for your Basiq integration.</p>

    <p>Applications can use the relevant Basiq API functionality to retrieve institution information and present supported options to users.</p>

    <p>Refer to the <a href="https://api.basiq.io/docs" target="_blank">Basiq API documentation</a> for institution-related endpoints.</p>

    {/* VALIDATE: Add the exact institution configuration endpoint and any dashboard configuration instructions. */}
</Accordion>

<Accordion title="How do I receive webhook notifications from Basiq?" icon="fa-info-circle">
    <p>Basiq supports webhook events that allow applications to receive notifications about relevant changes and activities.</p>

    <p>Webhooks can help applications respond to events without continuously polling the API.</p>

    <p>Refer to the <a href="https://api.basiq.io/docs" target="_blank">Basiq Developer Hub</a> for supported events, configuration and implementation guidance.</p>

    {/* VALIDATE: Add the current webhook setup guide, event catalogue, authentication requirements and retry behaviour. */}
</Accordion>

<Accordion title="What connection and consent events are available?" icon="fa-info-circle">
    <p>Basiq provides event and status information to help applications monitor user connections and consent activity.</p>

    <p>The events available depend on the API functionality and webhook configuration used by your integration.</p>

    <p>Refer to the <a href="https://api.basiq.io/docs" target="_blank">Basiq API documentation</a> for the current event definitions.</p>

    {/* VALIDATE: Publish the approved list of events, including relevant consent and connection lifecycle events. */}
</Accordion>

<Accordion title="How can I monitor connector availability?" icon="fa-info-circle">
    <p>Connector availability can vary depending on the financial institution and its underlying services.</p>

    <p>Applications should monitor connection and job statuses and handle institution-side errors appropriately.</p>

    <p>For service incidents and availability information, refer to Basiq's designated service status channel.</p>

    {/* VALIDATE: Insert the official Basiq status page URL and explain whether connector-level availability is exposed. */}
</Accordion>

<Accordion title="How do I monitor API and connection performance?" icon="fa-info-circle">
    <p>Applications should monitor API responses, job completion statuses, error codes and relevant connection events.</p>

    <p>This information can help identify integration issues, institution-side disruptions and changes in connection performance.</p>

    <p>Refer to the <a href="https://api.basiq.io/docs" target="_blank">Basiq Developer Hub</a> for available API and event information.</p>

    {/* VALIDATE: Confirm which metrics, dashboards, logs and reporting features are available to customers. */}
</Accordion>

<Accordion title="What reporting and consumer affordability products does Basiq offer?" icon="fa-info-circle">
    <p>Basiq offers financial data capabilities that can support use cases such as consumer affordability assessment and financial insights.</p>

    <p>Product availability, functionality and access may depend on your organisation's agreement and enabled products.</p>

    <p>Contact your Basiq representative to discuss available products and requirements.</p>

    {/* VALIDATE: Add current product names, supported reports, required inputs, outputs and product documentation links. */}
</Accordion>

<Accordion title="How do I migrate from API v2 to API v3?" icon="fa-info-circle">
    <p>Basiq API v3 provides support for both Digital Data Capture (DDC) and Consumer Data Right (CDR) connection methods.</p>

    <p>API v2 supports DDC only.</p>

    <p>When migrating, review the relevant API changes, data structures, authentication requirements and connection workflows before updating your integration.</p>

    <p>Refer to the <a href="https://api.basiq.io/docs" target="_blank">Basiq Developer Hub</a> for the current API documentation.</p>
</Accordion>

<Accordion title="How do I move from DDC to Open Banking?" icon="fa-info-circle">
    <p>Open Banking uses the Consumer Data Right framework to enable consumers to authorise financial institutions to share their data through secure APIs.</p>

    <p>Unlike DDC, Open Banking does not require consumers to provide their internet banking credentials to the ADR.</p>

    <p>Moving from DDC to Open Banking requires your application to support the relevant CDR consent and authorisation workflows.</p>

    <p>Refer to the <a href="https://api.basiq.io/docs" target="_blank">Basiq Developer Hub</a> for implementation guidance.</p>
</Accordion>

<Accordion title="How do I get production access?" icon="fa-info-circle">
    <p>Production access depends on your organisation's onboarding, account configuration and applicable commercial and compliance requirements.</p>

    <p>Contact your Basiq representative or Support team to discuss production access and any required steps.</p>

    <p>For development and integration testing, refer to the <a href="https://api.basiq.io/docs/sandbox" target="_blank">Basiq sandbox documentation</a>.</p>

    {/* VALIDATE: Confirm current production onboarding process, approval requirements and support contact details. */}
</Accordion>

</Accordion>
