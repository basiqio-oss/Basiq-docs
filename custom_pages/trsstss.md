---
title: Consent Management Policy
fullscreen: false
hidden: true
---
<Accordion title="Introduction to the Consumer Data Right (CDR)" icon="fa-info-circle" style={{ backgroundColor: '#f0f8ff', color: '#003366', borderRadius: '8px', padding: '15px', animation: 'fadeIn 1s ease-out' }}>
  <div style={{ fontSize: '18px', fontWeight: 'bold', color: '#003366' }}>
    The Consumer Data Right (CDR) is designed to regulate the collection, handling, and sharing of consumer data under privacy safeguards. This framework empowers users with control over their personal data, ensuring secure management and sharing across various platforms.
  </div>

  <ul style={{ color: '#003366', listStyleType: 'circle', paddingLeft: '20px' }}>
    <li>Data is securely managed and controlled.</li>
    <li>Users have full control over how their data is shared and used.</li>
  </ul>
</Accordion>

<Cards columns={3} style={{ marginTop: '20px' }}>
  <Card title="Key User Benefits" icon="fa-check-circle" style={{ backgroundColor: '#e6f7ff', color: '#0066cc', borderRadius: '8px', padding: '20px', animation: 'fadeIn 2s ease-out' }}>
    <ul style={{ fontSize: '16px', color: '#0066cc' }}>
      <li><strong>Choice and Control:</strong> Users decide what data to share, how it’s used, and who can access it.</li>
      <li><strong>Manage Consent:</strong> Users can view, modify, or revoke their consents at any time.</li>
      <li><strong>Data Deletion Requests:</strong> Users can request deletion or de-identification of their personal data.</li>
    </ul>
  </Card>

  <Card title="What is an Accredited Data Recipient (ADR)?" icon="fa-shield-alt" style={{ backgroundColor: '#dff0d8', color: '#4cae4c', borderRadius: '8px', padding: '20px', animation: 'fadeIn 3s ease-out' }}>
    <p style={{ fontSize: '16px', color: '#4cae4c' }}>
      An **Accredited Data Recipient (ADR)** is an organization approved under the CDR framework to receive and manage consumer data securely.
    </p>

    <ul style={{ color: '#4cae4c', listStyleType: 'circle', paddingLeft: '20px' }}>
      <li>Transparent disclosure of how data is used.</li>
      <li>Secure storage and transfer of consumer data.</li>
      <li>Privacy safeguards ensuring data is only used as consented by the user.</li>
    </ul>
  </Card>

  <Card title="How Data is Used" icon="fa-cogs" style={{ backgroundColor: '#f8f8f8', color: '#007bff', borderRadius: '8px', padding: '20px', animation: 'fadeIn 4s ease-out' }}>
    <div style={{ fontSize: '16px', fontWeight: 'bold', color: '#007bff' }}>
      Here's how data can be used under the CDR framework:
    </div>

    <ul style={{ color: '#007bff', listStyleType: 'circle', paddingLeft: '20px' }}>
      <li><strong>Providing Personalised Solutions</strong>: Tailoring recommendations based on user activities.</li>
      <li><strong>Operational Purposes</strong>: Fraud detection, prevention, and analytical reporting using de-identified data.</li>
      <li><strong>Communication</strong>: Sending updates, notifications, or support for services.</li>
    </ul>
  </Card>
</Cards>

<Accordion title="Data Security" icon="fa-lock" style={{ backgroundColor: '#f8f9fa', color: '#343a40', borderRadius: '8px', padding: '15px', animation: 'fadeIn 2s ease-out' }}>
  <div style={{ fontSize: '16px', fontWeight: 'bold', color: '#343a40' }}>
    It’s important to ensure that data is securely managed, following strict protocols for storage, encryption, and access.
  </div>

  <ul style={{ color: '#343a40', listStyleType: 'circle', paddingLeft: '20px' }}>
    <li><strong>Storage:</strong> All data must be securely stored in Australia.</li>
    <li><strong>Encryption:</strong> Encrypt all CDR data in transit and at rest.</li>
    <li><strong>Access Control:</strong> Limit data access to authorized personnel only.</li>
    <li><strong>Audits:</strong> Regular audits ensure compliance with data security practices.</li>
  </ul>
</Accordion>

