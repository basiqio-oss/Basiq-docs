---
title: TA
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
The Trusted Advisor (TA) access model enables qualified professionals to securely access consumer data for financial advice or related services under the Consumer Data Right (CDR). 

## Overview

The Trusted Advisor access model allows organisations or individuals to access consumer data for providing financial advice. Partners who qualify as Trusted Advisors can be granted access to the Consumer Data Right (CDR) platform under Basiq. Trusted Advisors are responsible for ensuring that their usage of consumer data complies with CDR regulations, whether operating as an individual or on behalf of an organization.

## Definition of a Trusted Advisor

A Trusted Advisor is a professional or organization that qualifies under CDR rules to access and use consumer financial data. Trusted Advisors include:

* Accountants
* Financial Brokers
* Financial Advisors
* Legal Professionals
* Tax Agents
* Financial Counselling Agencies

## Key Features of Trusted Advisor Access

### **Direct Data Access from Basiq**:

Trusted Advisor details (e.g., name, reference ID, and type) must be submitted directly within the application details.\
The TA details cannot be modified or passed dynamically via an API token. This ensures that all data comes directly from Basiq's secure platform, maintaining compliance with CDR rules and safeguarding user privacy.

<HTMLBlock>{`
<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(50.18807092960774% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/8J9a5bQBnoBgV6arTjFo?embed&embed_mobile=tab&embed_desktop=inline" title="Basiq - Trusted Advisor Direct" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->
`}</HTMLBlock>

#### **Consent Customizer Limitations**:

The Consent Customizer, which manages the user-facing consent flow, does not allow for editing certain elements for TAIndividual applications. Specifically:

1. Header image, disclosure of supporting parties, brand name, and title/subtitle text cannot be changed.
2. The consent screen will use Basiq branding throughout to ensure consistency.

<HTMLBlock>{`
<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(50.18807092960774% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/9ccPc0f4U2DNFqX1sF7q?embed&embed_mobile=tab&embed_desktop=inline" title="verified - TA Direct " frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->
`}</HTMLBlock>

#### **Pre-Consent User Experience**:

Given the branding restrictions, we recommend that customers implement an introductory pre-consent screen. This screen should inform users that their consent is being handled through a partnership with Basiq (e.g., "Piper partners with Basiq to securely import your bank transactions"). This step ensures transparency before users are redirected to the Basiq-branded consent flow.

### **Trusted Advisor Access via PRM**:

The Trusted Advisor access model through a PRM allows organizations to access consumer data for providing financial advice while operating under their own software product. Trusted Advisors using this model must follow specific guidelines to ensure compliance with the Consumer Data Right (CDR) regulations.

For Trusted Advisor access via PRM, customers may or may not provide their Trusted Advisor information within the application details. Basiq does not need to validate these values, as the customer must operate as a PRM using their own software product.

**Consent Customizer**: The Consent Customizer allows editing of all fields, enabling customers to customize the user-facing consent flow according to their requirements.

#### **Methods for Providing Trusted Advisor Values**:

Partners can supply Trusted Advisor (TA) values to be presented to the end user and stored in their consent using two different methods:

1. **Dashboard Values**: An Administrator can provide the Trusted Advisor details directly within the application settings in the Basiq Dashboard. These values will be displayed to the end user and stored in their consent.
2. **Token Values**: Customers can also pass Trusted Advisor values dynamically via API tokens. However, if the override toggle is enabled in the Dashboard, the predefined values will always take precedence over token values, ensuring that the correct details are consistently used for all Trusted Advisors under a specific application.

### **Verification by the Legal Team**:

All submitted Trusted Advisor information must be reviewed and verified by Basiq’s Legal team. The application will only proceed once this verification is complete. To maintain compliance, applications will not be enabled for Open Banking or other CDR data access until this verification has been successfully performed.

## Token Endpoint Extension

In order to support the Trusted Advisor model for partners, Basiq has extended the POST `/token` endpoint for requests with the scope "CLIENT\_ACCESS." The new organisation fields should be included in the request body as follows:

```json body
{
    "scope": "CLIENT_ACCESS", 
    "userId": "10be99c6-1944-4552-bd6f-08d893875179",
    "orgName": "Accountants XYZ Pty Ltd",
    "orgRefID": "0123456789",
    "orgRefType": "ABN",
    "orgType": "Financial Broker"
}
```

The supported values for the orgRefType field are `ABN`, `AFSL`, and `ACN`.

The supported values for the orgType field are `Accountant`, `Financial Broker`, `Financial Advisor`, `Legal Professional`, `Tax Agent`, and `Financial Counselling Agency`.

You can use this token to initiate your consent UI and resume the operation. If you have any questions or need further assistance, please contact our support team
