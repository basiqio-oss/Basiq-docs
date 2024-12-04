---
title: Institutions
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Many partners are keen to get more information on institutions at a more granular level. We make sure all this information is accessible not just for getting **up to date** stats on each institution but also to help troubleshoot issues in real time. Here are a couple of pointers on how to make the most of the `/institutions` endpoint. 

## Institution Connectors: Stage, Status and Stats

Use attributes `stage`,  `status` and `stats` to determine the **maturity, availability and performance** respectively for each institution connector. Scroll down for more detailed information on both these attributes.

### Stats 

The **Stats** of institution connectors are evaluated every 24 hours using jobs occurring in the previous 7 days to provide an indication of average performance.

### Under maintenance connectors

Institution connectors with `status` = "**under-maintenance**" - can and should still be used. This status lets you know that they are being continuously improved e.g. improving data enrichment or adding new products, until they mature into `stage` = "**live**".

### Institution Connector Stages

When we release a new connector it is initially released as **alpha** or **beta** version.  The more data we see the more mature the connector becomes until it is upgraded to **live**.  Below are some high level guidelines to indicate what you can expect during each stage.

**Beta:** This is a very new connector. We leave the connector in this Stage until we have enough variety and coverage of data to upgrade the connector. This is an iterative process and we love partnering with Fintechs to improve our connectors. For a beta connector you can expect the following:
- verification of credentials for login
- account class and type (limited support for product name to account type mappings)
- account and transaction data for savings and transaction accounts to start
- account status, account number, account balance, available funds for above account types
- transaction status, amount, balance, description, postdate
- monitoring of test accounts

**Alpha:** this is a partially complete connector.  Use the features attributes to determine what is supported with these connectors.  Partners keen to help move these **alpha** connectors to **beta** stage can use these connectors as the more data the platform retrieves the quicker the connector can mature.

**Live:** This is a mature connector, where we have seen a great variety of account types and transaction data in order to confidently create the right patterns to enable excellent coverage for expense categorisation, and insights for Affordability.  For a **live** connector you can expect the following:

* comprehensive list of verified product name to account type mappings 
* support for most account types with emphasis on savings, transactions, credit card and mortgage
* account holder, account class and type (comprehensive support of product name and account type mappings)
* mortgage meta data where available
* transaction direction (debit/credit) and class (payment, bank-fee etc)
* transaction sub-class for payments (enrichment of payments) 
* transaction intervals (for bank statements)
* connection profile data
* institution works with affordability solution for income and expenses
* comprehensive monitoring

## Supported features

Use these attributes to determine which **features** are supported for each institution and data source: 

- ** web** -  denotes all data shared via digital data capture connectors
- ** open-banking** -  denotes all data shared via open banking connectors
- **pdf** - denotes data uploaded via official pdf bank statements
- **csv** - denotes data uploaded via csv statements

Example 1:   `"accountNo": ["web", "open-banking", "pdf", "csv"]`  indicates that the  **Accounts.accountNo** attribute is available for this institution -  for data sourced from **open banking, web, pdf and csv** 

Example 2: `"accountNo": ["pdf"]` indicates that the  **accountNo** attribute is available for this institution - only for data sourced from **pdf** statements