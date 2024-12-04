---
title: Basiq platform components
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
The below diagram shows a simplified representation of the main components in the Basiq Platform. 

* A **Partner** will set up their "Application" in the platform. One Partner can have many Applications. This will define the list of Institutions and data sources the Application will support (e.g. will it support Open Banking data sources) and also the information to personalise the consent flow for a Consumer interacting with the Partner App.
* A **Consumer** will be redirected to the Basiq Consent Flow, they will provide Consent and this will be stored in the platform.
* A **Consumer** will then connect one or more Institutions under the Consent agreement.
* **The Basiq Platform** will then fetch the data from the institutions.
* **The Basiq Platform** will manage this consent ongoing both in the Basiq Platform and via event triggered notifications to the Partner platform.
* A **Partner** will retrieve the aggregate enhanced financial data via the Single Unified API capable of serving data from multiple data sources - Open Banking (CDR), Digital Data Capture (DDC), direct APIs, CSV and PDF uploads.
* **Consumers** will be able to manage their consent ongoing via the Basiq provided Consent Dashboard.

![1098](https://files.readme.io/1a93039-openbankingcomponents_1.svg "openbankingcomponents (1).svg")
