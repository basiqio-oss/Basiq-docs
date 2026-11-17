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
# Frequently asked questions


<Image src="https://files.readme.io/6187bf8ac3419d7f0b37f637f292af736f81f1489917d737d444936e52ecf3a8-82119ec-FAQ_Header.jpg" alt="Frequently asked questions" align="center" />

When incorporating the Basiq API into your application, it's essential to follow best practices that contribute to the success of your implementation. These practices span security, user experience (UX), scalability and more.

Explore the frequently asked questions below for guidance on the Basiq platform.

## Getting Started with Open Banking and Basiq

<Accordion title="What is Open Banking?" icon="far fa-circle-info">
    <p><strong>Open Banking (CDR):</strong> Open Banking, also known as the Consumer Data Right (CDR) in Australia, is a framework that allows consumers to authorise the sharing of their financial data through secure APIs. Regulated by the Australian Government, it requires participating financial institutions to share data through APIs specifically built for this purpose.</p>

    <p>Unlike Digital Data Capture (DDC), CDR does not require consumers to share their internet banking credentials with the Accredited Data Recipient. It provides a standardised and regulated way to access financial data.</p>
</Accordion>

<Accordion title="What is a DDC Connector?" icon="far fa-circle-info">
    <p><strong>Digital Data Capture (DDC)</strong> is a method of aggregating financial data that involves using the credentials and authentication process associated with a bank's internet banking service. The connection accesses the bank's online banking portal to retrieve a user's accounts and transactions.</p>

    <p>DDC can be affected by changes to a bank's website, authentication process or security controls.</p>

    <p><strong>API Versions:</strong> Version 2 of the Basiq API supports DDC only. Version 3 supports both DDC and CDR connection methods.</p>
</Accordion>

<Accordion title="What is a Data Holder (DH) and an Accredited Data Recipient (ADR)?" icon="far fa-circle-info">
    <p>A <strong>Data Holder (DH)</strong> is an organisation that holds consumer data, such as a bank. Under the CDR framework, consumers can authorise a Data Holder to share their data with an eligible recipient.</p>

    <p>An <strong>Accredited Data Recipient (ADR)</strong> is an organisation accredited to receive consumer data under the CDR framework, subject to the consumer's consent and applicable regulatory requirements.</p>

    <p>Basiq operates as an ADR within the CDR ecosystem.</p>

    <p>For a list of registered participants, refer to the government's <a href="https://www.cdr.gov.au/find-a-provider" target="_blank" rel="noopener noreferrer">CDR provider directory</a>.</p>
</Accordion>

<Accordion title="What is the difference between DDC and Open Banking?" icon="far fa-circle-info">
    <p><strong>DDC:</strong> Uses the bank's internet banking connection and authentication process to retrieve financial data.</p>

    <p><strong>Open Banking (CDR):</strong> Allows consumers to authenticate directly with their financial institution and authorise data sharing through secure APIs.</p>

    <p>Open Banking follows a regulated, standardised framework and does not require consumers to share their internet banking credentials with the ADR.</p>

    <p>The connection method available depends on the financial institution, account type and Basiq integration.</p>
</Accordion>

<Accordion title="What data does Basiq retrieve from users' bank accounts?" icon="far fa-circle-info">
  <p>Basiq can retrieve financial information made available by the financial institution and authorised by the consumer. This may include:</p>

  <ul>
    <li>Account information, such as account type, number and balance.</li>
    <li>Transaction history, including dates, descriptions and amounts.</li>
    <li>Pending and posted transactions.</li>
    <li>Other permitted financial data supported by the institution and connection method.</li>
  </ul>

  <p>The data available depends on the consumer's authorisation, the institution and the connection method.</p>

  <p>For a full breakdown of available fields, refer to the <a href="https://api.basiq.io/docs/consent-scopes" target="_blank" rel="noopener noreferrer">Basiq data structure documentation</a>.</p>
</Accordion>

