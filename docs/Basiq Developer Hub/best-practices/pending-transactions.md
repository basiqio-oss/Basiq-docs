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
  robots: noindex
next:
  description: ''
---
### When it comes to building out your interface, the UX is an essential part of ensuring processes run smoothly and successfully.

User experience is one of the most important processes to get right when scaling and delivering financial services, especially when it comes to onboarding.

Poor onboarding experiences mean you and your team have to work harder to convert the same amount of customers. Marketing teams need to attract more visitors and Support teams spend time guiding confused users and troubleshooting issues that could have been self-resolved. To help you reduce churn and increase customer happiness, we’ve provided some quick tips.

 ## Build trust to securely share data

When you build trust with your customers early you ensure a seamless flow whether they are linking one or many banks.
There are a variety of ways you can build trust with your customer base when they are sharing data, such as:

- a good, clear exchange, and
- well planned UX through the whole journey. 

We often hear from our partners that not having the right value exchange is the biggest blocker in customers sharing their data. In terms of the incentive for the end customer, it is all about getting the best outcome faster, so it helps for them to understand that sharing their data this way allows that.

Our article [here](http://docs.basiq.io/en/articles/5298389-securely-connecting-your-data-with-basiq) covers everything you or your users might need to know about how we handle data safely.

## Keep the customer engaged

The process is asynchronous so you don't have to wait for one connection to complete to start another one.  When you create a connection to a banking institution it kicks off an async job which has 3 steps:

1. Verify credentials
2. Retrieve accounts
3. Retrieve transactions

This means that you can keep your end customer informed on progress if you wish or you can distract them with another part of your process

## Distract the customer - make it a background process

Our most successful partners don't have any issue with customers sharing credentials and create a user flow which doesn't involve the customer waiting for the connection to complete - as soon as the **verify credentials** step is complete the customer is taken onto the next step in their connection flow. This is *strongly recommended* to limit drop off or user frustration.

Our [institution's endpoint](#institutions) really lets you build the best UX journey with dynamic information around institution availability, maturity, stats for each step in the process. This means you can really tailor the customer journey depending on this information. If you're planning to build your own bank picker, have a look at [our guide on how to do it](https://api.basiq.io/docs/build-your-own-1).