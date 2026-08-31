---
title: May '24 - Product Updates 📅
author: Ashman Malik
hidden: false
published_at: '2024-05-23T02:40:54.360Z'
type: added
---
## Changelog 📝

### Stay Updated :loudspeaker:

<HTMLBlock>{`
<a href="https://api.basiq.io/changelog.rss" target="_blank">   <img src="https://img.shields.io/badge/RSS-Subscribe-orange?style=for-the-badge" alt="RSS Subscribe"> </a>
`}</HTMLBlock>

## New Features 🌟

**Account Updated Event Released**: We're excited to announce the launch of the Account Updated Event! 🚀 Stay up-to-date with the latest account changes instantly.

**New Payment Details in CDR**:

* We’ve introduced new **paymentDetails** fetching capabilities through CDR:
  * **BPAY Options**:
    * **billerCode**: Instantly identify your biller.
    * **billerName**: Clearly see who you are paying.
    * **crn**: Use Custom Reference Numbers for simplified payment tracking.
  * **apcaNumber** is also now available for more streamlined banking transactions. 🏦💳

**Dashboard Updates**: We have added 2 additional fields in the dashboard customiser: Reference name and Manage consent URL. The values of these fields will be shown in the Cancellation modal and Manage your data sharing modal. 🛠️💼 Read more details [here](https://api.basiq.io/docs/consent-ui-customisation#flow-tab-setting).

<Image align="center" className="border" border={true} src="https://files.readme.io/bcd37b1-dash.png" />

## Enhancements ✨

**Reports for Multi Users**: Generate comprehensive reports for multiple users at once. More power to team management! 📊 You can read more details [here](https://api.basiq.io/docs/reporting#allow-multiple-users-in-reports).

**Expense Details Update in Dashboard**: We've refined how expense details are presented on your dashboard for users of Affordability, making it easier to track your spending and manage finances efficiently. 📉

> 📘 Note
>
> This update is specific to the Affordability product, and does not apply to Insights/Reporting.

<Image align="center" className="border" border={true} src="https://files.readme.io/207448e-ExpenseDetails.png" />

## Improvements 🔧

**Updated Upload Statement Form on Basiq Dashboard**:

To improve customer experience and minimise errors, we now require partners to select a file format before uploading a statement. This ensures compatibility and prevents uploads for unsupported institutions. 📁🔍

<Image align="center" className="border" border={true} src="https://files.readme.io/abf8bdb-Statementupload.png" />

## API Updates 🌐

**New Event in Production**:\
The `connection.invalidated` event is now live in production. This event is triggered when a connection status changes from active to invalid due to user-related errors. The specific user-related errors that will trigger this event for web and OB connections are as follows:

**Web Connections**:

* 🛑 user-action-required.
* ❌ invalid-username-or-password.
* 🚫 invalid-connection.
* 🔒 locked-account.
* 🔐 multifactor-required.

**OpenBanking Connections**:

* ⏳ expired CDR arrangement - user didn’t re-authorise.
* ⚠️ any issue occurred during user re-authorisation.

We're continuously working to make our services better for you! Keep the feedback coming! 🙌