<Accordion title="How do I test my integration with Basiq?" icon="far fa-circle-info">
  <p>Use the Basiq sandbox environment to test your integration without accessing real consumer financial data.</p>

  <p>The sandbox allows you to simulate user interactions, API calls and different response scenarios to validate your implementation.</p>

  <p>For setup instructions, refer to the <a href="https://api.basiq.io/reference/testing" target="_blank" rel="noopener noreferrer">sandbox documentation</a>.</p>
</Accordion>

## Consent, Privacy and Security

<Accordion title="How does the Open Banking consent process work?" icon="far fa-circle-info">
  <p>Open Banking allows consumers to authorise an Accredited Data Recipient (ADR) to access their financial data through the Consumer Data Right (CDR) framework.</p>

  <p>When connecting an account through Basiq:</p>

  <ul>
    <li>The consumer selects their financial institution.</li>
    <li>The consumer is redirected to the bank's authentication experience.</li>
    <li>The consumer authenticates directly with their bank.</li>
    <li>The consumer reviews and authorises the requested data-sharing permissions.</li>
    <li>Once consent is established, Basiq can retrieve the authorised data through the institution's CDR APIs.</li>
  </ul>

  <p>The authentication and authorisation experience is managed by the Data Holder. Basiq does not control the bank's individual authentication requirements or user interface.</p>
</Accordion>

<Accordion title="What is the difference between data collection consent and data disclosure consent?" icon="far fa-circle-info">
    <p><strong>Data collection consent</strong> allows an Accredited Data Recipient (ADR) to collect a consumer's data from a Data Holder, such as a bank, under the Consumer Data Right (CDR) framework.</p>

    <p><strong>Data disclosure consent</strong> relates to the authorised sharing of consumer data by an ADR with another eligible recipient, where the relevant CDR disclosure arrangements apply.</p>

    <p>These are separate consent arrangements with different purposes and obligations. The applicable requirements depend on the data-sharing arrangement and the role of each participant.</p>

    <p>For further information, refer to the <a href="https://www.cdr.gov.au/" target="_blank" rel="noopener noreferrer">Consumer Data Right website</a>.</p>
</Accordion>

<Accordion title="How long does an Open Banking consent remain active?" icon="far fa-circle-info">
    <p>Open Banking consents are subject to the consent duration and expiry requirements under the Consumer Data Right (CDR) Rules.</p>

    <p>The applicable duration depends on the type of consent and the relevant regulatory requirements.</p>

    <p>Applications integrating Basiq should monitor consent status and expiry information and provide appropriate notifications to consumers where required.</p>

    <p>For further information, refer to the <a href="https://www.cdr.gov.au/" target="_blank" rel="noopener noreferrer">CDR Rules and regulatory guidance</a>.</p>
</Accordion>

<Accordion title="Can a consumer revoke their Open Banking consent?" icon="far fa-circle-info">
    <p>Yes. Consumers can withdraw their CDR consent through the applicable consent management process.</p>

    <p>When consent is withdrawn, the ADR must cease collecting data under that consent in accordance with the applicable CDR requirements.</p>

    <p>Revocation may also trigger obligations relating to the handling, deletion or de-identification of previously collected data, depending on the applicable regulatory requirements and circumstances.</p>

    <p>Applications should provide consumers with a clear way to manage their consents and understand the impact of withdrawing access.</p>

    <p>For further information, refer to the <a href="https://www.cdr.gov.au/" target="_blank" rel="noopener noreferrer">CDR website</a>.</p>
</Accordion>

<Accordion title="What happens when an Open Banking consent expires?" icon="far fa-circle-info">
    <p>When a CDR consent expires, the ADR can no longer rely on that expired consent to continue collecting data.</p>

    <p>The consumer may need to complete a new authorisation process to re-establish access to their financial information.</p>

    <p>Applications should monitor consent expiry and communicate any required actions to consumers before access is interrupted.</p>
</Accordion>

<Accordion title="Can a consumer renew or extend their consent?" icon="far fa-circle-info">
    <p>Consent renewal depends on the applicable CDR requirements and the current consent status.</p>

    <p>Where a new authorisation is required, the consumer must complete the relevant process with their financial institution.</p>

    <p>Applications should monitor consent expiry and provide consumers with a clear way to reconnect when required.</p>

  {/* VALIDATE: Confirm Basiq-supported consent extension and renewal operations, eligibility and API behaviour before publishing. */}
