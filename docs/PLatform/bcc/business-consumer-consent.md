---
title: Business Consumer Consent
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
# Overview

Business Consumer Consent (BCC) within Australia's Consumer Data Right (CDR) expands data sharing options for business consumers. This document outlines integrating Basiq's consent UI into a service provider's platform, facilitating secure and compliant data sharing with business consumers. Before proceeding with integration steps, let's explore how to interact with the BCC. 

## What is Business Consumer Consent?

Business Consumer Consent allows businesses to share financial data with a broader range of service providers beyond the traditional "Trusted Adviser" list. This includes professionals such as bookkeepers, finance brokers, insurance brokers, and business coaches. By providing consent, businesses can access a wider array of financial services and applications to streamline operations and make more informed decisions.

To interact with the Business Consumer Consent UI, partners can configure various aspects through the Customiser. These include setting the Brand, purpose, scope, consent period, and data retrieval period. Additionally, it's essential to integrate consent management and re-authorization as mandatory steps in the integration process.

### Key Benefits:

 **Data Sharing:** Gain flexibility to share financial data with a broader range of service providers, enabling access to a wider array of financial services and applications.

**Financial Management:** Streamline financial administration processes, including payroll, invoicing, payments, accounting, and tax preparation, with access to innovative tools and services.

**Access to Funding Options**: Unlock opportunities to access various funding options, including asset finance and business loans, by sharing bank statements with finance brokers.

**Compliance and Security**: Rest assured that data sharing is compliant with the latest regulations under the Consumer Data Right framework, ensuring the highest standards of data privacy and security.

## Integration Steps

**Create Business Application**

Create a Business application to initiate the integration process. Ensure that the business user possesses a valid Australian Business Number (ABN) or Australian Company Number (ACN) before proceeding. Use Basiq's API to create a business user profile with the required attributes.

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(54.55861070911722% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/qzLNW0R7uvQW7JKq7g65?embed" title="Basiq - BCC Application" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

**Create Business User in Basiq**

* Ensure the business user has a valid Australian Business Number (ABN) or Australian Company Number (ACN).
* Use Basiq's API to [create a business user](https://api.basiq.io/reference/createuser) profile with the necessary attributes.

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(54.55861070911722% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/9Boto4N8SFoWrfTB93Hp?embed" title="Basiq - Create Business User" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

2. **Configure Consent Parameters**  

This includes setting the Brand Name, purpose, scope, consent period, and data retrieval period. This step ensures consistency and allows partners to customize the displayed name to their customers. 

> 📘 Note:
>
> Reach out to [support@basiq.io](mailto:support@basiq.io) to enable the app for BCC data access.

**Invite Business Consumer to Share Data**

Implement a pre-consent screen within your application, informing the customer about the data sharing process. Upon user agreement, redirect the customer to Basiq’s consent UI flow.

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(54.55861070911722% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/bIWnrcucH6rzsanet1Nw?embed" title="Business Consumer Consent Pre-consent" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

**Provide Business Consumer Consent**

* Integrate Basiq's enhanced consent UI, which is compliant with the latest CDR updates.
* The UI should allow the business consumer to:
  * Provide your Brand Name. 
  * Declare service use for business purposes.
  * Provide consent for data collection for up to 12 months.
  * Connect to all relevant financial institutions (DHs) and select bank accounts via the Basiq interface.

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(48.645833333333336% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/52qv95oOthdzSyeAeKlV?embed" title="Basiq - BCC" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

**Retrieve CDR Banking Data**

Upon consent, use Basiq’s API to retrieve CDR banking data. Implement secure data handling practices to maintain compliance with regulatory requirements.

**Share CDR Banking Data**

Share the retrieved CDR data within your application, adhering to the specified purposes and timeframes outlined in the consent provided.

> 📘 Note
>
> it's important to note that the *"Brand Name"* value is now required for all applications, including those not using BCC. This ensures consistency and allows partners to configure the displayed name to their customers.

### Additional Steps:

**Manage Consent and Authorization**: Use `action=manage` to handle consent and authorization journey, you can read more about managing consent [here](https://api.basiq.io/docs/consent-ui#manage-consent-actionmanage). 

**Enable CDR Data:** Reach out to [support@basiq.io](mailto:support@basiq.io) to enable the app for CDR data access.
