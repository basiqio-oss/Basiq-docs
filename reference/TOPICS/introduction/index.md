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
    <button onClick={() => Intercom('showNewMessage', 'issues on FAQs:')} style={{
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
          }} onMouseEnter={(e) => {
            e.target.style.transform = 'scale(1.1)';
            e.target.style.backgroundColor = '#333333'; // Slightly lighter dark on hover
          }} onMouseLeave={(e) => {
            e.target.style.transform = 'scale(1)';
            e.target.style.backgroundColor = '#1E1E1E'; // Original dark
          }}>Support team</button>
  </div>
</div>