</Accordion>

<Accordion title="Can consumers choose which bank accounts they share?" icon="far fa-circle-info">
    <p>The accounts and data a consumer can share depend on the permissions and account-selection options presented during the financial institution's authorisation journey.</p>

    <p>Data access is limited to the accounts and data types authorised by the consumer.</p>

    <p>Available options may vary between financial institutions.</p>
</Accordion>

<Accordion title="Who can access a consumer's financial data?" icon="far fa-circle-info">
    <p>Financial data accessed through Open Banking is subject to the consumer's consent and the applicable CDR requirements.</p>

    <p>Access is restricted to authorised parties and permitted purposes under the CDR framework.</p>

    <p>Organisations integrating with Basiq are responsible for ensuring their use of consumer data complies with their applicable legal and regulatory obligations.</p>

    <p>For more information, refer to the <a href="https://www.cdr.gov.au/" target="_blank" rel="noopener noreferrer">CDR website</a>.</p>
</Accordion>

<Accordion title="Does Basiq share consumer financial data with third parties?" icon="far fa-circle-info">
    <p>Data sharing is governed by the consumer's consent, the applicable CDR requirements and Basiq's contractual and privacy obligations.</p>

    <p>Organisations integrating with Basiq must ensure consumer data is handled and used only for authorised purposes.</p>

    <p>For further information, refer to Basiq's privacy and legal documentation.</p>

  {/* VALIDATE: Confirm current subprocessors, service providers, disclosure arrangements and approved privacy policy links. */}
</Accordion>

<Accordion title="How does Basiq protect consumer financial data?" icon="far fa-circle-info">
    <p>Basiq operates within the Australian Consumer Data Right (CDR) framework and is subject to applicable regulatory obligations for Accredited Data Recipients.</p>

    <p>Financial data access is governed by consumer consent and the applicable CDR requirements.</p>

    <p>Basiq applies security and privacy controls to protect consumer information and support secure data handling across its platform.</p>

    <p>For further information about Basiq's security and privacy practices, refer to the relevant security and privacy documentation or contact Basiq.</p>
</Accordion>

<Accordion title="Does Basiq store consumers' bank login credentials?" icon="far fa-circle-info">
  <p>The answer depends on the connection method.</p>

  <p><strong>Open Banking (CDR):</strong> Consumers authenticate directly with their financial institution through its authorisation experience. Basiq does not require consumers to provide their internet banking credentials to Basiq for this CDR authentication process.</p>

  <p><strong>Digital Data Capture (DDC):</strong> This connection method uses the credentials and authentication process associated with the bank's internet banking service.</p>

  <p>For more information, refer to the <a href="https://docs.basiq.io/en/articles/5298389-securely-connecting-your-data-with-basiq" target="_blank" rel="noopener noreferrer">Basiq API documentation</a>.</p>
</Accordion>

