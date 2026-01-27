---
title: Welcome to Basiq
excerpt: >-
  Basiq is a Consumer Data Right accredited API platform that provides the
  building blocks of financial services.
deprecated: false
hidden: false
icon: fad fa-hand-wave
metadata:
  robots: index
---
<Grid columns="3" gap="20px" style={{ gridTemplateColumns: 'repeat(auto‑fit, minmax(200px, 1fr))' }}>
  <CoolCard header="Quick Start" href="https://api.basiq.io/docs/getting-started" icon="fa-duotone fa-solid fa-rocket-launch" text="Register your app, get API keys, authenticate, and create a user" />

  <CoolCard header="API Reference" href="https://api.basiq.io/reference/introduction" icon="fa-duotone fa-solid fa-code-simple" text="Full OpenAPI specification & endpoints for Connect, Enrich, Reporting, Webhooks, Affordability" />

  <CoolCard header="Consent Management" href="https://api.basiq.io/docs/consent" icon="fa-duotone fa-solid fa-brush" text="Configure consent UI, customize policy, institutions and branding" />
</Grid>

{/* Note to editors: Consider moving Recent Releases to Basics as they’re demoted */}

## Recent Releases

<Grid columns="3" gapX="30px" gapY="30px" paddingY="1.5em" style={{ gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))' }}>
  <CoolTile header={<span>Payees API <span style={{ color: '#f59e0b', fontSize: '0.8em' }}>NEW</span></span>} href="https://api.basiq.io/reference/payees" icon="fa-duotone fa-solid fa-users" text="Manage and retrieve payee information with support for multiple payee types including domestic, biller, international, and digital wallet payments." />

  <CoolTile header={<span>Expense Ratio Insights <span style={{ color: '#f59e0b', fontSize: '0.8em' }}>NEW</span></span>} href="https://api.basiq.io/reference/getexpenseratioinsights" icon="fa-duotone fa-solid fa-chart-pie" text="Analyze spending patterns and expense distribution across categories with detailed financial insights." />

  <CoolTile header={<span>Verify Income Insights <span style={{ color: '#f59e0b', fontSize: '0.8em' }}>NEW</span></span>} href="https://api.basiq.io/reference/verifyincomeinsight" icon="fa-duotone fa-solid fa-money-bill-wave" text="Verifies if a user’s income falls within a specified range using a required min and optional max value." />

  <CoolTile header={<span>Identity API - Insights <span style={{ color: '#f59e0b', fontSize: '0.8em' }}>NEW</span></span>} href="https://api.basiq.io/reference/getidentityinsights/" icon="fa-duotone fa-solid fa-id-card" text="Identity features are on the way — stay tuned for updates." />

  <CoolTile header={<span>Insights API – Account Details <span style={{ color: '#f59e0b', fontSize: '0.8em' }}>NEW</span></span>} href="https://api.basiq.io/reference/getaccountinsights#/" icon="fa-duotone fa-solid fa-lightbulb" text="Get detailed account insights via /users/{userId}/insights/account to build richer account experiences." />

  <CoolTile header={<span>Account Balance Verification <span style={{ color: '#f59e0b', fontSize: '0.8em' }}>NEW</span></span>} href="https://api.basiq.io/reference/getbalanceinsights#/" icon="fa-duotone fa-solid fa-scale-balanced" text="Query account balance insights with flexible filtering (min/max parameters)." />

  <CoolTile header="Analytics API – Connection Analytics" href="https://api.basiq.io/reference/getconnectionanalytics#/" icon="fa-duotone fa-solid fa-chart-line" text="Retrieve insights about user connections to build stronger analytics dashboards." />

  <CoolTile header="Merchant Search & Retrieve" href="https://api.basiq.io/reference/merchantsearch" icon="fa-duotone fa-solid fa-store" text="Enrich your transactions by searching and retrieving merchant info." />

  <CoolTile header="Basiq Demo App" href="https://demo.basiq.io" icon="fa-duotone fa-solid fa-display" text="A one-stop demo app to explore Basiq’s APIs and end-to-end workflows." />
</Grid>

## Developer Basics

<Grid columns="3" gapX="30px" gapY="30px" paddingY="1.5em">
  <CoolTile header="Developer Hub" href="https://api.basiq.io/reference/developer-hub" icon="fa-duotone fa-solid fa-layer-group" text="Guides, best practices, SDK & CLI support" />

  <CoolTile header="Access Methods" href="https://api.basiq.io/docs/access-method" icon="fa-duotone fa-solid fa-link" text="Web connector, Open Banking, statement upload options" />

  <CoolTile header="Connections & Sync" href="https://api.basiq.io/docs/data-connections" icon="fa-duotone fa-solid fa-code-branch" text="Manage user connections, refresh patterns, caching" />

  <CoolTile header="Reports & Affordability APIs" href="https://api.basiq.io/docs/consumer-affordability/" icon="fa-duotone fa-solid fa-chart-simple" text="Create and retrieve statements, affordability and expense summaries" />

  <CoolTile header="Webhooks & Real‑time" href="https://api.basiq.io/reference/addwebhook/" icon="fa-duotone fa-solid fa-bell" text="Post‑back events for jobs, connections or data updates" />

  <CoolTile header="SDK / CLI" href="https://api.basiq.io/reference/developer-hub" icon="fa-duotone fa-solid fa-terminal" text="Generate JavaScript / TypeScript SDK from OpenAPI or use CLI" />
</Grid>

## Integration Guides

<Grid columns="3" gapX="30px" gapY="30px" paddingY="1.5em" style={{ gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))' }}>
  <CoolTile header="Activate Your Account" href="https://api.basiq.io/docs/activate-your-account" icon="fa-duotone fa-solid fa-user-check" text="Steps to verify and activate your Basiq account." />

  <CoolTile header="Application Setup" href="https://api.basiq.io/docs/application-setup" icon="fa-duotone fa-solid fa-gears" text="Register your application and generate API keys." />

  <CoolTile header="Consent UI Customisation" href="https://api.basiq.io/docs/consent-ui-customisation" icon="fa-duotone fa-solid fa-palette" text="Tailor the consent flow, branding, and policies." />
</Grid>

## API & Connector Health

<StatusPage title="API & Connectors" url="https://status.basiq.io/" />

<br />