<Tabs style={{ animation: 'fadeIn 3s ease-out' }}>
  <Tab title="1. Using the Basiq Dashboard for Consent Management">
    <Accordion title="A. Partner Revoking Consent on Behalf of Users" icon="fa-user-cog" style={{ backgroundColor: '#e0f7fa', color: '#00796b', borderRadius: '8px', padding: '15px', animation: 'fadeIn 3s ease-out' }}>
      <p style={{ fontSize: '16px', color: '#00796b' }}>
        Partners can access the Basiq dashboard and revoke consent on behalf of users when needed.
      </p>

      <ul style={{ color: '#00796b', listStyleType: 'circle', paddingLeft: '20px' }}>
        <li>Log into the Basiq dashboard.</li>
        <li>Navigate to the "Users" section.</li>
        <li>Locate the user whose consent needs to be revoked.</li>
        <li>Click to revoke consent.</li>
      </ul>
    </Accordion>

    <Accordion title="B. User Revoking Consent Directly" icon="fa-user" style={{ backgroundColor: '#e8f5e9', color: '#388e3c', borderRadius: '8px', padding: '15px', animation: 'fadeIn 4s ease-out' }}>
      <p style={{ fontSize: '16px', color: '#388e3c' }}>
        Partners can send a URL to the user from the Basiq dashboard, allowing them to revoke consent independently.
      </p>

      <ul style={{ color: '#388e3c', listStyleType: 'circle', paddingLeft: '20px' }}>
        <li>Generate a URL link from the Basiq dashboard.</li>
        <li>Send the link to the user (via email or other methods).</li>
        <li>The user reviews their consents and revokes them.</li>
      </ul>
    </Accordion>
  </Tab>

  <Tab title="2. Using the action=manage Parameter for Consent Management">
    <Accordion title="How it Works" icon="fa-link" style={{ backgroundColor: '#f5f5f5', color: '#8e24aa', borderRadius: '8px', padding: '15px', animation: 'fadeIn 2s ease-out' }}>
      <p style={{ fontSize: '16px', color: '#8e24aa' }}>
        The `action=manage` parameter directs users to the Consent Management Portal (CMP), where they can manage and revoke their consents directly.
      </p>

      <HTMLBlock>{`
                                <div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;">
                                  <iframe src="https://demo.arcade.software/Wad1ic93gwfM3NQFdMJ3?embed" title="Basiq | action=manage" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe>
                                </div>
      `}</HTMLBlock>
    </Accordion>
  </Tab>
</Tabs>

<Cards columns={3} style={{ marginTop: '20px' }}>
  <Card title="Consent Management Details" href="/consent/manage" icon="fa-info-circle" style={{ backgroundColor: '#ffe0b2', color: '#e65100', borderRadius: '8px', padding: '20px', animation: 'fadeIn 3s ease-out' }}>
    Users can view and manage their existing consents, including expiry details and connected institutions.
  </Card>

  <Card title="View Consent" href="/consent/view" icon="fa-eye" style={{ backgroundColor: '#ffccbc', color: '#d32f2f', borderRadius: '8px', padding: '20px', animation: 'fadeIn 4s ease-out' }}>
    Review active consents and details.
  </Card>

  <Card title="Revoke Consent" href="/consent/manage" icon="fa-times-circle" style={{ backgroundColor: '#ffebee', color: '#c62828', borderRadius: '8px', padding: '20px', animation: 'fadeIn 5s ease-out' }}>
    Revoke individual or all consents.
  </Card>
</Cards>

<Accordion title="Data Retention and De-identification" icon="fa-cogs" style={{ backgroundColor: '#e3f2fd', color: '#1976d2', borderRadius: '8px', padding: '15px', animation: 'fadeIn 2s ease-out' }}>
  <Accordion title="Deletion Process" icon="fa-trash" style={{ backgroundColor: '#f1f8e9', color: '#388e3c', borderRadius: '8px', padding: '15px' }}>
    Securely delete user data when consent is withdrawn. Inform third-party data processors to delete or de-identify shared data.
  </Accordion>

  <Accordion title="De-identification" icon="fa-paint-brush" style={{ backgroundColor: '#fffde7', color: '#f57f17', borderRadius: '8px', padding: '15px' }}>
    Stripping identifiable information (e.g., user ID, timestamps), while retaining only aggregated, anonymized insights.
  </Accordion>

  <Accordion title="Retention Policy" icon="fa-clipboard-check" style={{ backgroundColor: '#e8f5e9', color: '#388e3c', borderRadius: '8px', padding: '15px' }}>
    Partners must delete data from their systems, ensuring Basiq deletes user data when the retention toggle is OFF.
  </Accordion>
</Accordion>

<Accordion title="User Rights" icon="fa-user-shield" style={{ backgroundColor: '#f3e5f5', color: '#8e24aa', borderRadius: '8px', padding: '15px', animation: 'fadeIn 3s ease-out' }}>
  <div style={{ fontSize: '16px', fontWeight: 'bold', color: '#8e24aa' }}>
    Users have the right to request:
  </div>

  <ul style={{ color: '#8e24aa', listStyleType: 'circle', paddingLeft: '20px' }}>
    <li>Deletion or de-identification of their data.</li>
    <li>Export of their data in machine-readable format.</li>
  </ul>
</Accordion>