<Accordion title="What happens to consumer data when consent is withdrawn?" icon="far fa-circle-info">
    <p>When a consumer withdraws their CDR consent, the ADR must cease collecting data under that consent in accordance with the applicable CDR requirements.</p>

    <p>Previously collected data may be subject to deletion, de-identification or other permitted retention requirements depending on the applicable circumstances.</p>

    <p>Revoking consent and deleting previously collected data are separate processes and should not be treated as the same action.</p>

    <p>Organisations using Basiq should ensure their data handling processes comply with the relevant CDR obligations.</p>

  {/* VALIDATE: Compliance to confirm deletion triggers, retention exceptions, timelines and Basiq's responsibilities versus ADR customer responsibilities. */}

  </Accordion>

  ## Institutions and Account Connectivity

  <Accordion title="Which financial institutions does Basiq support?" icon="far fa-circle-info">
      <p>Basiq supports a range of Australian financial institutions through its available Open Banking and other connector integrations.</p>

      <p>Institution availability, connection methods and supported data types can vary depending on the institution and account type.</p>

      <p>For the latest supported institutions, refer to the <a href="https://dashboard.basiq.io/status" target="_blank" rel="noopener noreferrer">Basiq API documentation</a> and the institution list available through the API.</p>

    {/* VALIDATE: Add the approved live institution directory link and clarify whether the list includes Open Banking and DDC connectors. */}
  </Accordion>

  <Accordion title="Why can't I find my bank in the institution list?" icon="far fa-circle-info">
    <p>If a financial institution is not appearing in the available institution list, there may be several reasons:</p>

    <ul>
      <li>The institution is not currently supported through the selected connection method.</li>
      <li>The institution may not provide the required CDR functionality.</li>
      <li>The institution may not support the account type being connected.</li>
      <li>The institution may have changed its connectivity or participation status.</li>
    </ul>

    <p>Check the available institution list and connection method in your Basiq integration. If the institution should be available but cannot be found, contact Basiq Support for assistance.</p>
  </Accordion>

  <Accordion title="Why is my financial institution showing as unavailable?" icon="far fa-circle-info">
    <p>An institution may temporarily become unavailable due to technical issues, scheduled maintenance or disruptions within the Data Holder's infrastructure.</p>

    <p>Basiq relies on financial institutions to respond to data requests. If an institution cannot process a request, the connection or data retrieval process may fail.</p>

    <p>We recommend:</p>

    <ul>
      <li>Checking whether the institution is experiencing an outage.</li>
      <li>Reviewing the API response and associated error code.</li>
      <li>Retrying the request when the institution becomes available.</li>
      <li>Providing clear communication to the end user.</li>
    </ul>

    <p>For further information, refer to our <a href="https://api.basiq.io/docs/errors" target="_blank" rel="noopener noreferrer">error code documentation</a>.</p>
  </Accordion>

  <Accordion title="Does Basiq support business bank accounts?" icon="far fa-circle-info">
    <p>Basiq supports access to financial data where the relevant financial institution and account type are available through the supported connection methods.</p>

    <p>Business account access may depend on the institution's CDR support, account eligibility and the authority of the person completing the authorisation process.</p>

    <p>Not all business account types or institutions necessarily provide the same data coverage.</p>
  </Accordion>

  <Accordion title="Can consumers connect joint bank accounts?" icon="far fa-circle-info">
      <p>Joint account access depends on the financial institution's Open Banking implementation and the eligibility of the account holder completing the authorisation process.</p>

      <p>The institution determines which accounts can be selected and shared during the authorisation journey.</p>

      <p>Not all joint accounts are necessarily available through every financial institution.</p>

    {/* VALIDATE: Confirm current Basiq and Data Holder support for joint account scenarios. */}
  </Accordion>

  <Accordion title="Can users connect trust accounts?" icon="far fa-circle-info">
      <p>Trust account availability depends on the financial institution, the account structure and the supported CDR account types.</p>

      <p>Where an account is not available through the institution's authorisation journey, it may not be accessible through Basiq.</p>

    {/* VALIDATE: Confirm supported trust account scenarios and any known institution limitations. */}
  </Accordion>

  <Accordion title="Can users access data from closed bank accounts?" icon="far fa-circle-info">
    <p>Access to historical information from a closed account depends on the financial institution and the data it makes available through the connection.</p>

    <p>If the institution does not return the closed account or its historical transactions, Basiq cannot independently retrieve that information from the institution.</p>
  </Accordion>

  <Accordion title="Can consumers connect multiple bank accounts and institutions?" icon="far fa-circle-info">
    <p>Yes. An application can support connections to multiple eligible accounts and financial institutions, subject to the institutions and account types supported.</p>

    <p>Each institution connection may require a separate authorisation journey.</p>

    <p>Your application should manage each connection and its associated consent status independently.</p>
  </Accordion>

  <Accordion title="Can users add another bank account after their initial connection?" icon="far fa-circle-info">
    <p>Users can initiate an additional institution connection where the application supports the relevant connection flow.</p>

    <p>The user may need to authenticate with the additional financial institution and provide the required consent before data can be accessed.</p>

    <p>Refer to the <a href="https://api.basiq.io/docs/consent-parameters#connectionid-parameter" target="_blank" rel="noopener noreferrer">Basiq API documentation</a> for connection implementation details.</p>
  </Accordion>

  ## Transactions and Financial Data

  <Accordion title="How frequently does Basiq retrieve financial data?" icon="far fa-circle-info">
      <p>Data retrieval frequency depends on the connection method, the Data Holder's capabilities, applicable CDR requirements and the integration's data retrieval process.</p>

      <p>For Open Banking, Basiq retrieves data through the institution's CDR APIs when a permitted data retrieval request is made.</p>

      <p>Data availability and freshness depend on the information provided by the Data Holder. Basiq cannot guarantee that every institution will return updated information at the same frequency.</p>

      <p>Applications should account for potential differences in data freshness when displaying account and transaction information.</p>

    {/* VALIDATE: Confirm specific refresh limits, Smart Cache behaviour and any institution-specific restrictions. */}
  </Accordion>

  <Accordion title="How can I refresh a user's financial data?" icon="far fa-circle-info">
    <p>Applications can initiate data retrieval using the relevant Basiq API operations.</p>

    <p>The returned data depends on the connection status, consent permissions, institution availability and applicable refresh behaviour.</p>

    <p>Refer to the <a href="https://api.basiq.io/docs/platform-connections#actions-on-a-connection" target="_blank" rel="noopener noreferrer">Basiq API documentation</a> for the relevant endpoints and implementation guidance.</p>
  </Accordion>

  <Accordion title="What is Smart Cache?" icon="far fa-circle-info">
      <p>Smart Cache relates to Basiq's data retrieval and caching behaviour, helping manage the availability of previously retrieved data and requests for updated information.</p>

      <p>Applications should understand the freshness of returned data and avoid assuming that every API request triggers a new retrieval from the financial institution.</p>

    {/* VALIDATE: Insert the approved explanation of Smart Cache, cache expiry, refresh behaviour and relevant API parameters. */}
  </Accordion>

  <Accordion title="Why hasn't my account information been updated?" icon="far fa-circle-info">
    <p>Account information may not reflect the latest information available through internet banking for several reasons:</p>

    <ul>
      <li>The Data Holder has not yet provided updated account information.</li>
      <li>The latest data retrieval request has not completed successfully.</li>
      <li>The institution is experiencing a temporary service disruption.</li>
      <li>The account information returned by the institution has not changed.</li>
    </ul>

    <p>Review the latest connection and job status to determine whether the data retrieval request completed successfully.</p>

    <p>For more information, refer to our <a href="https://api.basiq.io/reference/getjobs" target="_blank" rel="noopener noreferrer">job handling documentation</a>.</p>
  </Accordion>

  <Accordion title="How far back can Basiq retrieve transaction history?" icon="far fa-circle-info">
    <p>The available transaction history depends on the financial institution, account type, connection method and the historical data made available by the Data Holder.</p>

    <p>Different institutions may provide different transaction history periods. As a result, the amount of historical data available may vary between accounts.</p>

    <p>Applications should not assume that all institutions provide the same historical transaction coverage.</p>

    <p>For information about the transaction fields returned by Basiq, refer to our <a href="https://api.basiq.io/docs/basiq-customise-ui#customisable-fields" target="_blank" rel="noopener noreferrer">data structure documentation</a>.</p>
  </Accordion>

  <Accordion title="Why are some transactions missing from my account?" icon="far fa-circle-info">
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

  <Accordion title="What is the difference between pending and posted transactions?" icon="far fa-circle-info">
    <p><strong>Pending transactions:</strong> Transactions that have been initiated or authorised but have not yet been fully processed by the financial institution.</p>

    <p><strong>Posted transactions:</strong> Transactions that have been processed and recorded against the account by the financial institution.</p>

    <p>Pending transactions may change, disappear or be replaced by posted transactions as the bank completes processing.</p>

    <p>The availability and representation of pending and posted transactions depend on the information provided by the Data Holder.</p>
  </Accordion>
