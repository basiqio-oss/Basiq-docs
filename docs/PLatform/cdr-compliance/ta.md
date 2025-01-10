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

\<Cards style=\{\{ marginTop: '20px' }}>
&#x20; \<Card title="What is an Accredited Data Recipient (ADR)?" icon="fa-shield-alt" style=\{\{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '20px', animation: 'fadeIn 1s ease-out' }}>
&#x20;   \<p style=\{\{ fontSize: '16px', color: '#003366' }}>
&#x20;     An \*\*Accredited Data Recipient (ADR)\*\* is an organization approved under the CDR framework to receive and manage consumer data securely. ADRs are required to adhere to strict privacy and security rules, ensuring that the consumer's data is used only with their consent.
&#x20;   \</p>

&#x20;   \<ul style=\{\{ color: '#003366', listStyleType: 'circle', paddingLeft: '20px' }}>
&#x20;     \<li>Adhere to transparent disclosure of data usage.\</li>
&#x20;     \<li>Ensure secure storage and transfer of consumer data.\</li>
&#x20;     \<li>Implement privacy safeguards for data sharing based on user consent.\</li>
&#x20;   \</ul>
&#x20; \</Card>

&#x20; \<Card title="Key User Benefits" icon="fa-check-circle" style=\{\{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '20px', animation: 'fadeIn 2s ease-out' }}>
&#x20;   \<ul style=\{\{ fontSize: '16px', color: '#003366' }}>
&#x20;     \<li>\<strong>Choice and Control:\</strong> Users decide what data to share, how it’s used, and who can access it.\</li>
&#x20;     \<li>\<strong>Manage Consent:\</strong> Users can view, modify, or revoke their consents at any time.\</li>
&#x20;     \<li>\<strong>Data Deletion Requests:\</strong> Users can request deletion or de-identification of their personal data.\</li>
&#x20;   \</ul>
&#x20; \</Card>

&#x20; \<Card title="How Data is Used" icon="fa-cogs" style=\{\{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '20px', animation: 'fadeIn 3s ease-out' }}>
&#x20;   \<div style=\{\{ fontSize: '16px', fontWeight: 'bold', color: '#003366' }}>
&#x20;     Data collected under the CDR framework is used for various purposes, all based on user consent.
&#x20;   \</div>

&#x20;   \<ul style=\{\{ color: '#003366', listStyleType: 'circle', paddingLeft: '20px' }}>
&#x20;     \<li>\<strong>Personalized Solutions:\</strong> Tailoring recommendations based on user activities.\</li>
&#x20;     \<li>\<strong>Operational Purposes:\</strong> Detecting fraud, preventing abuse, and performing analytical reporting using de-identified data.\</li>
&#x20;     \<li>\<strong>Communication:\</strong> Sending updates, notifications, or support for services related to the user's preferences.\</li>
&#x20;   \</ul>
&#x20; \</Card>
\</Cards>

