---
title: Consent Management Policy
fullscreen: false
hidden: true
---
<Accordion title="Introduction to the Consumer Data Right (CDR)" icon="fa-info-circle" style={{ backgroundColor: '#f0f8ff', color: '#003366', borderRadius: '8px', padding: '10px' }}>
  <div style={{ fontSize: '16px', fontWeight: 'bold', color: '#003366' }}>
    The Consumer Data Right (CDR) regulates the collection and handling of CDR data in line with privacy safeguards and rules that:
  </div>

  <ul style={{ color: '#003366', listStyleType: 'circle', paddingLeft: '20px' }}>
    <li>Ensure your data is managed securely.</li>
    <li>Provide you with control over how your data is shared and used.</li>
  </ul>
</Accordion>

<Cards columns={2}>
  <Card title="Key User Benefits" icon="fa-check-circle" style={{ backgroundColor: '#e6f7ff', color: '#0066cc', borderRadius: '8px', padding: '20px' }}>
    <ul style={{ fontSize: '16px', color: '#0066cc' }}>
      <li><strong>Choice and Control:</strong> Users decide what data to share, how it’s used, and who can access it.</li>
      <li><strong>Manage Consent:</strong> Users can view, modify, or revoke their consents at any time.</li>
      <li><strong>Data Deletion Requests:</strong> Users can request deletion or de-identification of their personal data.</li>
    </ul>
  </Card>

  <Card title="What is an Accredited Data Recipient (ADR)?" icon="fa-shield-alt" style={{ backgroundColor: '#dff0d8', color: '#4cae4c', borderRadius: '8px', padding: '20px' }}>
    <p style={{ fontSize: '16px', color: '#4cae4c' }}>
      An **Accredited Data Recipient (ADR)** is an organization approved under the CDR framework to receive and manage consumer data securely.
    </p>

    <ul style={{ color: '#4cae4c', listStyleType: 'circle', paddingLeft: '20px' }}>
      <li>Transparent disclosure of how data is used.</li>
      <li>Secure storage and transfer of consumer data.</li>
      <li>Privacy safeguards ensuring data is only used as consented by the user.</li>
    </ul>
  </Card>
</Cards>

<Accordion title="Types of Data Collected" icon="fa-database" style={{ backgroundColor: '#fff3e6', color: '#ff6600', borderRadius: '8px', padding: '10px' }}>
  <div style={{ fontSize: '16px', fontWeight: 'bold', color: '#ff6600' }}>
    With user consent, ADRs may collect the following types of data:
  </div>

  <ul style={{ color: '#ff6600', listStyleType: 'circle', paddingLeft: '20px' }}>
    <li><strong>Personal Information</strong>: Full Name, Contact Details, Occupation</li>
    <li><strong>Transaction Data</strong>: Details about purchases, payments, associated metadata.</li>
    <li><strong>De-Identified Data</strong>: Data stripped of personally identifiable information for analytics and reporting.</li>
  </ul>
</Accordion>

<Accordion title="How Data is Used" icon="fa-cogs" style={{ backgroundColor: '#f8f8f8', color: '#007bff', borderRadius: '8px', padding: '10px' }}>
  <div style={{ fontSize: '16px', fontWeight: 'bold', color: '#007bff' }}>
    Example framework for the usage of CDR data:
  </div>

  <ul style={{ color: '#007bff', listStyleType: 'circle', paddingLeft: '20px' }}>
    <li><strong>Providing Personalised Solutions</strong>: Tailoring recommendations based on user activities.</li>
    <li><strong>Operational Purposes</strong>: Fraud detection, prevention, and analytical reporting using de-identified data.</li>
    <li><strong>Communication</strong>: Sending updates, notifications, or support for services.</li>
  </ul>
</Accordion>

<Accordion title="Data Security" icon="fa-lock" style={{ backgroundColor: '#f8f9fa', color: '#343a40', borderRadius: '8px', padding: '10px' }}>
  <div style={{ fontSize: '16px', fontWeight: 'bold', color: '#343a40' }}>
    Ensure compliance with these practices:
  </div>

  <ul style={{ color: '#343a40', listStyleType: 'circle', paddingLeft: '20px' }}>
    <li><strong>Storage</strong>: All data must be stored securely in Australia.</li>
    <li><strong>Encryption</strong>: Encrypt all CDR data in transit and at rest.</li>
    <li><strong>Access Control</strong>: Limit data access to authorized personnel or systems.</li>
    <li><strong>Audits</strong>: Regularly audit data handling practices.</li>
  </ul>
</Accordion>