</Accordion>

<Accordion title="What are Web and Open Banking transaction date/times?" icon="far fa-circle-info">
  <h2>Web Connectors:</h2>

  <p>Web connectors provide the <code>transaction.Date</code> field. A timestamp is not available from the connector.</p>

  <p>Basiq stores the transaction date and appends midnight time when compiling the <code>user_transactions_get</code> response. The resulting timestamp uses <code>00:00:00Z</code>.</p>

  <h2>Open Banking (CDR) Connectors:</h2>

  <p>Open Banking connectors provide a full datetime through <code>obTransactionDateTime</code>.</p>

  <ul>
    <li><code>postingDateTime</code> is used for posted transactions.</li>
    <li><code>executionDateTime</code> is used for pending transactions.</li>
  </ul>

  <p>Basiq normalises the datetime to UTC when compiling the transaction response. If <code>obTransactionDateTime</code> cannot be validated, midnight is added to the transaction date.</p>

  <h2>Exposing Data via GET /transactions Endpoint:</h2>

  <p>For posted transactions, Basiq returns <code>postDate</code>. For pending transactions, Basiq returns <code>transactionDate</code>.</p>

  <p>CDR uses RFC3339 datetime formatting, which includes the relationship to Coordinated Universal Time (UTC). Where a Data Holder provides a UTC offset, Basiq normalises the datetime to UTC. For example, <code>2021-11-19T00:00:00+11:00</code> becomes <code>2021-11-18T13:00:00Z</code>.</p>

  <p>All Open Banking datetimes are represented in UTC. Basiq does not convert these values into each consumer's local timezone.</p>

  <p>If a Data Holder appends <code>00:00:00Z</code> without correctly converting the original local date and time to UTC, the resulting timestamp may not reflect the actual transaction time. Basiq raises these behaviours with the relevant Data Holder through the CDR Portal.</p>
