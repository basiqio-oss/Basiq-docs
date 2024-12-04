---
title: Send
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
#### To *Send* is to pay out funds from your float account to one of your users or your own account held at a bank.

**Example:** Piper Pay, an investment app, has been holding investment funds for one of its users, Adam. Adam has made a profit on his investment and instructs Piper Pay to pay out the profits to his account. Upon receiving the instruction to pay out the profits, Piper Pay would call the Basiq Send (payouts) API to send the funds from their float account to Adam's account at ANZ.

### Send payment methods

When performing a `payout` instruction, partners have the ability to indicate the payment method as `fast`, `batch`, or `fast/batch`. The details of each one are as follows:

* `fast` means the payout will be transmitted over fast/real-time payments networks (e.g. NPP / OSKO in Australia) provided the recipient bank and account can accept fast payments. In this case funds should land in the recipient bank account within a minute in most cases.
* `batch` means the payout will be transmitted over batch payments networks (e.g. BECS/DE in Australia). In this case funds should land in the recipient bank account within 2 business days
* `fast/batch` means the payout will first be attempted to be sent over the fast/real-time network and if a failure occurs (e.g. the recipient bank and/or account is not enabled for fast/real-time) then the payout will be sent as a batch payment.

### **Prerequisites for using Send**

* The payee user must be set up as active in the partner application, and therefore have a `userId` to associate the payment with. Read more about creating a user [here](ref:createuser)
* The payee user must have a valid user name and email address. This includes having a first name with a minimum of 2 characters and a last name with a minimum of 2 characters and the email address exist and be a valid email address.
* The application must be enabled for payments by Basiq, with the appropriate environment setup. You can enable the application for payments in Sandbox or request production access through the Basiq dashboard. 
* You should have enough funds in the float account in order to perform payouts. All payouts are sent out using funds you have in the float account held by Basiq and/or its 3rd party partners/providers. Please refer to [Managing float accounts](doc:managing-float-accounts)
