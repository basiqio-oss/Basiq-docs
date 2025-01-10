---
title: Consent Management Policy Template
deprecated: false
hidden: true
metadata:
  robots: index
---
This document explains how partners can integrate and present a Consent Management Portal on their websites, ensuring compliance with the Consumer Data Right (CDR) requirements. This guide includes details on managing user consents, data retention policies, data deletion, and de-identification.

## Introduction to the Consumer Data Right (CDR)

The Consumer Data Right (CDR) regulates the collection and handling of CDR data in line with privacy safeguards and rules that:

* Ensure your data is managed securely.
* Provide you with control over how your data is shared and used.

<Cards columns={2} style={{ marginTop: '20px' }}>
  <Card title="What is an Accredited Data Recipient (ADR)?" icon="fa-shield-alt" style={{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '20px', animation: 'fadeIn 1s ease-out' }}>
    <p style={{ fontSize: '16px', color: '#003366' }}>
      An **Accredited Data Recipient (ADR)** is an organization approved under the CDR framework to receive and manage consumer data securely. ADRs are required to adhere to strict privacy and security rules, ensuring that the consumer's data is used only with their consent.
    </p>

    <ul style={{ color: '#003366', listStyleType: 'circle', paddingLeft: '20px' }}>
      <li>Adhere to transparent disclosure of data usage.</li>
      <li>Ensure secure storage and transfer of consumer data.</li>
      <li>Implement privacy safeguards for data sharing based on user consent.</li>
    </ul>
  </Card>

  <Card title="Key User Benefits" icon="fa-check-circle" style={{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '20px', animation: 'fadeIn 2s ease-out' }}>
    <ul style={{ fontSize: '16px', color: '#003366' }}>
      <li><strong>Choice and Control:</strong> Users decide what data to share, how it’s used, and who can access it.</li>
      <li><strong>Manage Consent:</strong> Users can view, modify, or revoke their consents at any time.</li>
      <li><strong>Data Deletion Requests:</strong> Users can request deletion or de-identification of their personal data.</li>
    </ul>
  </Card>

  <Cards />

  <Cards columns={2} style={{ marginTop: '20px' }} />

  <Card title="How Data is Used" icon="fa-cogs" style={{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '20px', animation: 'fadeIn 3s ease-out' }}>
    <div style={{ fontSize: '16px', fontWeight: 'bold', color: '#003366' }}>
      Data collected under the CDR framework is used for various purposes, all based on user consent.
    </div>

    <ul style={{ color: '#003366', listStyleType: 'circle', paddingLeft: '20px' }}>
      <li><strong>Personalized Solutions:</strong> Tailoring recommendations based on user activities.</li>
      <li><strong>Operational Purposes:</strong> Detecting fraud, preventing abuse, and performing analytical reporting using de-identified data.</li>
      <li><strong>Communication:</strong> Sending updates, notifications, or support for services related to the user's preferences.</li>
    </ul>
  </Card>

  <Card title="" icon="fa-user">
    <img src="https://i0.wp.com/greener.com.au/wp-content/uploads/2023/06/CDR-2.png" />
  </Card>
</Cards>

<Accordion title="Data Security" icon="fa-lock" style={{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px', animation: 'fadeIn 2s ease-out' }}>
  <div style={{ fontSize: '16px', fontWeight: 'bold', color: '#003366' }}>
    It’s important to ensure that data is securely managed, following strict protocols for storage, encryption, and access.
  </div>

  <ul style={{ color: '#003366', listStyleType: 'circle', paddingLeft: '20px' }}>
    <li><strong>Storage:</strong> All data must be securely stored in Australia.</li>
    <li><strong>Encryption:</strong> Encrypt all CDR data in transit and at rest.</li>
    <li><strong>Access Control:</strong> Limit data access to authorized personnel only.</li>
    <li><strong>Audits:</strong> Regular audits ensure compliance with data security practices.</li>
  </ul>
</Accordion>

## Consent Management

To support the proper management of user consent in compliance with the Consumer Data Right (CDR) regulations, partners have two main options for implementing consent management:

\<Tabs style=\{\{ animation: 'fadeIn 3s ease-out' }}>
&#x20; \<Tab title="1. Using the Basiq Dashboard">
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

&#x20;     \<div style=\{\{ position: 'relative', paddingBottom: 'calc(50.161117078410314% + 41px)', height: '0', width: '100%' }}>
&#x20;                 \<iframe
&#x20;                   src="https\://demo.arcade.software/xfi9ECT8ilSRYF2gzsHb?embed\&embed\_mobile=tab\&embed\_desktop=inline\&show\_copy\_link=true"
&#x20;                   title="Partners Revoking Consent"
&#x20;                   frameBorder="0"
&#x20;                   loading="lazy"
&#x20;                   webkitallowfullscreen
&#x20;                   mozallowfullscreen
&#x20;                   allowFullScreen
&#x20;                   allow="clipboard-write"
&#x20;                   style=\{\{ position: 'absolute', top: '0', left: '0', width: '100%', height: '100%', colorScheme: 'light' }}
&#x20;                 />
&#x20;               \</div>                                                                                                                             \<div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;">

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

&#x20; \<Tab title="2. Using the action=manage Parameter">
&#x20;   \<Accordion title="How it Works" icon="fa-link" style=\{\{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px', animation: 'fadeIn 2s ease-out' }}>
&#x20;     \<p style=\{\{ fontSize: '16px', color: '#003366' }}>
&#x20;       The action=manage parameter directs users to the Consent Management Portal (CMP), where they can manage and revoke their consents directly.
&#x20;     \</p>

&#x20;     \<HTMLBlock>\{\`
&#x20;                                                                                                                                                       \<div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;">
&#x20;                                                                                                                                                         \<iframe src="https\://demo.arcade.software/Wad1ic93gwfM3NQFdMJ3?embed" title="Basiq | action=manage" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;">\</iframe>
&#x20;                                                                                                                                                       \</div>
&#x20;     \`}\</HTMLBlock>
&#x20;   \</Accordion>
&#x20; \</Tab>
\</Tabs>

\<Accordion title="Consent Management Details" icon="fa-info-circle">
&#x20; Users can view and manage their existing consents, including expiry details and connected institutions.
\</Accordion>

\<Cards columns=\{3}>
&#x20; \<Card title="View Consent" href="/consent/view" icon="fa-eye">
&#x20;   Review active consents and details.
&#x20; \</Card>

&#x20; \<Card title="Revoke Consent" href="/consent/manage" icon="fa-times-circle">
&#x20;   Revoke individual or all consents.
&#x20; \</Card>

&#x20; \<Card title="Support" href="/contact" icon="fa-envelope">
&#x20;   Contact support for assistance.
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