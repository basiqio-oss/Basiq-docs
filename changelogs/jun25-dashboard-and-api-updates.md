---
title: Jun'25 - 🔍 Improvements to Reports UI and PDF
author: Ashman Malik
hidden: false
published_at: '2025-06-25T04:55:45.506Z'
type: added
---
### 🆕 Business Affordability API Now Live

**📄 Documentation:** [Business Affordability API Docs](https://api.basiq.io/docs/business-affordability)

We’re excited to launch the **Business Affordability Report API**, providing partners with deep insights into the financial health of business entities—whether sole traders or large enterprises.

✅ **What’s Included:**

* Brand new **Business Affordability Report API**
* Dashboard enhancements on the Reports page (now live in production)

This API builds on our Consumer Affordability foundation and supports smarter, faster, and more inclusive B2B lending through consent-based access to business financial data.

***

### ⚠️ New Error Message for Missing Consent

We’ve introduced a new 400 Bad Request error for **Classic Affordability** and **Insight Reports**, shown only when:

* A consent has been revoked or expired, *and*
* Core has not yet completed user data deletion

> **Error message:** `400 Bad request – user doesn't have an active consent`

📝 Note:\
This should be rare, but may occur if a partner attempts to create a report *immediately* after consent is revoked and before deletion finalises.

***

### 🧾 Developer Hub Footer & Legal Disclaimer Update

**What’s New:**

* ABN details for Basiq & Cuscal
* CDR accreditation number: `ADRBNK000208`
* Clarification that Basiq is *not* an Authorised Deposit-Taking Institution

These updates improve clarity, legal compliance, and transparency across our platforms. Big thanks to Legal, Brand, and Product for the collaboration!