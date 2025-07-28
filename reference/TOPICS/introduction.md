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

Basiq’s Products allow you to:

<Cards columns={3}>
  <Card title="Connect" icon="fa-link">
    Access account and transaction data in real-time.
  </Card>

  <Card title="Enrich" icon="fa-chart-line">
    Enhance transactions with merchant data.
  </Card>

  <Card title="Discover" icon="fa-search">
    Gain deeper insights into your customer's finances.
  </Card>
</Cards>

Our partner ecosystem branches far and wide, but our most common use cases are:

<Tabs>
  <Tab title="Use Cases">
    <Cards columns={2}>
      <Card title="Account Aggregation" icon="fa-database">
        Access and aggregate all your customers' financial data in one place. Build or add Personal Financial Management (PFM) functionality and provide tailored product offerings and recommendations.
      </Card>

      <Card title="Account Verification" icon="fa-check-circle">
        Instantly verify account ownership and balances in real time. Automate responsible lending, reduce dishonor fees for payments, and improve collections.
      </Card>
    </Cards>

    <Cards columns={2}>
      <Card title="Data Enrichment" icon="fa-layer-group">
        Gain insights into customer transactions with powerful overlay services: expense classification, merchant identification, income detection, and behavioral spend analytics.
      </Card>

      <Card title="Wealth Management" icon="fa-chart-pie">
        Use enriched data for next-generation financial planning and wealth management solutions.
      </Card>
    </Cards>
  </Tab>

  <Tab title="Supported Regions">
    > 🚧 **Basiq APIs are currently only available in Australia and New Zealand.**\
    > We are working to expand availability to other countries. Visit this link for a complete list of [supported financial institutions](https://dashboard.basiq.io/status).
  </Tab>
</Tabs>

<Accordion title="Partner Showcase" icon="fa-users">
  Check out how some of our customers are using Basiq. Visit our [Partner Showcase](https://basiq.io/blog/category/partner-showcase/) to see Basiq in action.
</Accordion>

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