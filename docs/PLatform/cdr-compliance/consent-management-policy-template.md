---
title: '# Consent Management Policy Template'
deprecated: false
hidden: true
metadata:
  robots: index
---
This document explains how partners can integrate and present a Consent Management Portal on their websites, ensuring compliance with the Consumer Data Right (CDR) requirements. This guide includes details on managing user consents, data retention policies, data deletion, and de-identification.

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

\<Tabs style=\{\{ animation: 'fadeIn 3s ease-out' }}>
&#x20; \<Tab title="1. Using the Basiq Dashboard for Consent Management">
&#x20;   \<Accordion title="A. Partner Revoking Consent on Behalf of Users" icon="fa-user-cog" style=\{\{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px', animation: 'fadeIn 3s ease-out' }}>
&#x20;     \<p style=\{\{ fontSize: '16px', color: '#003366' }}>
&#x20;       Partners can access the Basiq dashboard and revoke consent on behalf of users when needed.
&#x20;     \</p>

&#x20;     \<ul style=\{\{ color: '#003366', listStyleType: 'circle', paddingLeft: '20px' }}>
&#x20;       \<li>Log into the Basiq dashboard.\</li>
&#x20;       \<li>Navigate to the "Users" section.\</li>
&#x20;       \<li>Locate the user whose consent needs to be revoked.\</li>
&#x20;       \<li>Click to revoke consent.\</li>
&#x20;     \</ul>
&#x20;   \</Accordion>

&#x20;   \<Accordion title="B. User Revoking Consent Directly" icon="fa-user" style=\{\{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px', animation: 'fadeIn 4s ease-out' }}>
&#x20;     \<p style=\{\{ fontSize: '16px', color: '#003366' }}>
&#x20;       Partners can send a URL to the user from the Basiq dashboard, allowing them to revoke consent independently.
&#x20;     \</p>

&#x20;     \<ul style=\{\{ color: '#003366', listStyleType: 'circle', paddingLeft: '20px' }}>
&#x20;       \<li>Generate a URL link from the Basiq dashboard.\</li>
&#x20;       \<li>Send the link to the user (via email or other methods).\</li>
&#x20;       \<li>The user reviews their consents and revokes them.\</li>
&#x20;     \</ul>
&#x20;   \</Accordion>
&#x20; \</Tab>

&#x20; \<Tab title="2. Using the action=manage Parameter for Consent Management">
&#x20;   \<Accordion title="How it Works" icon="fa-link" style=\{\{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px', animation: 'fadeIn 2s ease-out' }}>
&#x20;     \<p style=\{\{ fontSize: '16px', color: '#003366' }}>
&#x20;       The \`action=manage\` parameter directs users to the Consent Management Portal (CMP), where they can manage and revoke their consents directly.
&#x20;     \</p>

&#x20;     \<HTMLBlock>\{\`
&#x20;                   \<div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;">
&#x20;                     \<iframe src="https\://demo.arcade.software/Wad1ic93gwfM3NQFdMJ3?embed" title="Basiq | action=manage" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;">\</iframe>
&#x20;                   \</div>
&#x20;     \`}\</HTMLBlock>
&#x20;   \</Accordion>
&#x20; \</Tab>
\</Tabs>

\<Cards columns=\{\{3}} style=\{\{ marginTop: '20px' }}>
&#x20; \<Card title="Consent Management Details" href="/consent/manage" icon="fa-info-circle" style=\{\{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '20px', animation: 'fadeIn 3s ease-out' }}>
&#x20;   Users can view and manage their existing consents, including expiry details and connected institutions.
&#x20; \</Card>

&#x20; \<Card title="View Consent" href="/consent/view" icon="fa-eye" style=\{\{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '20px', animation: 'fadeIn 4s ease-out' }}>
&#x20;   Review active consents and details.
&#x20; \</Card>

&#x20; \<Card title="Revoke Consent" href="/consent/manage" icon="fa-times-circle" style=\{\{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '20px', animation: 'fadeIn 5s ease-out' }}>
&#x20;   Revoke individual or all consents.
&#x20; \</Card>
\</Cards>

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