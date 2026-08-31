---
title: June '24 - Product Updates and Enhancements
author: Ashman Malik
hidden: false
published_at: '2024-06-21T02:43:51.433Z'
type: added
---
## :star2: Basiq Dashboard Updates

* 🔒 **Authenticator Apps for 2FA**: The Basiq Dashboard now supports Authenticator apps as a method for Two-Factor Authentication (2FA). We will gradually prompt users who have not enabled 2FA to set it up, and eventually, it will become mandatory.

<Image align="center" className="border" border={true} src="https://files.readme.io/1e5ffa0-2FA.png" />

* 🔄 **MFA Connection Status**: The Basiq Dashboard now accurately displays the status of Multi-Factor Authentication (MFA) connections. <hr />

## :speaker: Product Updates

Please find below the key highlights of the latest features and improvements our team has released over the past few weeks.

1. 👤 **Enhanced User Connections Visibility**: All connections, except for deleted ones, are now visible through the [get user connections endpoints](https://api.basiq.io/docs/data-connections#connection-status). This improvement enhances the developer experience and provides better visibility during the initial stages of the Consumer Data Right (CDR) journey. <hr />
2. 🔔 **New Events for Enhanced Notifications**: We have added [new events](https://api.basiq.io/reference/events) for `account.updated`, `connection.invalidated`, and `transactions.updated`. These events enable our partners to set up notifications based on more meaningful and specific triggers. <hr />
3. 🔗 **Extended Connectors Endpoint**: The [connectors endpoint](https://api.basiq.io/reference/getconnectors) has been extended with new CDR fields, offering more comprehensive data integration capabilities.
   1. :email: **cdrEmail** - The email address for CDR-related inquiries.
   2. :scroll: **cdrPolicy** - The URL to the CDR policy document detailing the institution's data practices and consumer rights.
   3. :1234: **cdrProviderNumber** - A unique identifier assigned to the CDR institution by the CDR program. <hr />
4. 🗑️ **Improved Data Deletion Process**: Our data deletion process has been refined to ensure more efficient handling of data. <hr />
5. ✅ **CDR Compliance Updates**: We have updated our [CDR compliance](https://api.basiq.io/docs/cdr-compliance) with the ACCC CDR Exemption register. Additionally, we've added a CDR Policy Link, CDR Support Email, and CDR Provider Number on the [Business Consumer Consent](https://api.basiq.io/docs/connecting-business-accounts-via-cdr) (BCC). <hr />
6. 📘 **New Account Verification Guide**: We’ve created a simplified “How-To” [guide on Account Verification](https://api.basiq.io/docs/account-verification). Previously, we only had the starter kit. This new guide allows customers to see prerequisites, flow, and screens used for Account Verification. The new guide can be found [here](https://api.basiq.io/docs/account-verification). <hr />
7. 📄 **Connection Status Documentation**: All connection statuses, including Pre-init, are now defined in our documentation. You can find the details [here](https://api.basiq.io/docs/data-connections#connection-status). <hr />
8. 🖨️ **PDF Report Retrieval via API**: You can now retrieve PDF format directly from the [API](https://api.basiq.io/reference/retrievereport). Previously, this was only possible via the Dashboard. For Statements & reports, PDFs are retrieved when using the Accept header (application/pdf) on a [GET request](https://api.basiq.io/reference/retrievereport). Only portrait mode is supported. <hr />

## 🌅 **Payments Feature Sunset**

We've officially sunsetted the Payments feature from Basiq. As part of this, the Payment APIs and Payment Guides have been removed from our [Developer Hub](https://api.basiq.io/docs). <hr />

## Stay Updated :loudspeaker:

<HTMLBlock>{`
<a href="https://api.basiq.io/changelog.rss" target="_blank">   <img src="https://img.shields.io/badge/RSS-Subscribe-orange?style=for-the-badge" alt="RSS Subscribe"> </a>
`}</HTMLBlock>

If you have any questions or need further assistance, don't hesitate to reach out to our support team. <hr />