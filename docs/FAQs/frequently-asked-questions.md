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
<Image align="center" src="https://files.readme.io/82119ec-FAQ_Header.jpg" />

When incorporating the Basiq API into your application, it's essential to follow best practices that significantly contribute to the success of any implementation. These practices span various areas, including security considerations, user experience (UX), scalability, and more. They have undergone thorough testing to provide you with the essential tools and guidelines for a successful integration. 

Explore the Frequently Asked Questions (FAQs) below for our platform:

<HTMLBlock>{`
<!DOCTYPE html>
<html>

<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    .accordion {
      background-color: #0075DC;
      color: #fff;
      cursor: pointer;
      padding: 18px;
      width: 100%;
      border: none;
      text-align: left;
      outline: none;
      font-size: 15px;
      transition: 0.4s;
    }

    .active,
    .accordion:hover {
      background-color: #3290e3;
    }

    .accordion:after {
      content: '\002B';
      color: #fff;
      font-weight: bold;
      float: right;
      margin-left: 5px;
    }

    .active:after {
      content: "\2212";
      color: #fff;
    }

    .panel {
      padding: 4px 18px;
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.5s ease-out;
    }
  </style>
</head>

<body>
  <!-- Q1 -->
  <button class="accordion">What is OpenBanking?</button>

  <div class="panel">
    <p>
      <strong>Open Banking (CDR):</strong> Open banking, also known as the Consumer Data Right (CDR) in Australia, is a
      new method for capturing user consent and sharing financial data. Regulated by the Australian federal government,
      it requires banks to share data via APIs specifically built for this purpose. Unlike DDC, CDR does not require
      users to share login credentials, is more performant and robust, and banks are mandated to participate.
    </p>
  </div>

  <!-- Q4 -->
  <button class="accordion">What is a DDC Connector?</button>

  <div class="panel">
    <p> <strong>DDC Connector:</strong> Digital Data Capture (or "screen scraping") is a well-established method of
      aggregating financial data. It involves securely sharing login credentials, which are then passed to the bank's
      internet banking portal. The portal is parsed to extract a user's accounts and transactions. This method can be
      slow and is susceptible to changes in the bank's portal. DDC has seen a decline, especially after recent data
      breaches, as banks take measures to prevent bot access to their internet banking portals.</p>
    <p>
      <strong>API Versions:</strong> Version 2 of the API supports DDC only. Version 3 supports both DDC and CDR,
      allowing dynamic switching between the two methods.
    </p>
  </div>

  <!-- Q2 -->
  <button class="accordion">What is a Data Holder (DH) and an Accredited Data Recipient (ADR)?</button>

  <div class="panel">
    <p><strong>A Data Holder</strong> refers to a business that currently holds a consumers’ data, such as a bank.
      Consumers have the authority to instruct registered Data Holders to share their data with an <strong>Accredited
        Data Recipient (ADR)</strong>.</p>
    <p>An <strong>ADR</strong> is a business accredited by the Australian Competition and Consumer Commission (ACCC) to
      receive consumer data from a Data Holder, contingent upon the consumer's explicit consent. The ADR then utilises
      the data for the specified purpose.</p>
    <p><strong>BASIQ</strong> operates as an ADR within the CDR system, having obtained accreditation by meeting the
      stringent criteria outlined by the ACCC.</p>
    <p>For a comprehensive list of registered Data Holders, refer to the government's CDR website: <a
        href="https://www.cdr.gov.au/find-a-provider" target="_blank">https://www.cdr.gov.au/find-a-provider</a></p>
  </div>

  <!-- Q3 -->
  <button class="accordion">What are Web and Open Banking transaction date/times?</button>
  <div class="panel">
    <h2>Web Connectors:</h2>
    <p>We only get <code>transaction.Date</code> field from the connector (timestamp not available).</p>
    <p>We only store date under user transaction data.</p>
    <p>When compiling <code>user_transactions_get</code> response, we add midnight time
      <code>normalizedDateTime := transaction.Date + utils.RFCMIDNIGHT</code>.</p>
    <p>We set the date for transactions, then <code>00:00:00Z</code> is appended (indicating UTC).</p>
    <h2>OB/CDR Connectors:</h2>
    <p>We get full datetime from the connector, as <code>obTransactionDateTime</code>.</p>
    <p><code>postingDateTime</code> in the case of posted transactions.</p>
    <p><code>executionDateTime</code> in the case of pending transactions.</p>
    <p>We store the date in two fields within user transactions data: <code>date</code> and
      <code>obTransactionDateTime</code>.</p>
    <p>When compiling <code>user_transactions_get</code> response, we normalize the time
      <code>normalizedDateTime.UTC().Format(time.RFC3339)</code>.</p>
    <p>In case <code>obTransactionDateTime</code> can't be validated, we add midnight to the
      <code>transaction.Date</code>.</p>
    <h2>Exposing Data via GET /transactions Endpoint:</h2>
    <p>For posted transactions, we return <code>postDate</code>.</p>
    <p>For pending transactions, we return <code>transactionDate</code>.</p>
    <p>We initially save transaction’s <code>dateTime</code> as received from the DH, without any modifications. Per CDR
      standard, RFC3339 is used for <code>dateTime</code>, meaning all times expressed have a stated relationship
      (offset) to Coordinated Universal Time (UTC).</p>
    <p>All DHs return data in UTC (plus offset, if there is any), or at least they are obligated to convert to UTC, not
      just set this timezone.</p>
    <p>Some DHs actually provide the offset to UTC, like ANZ. Example is "<code>2021-11-19T00:00:00+11:00</code>". This
      represents UTC + 11 hours. In our system, we have a logic where we calculate this offset to provide in
      standardized format in UTC without the offset so, "<code>2021-11-19T00:00:00+11:00</code>" becomes
      "<code>2021-11-18T13:00:00Z</code>". We subtracted 11 hours from midnight, and got the previous day at 13:00
      hours. This is correct behavior from our side.</p>
    <p>Note: all <code>dateTimes</code> for open banking are in UTC, as this is CDR standard. We cannot convert to local
      times depending on the time zone, this is impossible for us, and we strive to have a single time zone (UTC is
      usually the standard).</p>
    <p>Some DHs just append <code>00:00:00Z</code> at the end - now, if they haven’t done conversion to UTC, but just
      take the date and say it is UTC, this is incorrect behavior from the DH side. In those instances, that transaction
      within the customer's Internet/Online Banking would show exact times in the local time zone.</p>
    <p>We raise these behaviors in a ticket to the DH via the CDR Portal and, over time, we will see improvements in the
      accuracy of these time stamps.</p>
  </div>

  <!-- Q5 -->
  <button class="accordion">Job error "Service is currently unavailable. Please try again later."
  </button>

  <div class="panel">
    <p>No, this error does not indicate any problem with Basiq. The error indicates that there was a problem retrieving
      your user's data from their bank, and as the Basiq job relates closely to your user interaction, we provide a
      range of actionable error codes to help you to provide the best possible user experience in those cases where the
      bank fails to return data.</p>
    <p>You can read more about these scenarios and recommended actions and user comms <a
        href="https://api.basiq.io/docs/handling-jobs" target="_blank">here</a>:</p>
    <p>The service-unavailable error code is our way to tell you (so that you can tell your user) that their bank was
      unable to return their data. The equivalent human experience is if I login to my NetBank internet banking and get
      an error from the bank, "We can't do this right now. Please try again later."</p>
    <p>If Basiq gets this response from the bank, there is nothing that we can do other than to pass this detail back to
      you and your user. Advice is to let your user know there was a problem retrieving their data but to leave the
      problem with you. You can retry after some appropriate period (e.g., an hour) by refreshing the connection, and if
      that works you can let the user know that their data has come through.</p>
    <p>If the error does not clear after a couple of retries, please reach out to Basiq support portal so that we can
      take a look. In that case, please just include the Basiq user ID, connection ID and if possible the job ID, to
      help us to trace the logs.</p>
    <p>Reasons that a job might fail with the service-unavailable error:</p>
    <ol>
      <li>the bank is having temporary problems or performance issues - this is the most common cause and should clear
        on a retry</li>
      <li>the bank has made changes to their internet banking portal - in this case, we will need to update our parser
        code to handle the change, this typically takes a couple of days but depends on the nature of the change</li>
      <li>the bank is blocking screen scraping - banks are not obliged to support web connections / screen scraping, and
        some of them are insisting on sharing data through CDR channels only</li>
    </ol>

  </div>

  <!-- Q6 -->
  <button class="accordion">What exactly is the Smart-Cache and why would I need it enabled?</button>

  <div class="panel">
    <p>The Smart-cache is Basiq's way of performing a nightly refresh on your user's data for you! For all active
      connections, we put the connection in the queue and fetch the most up-to-date data for you once refreshed, e.g.,
      new transactions and updated account balance, etc.</p>
    <p><b>Open Banking</b> allows you up to 20 refreshes per day, which is a huge benefit as compared to <b>Web connections</b>, which
      requires a more sophisticated approach to not overload the specific institution's server.</p>
  </div>

 
   <!-- Q7 -->
  <button class="accordion">What happens to my data when consent is revoked or expired?</button>

  <div class="panel">
     <p>
    	Partners should be aware that all data on Basiq is deleted upon expiration or revocation of consent. Partners may wish to keep a de-identified version of the data based on the retainData settings within Basiq customise UI. There may be circumstances where partners are subject to other legal obligations that necessitate the retention of data. These obligations could arise from laws related to financial record-keeping, anti-money laundering regulations, or other relevant legislation. Under these circumstances and based on independent legal advice partners might be able to retain the data beyond expiry date in accordance to relevant legislation.
    </p>
    
  </div>
  
 <!-- Q8 -->
  <button class="accordion">Why can't I see all the user's accounts when connected via OpenBanking?</button>

  <div class="panel">
    <p>For open banking (or "CDR", the Consumer Data Right), the user explicitly selects which accounts they want to share with Basiq and your app. The user's selection creates a sharing arrangement between the bank and Basiq, and the selected accounts are in scope for the arrangement (in Basiq we call this a "connection"). The selected accounts and only those accounts are shared with Basiq. If you want the user to add the remaining accounts, you should provide a new consent link with the connectionId parameter to the user, so they can share the missing accounts..</p>
  </div>
  
 <!-- Q9 -->
  <button class="accordion">Why am I not receiving the verification code by email when I follow the “Forgot your password?” link?</button>

  <div class="panel">
     <p>If you are not receiving the verification code by email when trying to reset your Dashboard password, it could be due to several reasons:</p>
    <ul>
        <li>
            <strong>Single Sign-On (SSO) Users:</strong>
            <p>If you use Single Sign-On (SSO) methods such as Google Account, Okta, or Azure to log in, you will not receive a verification code. Instead, you need to recover your password through your SSO provider.</p>
        </li>
        <li>
            <strong>Email Issues:</strong>
            <ul>
                <li><strong>Spam/Junk Folder:</strong> Check your spam or junk email folders to see if the verification email was filtered there.</li>
                <li><strong>Email Address:</strong> Ensure that the email address you are checking is the one associated with your Dashboard account.</li>
                <li><strong>Email Filters:</strong> Make sure there are no filters set up in your email account that might be blocking or redirecting the verification emails.</li>
            </ul>
        </li>
        <li>
            <strong>Technical Issues:</strong>
            <ul>
                <li><strong>Server Delays:</strong> Occasionally, there might be delays with the email server. Wait a few minutes and try again.</li>
                <li><strong>Incorrect Details:</strong> Double-check that you entered the correct email address when requesting the verification code.</li>
            </ul>
        </li>
    </ul>
    <p>If you have verified all the above points and are still not receiving the verification code, please contact our support team for further assistance.</p>
  </div>
  
   <!-- Q10 -->
  <button class="accordion">Can a user have multiple connections with the same bank?</button>

  <div class="panel">
       <p><strong>Web Connections:</strong> Yes, a user can connect multiple times with the same bank using different credentials.</p>
    <p><strong>Open Banking Connections:</strong> No, only one connection at a time is allowed for each bank.</p>
  </div>
  
  
  <!-- Q100 -->
<button class="accordion">Why is the user getting the message: "You have no accounts eligible for sharing"?</button>

<div class="panel">
  <p>An account may be ineligible for open banking data sharing under the Consumer Data Right (CDR) for several reasons, particularly within the banking sector:</p>
  <ul>
    <li><b>Online Accessibility:</b> A key eligibility criterion for Consumer Data Right (CDR) consumers related to a particular data holder in the banking sector is that the account must be set up in a way that it can be accessed online.</li>
    <li><b>Age Restrictions:</b> Account data related to a joint account or partnership account for which any of the individuals who are account holders is less than 18 years of age at that time is not considered required consumer data nor voluntary consumer data, making such accounts potentially ineligible for open banking data sharing.</li>
    <li><b>Historical Transactions:</b> For an account that is open, transaction data relating to transactions that occurred more than 7 years before the current time is not considered required consumer data at that time.</li>
    <li><b>Closed Accounts:</b> For an account that is closed, certain types of data (e.g., account data related to authorizations for direct debit deductions more than 13 months old, transaction data for transactions that occurred more than 12 months before the account was closed if the account was closed no more than 24 months ago, and all account data if the account was closed more than 24 months before the current time) are not considered required consumer data.</li>
    <li><b>Restrictions on Specific Data Types:</b> Certain data types, like those related to transactions or events that occurred more than 2 years before the current time for an account that is open, are not considered required consumer data.</li>
    <li><b>Joint Accounts:</b> All parties involved in the joint account must agree to share their data. If such consent is not obtained or the account setup does not support obtaining such consent, the account may be ineligible.</li>
  </ul>
  <p>The user is advised to directly contact the respective Data Holder to ascertain the specific reason for the disablement of their account for data sharing. Additionally, they should inquire about the possibility of enabling the account if feasible.</p>
</div>


  
  
  
  
  <script> var acc = document.getElementsByClassName("accordion"); var i; for (i = 0; i < acc.length; i++) { acc[i].addEventListener("click", function () { this.classList.toggle("active"); var panel = this.nextElementSibling; if (panel.style.maxHeight) { panel.style.maxHeight = null; } else { panel.style.maxHeight = panel.scrollHeight + "px"; } }); } </script>
</body>

</html>
`}</HTMLBlock>

Please reach out to support, if you have any further questions or concerns.
