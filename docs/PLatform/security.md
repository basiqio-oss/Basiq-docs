---
title: Security
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
<Image align="center" src="https://files.readme.io/faf2addd103fed685b2347a691310797d63d7fed623b361bd8d68035e5fbd9b1-6c2e4ae-Group_2061.jpg" />

# First things first

**We can’t do anything with users money.** All access is read-only, meaning we can see accounts and transactions to report on them, but are unable to perform any actions on behalf of the user. 

**We don’t hold onto, or sell, data.** When an application or service no longer needs access to the data then it’s as simple as letting us know, after which it is immediately deleted. We have never sold any data shared by customers and we never will. 

**We don’t have access to login details.** The credentials provided are stored in AWS data centres in Sydney and Melbourne using AES-256 envelope encryption, meaning each connection is encrypted with its own key. The Basiq team has strict and limited access to data and systems, and never have access to banking credentials shared with us.

**We are as safe as any bank.** Our infrastructure is hosted and managed in an ISO 27001, SOC 1 & SOC 2, PCI Level 1, FISMA Moderate and SOX certified data centre... Put simply: your data is stored in the same way as data in the most highly regulated organisations around the world.

 

# How data is shared

BASIQ provides partners with a comprehensive suite of access methods to aggregate financial data efficiently. These options empower partners to retrieve and utilise data from various sources, enabling the development of innovative financial solutions tailored to their clients' needs.

The **Web Connector**, also known as "screen scraping," securely shares login credentials to access a bank's internet banking portal and extract a user's accounts and transactions. While effective, this method can be slower and susceptible to changes in the bank's portal, often prompting banks to reinforce security measures.

BASIQ offers two versions of its API to ensure partners have flexible and adaptable data access options. Version 2 exclusively supports **Digital Data Capture (DDC)**, where data is accessed through screen scraping. In contrast, Version 3 supports both DDC and the **Consumer Data Right (CDR)**, enabling partners to seamlessly switch between methods and ensuring compliance with evolving data access standards and regulations.

Open Banking provides partners with secure access to bank account data through standardised APIs. As an Accredited Data Recipient under the **Consumer Data Right (CDR)**, BASIQ ensures compliance with Open Banking regulations, offering direct access to account information, transaction history, and more from financial institutions. This method promotes compatibility and simplifies data aggregation across multiple banking platforms, empowering partners to offer comprehensive financial services.

**Statement Integration** enables partners to aggregate financial data from uploaded statements. Partners can effortlessly upload documents in various formats, such as PDFs or CSV files, to the BASIQ platform. With advanced parsing technology, the platform automatically extracts key data points, including transaction details, account balances, and metadata. This method offers unparalleled flexibility and convenience in handling diverse data sources, speeding up integration and allowing rapid deployment of financial solutions.

> By offering these diverse access methods, BASIQ ensures that its partners are equipped to handle modern financial data requirements effectively, adapting to the latest industry standards and consumer expectations.