</Accordion>

## Connections and Troubleshooting

<Accordion title="Why does a connection become invalid or require re-authentication?" icon="far fa-circle-info">
  <p>A connection may become invalid when the financial institution requires the user to authenticate again or when the existing authorisation can no longer be used.</p>

  <p>Possible reasons include:</p>

  <ul>
    <li>Expired or revoked consent.</li>
    <li>Changes to the user's online banking access.</li>
    <li>Institution-side security requirements.</li>
    <li>Changes to the connection or authentication process.</li>
    <li>An expired Web (DDC) session or additional authentication requirements.</li>
  </ul>

  <p>For CDR connections, authentication and consent are managed through the Data Holder's authorisation experience. For Web (DDC) connections, changes to the bank's authentication process or expired sessions may require the consumer to reconnect.</p>

  <p>The authentication experience and requirements are determined by the financial institution. Applications should handle invalid connection states and guide users through the appropriate reconnection process.</p>
</Accordion>

<Accordion title="What happens when a user abandons the bank authorisation process?" icon="far fa-circle-info">
    <p>If a user leaves or cancels the authorisation journey before completing it, the required consent may not be established.</p>

    <p>In that case, the application may not be able to retrieve the requested financial data.</p>

    <p>Your application should handle incomplete or unsuccessful connection attempts and allow the user to try again where appropriate.</p>
</Accordion>

<Accordion title="Why am I not receiving an OTP from my bank?" icon="far fa-circle-info">
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

<Accordion title="Why is my Basiq job still pending?" icon="far fa-circle-info">
  <p>A Basiq job may remain pending while the data retrieval process is being completed.</p>

  <p>This can occur when:</p>

  <ul>
    <li>The financial institution is taking longer than expected to respond.</li>
    <li>The Data Holder is experiencing temporary technical issues.</li>
    <li>The requested data is still being processed.</li>
  </ul>

  <p>Applications should monitor the job status and wait for the relevant completion or failure response before assuming that data retrieval has finished.</p>

  <p>For recommended implementation behaviour, refer to <a href="https://api.basiq.io/reference/getjobs" target="_blank" rel="noopener noreferrer">Handling Jobs</a>.</p>
</Accordion>

