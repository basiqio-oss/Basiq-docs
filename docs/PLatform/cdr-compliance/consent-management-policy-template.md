---
title: '# Consent Management Policy Template'
deprecated: false
hidden: true
metadata:
  robots: index
---
<Cards style={{ marginTop: '20px', display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '20px' }}>
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
</Cards>

<Cards style={{ marginTop: '20px', display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '20px' }}>
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

  <Card title="Consent Management Details" href="/consent/manage" icon="fa-info-circle" style={{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '20px', animation: 'fadeIn 3s ease-out' }}>
    Users can view and manage their existing consents, including expiry details and connected institutions.
  </Card>

  <Card title="View Consent" href="/consent/view" icon="fa-eye" style={{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '20px', animation: 'fadeIn 4s ease-out' }}>
    Review active consents and details.
  </Card>

  <Card title="Revoke Consent" href="/consent/manage" icon="fa-times-circle" style={{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '20px', animation: 'fadeIn 5s ease-out' }}>
    Revoke individual or all consents.
  </Card>
</Cards>

<Accordion title="Data Retention and De-identification" icon="fa-cogs" style={{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px', animation: 'fadeIn 2s ease-out' }}>
  <Accordion title="Deletion Process" icon="fa-trash" style={{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px' }}>
    Securely delete user data when consent is withdrawn. Inform third-party data processors to delete or de-identify shared data.
  </Accordion>

  <Accordion title="De-identification" icon="fa-paint-brush" style={{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px' }}>
    Stripping identifiable information (e.g., user ID, timestamps), while retaining only aggregated, anonymized insights.
  </Accordion>

  <Accordion title="Retention Policy" icon="fa-clipboard-check" style={{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px' }}>
    Partners must delete data from their systems, ensuring Basiq deletes user data when the retention toggle is OFF.
  </Accordion>
</Accordion>

<Accordion title="User Rights" icon="fa-user-shield" style={{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px', animation: 'fadeIn 3s ease-out' }}>
  <div style={{ fontSize: '16px', fontWeight: 'bold', color: '#003366' }}>
    Users have the right to request:
  </div>

  <ul style={{ color: '#003366', listStyleType: 'circle', paddingLeft: '20px' }}>
    <li>Deletion or de-identification of their data.</li>
    <li>Export of their data in machine-readable format.</li>
  </ul>
</Accordion>