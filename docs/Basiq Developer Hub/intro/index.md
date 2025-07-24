---
title: Introduction
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
### Welcome to Basiq

Basiq is a cutting-edge platform designed to revolutionise the way businesses and developers interact with financial data. At its core, Basiq provides a robust, secure, and efficient means to access and process financial information. Our platform is built with the intention of simplifying financial data integration, offering tools and services that enable businesses to make informed decisions, enhance customer experiences, and innovate in the financial technology space. Basiq is a [Consumer Data Right accredited](https://www.basiq.io/blog/basiq-launches-cdr-data-holder-and-data-recipient-solution/) API platform that provides the building blocks of financial services.

<Grid columns="3" gap="20px" style={{ gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))' }}>
  <CoolCard header="Quick Start" href="https://api.basiq.io/docs/getting-started" icon="fa-duotone fa-solid fa-rocket-launch" text="Get Started with BASIQ" />

  <CoolCard header="API Reference" href="https://api.basiq.io/reference/introduction/" icon="fa-duotone fa-solid fa-code-simple" text="Call your APIs" />
</Grid>

### Our Mission

Our mission is to empower developers and businesses by providing a seamless and secure gateway to financial data. We strive to bridge the gap between financial institutions and fintech innovators, ensuring that accessing and utilising financial data is as effortless as possible, while maintaining the highest standards of security and compliance.

### Core Features of Basiq

**1. Financial Data Services:** Access detailed financial data from a range of institutions. With Basiq, you can retrieve account balances, transaction details, and more, ensuring a comprehensive view of financial information.

**2. Payment Services:** Our platform facilitates various payment services, including the ability to collect, send, and receive payments. Basiq simplifies payment processing, making transactions smoother and more efficient.

**3. Data Enrichment Services:** Enhance your financial data with our enrichment services. Basiq provides additional context to transactions, helping you to better understand spending behavior and categorise transaction data effectively.

**4. Reporting Services:** Generate insightful reports and analytics from financial data. Our reporting tools help you to analyse financial trends and gain deeper insights into customer behavior.

**5. Webhooks and Real-time Notifications:** Stay updated with real-time notifications. Basiq’s webhook services provide immediate alerts for account events, facilitating prompt responses to important changes.

### Why Choose Basiq?

* **Ease of Integration:** Basiq is designed to be developer-friendly, with comprehensive documentation, SDKs, and APIs that make integration a breeze.

* **Compliance and Security:** We prioritise data security and compliance with financial regulations, including adherence to the <Glossary>CDR</Glossary> standards.

* **Innovative Solutions:** Basiq is at the forefront of fintech innovation, constantly evolving to include the latest in financial technology.

* **Support and Community:** We offer robust support and have an active community of developers. Whether you’re a startup or an established enterprise, our team and community are here to assist.

### Getting Started with Basiq

To begin your journey with Basiq, follow these simple steps:

1. **Sign Up:** [Register](https://dashboard.basiq.io/) for a Basiq account to access our dashboard and APIs.
2. **Explore the Dashboard:** Familiarise yourself with the Basiq Dashboard, your central hub for managing integrations and services.
3. **Read the Documentation:** Our comprehensive guides and API documentation provide all the information you need to start integrating Basiq services.
4. **Experiment in a Sandbox:** Use our sandbox environment to safely [test](https://api.basiq.io/reference/testing) and develop your applications.

We’re excited to have you on board and look forward to supporting your journey in leveraging financial data to its fullest potential.

<div
  style={{
    marginTop: '2rem',
    marginBottom: '2rem',
    display: 'flex',
    flexWrap: 'wrap',
    alignItems: 'center',
    justifyContent: 'center',
    gap: '1.5rem',
    padding: '1.5rem',
    background: 'linear-gradient(to bottom right, #f9fafb, #f3f4f6)',
    border: '1px solid #e5e7eb',
    borderRadius: '0.75rem',
    boxShadow: '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
    textAlign: 'center',
    fontFamily: 'system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif',
  }}
>
  <div
    style={{
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
    }}
  >
    <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#4b5563" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ marginRight: '1rem', flexShrink: 0 }}>
      <path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z" />

      <path d="M8 12h.01" />

      <path d="M12 12h.01" />

      <path d="M16 12h.01" />
    </svg>

    <p
      style={{
        fontSize: '1.125rem',
        fontWeight: 600,
        color: '#1f2937',
        margin: 0,
      }}
    >
      Got a question or need assistance?
    </p>
  </div>

  <button onClick={() => Intercom('showNewMessage', 'issues on FAQs:')} style={{
                      padding: '0.75rem 2rem',
                      fontSize: '1rem',
                      fontWeight: 600,
                      borderRadius: '9999px',
                      boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
                      transition: 'all 0.3s ease-in-out',
                      backgroundColor: '#1f2937',
                      color: '#ffffff',
                      border: 'none',
                      cursor: 'pointer',
                      outline: 'none',
                      flexShrink: 0,
                    }} onMouseEnter={(e) => {
                      e.currentTarget.style.backgroundColor = '#374151';
                      e.currentTarget.style.transform = 'scale(1.05)';
                    }} onMouseLeave={(e) => {
                      e.currentTarget.style.backgroundColor = '#1f2937';
                      e.currentTarget.style.transform = 'scale(1)';
                    }} onFocus={(e) => {
                      e.currentTarget.style.outline = '2px solid #6b7280';
                      e.currentTarget.style.outlineOffset = '2px';
                      e.currentTarget.style.backgroundColor = '#374151';
                      e.currentTarget.style.transform = 'scale(1.05)';
                    }} onBlur={(e) => {
                      e.currentTarget.style.outline = 'none';
                      e.currentTarget.style.outlineOffset = '0px';
                      e.currentTarget.style.backgroundColor = '#1f2937';
                      e.currentTarget.style.transform = 'scale(1)';
                    }}>Chat with Support</button>
</div>