---
title: Basiq Introduction
fullscreen: false
hidden: true
metadata:
  title: ''
  description: ''
---
import { useState, useEffect } from 'react';

<div style={{ margin: '20px 0' }}>
  <ModalDemo />
</div>

export const ModalDemo = () => {
  const [isOpen, setIsOpen] = useState(false);

  // Open the modal automatically when the page loads
  useEffect(() => {
    setIsOpen(true);  // Modal opens on page load

    const handleEscape = (event) => {
      if (event.key === 'Escape') {
        setIsOpen(false);
      }
    };
    window.addEventListener('keydown', handleEscape);

    // Cleanup event listener on component unmount
    return () => window.removeEventListener('keydown', handleEscape);
  }, []); // Empty dependency array ensures this runs only once on mount

  const toggleModal = () => setIsOpen(!isOpen);

  return (
    <div>
      <button
        onClick={toggleModal}
        style={{
          padding: '12px 20px',
          fontSize: '16px',
          backgroundColor: '#007BFF',
          color: '#fff',
          border: 'none',
          borderRadius: '8px',
          cursor: 'pointer',
          marginTop: '20px',
          transition: 'background-color 0.3s',
        }}
        onMouseEnter={(e) => e.target.style.backgroundColor = '#0056b3'}
        onMouseLeave={(e) => e.target.style.backgroundColor = '#007BFF'}
      >
        Open Modal
      </button>

      {isOpen && (
        <div
          style={{
            position: 'fixed',
            top: '0',
            left: '0',
            width: '100vw',
            height: '100vh',
            backgroundColor: 'rgba(0, 0, 0, 0.7)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            animation: 'fadeIn 0.3s',
            zIndex: '1000',
          }}
          onClick={toggleModal}
        >
          <div
            style={{
              backgroundColor: '#fff',
              padding: '30px',
              borderRadius: '12px',
              boxShadow: '0 8px 16px rgba(0, 0, 0, 0.2)',
              minWidth: '600px',
              minHeight: '400px',
              textAlign: 'center',
              animation: 'slideIn 0.4s',
              overflow: 'hidden',
              position: 'relative', // Positioning context for the close button
            }}
            onClick={(e) => e.stopPropagation()}
          >
            {/* Cross Button in the Top Right Corner */}
            <button
              onClick={toggleModal}
              style={{
                position: 'absolute',
                top: '10px',
                right: '10px',
                backgroundColor: 'transparent',
                border: 'none',
                fontSize: '24px',
                color: '#333',
                cursor: 'pointer',
                fontWeight: 'bold',
                transition: 'color 0.3s',
              }}
              onMouseEnter={(e) => e.target.style.color = '#dc3545'}
              onMouseLeave={(e) => e.target.style.color = '#333'}
            >
              &times;
            </button>

            <h2 style={{ marginBottom: '20px' }}>Modal with Iframe</h2>
            <p style={{ fontSize: '14px', marginBottom: '20px' }}>
              This is a modal with an embedded iframe. You can close it by clicking outside or using the cross button.
            </p>

            {/* Iframe Embedding */}
            <div
              style={{
                position: 'relative',
                paddingBottom: 'calc(54.55861070911722% + 41px)',
                height: '0',
                width: '100%',
                borderRadius: '8px',
                overflow: 'hidden',
              }}
            >
              <iframe
                src="https://demo.arcade.software/zTaAEuzoNYTom6qJRvat?embed"
                title="Basiq Dashboard | Activate your Account"
                frameBorder="0"
                loading="lazy"
                webkitAllowFullScreen
                mozAllowFullScreen
                allowFullScreen
                allow="clipboard-write"
                style={{
                  position: 'absolute',
                  top: '0',
                  left: '0',
                  width: '100%',
                  height: '100%',
                  colorScheme: 'light',
                  borderRadius: '8px',
                }}
              ></iframe>
            </div>
          </div>
        </div>
      )}

      <style>
        {`
          @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
          }
          @keyframes slideIn {
            from { transform: translateY(-50px); }
            to { transform: translateY(0); }
          }
        `}
      </style>
    </div>
  );
};

<br />

# Welcome to Basiq

Basiq is a cutting-edge platform designed to revolutionize the way businesses and developers interact with financial data. At its core, Basiq provides a robust, secure, and efficient means to access and process financial information. Our platform simplifies financial data integration, offering tools and services to enable businesses to make informed decisions, enhance customer experiences, and innovate in the financial technology space.

