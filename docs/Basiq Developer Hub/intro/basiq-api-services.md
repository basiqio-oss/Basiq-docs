---
title: Basiq API services
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
Basiq provides a number of services enabling developers to build innovative financial solutions:

## Access account and transaction data in real-time

Gain secure and ongoing access to customer-consented data from a wide range of financial institutions across banks, credit unions, super funds, payment providers and more. Our Basiq Consent UI also allows you to easily provide customers with a simple, informed and trustworthy data sharing experience that aligns with the recommendations from the ACCC and CDR.

## Enhance transactions with merchant data

Accelerate new features based on powerful spending insights with real-time enrichment, detailed expense classification, accurate merchant location and the latest merchant information.

## Gain deeper insights of your customer's finances

Get a better understanding of your customer's financials by identifying income sources, expenses, assets and liabilities

## Insight-driven automation \[coming soon]

Automate workflows to enable personalised, autonomous finance offerings with event-driven data.

> 📘 Connect
>
> Base URL is → [https://au-api.basiq.io](https://au-api.basiq.io) - you can use our sandbox environment for free right now - just grab an API key!

> 📘 Enrich
>
> Enrich URL is → [https://au-api.basiq.io/enrich](https://au-api.basiq.io/enrich) - you can use our sandbox environment for free - contact us to have your API key activated.

> 📘 REPORTING (INSIGHTS)
>
> The Reports URL is → [https://au-api.basiq.io/reports](https://au-api.basiq.io/reports) - you can use our sandbox environment for free - contact us to have your API key activated.

## How does the API work?

<Image align="center" src="https://files.readme.io/4f374b2-introduction.png" />

# API Enablement

> 📘 For enablement purposes, please contact our Sales team or Customer success teams at either [support@basiq.io ](mailto:support@basiq.io).

<div
  style={{
    border: "2px solid #1E1E1E", // Dark border
    borderRadius: "8px",
    backgroundColor: "#1E1E1E", // Dark background
    padding: "16px",
    margin: "16px 0",
    fontFamily: "Arial, sans-serif",
    color: "#ffffff", // Light text for contrast
  }}
>
  <strong style={{ color: "#ffffff" }}>📢 Attention!</strong> If you have any issues, please reach out to our amazing support team.

  <div style={{ display: 'flex', alignItems: 'center' }}>
    <button
      onClick={() => Intercom('showNewMessage', 'issues on FAQs:')}
      style={{
        padding: '12px 30px',
        backgroundColor: '#1E1E1E',
        color: '#ffffff',
        border: '2px solid #ffffff', // Add contrast border if needed
        borderRadius: '50px',
        fontSize: '16px',
        fontWeight: '600',
        textTransform: 'uppercase',
        cursor: 'pointer',
        transition: 'background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease',
        outline: 'none',
        display: 'flex',
        justifyContent: 'center',
        height: '45px',
        position: 'relative',
        overflow: 'hidden',
        marginLeft: '10px',
        minWidth: '150px',
      }}
      onMouseEnter={(e) => {
        e.target.style.transform = 'scale(1.1)';
        e.target.style.backgroundColor = '#333333'; // Slightly lighter dark on hover
      }}
      onMouseLeave={(e) => {
        e.target.style.transform = 'scale(1)';
        e.target.style.backgroundColor = '#1E1E1E'; // Original dark
      }}
    >
      Support team
    </button>
  </div>
</div>