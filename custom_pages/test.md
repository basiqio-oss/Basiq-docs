---
title: Basiq Introduction
fullscreen: false
hidden: true
metadata:
  title: ''
  description: ''
---
import \{ useState, useEffect } from 'react';

\<div style=\{\{ margin: '20px 0' }}>
&#x20; \<ModalDemo />
\</div>

export const ModalDemo = () => \{
&#x20; const \[isOpen, setIsOpen] = useState(false);

&#x20; // Open the modal automatically when the page loads
&#x20; useEffect(() => \{
&#x20;   setIsOpen(true);  // Modal opens on page load

&#x20;   const handleEscape = (event) => \{
&#x20;     if (event.key === 'Escape') \{
&#x20;       setIsOpen(false);
&#x20;     }
&#x20;   };
&#x20;   window\.addEventListener('keydown', handleEscape);

&#x20;   // Cleanup event listener on component unmount
&#x20;   return () => window\.removeEventListener('keydown', handleEscape);
&#x20; }, \[]); // Empty dependency array ensures this runs only once on mount

&#x20; const toggleModal = () => setIsOpen(!isOpen);

&#x20; return (
&#x20;   \<div>
&#x20;     \<button
&#x20;       onClick=\{toggleModal}
&#x20;       style=\{\{
&#x20;         padding: '12px 20px',
&#x20;         fontSize: '16px',
&#x20;         backgroundColor: '#007BFF',
&#x20;         color: '#fff',
&#x20;         border: 'none',
&#x20;         borderRadius: '8px',
&#x20;         cursor: 'pointer',
&#x20;         marginTop: '20px',
&#x20;         transition: 'background-color 0.3s',
&#x20;       }}
&#x20;       onMouseEnter=\{(e) => e.target.style.backgroundColor = '#0056b3'}
&#x20;       onMouseLeave=\{(e) => e.target.style.backgroundColor = '#007BFF'}
&#x20;     \>
&#x20;       Open Modal
&#x20;     \</button>

&#x20;     \{isOpen && (
&#x20;       \<div
&#x20;         style=\{\{
&#x20;           position: 'fixed',
&#x20;           top: '0',
&#x20;           left: '0',
&#x20;           width: '100vw',
&#x20;           height: '100vh',
&#x20;           backgroundColor: 'rgba(0, 0, 0, 0.7)',
&#x20;           display: 'flex',
&#x20;           alignItems: 'center',
&#x20;           justifyContent: 'center',
&#x20;           animation: 'fadeIn 0.3s',
&#x20;           zIndex: '1000',
&#x20;         }}
&#x20;         onClick=\{toggleModal}
&#x20;       \>
&#x20;         \<div
&#x20;           style=\{\{
&#x20;             backgroundColor: '#fff',
&#x20;             padding: '30px',
&#x20;             borderRadius: '12px',
&#x20;             boxShadow: '0 8px 16px rgba(0, 0, 0, 0.2)',
&#x20;             minWidth: '600px',
&#x20;             minHeight: '400px',
&#x20;             textAlign: 'center',
&#x20;             animation: 'slideIn 0.4s',
&#x20;             overflow: 'hidden',
&#x20;             position: 'relative',
&#x20;           }}
&#x20;           onClick=\{(e) => e.stopPropagation()}
&#x20;         \>
&#x20;           \{/\* Cross Button in the Top Right Corner \*/}
&#x20;           \<button
&#x20;             onClick=\{toggleModal}
&#x20;             style=\{\{
&#x20;               position: 'absolute',
&#x20;               top: '10px',
&#x20;               right: '10px',
&#x20;               backgroundColor: 'transparent',
&#x20;               border: 'none',
&#x20;               fontSize: '24px',
&#x20;               color: '#333',
&#x20;               cursor: 'pointer',
&#x20;               fontWeight: 'bold',
&#x20;               transition: 'color 0.3s',
&#x20;             }}
&#x20;             onMouseEnter=\{(e) => e.target.style.color = '#dc3545'}
&#x20;             onMouseLeave=\{(e) => e.target.style.color = '#333'}
&#x20;           \>
&#x20;             \&times;
&#x20;           \</button>

&#x20;           \<h2 style=\{\{ marginBottom: '20px' }}>Modal with Cards and Iframe\</h2>
&#x20;           \<p style=\{\{ fontSize: '14px', marginBottom: '20px' }}>
&#x20;             This is a modal with cards and an embedded iframe. You can close it by clicking outside or using the cross button.
&#x20;           \</p>

&#x20;           \{/\* Cards Section \*/}
&#x20;           \<div style=\{\{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '20px', marginBottom: '20px' }}>
&#x20;             \<Card title="Financial Data Services" icon="fa-database">
&#x20;               Access detailed financial data from a range of institutions. Retrieve account balances, transaction details, and more for a comprehensive financial view.
&#x20;             \</Card>
&#x20;             \<Card title="Payment Services" icon="fa-credit-card">
&#x20;               Facilitate various payment services, including the ability to collect, send, and receive payments. Simplify payment processing for smoother transactions.
&#x20;             \</Card>
&#x20;             \<Card title="Data Enrichment Services" icon="fa-chart-bar">
&#x20;               Enhance your financial data with enrichment services. Gain insights into spending behavior and categorize transaction data effectively.
&#x20;             \</Card>
&#x20;             \<Card title="Reporting Services" icon="fa-file-alt">
&#x20;               Generate insightful reports and analytics from financial data. Analyze trends and gain deeper insights into customer behavior with powerful tools.
&#x20;             \</Card>
&#x20;             \<Card title="Webhooks & Real-time Notifications" icon="fa-bell">
&#x20;               Stay updated with real-time notifications. Use Basiq’s webhook services to receive immediate alerts for account events.
&#x20;             \</Card>
&#x20;           \</div>

&#x20;           \{/\* Iframe Embedding \*/}
&#x20;           \<div
&#x20;             style=\{\{
&#x20;               position: 'relative',
&#x20;               paddingBottom: 'calc(54.55861070911722% + 41px)',
&#x20;               height: '0',
&#x20;               width: '100%',
&#x20;               borderRadius: '8px',
&#x20;               overflow: 'hidden',
&#x20;             }}
&#x20;           \>
&#x20;             \<iframe
&#x20;               src="https\://demo.arcade.software/zTaAEuzoNYTom6qJRvat?embed"
&#x20;               title="Basiq Dashboard | Activate your Account"
&#x20;               frameBorder="0"
&#x20;               loading="lazy"
&#x20;               webkitAllowFullScreen
&#x20;               mozAllowFullScreen
&#x20;               allowFullScreen
&#x20;               allow="clipboard-write"
&#x20;               style=\{\{
&#x20;                 position: 'absolute',
&#x20;                 top: '0',
&#x20;                 left: '0',
&#x20;                 width: '100%',
&#x20;                 height: '100%',
&#x20;                 colorScheme: 'light',
&#x20;                 borderRadius: '8px',
&#x20;               }}
&#x20;             \>\</iframe>
&#x20;           \</div>
&#x20;         \</div>
&#x20;       \</div>
&#x20;     )}

&#x20;     \<style>
&#x20;       \{\`
&#x20;         @keyframes fadeIn \{
&#x20;           from \{ opacity: 0; }
&#x20;           to \{ opacity: 1; }
&#x20;         }
&#x20;         @keyframes slideIn \{
&#x20;           from \{ transform: translateY(-50px); }
&#x20;           to \{ transform: translateY(0); }
&#x20;         }
&#x20;         .card \{
&#x20;           border: 1px solid #ddd;
&#x20;           border-radius: 8px;
&#x20;           padding: 20px;
&#x20;           box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
&#x20;           transition: transform 0.3s, box-shadow 0.3s;
&#x20;         }
&#x20;         .card:hover \{
&#x20;           transform: translateY(-5px);
&#x20;           box-shadow: 0 6px 16px rgba(0, 0, 0, 0.2);
&#x20;         }
&#x20;         .card-icon \{
&#x20;           font-size: 36px;
&#x20;           margin-bottom: 10px;
&#x20;           color: #007BFF;
&#x20;         }
&#x20;         .card-title \{
&#x20;           font-size: 18px;
&#x20;           font-weight: bold;
&#x20;           margin-bottom: 10px;
&#x20;         }
&#x20;         .card-content \{
&#x20;           font-size: 14px;
&#x20;           color: #555;
&#x20;         }
&#x20;       \`}
&#x20;     \</style>
&#x20;   \</div>
&#x20; );
};

// Card Component
const Card = (\{ title, icon, children }) => \{
&#x20; return (
&#x20;   \<div className="card">
&#x20;     \<div className="card-icon">
&#x20;       \<i className=\{\`fa $\{icon}\`}>\</i>
&#x20;     \</div>
&#x20;     \<div className="card-title">\{title}\</div>
&#x20;     \<div className="card-content">\{children}\</div>
&#x20;   \</div>
&#x20; );
};


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