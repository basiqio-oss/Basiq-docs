---
title: Integration Overview
excerpt: >-
  Welcome to the Basiq Dashboard Integration guide. Configuring your environment
  on our dashboard is a vital step for effectively leveraging Basiq services and
  protecting your customers data.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: activate-your-account
      title: Activate your Account
---
### Getting Started

Begin by creating an account on the Basiq Dashboard, accessible at [Basiq Dashboard](https://dashboard.basiq.io). This initial step grants you the access needed to manage and utilise Basiq's services, marking the start of your journey with us.

<Embed url="https://basiq-hosted-files.s3.ap-southeast-2.amazonaws.com/docs-resources/Basiq%20Integration-%20Application%20Flow%20(Sequence%20Diagram).pdf" href="https://basiq-hosted-files.s3.ap-southeast-2.amazonaws.com/docs-resources/Basiq%20Integration-%20Application%20Flow%20(Sequence%20Diagram).pdf" typeOfEmbed="pdf" html="%3Ciframe%20src%3D%22https%3A%2F%2Fdrive.google.com%2Fviewerng%2Fviewer%3Furl%3Dhttps%253A%2F%2Fbasiq-hosted-files.s3.ap-southeast-2.amazonaws.com%2Fdocs-resources%2FBasiq%252520Integration-%252520Application%252520Flow%252520%2528Sequence%252520Diagram%2529.pdf%26embedded%3Dtrue%22%20width%3D%22600%22%20height%3D%22780%22%20style%3D%22border%3A%20none%3B%22%3E%3C%2Fiframe%3E" />

### Key Configuration Steps:

**1. Application Setup**: Create seperate applications for various development stages or specific use cases. This helps keep your data organised and your production data safe and isolated from your other development environments.

**2. Permission Sets**: Establish role-based permissions for your team members and API keys. This ensures everyone has the right level of access for their role and enhances the protection of sensitive data.

**3. Consent UI Customisation**: Tailor the Consent UI to match your application's branding and specify the services and data required by your application.

**4. API Key Generation**: For direct integration with Basiq's API services, this section provides a straightforward guide on how to set up and configure your API Keys effectively.

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