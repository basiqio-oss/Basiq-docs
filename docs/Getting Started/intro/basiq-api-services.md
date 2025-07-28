---
title: Basiq API services
excerpt: ''
deprecated: false
hidden: true
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