---
title: Callouts
fullscreen: false
hidden: true
---
### Custom Callout Example

<div
  style={{
  border: "2px solid #4caf50", 
  borderRadius: "8px", 
  backgroundColor: "#e8f5e9", 
  padding: "16px", 
  margin: "16px 0", 
  fontFamily: "Arial, sans-serif"
}}
>
  <strong>📢 Attention!</strong> This is a callout box made directly in MDX using inline HTML and CSS.

  <ul>
    <li>Simple to create.</li>
    <li>No extra libraries required.</li>
    <li>Fully customizable with CSS.</li>
  </ul>
</div>

Here is the rest of your MDX content!

```jsx title="/src/components/HelloCodeTitle.js"
function HelloCodeTitle(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

import React from "react";

const styles = \{
&#x20; card: \{
&#x20;   background: "#f9f9f9",
&#x20;   padding: "1.5rem",
&#x20;   borderRadius: "8px",
&#x20;   boxShadow: "0px 4px 8px rgba(0, 0, 0, 0.1)",
&#x20;   marginBottom: "1rem",
&#x20; },
&#x20; accordionHeader: \{
&#x20;   fontSize: "1.25rem",
&#x20;   fontWeight: "bold",
&#x20;   marginBottom: "0.5rem",
&#x20; },
&#x20; accordionBody: \{
&#x20;   fontSize: "1rem",
&#x20;   color: "#333",
&#x20; },
&#x20; column: \{
&#x20;   padding: "1rem",
&#x20; },
&#x20; tabs: \{
&#x20;   display: "flex",
&#x20;   gap: "1rem",
&#x20;   borderBottom: "2px solid #eaeaea",
&#x20;   marginBottom: "1rem",
&#x20; },
&#x20; tab: \{
&#x20;   padding: "0.75rem 1rem",
&#x20;   fontWeight: "bold",
&#x20;   cursor: "pointer",
&#x20;   border: "none",
&#x20;   background: "none",
&#x20; },
&#x20; activeTab: \{
&#x20;   color: "#007BFF",
&#x20;   borderBottom: "3px solid #007BFF",
&#x20; },
};

const Accordion = (\{ title, icon, children }) => (
&#x20; \<div style=\{styles.card}>
&#x20;   \<div style=\{styles.accordionHeader}>
&#x20;     \<i className=\{\`fa $\{icon}\`}>\</i> \{title}
&#x20;   \</div>
&#x20;   \<div style=\{styles.accordionBody}>
&#x20;     \{children}
&#x20;   \</div>
&#x20; \</div>
);

const Card = (\{ title, icon, children }) => (
&#x20; \<div style=\{styles.card}>
&#x20;   \<div style=\{\{ fontWeight: "bold", fontSize: "1.2rem" }}>
&#x20;     \<i className=\{\`fa $\{icon}\`}>\</i> \{title}
&#x20;   \</div>
&#x20;   \<div style=\{styles.accordionBody}>
&#x20;     \{children}
&#x20;   \</div>
&#x20; \</div>
);

const Column = (\{ children }) => (
&#x20; \<div style=\{styles.column}>
&#x20;   \{children}
&#x20; \</div>
);

const Tab = (\{ title, children }) => (
&#x20; \<div>
&#x20;   \<h3>\{title}\</h3>
&#x20;   \<div>\{children}\</div>
&#x20; \</div>
);

const Tabs = (\{ children }) => (
&#x20; \<div>
&#x20;   \<div style=\{styles.tabs}>
&#x20;     \{children}
&#x20;   \</div>
&#x20; \</div>
);

const App = () => \{
&#x20; return (
&#x20;   \<Tabs>
&#x20;     \<Tab title="What the Basiq API can do for you">
&#x20;       \<div style=\{\{ display: "flex", justifyContent: "space-between" }}>
&#x20;         \<Column>
&#x20;           \<Accordion title="✅ Account verification" icon="fa-check-circle">
&#x20;             Instantly verify account ownership and balances in real-time to improve the user experience and mitigate fraud and risk.&#x20;
&#x20;           \</Accordion>
&#x20;           \<Accordion title="✅ Data aggregation for single view of customer finances" icon="fa-chart-line">
&#x20;             Access and aggregate all your customers' financial data in one place to get a single view of customer finances.
&#x20;           \</Accordion>
&#x20;         \</Column>

&#x20;         \<Column>
&#x20;           \<Accordion title="✅ Provide ongoing access to customer data" icon="fa-sync-alt">
&#x20;             Secure ongoing access to reliable account, transaction, and identity data from 100+ institutions in real-time.
&#x20;           \</Accordion>
&#x20;           \<Accordion title="✅ Data enrichment to understand spend behaviour" icon="fa-dollar-sign">
&#x20;             Gain greater insight into customer transactions with powerful overlay services, including expense classification, merchant logos.
&#x20;           \</Accordion>
&#x20;         \</Column>

&#x20;         \<Column>
&#x20;           \<Accordion title="✅ Powerful insights for deep financial analysis" icon="fa-chart-pie">
&#x20;             Get a better understanding of your customer's financials by identifying income sources, expenses, assets, and liabilities.
&#x20;           \</Accordion>
&#x20;           \<Accordion title="✅ We provide event notifications" icon="fa-bell">
&#x20;             We offer Webhook support for event notifications. You can \<a href="https\://api.basiq.io/docs/webhooks" target="\_blank">subscribe\</a> to changes.
&#x20;           \</Accordion>
&#x20;         \</Column>
&#x20;       \</div>
&#x20;     \</Tab>

&#x20;     \<Tab title="What the Basiq API can't do for you">
&#x20;       \<div style=\{\{ display: "flex", justifyContent: "space-between" }}>
&#x20;         \<Card title="❌ No write access" icon="fa-ban">
&#x20;           Basiq has read-only access, meaning we cannot update or create any data when a customer provides their credentials.
&#x20;         \</Card>
&#x20;         \<Card title="❌ No credit card numbers" icon="fa-credit-card">
&#x20;           Credit card numbers are always masked to maintain PCI compliance.
&#x20;         \</Card>
&#x20;         \<Card title="❌ We don't share your data" icon="fa-shield-alt">
&#x20;           We take data privacy very seriously and do not share any of your data without your consent.
&#x20;         \</Card>
&#x20;       \</div>
&#x20;     \</Tab>
&#x20;   \</Tabs>
&#x20; );
};

export default App;