> 📘 Info:
>
> *Basiq is a[Consumer Data Right accredited](https://www.basiq.io/blog/basiq-launches-cdr-data-holder-and-data-recipient-solution/) API platform that provides the building blocks of financial services.*

<Columns layout="auto">
  <Column>
    ## Our Mission

    Empower developers and businesses by providing a seamless and secure gateway to financial data. We strive to bridge the gap between financial institutions and fintech innovators, ensuring effortless access and utilization of financial data while maintaining the highest standards of security and compliance.
  </Column>

  <Column>
    <p />

    <Image align="center" src="https://files.readme.io/d5d0e45-bb68dee-DevHub_01.png" />
  </Column>
</Columns>

***

## Core Features of Basiq

<Cards columns={3}>
  <Card title="Financial Data Services" icon="fa-database">
    Access detailed financial data from a range of institutions. Retrieve account balances, transaction details, and more for a comprehensive financial view.
  </Card>

  <Card title="Payment Services" icon="fa-credit-card">
    Facilitate various payment services, including the ability to collect, send, and receive payments. Simplify payment processing for smoother transactions.
  </Card>

  <Card title="Data Enrichment Services" icon="fa-chart-bar">
    Enhance your financial data with enrichment services. Gain insights into spending behavior and categorize transaction data effectively.
  </Card>

  <Card title="Reporting Services" icon="fa-file-alt">
    Generate insightful reports and analytics from financial data. Analyze trends and gain deeper insights into customer behavior with powerful tools.
  </Card>

  <Card title="Webhooks & Real-time Notifications" icon="fa-bell">
    Stay updated with real-time notifications. Use Basiq’s webhook services to receive immediate alerts for account events.
  </Card>
</Cards>

***

## Why Choose Basiq?

<Cards columns={2}>
  <Card title="Ease of Integration" icon="fa-code">
    Basiq is designed to be developer-friendly, with comprehensive documentation, SDKs, and APIs that make integration effortless.
  </Card>

  <Card title="Compliance and Security" icon="fa-shield-alt">
    Adherence to financial regulations and <Glossary>CDR</Glossary> standards ensures top-tier security and compliance.
  </Card>

  <Card title="Innovative Solutions" icon="fa-lightbulb">
    Stay at the forefront of fintech innovation with Basiq’s constantly evolving platform and advanced capabilities.
  </Card>

  <Card title="Support and Community" icon="fa-users">
    Access robust support and an active community of developers. Whether you’re a startup or enterprise, we’re here to assist.
  </Card>
</Cards>

***

## Getting Started with Basiq

## Getting Started with Basiq

<Tabs>
  <Tab title="Overview">
    Welcome to Basiq! Follow these steps to seamlessly integrate with our platform and unlock the power of financial data. Whether you're testing in our sandbox environment or going live, we've got you covered with tools, support, and comprehensive documentation.

    <Cards columns={3}>
      <Card title="Step 1: Sign Up" icon="fa-user-plus" href="https://dashboard.basiq.io/" target="_blank">
        Create a free account on the Basiq Dashboard to start exploring the platform. This will act as your central hub for managing APIs and integrations.
      </Card>

      <Card title="Step 2: Explore the Dashboard" icon="fa-chart-line">
        Familiarize yourself with the Basiq Dashboard. Track your usage, monitor data, and manage integrations all in one place.
      </Card>

      <Card title="Step 3: Access Documentation" icon="fa-book-open" href="https://api.basiq.io/reference/" target="_blank">
        Dive into our comprehensive API documentation. Learn how to fetch data, set up webhooks, and more!
      </Card>
    </Cards>
  </Tab>

  <Tab title="Sandbox Environment">
    <Cards columns={2}>
      <Card title="What is the Sandbox?" icon="fa-flask">
        The Sandbox is a safe testing environment to simulate real-world scenarios with dummy data. Perfect for building and experimenting with integrations.
      </Card>

      <Card title="How to Use It?" icon="fa-tools">
        Use the Sandbox to test API endpoints, fetch mock transaction data, and ensure your app is fully functional before going live.
      </Card>
    </Cards>

    <p>
      <strong>Features of the Sandbox:</strong>

      <ul>
        <li>Preconfigured test users</li>
        <li>Simulated account and transaction data</li>
        <li>Full access to API functionalities</li>
      </ul>
    </p>

    <p>
      <strong>Pro Tip:</strong> Once testing is complete, switching to production is seamless.
      Simply update your API keys to live credentials in the dashboard.
    </p>
  </Tab>

  <Tab title="Moving to Production">
    <Cards columns={2}>
      <Card title="Step 1: Upgrade Your Account" icon="fa-rocket">
        To move to production, you'll need to verify your organization and upgrade your account. This ensures secure access to live data.
      </Card>

      <Card title="Step 2: Monitor and Scale" icon="fa-server">
        Once live, use the Basiq Dashboard to monitor API usage, scale your integration, and gain real-time insights into your application's performance.
      </Card>
    </Cards>

    <Image align="center" src="https://files.readme.io/7d874db-43206b9-DevHub_02.png" />
  </Tab>
</Tabs>

***

> 📘 We’re thrilled to have you onboard and look forward to helping you leverage financial data to its fullest potential!