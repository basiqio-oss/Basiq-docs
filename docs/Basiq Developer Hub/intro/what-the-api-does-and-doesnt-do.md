---
title: API capabilities
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
        e.target.style.backgroundColor = '#1565c0'; // Darker blue on hover
      }}
      onMouseLeave={(e) => {
        e.target.style.transform = 'scale(1)';
        e.target.style.backgroundColor = '#1e88e5'; // Original blue
      }}
    >
      Support team
    </button>
  </div>
</div>