<Accordion title="Why do I have a 'missing bank data' error in my job output?" icon="far fa-circle-info">
  <p>The output can show missing data because your user's bank failed to provide the requested information. This can happen for various reasons, including:</p>

  <ul>
    <li>The bank's response to our API is incomplete or contains missing data.</li>
    <li>Your user's online banking session expired or was terminated unexpectedly.</li>
    <li>The bank's technical infrastructure is experiencing downtime or disruptions.</li>
  </ul>

  <p>Further details are available in the <a href="https://api.basiq.io/docs/errors#consent-ui-and-bank-errors" target="_blank" rel="noopener noreferrer">error code documentation</a>.</p>
</Accordion>

<Accordion title="What does the job error 'Service is currently unavailable. Please try again later.' mean?" icon="far fa-circle-info">
  <p>This error indicates that there was a problem retrieving your user's data from their bank. It does not necessarily indicate a problem with Basiq.</p>

  <p>The service-unavailable error tells your application that the financial institution was unable to return data in response to a request.</p>

  <p>Refer to the <a href="https://api.basiq.io/reference/getjobs" target="_blank" rel="noopener noreferrer">handling jobs documentation</a> for recommended actions and user communications.</p>
</Accordion>

<Accordion title="How do I troubleshoot a failed connection?" icon="far fa-circle-info">
  <p>When a connection fails, first review the connection status, job response and associated error information.</p>

  <p>Common causes include:</p>

  <ul>
    <li>Temporary financial institution outages.</li>
    <li>Authentication or authorisation failures.</li>
    <li>Expired or revoked consent.</li>
    <li>Incomplete responses from the financial institution.</li>
    <li>Unsupported account types or institution limitations.</li>
  </ul>

  <p>Refer to Basiq's <a href="https://api.basiq.io/docs/error-codes" target="_blank" rel="noopener noreferrer">error codes</a> and <a href="https://api.basiq.io/reference/getjobs" target="_blank" rel="noopener noreferrer">handling jobs documentation</a>.</p>
</Accordion>

<Accordion title="What should I do if my API request returns an error?" icon="far fa-circle-info">
  <p>If your request returns an error, review the error code and accompanying message to understand the issue.</p>

  <p>The <a href="https://api.basiq.io/docs/errors" target="_blank" rel="noopener noreferrer">error code documentation</a> provides explanations for each error code and guidance on how to handle them.</p>

  <p>Common issues include authentication errors, incorrect request formats or temporary issues with the bank's API.</p>

  <p>Ensure your implementation follows Basiq's guidelines for error handling and data retrieval to improve user experience and service reliability.</p>
</Accordion>

<Accordion title="What information should I provide when contacting Basiq Support?" icon="far fa-circle-info">
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

## API, Integrations and Platform Management

<Accordion title="How do I configure Basiq's Consent UI?" icon="far fa-circle-info">
    <p>Basiq provides integration options to support the consumer authorisation and connection experience.</p>

    <p>The configuration required depends on the integration approach and the Basiq products enabled for your organisation.</p>

    <p>Refer to the <a href="https://api.basiq.io/docs/basiq-customise-ui" target="_blank" rel="noopener noreferrer">Basiq Developer Hub</a> for implementation guidance.</p>

  {/* VALIDATE: Add the exact Consent UI configuration guide and supported integration options. */}
</Accordion>

<Accordion title="Can I customise the consent experience with my own branding?" icon="far fa-circle-info">
    <p>Branding and customisation options depend on the Basiq integration method and the components used in the connection journey.</p>

    <p>Any customisation must continue to meet applicable CDR requirements and financial institution authorisation standards.</p>

  {/* VALIDATE: Confirm available branding controls, supported UI components and restrictions. */}
</Accordion>

<Accordion title="How do I configure available financial institutions?" icon="far fa-circle-info">
    <p>Available institutions depend on the connection methods and products enabled for your Basiq integration.</p>

    <p>Applications can use the relevant Basiq API functionality to retrieve institution information and present supported options to users.</p>

    <p>Refer to the <a href="https://api.basiq.io/docs/connecting-business-accounts-via-cdr" target="_blank" rel="noopener noreferrer">Basiq API documentation</a> for institution-related endpoints.</p>

  {/* VALIDATE: Add the exact institution configuration endpoint and any dashboard configuration instructions. */}
