---
title: Access Methods
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
# Overview:

BASIQ offers partners a comprehensive suite of access methods designed to facilitate the aggregation of financial data. These methods empower partners to efficiently retrieve and utilise data from various sources, enabling them to develop innovative financial solutions tailored to their clients' needs.

<Cards columns={3}>
  <Card title="Web Connector" icon="fa-link" href="#web-connector">
    Securely shares login credentials to access bank portals and extract user accounts and transactions. Effective yet requires updates due to evolving bank security measures.
  </Card>

  <Card title="Open Banking" icon="fa-unlock" href="#open-banking">
    Enables secure access to bank account data via standardised APIs, ensuring compliance with regulations and simplifying multi-platform aggregation.
  </Card>

  <Card title="Statements Upload" icon="fa-upload" href="#statements-upload">
    Allows partners to upload financial statements in various formats, extracting transaction details, balances, and metadata for seamless integration.
  </Card>
</Cards>

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(48.645833333333336% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/IubyLqDtxwahi3LLLblm?embed" title="Basiq - Access Methods" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

## Web Connector:

<Tabs>
  <Tab title="Overview">
    The Web Connector, also known as "screen scraping", securely shares login credentials to access the bank's internet banking portal and extract a user's accounts and transactions. While effective, this method can be slow and susceptible to changes in the bank's portal, prompting banks to reinforce security measures.
  </Tab>

  <Tab title="API Versions">
    <Columns layout="auto">
      <Column>
        <Card title="Version 2" icon="fa-code">
          Supports **DDC (Digital Data Capture)** only. This version limits access to data through screen scraping.
        </Card>
      </Column>

      <Column>
        <Card title="Version 3" icon="fa-sync">
          Accommodates both **DDC and CDR (Consumer Data Right)**, allowing seamless adaptability to evolving standards.
        </Card>
      </Column>
    </Columns>
  </Tab>
</Tabs>

## Open Banking:

<Accordion title="Open Banking" icon="fa-unlock">
  The Open Banking access method enables partners to securely access bank account data through standardised APIs. BASIQ ensures compliance with Open Banking regulations, facilitating seamless access to account information, transaction history, and more directly from financial institutions. This method promotes compatibility and simplifies data aggregation across multiple banking platforms, empowering partners to offer comprehensive financial services.
</Accordion>

## Statements Upload:

<Columns layout="auto">
  <Column>
    <Card title="User-Friendly" icon="fa-smile">
      Partners can upload statements in formats such as PDFs or CSV files to the BASIQ platform effortlessly.
    </Card>
  </Column>

  <Column>
    <Card title="Advanced Parsing" icon="fa-brain">
      Our technology extracts transaction details, account balances, and metadata from uploaded files.
    </Card>
  </Column>

  <Column>
    <Card title="Flexibility" icon="fa-bolt">
      Provides unparalleled flexibility in handling diverse data sources, expediting integration processes.
    </Card>
  </Column>
</Columns>

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