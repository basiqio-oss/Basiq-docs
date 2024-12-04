---
title: Pending transactions
excerpt: >-
  Understand what is the difference between a pending transaction and a posted
  transaction.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
A pending transaction is an approved debit or credit transaction that has not been fully processed yet (i.e. has not been posted). On average a transaction may stay in the pending state for 3 - 5 business days. For pre-authorisations (e.g security deposits for hotels or car rentals), this can be up to 31 days. During this time the pending transaction amount is deducted from the ‘available funds,’ while the ‘account balance’ remains as is.

A posted transaction is a debit or credit that has been fully processed. Once a transaction is posted the account balance on the account is also updated.

## To give you a better understanding of the process, here is how a typical payment is handled:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/60680a7-payment-flowchart.png",
        "payment-flowchart.png",
        999
      ],
      "align": "center",
      "sizing": "80"
    }
  ]
}
[/block]


### Note that in some instances the description that appears for a pending transaction may change once it is posted.

# How Basiq deals with pending transactions

- Each transaction has a status of "pending" or "posted". This helps you differentiate between the two.
- Every time a connection is refreshed (i.e. users latest financial data is retrieved) the pending transactions are deleted and new ones are imported. This is the opposite to posted transactions - that are never deleted.

# Recommendation on how to deal with pending transactions

- It is strongly recommended that you **always separate the pending transactions from the posted ones** in your database and that you treat them as temporary records. 
- It's rare that an application would need to list pending transactions, so we recommend that our customers ignore these. In the case that it is absolutely necessary, highlight _pending_ transactions within your app, so that the user knows that these may change.

Additionally, if your filter includes dates within 7 days of the current day, return the pending transactions as part of the results. This helps ensure that users are aware of the most recent activity that may not yet be finalised.

> 📘 Pending transaction ID's
> 
> Because we have no way of knowing with confidence that the transaction that we retrieved today is the same as the pending one we retrieved yesterday, dispose of all pending transactions each time we refresh.  
> **This means the `transaction.id` for a pending transaction will change every time a connection is refreshed.**