</Accordion>

<Accordion title="How do I receive webhook notifications from Basiq?" icon="far fa-circle-info">
    <p>Basiq supports webhook events that allow applications to receive notifications about relevant changes and activities.</p>

    <p>Webhooks can help applications respond to events without continuously polling the API.</p>

    <p>Refer to the <a href="https://api.basiq.io/docs/webhooks" target="_blank" rel="noopener noreferrer">Basiq Developer Hub</a> for supported events, configuration and implementation guidance.</p>

  {/* VALIDATE: Add the current webhook setup guide, event catalogue, authentication requirements and retry behaviour. */}
</Accordion>

<Accordion title="What connection and consent events are available?" icon="far fa-circle-info">
    <p>Basiq provides event and status information to help applications monitor user connections and consent activity.</p>

    <p>The events available depend on the API functionality and webhook configuration used by your integration.</p>

    <p>Refer to the <a href="https://api.basiq.io/reference/listeventtypes" target="_blank" rel="noopener noreferrer">Basiq API documentation</a> for the current event definitions.</p>

  {/* VALIDATE: Publish the approved list of events, including relevant consent and connection lifecycle events. */}
</Accordion>

<Accordion title="How can I monitor connector availability?" icon="far fa-circle-info">
    <p>Connector availability can vary depending on the financial institution and its underlying services.</p>

    <p>Applications should monitor connection and job statuses and handle institution-side errors appropriately.</p>

    <p>For service incidents and availability information, refer to Basiq's designated service status channel.</p>

  {/* VALIDATE: Insert the official Basiq status page URL and explain whether connector-level availability is exposed. */}
</Accordion>

<Accordion title="What reporting and consumer affordability products does Basiq offer?" icon="far fa-circle-info">
    <p>Basiq offers financial data capabilities that can support use cases such as consumer affordability assessment and financial insights.</p>

    <p>Product availability, functionality and access may depend on your organisation's agreement and enabled products.</p>

    <p>Contact your Basiq representative to discuss available products and requirements.</p>

  {/* VALIDATE: Add current product names, supported reports, required inputs, outputs and product documentation links. */}
</Accordion>

<Accordion title="How do I migrate from API v2 to API v3?" icon="far fa-circle-info">
  <p>Basiq API v3 supports both Digital Data Capture (DDC) and Consumer Data Right (CDR) connection methods.</p>

  <p>API v2 supports DDC only.</p>

  <p>When migrating, review the relevant API changes, data structures, authentication requirements and connection workflows before updating your integration.</p>

  <p>Refer to the <a href="https://api.basiq.io/docs/migrating-users-from-web-to-openbanking-connection" target="_blank" rel="noopener noreferrer">Basiq Developer Hub</a> for the current API documentation.</p>
</Accordion>

<Accordion title="How do I move from DDC to Open Banking?" icon="far fa-circle-info">
  <p>Open Banking uses the Consumer Data Right framework to enable consumers to authorise financial institutions to share their data through secure APIs.</p>

  <p>Unlike DDC, Open Banking does not require consumers to provide their internet banking credentials to the ADR.</p>

  <p>Moving from DDC to Open Banking requires your application to support the relevant CDR consent and authorisation workflows.</p>

  <p>Refer to the <a href="https://api.basiq.io/docs/migrating-users-from-web-to-openbanking-connection" target="_blank" rel="noopener noreferrer">Basiq Developer Hub</a> for implementation guidance.</p>
</Accordion>

<Accordion title="How do I get production access?" icon="far fa-circle-info">
    <p>Production access depends on your organisation's onboarding, account configuration and applicable commercial and compliance requirements.</p>

    <p>Contact your Basiq representative or Support team to discuss production access and any required steps.</p>

    <p>For development and integration testing, refer to the <a href="https://api.basiq.io/docs/sandbox" target="_blank" rel="noopener noreferrer">Basiq sandbox documentation</a>.</p>

  {/* VALIDATE: Confirm current production onboarding process, approval requirements and support contact details. */}
</Accordion>