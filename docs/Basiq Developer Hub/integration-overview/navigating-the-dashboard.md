---
title: Navigating the Dashboard
excerpt: >-
  The Basiq Dashboard is an intuitive and comprehensive interface designed for
  effective management and observation of financial data. Here's a guide to help
  you navigate through its various functionalities.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Application Section

In the 'Applications' section, you can manage your integrated applications, oversee their performance, and set up different environments tailored for various stages of development and deployment. This area is crucial for configuring your applications to align with specific project needs and operational stages.

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/zMaHRaQNiMNRa94QpO0y?embed" title="Basiq - Application Section" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

## User Management

The 'Users' section is dedicated to managing users associated with your applications. Here, you'll find detailed information about users' financial connections, transactions, and accounts. It's also where you can create and manage 'magic links' for requesting user consent, ensuring compliance and secure data access.

## API Keys

The 'API Keys' section is where you securely generate and manage API keys necessary for application integration and data access. This feature is essential for establishing secure communication between your applications and the Basiq platform.

## Consent UI Customisation

In the 'Consent UI' section, you have the ability to customize the user consent interface. This customization enhances the user experience during the consent process, allowing you to align the look and feel of the consent UI with your application's branding.

## Reporting and Insights

The 'Reports' section enables you to generate and view insightful reports. These reports provide valuable insights into financial data, aiding in informed decision-making and strategic planning.

## Status Monitoring

In the 'Status' section, monitor the real-time status of connectors to financial institutions. This monitoring ensures seamless data integration and helps in quickly addressing any connectivity issues.

## Help and Support

The 'Help' section provides access to a range of support options and resources, including FAQs, user guides, and direct contact information for further assistance. This section is your go-to resource for any queries or guidance needed while using the dashboard.

## Settings Configuration

The 'Settings' section is where you configure company-wide settings, including enforcing Single Sign-On (SSO) and managing permission sets. This section also allows for the invitation and management of team members, granting them access to the dashboard with appropriate permissions.

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(54.55861070911722% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/0AIUrzyTIvrRiRGvsHdn?embed" title="Basiq - Single Sign-On" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

## Account Settings

In the 'Account Settings' section, manage your personal dashboard account settings. This includes updating passwords, activating two-factor authentication, and other personal account management functionalities.

> 📘 *The Basiq Dashboard is designed to be dynamic, regularly evolving with new features and updates to enhance your financial data management experience. Familiarise yourself with these sections to maximise the benefits of the Basiq platform.*

<div
  style={{
    border: "2px solid #4e9ccf", // Classic blue border
    borderRadius: "8px",
    backgroundColor: "#e3f2fd", // Light blue background (cascade effect)
    padding: "16px",
    margin: "16px 0",
    fontFamily: "Arial, sans-serif",
    color: "#333", // Dark text for readability
  }}
>
  <strong style={{ color: "#1e88e5" }}>📢 Attention!</strong> If you have any issues, please reach out to our amazing support team.

  <div style={{ display: 'flex', alignItems: 'center' }}>
    <button
      onClick={() => Intercom('showNewMessage', 'issues on FAQs:')}
      style={{
        padding: '12px 30px',
        backgroundColor: '#1e88e5', // Classic blue button color
        color: '#ffffff',
        border: 'none',
        borderRadius: '50px',
        fontSize: '16px',
        fontWeight: '600',
        textTransform: 'uppercase',
        cursor: 'pointer',
        boxShadow: '0 4px 10px rgba(30, 136, 229, 0.2)', // Soft blue shadow
        transition: 'background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease',
        outline: 'none',
        display: 'flex',
        justifyContent: 'center',
        height: '45px',
        position: 'relative',
        overflow: 'hidden',
        marginLeft: '10px', // Add space between text and button
        minWidth: '150px', // Ensure the button has enough width for the text
      }}
      onMouseEnter={(e) => {
        e.target.style.transform = 'scale(1.1)';
        e.target.style.boxShadow = '0 6px 15px'; // Darker shadow on hover
        e.target.style.backgroundColor = '#1565c0'; // Darker blue on hover
      }}
      onMouseLeave={(e) => {
        e.target.style.transform = 'scale(1)';
        e.target.style.boxShadow = '0 4px 10px';
        e.target.style.backgroundColor = '#1e88e5'; // Original blue
      }}
    >
      Support team
    </button>
  </div>
</div>