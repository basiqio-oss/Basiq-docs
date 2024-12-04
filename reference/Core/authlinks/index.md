---
title: AuthLinks
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
The Auth Links (auth\_link) object represents a secured authorised link attached to a user. The link can be sent to a user (applicant) to allow for the self-service capture of financial data. The auth\_link is a URL that directs a user to Basiq's hosted consent.

Once authenticated via 2FA the user/applicant can upload banking data either via a direct bank connection or via official PDF bank statement upload.

Auth Link objects expire after 3 days. Attempting to use the URL returned by the object after it has expired will fail. There is no limit to the number of Auth Link objects that can be created for a User, but only the latest Auth Link will be valid.

The URL associated with a single auth\_link object will allow a user/applicant to link and share data from multiple accounts at multiple financial institutions.

When the user selects 'I have disclosed all my accounts' the auth\_link is automatically deleted.

> 📘 Generate a secure link by Creating an Auth Link resource
>
> When a new Auth Link POST request is made, 2FA is activated against the link using the mobile phone number attached to the User object. It is important to ensure that this is a valid mobile number and belongs to the User/applicant as 2FA is via SMS.
