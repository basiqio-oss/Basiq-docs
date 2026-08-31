---
title: Aug'24 - API & Dashboard Improvements
author: Ashman Malik
hidden: false
published_at: '2024-09-01T23:15:35.765Z'
type: added
---
We are excited to share the latest updates and improvements we've made to the API and Dashboard in August 2024. These updates focus on enhancing user experience, improving security, and providing more accurate data insights. Here's what's new:

## 🌟 **Consent Management Enhancements**

* **Mandatory`account.basic` Scope**: To streamline consent management, the `account.basic` scope is now a required field in the Customiser UI for Consent Management. This applies to:
  * **Platform > Consent Management > Consent Scopes**: [Learn more](https://api.basiq.io/docs/consent-scopes)
  * **Integration > Customise UI**: [Learn more](https://api.basiq.io/docs/consent-ui-customisation)
  * **Dashboard > Customise UI**: [Learn more](https://api.basiq.io/docs/basiq-customise-ui)

## <hr/> 🆕 **New Field: revoked in Consent API**

* We have added a new revoked field to the **GET Consent API** to indicate the date a consent was revoked. This field will be populated when user consent is deleted or when a user is deleted. The `revoked` field uses the format: `now().UTC().Format(time.RFC3339)`.
  * Updated documentation is available [here](https://api.basiq.io/reference/getconsents). 

## <hr/>📊 **Reports Insights**

* **New Groups for Loan and Credit Card Repayment Detections**: We’ve expanded our insights to include new groups for [better loan and credit card repayment detections](https://api.basiq.io/reference/retrievereport):
  * **EXP-057 (Loan Repayments)**
  * **EXP-061 (Credit Card Repayments)**
  * **EXP-062 (Credit Card Transfers)**
  * **EXP-063 (Loan Transfers)**
* **Improved Metrics Logic**: Metrics are now calculated using deduplicated transaction sets, resulting in more accurate data points. Previously, transactions that appeared in multiple groups could cause skewed metrics due to duplication. This update ensures that each transaction is counted only once, even if it falls under multiple groups. 

## <hr/>🔐 **Security Update: Enforcing Multi-Factor Authentication (MFA)**

Multi-Factor Authentication (MFA) is now enforced to enhance the security of our systems. For more details, please check our [documentation](https://api.basiq.io/docs/quickstart-basiq-dashboard#enforcing-multi-factor-authentication-mfa). 

## <hr/>:heart_decoration: **Improved CDR Receipt Notifications**:

* **Consent Creation Notifications**: Notifications are now sent only upon CDR connection activation, preventing unnecessary alerts.

## <hr/>🌐 **Web Connectors Update**

* **Greater Bank**: Updated the web connector to accommodate recent changes to Greater Bank's online banking portal. 

## <hr/>🚀 **New Data Holder Coming Soon: Liberty Financial Pty Ltd**

We are pleased to announce that **Liberty Financial Pty Ltd** will soon be added as a supported data holder in our Connectors API. Liberty Financial has recently become available for Open Banking, and we are working to ensure our platform supports this institution. 

We are excited to expand our support for Open Banking by including Liberty Financial Pty Ltd and look forward to providing you with enhanced connectivity and services. Stay tuned for further updates on the availability of this new data holder in our Connectors API.

<br />

## <hr/>Stay Updated :loudspeaker:

<HTMLBlock>{`
<a href="https://api.basiq.io/changelog.rss" target="_blank">   <img src="https://img.shields.io/badge/RSS-Subscribe-orange?style=for-the-badge" alt="RSS Subscribe"> </a>
`}</HTMLBlock>

If you have any questions or need further assistance, don't hesitate to reach out to our support team. <hr/>