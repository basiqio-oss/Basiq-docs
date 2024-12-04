---
title: Identity
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
### Introduction

Basiq provides powerful identity solutions designed to enable developers to seamlessly integrate banking data retrieval and identity verification functionalities into their applications. With Basiq's Identity Solutions, developers can empower users to connect their bank accounts securely, retrieve identity information from their banks, and utilise this data for various identity verification services.

This developer guide focuses on utilising Basiq's Identity APIs to retrieve identity information associated with a user's bank account(s). It assumes that users have already been set up within your application, and consent has been obtained for accessing their financial data.

### Integration Overview

Before integrating Basiq's Identity APIs into your application, ensure you have completed the steps outlined in [Integration Overview](doc:integration-overview) to setup a user and guide them through the consent and retrieve their financial data from their preferred financial institution.

Once users are set up and their financial data is retrieved successfully, you can proceed to access their identity information using Basiq's Identity APIs.

### Accessing Identity Information

Basiq's Identity APIs allow you to retrieve identity information associated with a specific user. The following endpoints can be used for accessing identity data:

**List User Identities:** The details of this API endpoint can be found at [Retrieve identities](ref:getuseridentities). The result of this API is a list of all the user's identities across all the financial institutions they have consented your application to access

**Get User Identity:** The details of this API endpoint can be found at [Retrieve an identity](ref:getuseridentity). The result of this API is the user's identity details for a specific identity object tied to a single financial institution.

### Conclusion

By following the instructions provided in this guide, developers can easily integrate Basiq's Identity APIs into their applications to retrieve identity information associated with users' financial data. Accessing and leveraging this identity data opens up possibilities for enhancing offerings relating to identity verification, KYC processes, risk assessment, and personalised user experiences within your application.
