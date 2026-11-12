---
title: FAQs
excerpt: Internal
deprecated: false
hidden: true
icon: fad fa-comment-question
metadata:
  robots: index
---
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
