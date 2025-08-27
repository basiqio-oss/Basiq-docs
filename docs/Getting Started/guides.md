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
  <CoolTile header="Analytics API" href="https://api.basiq.io/reference/getuseranalytics" icon="fa-duotone fa-solid fa-chart-line" isBeta text="Access categorised insights and financial behavior patterns" />

  <CoolTile header={<span>Basiq Demo App <span style={{ color: '#f59e0b', fontSize: '0.8em' }}>NEW</span></span>} href="https://demo.basiq.io" icon="fa-duotone fa-solid fa-display" text="A one-stop demo app to explore Basiq’s APIs and end-to-end workflows." />

  <CoolTile header="Merchant Search & Retrieve" href="https://api.basiq.io/reference/merchantsearch" icon="fa-duotone fa-solid fa-store" text="Enrich your transactions by searching and retrieving merchant info" />

  <CoolTile header="PFM App Update" href="https://api.basiq.io/docs/demo-pfm" icon="fa-duotone fa-solid fa-mobile-screen" text="New PFM demo app with budgeting, transactions and affordability" />

  <CoolTile header="Consent Status Filters" href="https://api.basiq.io/reference/getconsents" icon="fa-duotone fa-solid fa-filter-circle-xmark" text="Retrieve consents using status filters: active, expired, revoked" />

  <CoolTile header="Business Affordability Report" href="https://api.basiq.io/docs/business-affordability" icon="fa-duotone fa-solid fa-file-invoice-dollar" text="Assess a business’s financial capacity with downloadable JSON or PDF reports." />
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

<StatusPage title="Commonwealth Bank (CBA) Web Connector - Significantly increased failure rate" url="https://status.basiq.io/" />

<br />
