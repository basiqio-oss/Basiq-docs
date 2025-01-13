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

<br />

import React from 'react';

const ResponsiveCardsAccordion = () => \{
&#x20; return (
&#x20;   \<div>
&#x20;     \<div
&#x20;       style=\{\{
&#x20;         display: 'grid',
&#x20;         gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))',
&#x20;         gap: '20px',
&#x20;         marginTop: '20px',
&#x20;       }}
&#x20;     \>
&#x20;       \{/\* Card 1 \*/}
&#x20;       \<div
&#x20;         title="What is an Accredited Data Recipient (ADR)?"
&#x20;         icon="fa-shield-alt"
&#x20;         style=\{\{
&#x20;           backgroundColor: '#ffffff',
&#x20;           color: '#003366',
&#x20;           borderRadius: '8px',
&#x20;           padding: '20px',
&#x20;           animation: 'fadeIn 1s ease-out',
&#x20;         }}
&#x20;       \>
&#x20;         \<p>
&#x20;           An \<strong>Accredited Data Recipient (ADR)\</strong> is an organization approved under the CDR framework to receive and manage consumer data securely. ADRs are required to adhere to strict privacy and security rules, ensuring that the consumer's data is used only with their consent.
&#x20;         \</p>
&#x20;         \<ul>
&#x20;           \<li>Adhere to transparent disclosure of data usage.\</li>
&#x20;           \<li>Ensure secure storage and transfer of consumer data.\</li>
&#x20;           \<li>Implement privacy safeguards for data sharing based on user consent.\</li>
&#x20;         \</ul>
&#x20;       \</div>

&#x20;       \{/\* Card 2 \*/}
&#x20;       \<div
&#x20;         title="Key User Benefits"
&#x20;         icon="fa-check-circle"
&#x20;         style=\{\{
&#x20;           backgroundColor: '#ffffff',
&#x20;           color: '#003366',
&#x20;           borderRadius: '8px',
&#x20;           padding: '20px',
&#x20;           animation: 'fadeIn 2s ease-out',
&#x20;         }}
&#x20;       \>
&#x20;         \<ul>
&#x20;           \<li>\<strong>Choice and Control:\</strong> Users decide what data to share, how it’s used, and who can access it.\</li>
&#x20;           \<li>\<strong>Manage Consent:\</strong> Users can view, modify, or revoke their consents at any time.\</li>
&#x20;           \<li>\<strong>Data Deletion Requests:\</strong> Users can request deletion or de-identification of their personal data.\</li>
&#x20;         \</ul>
&#x20;       \</div>
&#x20;     \</div>

&#x20;     \{/\* Card 3 \*/}
&#x20;     \<div
&#x20;       style=\{\{
&#x20;         display: 'grid',
&#x20;         gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))',
&#x20;         gap: '20px',
&#x20;         marginTop: '20px',
&#x20;       }}
&#x20;     \>
&#x20;       \<div
&#x20;         title="How Data is Used"
&#x20;         icon="fa-cogs"
&#x20;         style=\{\{
&#x20;           borderRadius: '8px',
&#x20;           padding: '20px',
&#x20;           animation: 'fadeIn 3s ease-out',
&#x20;         }}
&#x20;       \>
&#x20;         \<div>
&#x20;           Data collected under the CDR framework is used for various purposes, all based on user consent.
&#x20;         \</div>
&#x20;         \<ul>
&#x20;           \<li>\<strong>Personalized Solutions:\</strong> Tailoring recommendations based on user activities.\</li>
&#x20;           \<li>\<strong>Operational Purposes:\</strong> Detecting fraud, preventing abuse, and performing analytical reporting using de-identified data.\</li>
&#x20;           \<li>\<strong>Communication:\</strong> Sending updates, notifications, or support for services related to the user's preferences.\</li>
&#x20;         \</ul>
&#x20;       \</div>

&#x20;       \{/\* Card with Image \*/}
&#x20;       \<div title="" icon="fa-user">
&#x20;         \<img
&#x20;           src="https\://i0.wp.com/greener.com.au/wp-content/uploads/2023/06/CDR-2.png"
&#x20;           alt="CDR Image"
&#x20;           style=\{\{
&#x20;             width: '100%',
&#x20;             height: 'auto',
&#x20;             borderRadius: '8px',
&#x20;           }}
&#x20;         />
&#x20;       \</div>
&#x20;     \</div>

&#x20;     \{/\* Accordion \*/}
&#x20;     \<div
&#x20;       style=\{\{
&#x20;         borderRadius: '8px',
&#x20;         padding: '15px',
&#x20;         animation: 'fadeIn 2s ease-out',
&#x20;         marginTop: '20px',
&#x20;       }}
&#x20;     \>
&#x20;       \<h3>Data Security\</h3>
&#x20;       \<div>
&#x20;         It’s important to ensure that data is securely managed, following strict protocols for storage, encryption, and access.
&#x20;       \</div>
&#x20;       \<ul>
&#x20;         \<li>\<strong>Storage:\</strong> All data must be securely stored in Australia.\</li>
&#x20;         \<li>\<strong>Encryption:\</strong> Encrypt all CDR data in transit and at rest.\</li>
&#x20;         \<li>\<strong>Access Control:\</strong> Limit data access to authorized personnel only.\</li>
&#x20;         \<li>\<strong>Audits:\</strong> Regular audits ensure compliance with data security practices.\</li>
&#x20;       \</ul>
&#x20;     \</div>

&#x20;     \{/\* Styles for mobile responsiveness \*/}
&#x20;     \<style>
&#x20;       \{\`
&#x20;         @media screen and (max-width: 768px) \{
&#x20;           div \{
&#x20;             grid-template-columns: 1fr; /\* Stack cards vertically on mobile \*/
&#x20;           }
&#x20;           div > div \{
&#x20;             padding: 15px;
&#x20;           }
&#x20;           img \{
&#x20;             width: 100%; /\* Make images responsive \*/
&#x20;           }
&#x20;         }

&#x20;         @media screen and (max-width: 480px) \{
&#x20;           div > div \{
&#x20;             padding: 10px;
&#x20;           }
&#x20;           h3 \{
&#x20;             font-size: 1.2rem; /\* Adjust heading font size \*/
&#x20;           }
&#x20;         }
&#x20;       \`}
&#x20;     \</style>
&#x20;   \</div>
&#x20; );
};

\< ResponsiveCardsAccordion />