---
title: AuthLinks
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The Auth Links (auth_link) object represents a secured authorised link attached to a user. The link can be sent to a user (applicant) to allow for the self-service capture of financial data. The auth_link is a URL that directs a user to Basiq's hosted consent.

Once authenticated via 2FA the user/applicant can upload banking data either via a direct bank connection or via official PDF bank statement upload.

Auth Link objects expire after 7 days. Attempting to use the URL returned by the object after it has expired will fail. There is no limit to the number of Auth Link objects that can be created for a User, but only the latest Auth Link will be valid.  An AuthLink can be used once. If the user exits the flow, they will need a new link.

The URL associated with a single auth_link object will allow a user/applicant to link and share data from multiple accounts at multiple financial institutions.

When the user selects 'I have disclosed all my accounts' the auth_link is automatically deleted.

> 📘 Generate a secure link by Creating an Auth Link resource
> 
> When a new Auth Link POST request is made, 2FA is activated against the link using the mobile phone number attached to the User object. It is important to ensure that this is a valid mobile number and belongs to the User/applicant as 2FA is via SMS. OTP code length increased from 4 to 6 characters. NPM package updated to version 1.1.0 (npm: [@basiq/connect-auth](https://www.npmjs.com/package/@basiq/connect-auth))

# Demo

[block:html]
{
  "html": "<div style=\"position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;\"><iframe src=\"https://demo.arcade.software/DhU1AMDeKC4f6PxNmJcP?embed\" title=\"Basiq | OTP \" frameborder=\"0\" loading=\"lazy\" webkitallowfullscreen mozallowfullscreen allowfullscreen allow=\"clipboard-write\" style=\"position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;\"></iframe></div>"
}
[/block]