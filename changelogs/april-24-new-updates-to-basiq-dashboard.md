---
title: April '24 - New Updates to Basiq Dashboard
author: Ashman Malik
hidden: false
published_at: '2024-04-19T01:24:51.014Z'
type: improved
---
We're thrilled to announce significant enhancements to the Basiq Dashboard. Here's what's new:

# 📄 Enhanced Reports and Statements Generation

PDF Statement Generation: Partners enabled for Reports can now generate PDF Statements directly from the User Account detail screen, integrating with our robust Bank Statements APIs by Insights.

**Per-Partner Enablement:** To enable this feature for new partners, please reach out to our Support team.

## ✨ UI Redesigns

**Redesigned Signup and Login UI:** We've updated the appearance of Dashboard registration, login, and other related screens to align visually with our redesigned Basiq website.

**SSO/Azure Partners:** The login prompt has changed from 'Login with AzureAD' to 'Sign in using SSO' to better reflect the authentication process.

## 🔧 Dashboard Functionalities

**Configurable Access:** Access to the Reports screen and the ability to generate statements within a user account is now configurable through our Support team.

**Improved Feedback Mechanisms:** The Dashboard now displays success and error messages more accurately. JSON output for reports now presents the full report data.

**Visual and Wording Updates:** Various UI elements and phrases have been refined for clarity and usability.

## 🛠️ Improvements and Bug Fixes

**Statement Uploads:** We've made several enhancements to the upload statements form as we prepare to transition partners from the Classic Dashboard.

**Bug Fix in Permissions:** Resolved an issue where Partners sometimes faced difficulties assigning permission sets to Members.

## 🆕 Identity Endpoint Enhancements

**Expanded Schema:** The schema for GET `/identities` and GET `/identities/{identityID}` has been expanded to include two new fields: `connectionID` and `institutionID`.

> 📘 🙏 Your Feedback Matters!
>
> We are continuously looking to improve, especially in enhancing our Statement functionality. Please keep sharing your valuable feedback!

> 👍 Quick Links
>
> * [Create and export Statements.](https://api.basiq.io/docs/bank-statements#how-to-create--export-statements-via-dashboard)
> * [Identity Endpoint](https://api.basiq.io/docs/identity)