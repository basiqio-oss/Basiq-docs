---
title: Consent Management Policy
fullscreen: false
hidden: true
---
import React from 'react';

const ConsentManagement = () => (

<>
  <div style={{ margin: '20px', padding: '10px', backgroundColor: '#f1f8e9', borderRadius: '8px' }}>
    <h2 style={{ color: '#388e3c', fontWeight: 'bold' }}>Introduction to the Consumer Data Right (CDR)</h2>

    <p style={{ fontSize: '16px', color: '#388e3c' }}>
      The Consumer Data Right (CDR) regulates the collection and handling of CDR data in line with privacy safeguards and rules that:
    </p>

    <ul style={{ fontSize: '16px', color: '#388e3c', listStyleType: 'circle', paddingLeft: '20px' }}>
      <li>Ensure your data is managed securely.</li>
      <li>Provide you with control over how your data is shared and used.</li>
    </ul>
  </div>

  <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '20px' }}>
    <div style={{ width: '45%', padding: '20px', backgroundColor: '#ffebee', borderRadius: '8px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)' }}>
      <h3 style={{ color: '#c62828', fontWeight: 'bold' }}>Key User Benefits</h3>

      <ul style={{ fontSize: '16px', color: '#c62828' }}>
        <li><strong>Choice and Control:</strong> Users decide what data to share, how it’s used, and who can access it.</li>
        <li><strong>Manage Consent:</strong> Users can view, modify, or revoke their consents at any time.</li>
        <li><strong>Data Deletion Requests:</strong> Users can request deletion or de-identification of their personal data.</li>
      </ul>
    </div>

    <div style={{ width: '45%', padding: '20px', backgroundColor: '#e3f2fd', borderRadius: '8px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)' }}>
      <h3 style={{ color: '#1976d2', fontWeight: 'bold' }}>What is an Accredited Data Recipient (ADR)?</h3>

      <p style={{ fontSize: '16px', color: '#1976d2' }}>
        An **Accredited Data Recipient (ADR)** is an organization approved under the CDR framework to receive and manage consumer data securely.
      </p>

      <ul style={{ fontSize: '16px', color: '#1976d2', listStyleType: 'circle', paddingLeft: '20px' }}>
        <li>Transparent disclosure of how data is used.</li>
        <li>Secure storage and transfer of consumer data.</li>
        <li>Privacy safeguards ensuring data is only used as consented by the user.</li>
      </ul>
    </div>
  </div>

  <div style={{ marginTop: '30px' }}>
    <div style={{ padding: '20px', backgroundColor: '#fffde7', borderRadius: '8px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)' }}>
      <h3 style={{ color: '#f57f17', fontWeight: 'bold' }}>Types of Data Collected</h3>

      <p style={{ fontSize: '16px', color: '#f57f17' }}>
        With user consent, ADRs may collect the following types of data:
      </p>

      <ul style={{ fontSize: '16px', color: '#f57f17', listStyleType: 'circle', paddingLeft: '20px' }}>
        <li><strong>Personal Information</strong>: Full Name, Contact Details, Occupation</li>
        <li><strong>Transaction Data</strong>: Details about purchases, payments, associated metadata.</li>
        <li><strong>De-Identified Data</strong>: Data stripped of personally identifiable information for analytics and reporting.</li>
      </ul>
    </div>
  </div>

  <div style={{ marginTop: '30px' }}>
    <div style={{ padding: '20px', backgroundColor: '#f8f9fa', borderRadius: '8px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)' }}>
      <h3 style={{ color: '#007bff', fontWeight: 'bold' }}>How Data is Used</h3>

      <p style={{ fontSize: '16px', color: '#007bff' }}>
        Example framework for the usage of CDR data:
      </p>

      <ul style={{ fontSize: '16px', color: '#007bff', listStyleType: 'circle', paddingLeft: '20px' }}>
        <li><strong>Providing Personalised Solutions</strong>: Tailoring recommendations based on user activities.</li>
        <li><strong>Operational Purposes</strong>: Fraud detection, prevention, and analytical reporting using de-identified data.</li>
        <li><strong>Communication</strong>: Sending updates, notifications, or support for services.</li>
      </ul>
    </div>
  </div>

  <div style={{ marginTop: '30px', padding: '20px', backgroundColor: '#f0f8ff', borderRadius: '8px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)' }}>
    <h3 style={{ color: '#003366', fontWeight: 'bold' }}>Data Security</h3>

    <p style={{ fontSize: '16px', color: '#003366' }}>
      Ensure compliance with these practices:
    </p>

    <ul style={{ fontSize: '16px', color: '#003366', listStyleType: 'circle', paddingLeft: '20px' }}>
      <li><strong>Storage:</strong> All data must be stored securely in Australia.</li>
      <li><strong>Encryption:</strong> Encrypt all CDR data in transit and at rest.</li>
      <li><strong>Access Control:</strong> Limit data access to authorized personnel or systems.</li>
      <li><strong>Audits:</strong> Regularly audit data handling practices.</li>
    </ul>
  </div>

  <div style={{ marginTop: '30px', display: 'flex', justifyContent: 'space-between' }}>
    <div style={{ width: '45%', padding: '20px', backgroundColor: '#e8f5e9', borderRadius: '8px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)' }}>
      <h3 style={{ color: '#388e3c', fontWeight: 'bold' }}>Using the Basiq Dashboard for Consent Management</h3>

      <img src="https://via.placeholder.com/300x150" alt="Basiq Dashboard" style={{ width: '100%', borderRadius: '8px', marginBottom: '15px' }} />

      <h4 style={{ color: '#388e3c' }}>A. Partner Revoking Consent on Behalf of Users</h4>

      <ul style={{ fontSize: '16px', color: '#388e3c', listStyleType: 'circle', paddingLeft: '20px' }}>
        <li>Log into the Basiq dashboard.</li>
        <li>Navigate to the "Users" section.</li>
        <li>Locate the user whose consent needs to be revoked.</li>
        <li>Click to revoke consent.</li>
      </ul>
    </div>

    <div style={{ width: '45%', padding: '20px', backgroundColor: '#fff3e0', borderRadius: '8px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)' }}>
      <h3 style={{ color: '#f57c00', fontWeight: 'bold' }}>Using the action=manage Parameter for Consent Management</h3>

      <img src="https://via.placeholder.com/300x150" alt="Action Manage" style={{ width: '100%', borderRadius: '8px', marginBottom: '15px' }} />

      <p style={{ fontSize: '16px', color: '#f57c00' }}>
        Partners can send a link with the `action=manage` parameter to allow users to manage their consents directly.
      </p>

      <iframe src="https://demo.arcade.software/Wad1ic93gwfM3NQFdMJ3?embed" title="Basiq | action=manage" frameBorder="0" style={{ width: '100%', height: '300px', borderRadius: '8px' }} />
    </div>
  </div>

  <div style={{ marginTop: '30px', padding: '20px', backgroundColor: '#e8f5e9', borderRadius: '8px', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)' }}>
    <h3 style={{ color: '#388e3c', fontWeight: 'bold' }}>Data Retention and De-identification</h3>
    <h4 style={{ color: '#388e3c' }}>Deletion Process</h4>

    <ul style={{ fontSize: '16px', color: '#388e3c', listStyleType: 'circle', paddingLeft: '20px' }}>
      <li>Securely delete user data when consent is withdrawn.</li>
      <li>Inform third-party data processors to delete or de-identify shared data.</li>
    </ul>

    <h4 style={{ color: '#388e3c' }}>De-identification</h4>

    <ul style={{ fontSize: '16px', color: '#388e3c', listStyleType: 'circle', paddingLeft: '20px' }}>
      <li>Strip identifiable information (e.g., user ID, timestamps).</li>
      <li>Retain only aggregated, anonymised insights.</li>
    </ul>

    <h4 style={{ color: '#388e3c' }}>Retention Policy</h4>

    <ul style={{ fontSize: '16px', color: '#388e3c', listStyleType: 'circle', paddingLeft: '20px' }}>
      <li>Partner Responsibility: If the retention toggle is OFF, partners must delete the data from their systems while ensuring Basiq deletes user data.</li>
    </ul>
  </div>
</>

);

\< ConsentManagement />