<Tabs>
  <Tab title="1. Using the Basiq Dashboard for Consent Management">
    <Accordion title="A. Partner Revoking Consent on Behalf of Users" icon="fa-user-cog" style={{ backgroundColor: '#e0f7fa', color: '#00796b', borderRadius: '8px', padding: '10px' }}>
      <p style={{ fontSize: '16px', color: '#00796b' }}>
        Partners can access the Basiq dashboard and revoke consent on behalf of users when they are unable to do so themselves.
      </p>

      <ul style={{ color: '#00796b', listStyleType: 'circle', paddingLeft: '20px' }}>
        <li>Log into the Basiq dashboard.</li>
        <li>Navigate to the "Users" section.</li>
        <li>Locate the user whose consent needs to be revoked.</li>
        <li>Click to revoke consent.</li>
      </ul>
    </Accordion>

    <Accordion title="B. User Revoking Consent Directly" icon="fa-user" style={{ backgroundColor: '#e8f5e9', color: '#388e3c', borderRadius: '8px', padding: '10px' }}>
      <p style={{ fontSize: '16px', color: '#388e3c' }}>
        Partners can send a URL to the user from the Basiq dashboard, directing them to the consent management interface where they can revoke consent independently.
      </p>

      <ul style={{ color: '#388e3c', listStyleType: 'circle', paddingLeft: '20px' }}>
        <li>Generate a URL link from the Basiq dashboard.</li>
        <li>Send the link to the user (via email or other methods).</li>
        <li>The user reviews their consents and revokes them.</li>
      </ul>
    </Accordion>
  </Tab>

  <Tab title="2. Using the action=manage Parameter for Consent Management">
    <Accordion title="How it Works" icon="fa-link" style={{ backgroundColor: '#f5f5f5', color: '#8e24aa', borderRadius: '8px', padding: '10px' }}>
      <p style={{ fontSize: '16px', color: '#8e24aa' }}>
        Partners can send a link with the `action=manage` parameter to allow users to manage their consents directly.
      </p>

      <HTMLBlock>{`
              <div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;">
                <iframe src="https://demo.arcade.software/Wad1ic93gwfM3NQFdMJ3?embed" title="Basiq | action=manage" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe>
              </div>
      `}</HTMLBlock>
    </Accordion>
  </Tab>
</Tabs>

<Cards columns={4}>
  <Card title="Consent Management Details" href="/consent/manage" icon="fa-info-circle" style={{ backgroundColor: '#ffe0b2', color: '#e65100', borderRadius: '8px', padding: '20px' }}>
    Users can view and manage their existing consents, including expiry details and connected institutions.
  </Card>

  <Card title="View Consent" href="/consent/view" icon="fa-eye" style={{ backgroundColor: '#ffccbc', color: '#d32f2f', borderRadius: '8px', padding: '20px' }}>
    Review active consents and details.
  </Card>

  <Card title="Revoke Consent" href="/consent/manage" icon="fa-times-circle" style={{ backgroundColor: '#ffebee', color: '#c62828', borderRadius: '8px', padding: '20px' }}>
    Revoke individual or all consents.
  </Card>

  <Card title="Support" href="/contact" icon="fa-envelope" style={{ backgroundColor: '#c8e6c9', color: '#388e3c', borderRadius: '8px', padding: '20px' }}>
    Contact support for assistance.
  </Card>

  <Card title="Learn More" href="/info" icon="fa-book" style={{ backgroundColor: '#f3e5f5', color: '#8e24aa', borderRadius: '8px', padding: '20px' }}>
    Understand how we use your data.
  </Card>
</Cards>

<Accordion title="Data Retention and De-identification" icon="fa-cogs" style={{ backgroundColor: '#e3f2fd', color: '#1976d2', borderRadius: '8px', padding: '10px' }}>
  <Accordion title="Deletion Process" icon="fa-trash" style={{ backgroundColor: '#f1f8e9', color: '#388e3c', borderRadius: '8px', padding: '10px' }}>
    * Securely delete user data when consent is withdrawn.
    * Inform third-party data processors to delete or de-identify shared data.
  </Accordion>

  <Accordion title="De-identification" icon="fa-paint-brush" style={{ backgroundColor: '#fffde7', color: '#f57f17', borderRadius: '8px', padding: '10px' }}>
    * Stripping identifiable information (e.g., user ID, timestamps).
    * Retaining only aggregated, anonymised insights.
  </Accordion>

  <Accordion title="Retention Policy" icon="fa-clipboard-check" style={{ backgroundColor: '#e8f5e9', color: '#388e3c', borderRadius: '8px', padding: '10px' }}>
    * Partner Responsibility: If the retention toggle is OFF, partners must delete the data from their systems while ensuring Basiq deletes user data.
  </Accordion>
</Accordion>

<Accordion title="User Rights" icon="fa-user-shield" style={{ backgroundColor: '#f3e5f5', color: '#8e24aa', borderRadius: '8px', padding: '10px' }}>
  Ensure your platform enables the following:

  <ul style={{ fontSize: '16px', color: '#8e24aa', listStyleType: 'circle', paddingLeft: '20px' }}>
    <li><strong>Access to Data:</strong> Users can request a copy of their data.</li>
    <li><strong>Correction of Errors:</strong> Users can correct inaccuracies.</li>
    <li><strong>Control:</strong> Allow users to manage consents and data sharing preferences.</li>
    <li><strong>Deletion Requests:</strong> Users can request permanent deletion of their data.</li>
  </ul>
</Accordion>