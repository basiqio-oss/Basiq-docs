---
title: May'23 - Accounts Metadata Extension
author: Ashman Malik
hidden: false
published_at: '2023-05-17T02:04:34.003Z'
type: improved
---
# May'23 :cloud:

<Image alt={940} border={false} caption="Accounts Metadata" title="de77ff4-Untitled_Facebook_Post_Landscape_1.jpg" src="https://files.readme.io/de77ff4-Untitled_Facebook_Post_Landscape_1.jpg" />

## :hammer: What's Improved?

We have improved our API by extending the accounts EP with CDR attributes in our `GET /accounts` and `GET /accounts/{id}` endpoints within connectors data. The new attributes are below.

**Fees:**

* name
* feeType
* amount
* accrualFrequency

**DepositRates:**

* depositRateType
* rate
* applicationFrequency

**LendingRates:**

* lendingRateType
* rate
* applicationFrequency

**Loan:**

* startDate
* endDate
* repaymentType
* minInstalmentAmount

**CreditCard:**

* minPaymentAmount
* paymentDueAmount
* paymentCurrency
* paymentDueDate

These attributes provide information about fees, deposit rates, lending rates, loan details, and credit card information within the context of banking accounts and transactions.

for more updates, read more on [GET /accounts](https://api.basiq.io/reference/getaccounts) and [GET /accounts/ `{id}`](https://api.basiq.io/reference/getaccount) endpoints.