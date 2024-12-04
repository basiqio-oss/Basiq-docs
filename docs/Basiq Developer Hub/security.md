---
title: Security
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
  pages:
    - type: link
      title: Encryption, Protection and Data Hashing
      url: https://api.basiq.io/docs/security
---
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6c2e4ae-Group_2061.svg",
        "Group 2061.svg",
        1188,
        616,
        "#000217"
      ],
      "sizing": "full"
    }
  ]
}
[/block]
&nbsp;

# First things first
**We can’t do anything with users money.** All access is read-only, meaning we can see accounts and transactions to report on them, but are unable to perform any actions on behalf of the user. 

**We don’t hold onto, or sell, data.** When an application or service no longer needs access to the data then it’s as simple as letting us know, after which it is immediately deleted. We have never sold any data shared by customers and we never will. 

**We don’t have access to login details.** The credentials provided are stored in AWS data centres in Sydney and Melbourne using AES-256 envelope encryption, meaning each connection is encrypted with its own key. The Basiq team has strict and limited access to data and systems, and never have access to banking credentials shared with us.

**We are as safe as any bank. **Our infrastructure is hosted and managed in an ISO 27001, SOC 1 & SOC 2, PCI Level 1, FISMA Moderate and SOX certified data centre... Put simply: your data is stored in the same way as data in the most highly regulated organisations around the world.

&nbsp;

# How data is shared
Currently there are two ways to share financial data with Basiq 
1. Granting read-only access to your internet banking using digital data capture.
2. Providing a downloaded PDF bank statement (less convenient and secure).

With the introduction of the Consumer Data Rights (CDR), specifically in the banking sector, The Australian Government is allowing customers to request their data be shared with trusted recipients. The good news, is that [Basiq is an Accredited Data Recipient](https://blog.basiq.io/basiq-launches-cdr-data-holder-and-data-recipient-solution/), meaning we are open and ready to consume CDR data as it becomes available. In the meantime, Basiq will dynamically switch to newly available datasets and increase the uptake of Open Banking APIs.