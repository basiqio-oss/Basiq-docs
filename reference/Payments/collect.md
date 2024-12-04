---
title: Collect
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
#### To *Collect* is to pull funds from a user, into your bank account - initiated by the payee.

**Example:** Piper Pay, a PFM app, charges a monthly $2.99 subscription fee for their customers to continue using their service. On the 1st of every month, they will collect this fee from their customers using the Basiq API.

### How does collect appear?

All `payrequests` submitted on an [Australian business day](ref:payments-processing-times) before 7pm will appear as individual payments on your payers' bank accounts. All the funds cleared and settled will be credited to your dedicated float account. You will then be able to [Send workflow](doc:send-workflow) those funds out from your float account.

**Example:** Piper Pay has 10 active users, so when they charge all users on the 1st of the month, each user will have a single transaction of $2.99 on their individual bill.

## **Prerequisites for using Collect**

* The paying user must be set up as active in the partner application, and therefore have a `userId` to associate the payment with. Read more about creating a user [here](ref:createuser)
* The paying user must have a valid user name and email address. This includes having a first name with a minimum of 2 characters and a last name with a minimum of 2 characters and the email address exist and be a valid email address.
* The application must be enabled for payments by Basiq, with the appropriate environment setup. You can enable the application for payments in Sandbox or request production access through the Basiq dashboard.

![1858](https://files.readme.io/54a8e39-e94f8ba-image_2.png "e94f8ba-image_2.png")

Alternatively you can always reach out to [support@basiq.io](mailto:support@basiq.io) if you have not already.