\<Accordion title="Data Security" icon="fa-lock" style=\{\{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px', animation: 'fadeIn 2s ease-out' }}>
&#x20; \<div style=\{\{ fontSize: '16px', fontWeight: 'bold', color: '#003366' }}>
&#x20;   It’s important to ensure that data is securely managed, following strict protocols for storage, encryption, and access.
&#x20; \</div>

&#x20; \<ul style=\{\{ color: '#003366', listStyleType: 'circle', paddingLeft: '20px' }}>
&#x20;   \<li>\<strong>Storage:\</strong> All data must be securely stored in Australia.\</li>
&#x20;   \<li>\<strong>Encryption:\</strong> Encrypt all CDR data in transit and at rest.\</li>
&#x20;   \<li>\<strong>Access Control:\</strong> Limit data access to authorized personnel only.\</li>
&#x20;   \<li>\<strong>Audits:\</strong> Regular audits ensure compliance with data security practices.\</li>
&#x20; \</ul>
\</Accordion>

\<Accordion title="A. Partner Revoking Consent on Behalf of Users" icon="fa-user-cog" style=\{\{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px', animation: 'fadeIn 3s ease-out' }}>
&#x20; \<p style=\{\{ fontSize: '16px', color: '#003366' }}>
&#x20;   Partners can access the Basiq dashboard and revoke consent on behalf of users when needed.
&#x20; \</p>

&#x20; \<ul style=\{\{ color: '#003366', listStyleType: 'circle', paddingLeft: '20px' }}>
&#x20;   \<li>Log into the Basiq dashboard.\</li>
&#x20;   \<li>Navigate to the "Users" section.\</li>
&#x20;   \<li>Locate the user whose consent needs to be revoked.\</li>
&#x20;   \<li>Click to revoke consent.\</li>
&#x20; \</ul>
\</Accordion>

\<Accordion title="B. User Revoking Consent Directly" icon="fa-user" style=\{\{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px', animation: 'fadeIn 4s ease-out' }}>
&#x20; \<p style=\{\{ fontSize: '16px', color: '#003366' }}>
&#x20;   Partners can send a URL to the user from the Basiq dashboard, allowing them to revoke consent independently.
&#x20; \</p>

&#x20; \<ul style=\{\{ color: '#003366', listStyleType: 'circle', paddingLeft: '20px' }}>
&#x20;   \<li>Generate a URL link from the Basiq dashboard.\</li>
&#x20;   \<li>Send the link to the user (via email or other methods).\</li>
&#x20;   \<li>The user reviews their consents and revokes them.\</li>
&#x20; \</ul>
\</Accordion>

\<Accordion title="Data Retention and De-identification" icon="fa-cogs" style=\{\{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px', animation: 'fadeIn 2s ease-out' }}>
&#x20; \<Accordion title="Deletion Process" icon="fa-trash" style=\{\{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px' }}>
&#x20;   Securely delete user data when consent is withdrawn. Inform third-party data processors to delete or de-identify shared data.
&#x20; \</Accordion>

&#x20; \<Accordion title="De-identification" icon="fa-paint-brush" style=\{\{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px' }}>
&#x20;   Stripping identifiable information (e.g., user ID, timestamps), while retaining only aggregated, anonymized insights.
&#x20; \</Accordion>

&#x20; \<Accordion title="Retention Policy" icon="fa-clipboard-check" style=\{\{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px' }}>
&#x20;   Partners must delete data from their systems, ensuring Basiq deletes user data when the retention toggle is OFF.
&#x20; \</Accordion>
\</Accordion>

\<Accordion title="User Rights" icon="fa-user-shield" style=\{\{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px', animation: 'fadeIn 3s ease-out' }}>
&#x20; \<div style=\{\{ fontSize: '16px', fontWeight: 'bold', color: '#003366' }}>
&#x20;   Users have the right to request:
&#x20; \</div>

&#x20; \<ul style=\{\{ color: '#003366', listStyleType: 'circle', paddingLeft: '20px' }}>
&#x20;   \<li>Deletion or de-identification of their data.\</li>
&#x20;   \<li>Export of their data in machine-readable format.\</li>
&#x20; \</ul>
\</Accordion>

&#x20; \<style>
&#x20;   /\* Dark Mode Styles \*/
&#x20;   body \{
&#x20;     background-color: #121212;
&#x20;     color: #e0e0e0;
&#x20;     font-family: Arial, sans-serif;
&#x20;     margin: 0;
&#x20;     padding: 0;
&#x20;   }

&#x20;   h1, h2, h3, p \{
&#x20;     color: #e0e0e0;
&#x20;   }

&#x20;   /\* Cards styling \*/
&#x20;   .card \{
&#x20;     background-color: #1f1f1f;
&#x20;     color: #e0e0e0;
&#x20;     border-radius: 8px;
&#x20;     padding: 20px;
&#x20;     margin: 15px 0;
&#x20;     box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
&#x20;   }

&#x20;   .card ul \{
&#x20;     list-style-type: circle;
&#x20;     padding-left: 20px;
&#x20;   }

&#x20;   .card a \{
&#x20;     color: #64b5f6;
&#x20;     text-decoration: none;
&#x20;   }

&#x20;   .card a:hover \{
&#x20;     text-decoration: underline;
&#x20;   }

&#x20;   .card-title \{
&#x20;     font-size: 18px;
&#x20;     font-weight: bold;
&#x20;     color: #64b5f6;
&#x20;     margin-bottom: 15px;
&#x20;   }

&#x20;   .card-icon \{
&#x20;     font-size: 20px;
&#x20;     margin-right: 10px;
&#x20;   }

&#x20;   /\* Accordion Styles \*/
&#x20;   .accordion \{
&#x20;     background-color: #333333;
&#x20;     color: #e0e0e0;
&#x20;     border-radius: 8px;
&#x20;     padding: 15px;
&#x20;     margin-top: 20px;
&#x20;     box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
&#x20;   }

&#x20;   .accordion-title \{
&#x20;     font-size: 18px;
&#x20;     font-weight: bold;
&#x20;     color: #64b5f6;
&#x20;     cursor: pointer;
&#x20;   }

&#x20;   .accordion-content \{
&#x20;     padding-left: 20px;
&#x20;     font-size: 16px;
&#x20;     margin-top: 10px;
&#x20;   }

&#x20;   .accordion ul \{
&#x20;     list-style-type: circle;
&#x20;   }

&#x20;   /\* Tabs \*/
&#x20;   .tabs \{
&#x20;     display: flex;
&#x20;     justify-content: space-around;
&#x20;     background-color: #333333;
&#x20;     padding: 10px 0;
&#x20;     border-radius: 8px;
&#x20;   }

&#x20;   .tab \{
&#x20;     color: #e0e0e0;
&#x20;     padding: 10px 15px;
&#x20;     cursor: pointer;
&#x20;     text-align: center;
&#x20;     flex: 1;
&#x20;   }

&#x20;   .tab:hover \{
&#x20;     background-color: #444444;
&#x20;     border-radius: 8px;
&#x20;   }

&#x20;   .tab-content \{
&#x20;     display: none;
&#x20;     padding: 20px;
&#x20;     background-color: #1f1f1f;
&#x20;     border-radius: 8px;
&#x20;     margin-top: 15px;
&#x20;   }

&#x20;   .tab-content.active \{
&#x20;     display: block;
&#x20;   }

&#x20;   /\* Buttons \*/
&#x20;   .btn \{
&#x20;     background-color: #64b5f6;
&#x20;     color: #121212;
&#x20;     border: none;
&#x20;     padding: 10px 15px;
&#x20;     border-radius: 8px;
&#x20;     cursor: pointer;
&#x20;     text-decoration: none;
&#x20;   }

&#x20;   .btn:hover \{
&#x20;     background-color: #2196f3;
&#x20;   }

&#x20;   /\* General Link Styling \*/
&#x20;   a \{
&#x20;     color: #64b5f6;
&#x20;   }

&#x20;   a:hover \{
&#x20;     text-decoration: underline;
&#x20;   }
&#x20; \</style>