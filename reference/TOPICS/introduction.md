---
title: Introduction
excerpt: ''
deprecated: false
hidden: false
icon: fad fa-hand-wave
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## What is Basiq?

Basiq is a [Consumer Data Right accredited](https://blog.basiq.io/basiq-launches-cdr-data-holder-and-data-recipient-solution/) API platform that provides the building blocks of financial services.

Our APIs enable secure access to customer-consented financial data and tools to uncover valuable insights. Over 200 fintechs and banks rely on our platform to deliver innovative financial solutions across lending, payments, wealth, digital banking and more.

<Grid columns="3" gap="20px" style={{ gridTemplateColumns: 'repeat(auto‑fit, minmax(200px, 1fr))' }}>
  <CoolCard header="Connect" icon="fa-duotone fa-link" text="Access account and transaction data in real-time." />

  <CoolCard header="Enrich" icon="fa-duotone fa-chart-line" text="Enhance transactions with merchant data." />

  <CoolCard header="Discover" icon="fa-duotone fa-search" text="Gain deeper insights into your customer's finances." />
</Grid>

***

## Use Cases

<Grid columns="2" gap="30px" style={{ marginTop: '2em' }}>
  <CoolTile header="Account Aggregation" icon="fa-duotone fa-database" text="Aggregate customer financial data and build PFM functionality with personalised insights." />

  <CoolTile header="Account Verification" icon="fa-duotone fa-check-circle" text="Verify account ownership and balances instantly for improved lending and payments." />
</Grid>

<Grid columns="2" gap="30px" style={{ marginTop: '1.5em' }}>
  <CoolTile header="Data Enrichment" icon="fa-duotone fa-layer-group" text="Classify transactions, identify merchants and uncover behavioral insights." />

  <CoolTile header="Wealth Management" icon="fa-duotone fa-chart-pie" text="Use enriched financial data for tailored wealth solutions and advice." />
</Grid>

***

## Supported Regions

> 🚧 **Basiq APIs are currently only available in Australia and New Zealand.**\
> Visit the [status page](https://dashboard.basiq.io/status) for supported institutions.

***

<Accordion title="Partner Showcase" icon="fa-duotone fa-users">
  Check out how some of our customers are using Basiq. Visit our [Partner Showcase](https://basiq.io/blog/category/partner-showcase/) to see Basiq in action.
</Accordion>

***

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
  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
    <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#4b5563" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ marginRight: '1rem', flexShrink: 0 }}>
      <path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z" />

      <path d="M8 12h.01" />

      <path d="M12 12h.01" />

      <path d="M16 12h.01" />
    </svg>

    <p style={{ fontSize: '1.125rem', fontWeight: 600, color: '#1f2937', margin: 0 }}>
      Got a question or need assistance?
    </p>
  </div>

  <button
    onClick={() => Intercom('showNewMessage', 'issues on FAQs:')}
    style={{
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
    }}
    onMouseEnter={(e) => {
      e.currentTarget.style.backgroundColor = '#374151';
      e.currentTarget.style.transform = 'scale(1.05)';
    }}
    onMouseLeave={(e) => {
      e.currentTarget.style.backgroundColor = '#1f2937';
      e.currentTarget.style.transform = 'scale(1)';
    }}
    onFocus={(e) => {
      e.currentTarget.style.outline = '2px solid #6b7280';
      e.currentTarget.style.outlineOffset = '2px';
      e.currentTarget.style.backgroundColor = '#374151';
      e.currentTarget.style.transform = 'scale(1.05)';
    }}
    onBlur={(e) => {
      e.currentTarget.style.outline = 'none';
      e.currentTarget.style.outlineOffset = '0px';
      e.currentTarget.style.backgroundColor = '#1f2937';
      e.currentTarget.style.transform = 'scale(1)';
    }}
  >
    Chat with Support
  </button>
</div>