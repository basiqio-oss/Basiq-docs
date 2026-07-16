---
title: API capabilities
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
# What the Basiq API can do for you

 

## ✅  Account verification

Instantly verify account ownership and balances in real time to improve the user experience and mitigate fraud and risk. Use this to automate responsible lending, reduce dishonour fees for payments and improve collections.

## ✅  Data aggregation for single view of customer finances

Access and aggregate all your customers financial data in one place to get a single view of customer finances. Use this to build or add PFM (Personal Financial Management) functionality and provide more tailored product offerings and recommendations.

## ✅  Provide ongoing access to customer data

Secure ongoing access to reliable account, transaction and identity data from +100 institutions in real-time to deliver more engaging and personalised experiences

## ✅  Data enrichment to understand spend behaviour

Gain greater insight into customer transactions with powerful overlay services across expense classification, merchant identification, merchant location and merchant logos. Ongoing access to enriched data lets you build next-generation financial planning and wealth management solutions.

## ✅  Powerful insights for deep financial analysis

Get a better understanding of your customer's financials by identifying income sources, expenses, assets and liabilities, and generate comprehensive, bank agnostic affordability reports for a complete picture of their financial position at any given point in time

## ✅  We provide event notifications

We offer Webhook support for event notifications. You can [subscribe](https://api.basiq.io/docs/webhooks) to changes in data through our Webhook feature and receive real-time updates.

# What the Basiq API can't do for you

 

## ❌  We don't provide write access

Basiq has read only access only, meaning we can not update or create any data when a customer provides their credentials.

## ❌  We don't expose customer credit card numbers

Credit card numbers are always masked to maintain PCI compliance.

## ❌  We don't share your data

We take data privacy very seriously and we do not hold onto or share any of your data without your consent.

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