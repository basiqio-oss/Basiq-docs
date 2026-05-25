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

<Grid
  columns="3"
  gapX="30px"
  gapY="30px"
  paddingY="1.5em"
  style={{ gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))" }}
>
  <CoolTile
    header="Create Insight"
    href="https://api.basiq.io/reference/createinsight"
    icon="fa-solid fa-plus-circle"
    text="Create an insight for one or more users in a single request. Supports Account, Balance, Identity, Income, and Expense Ratio verification types."
  />

  <CoolTile
    header="List Insight Types"
    href="https://api.basiq.io/reference/getinsighttypes"
    icon="fa-solid fa-list"
    text="Returns all supported Insight types and their input schemas for validation and discovery."
  />

  <CoolTile
    header="Retrieve Insight Type"
    href="https://api.basiq.io/reference/getinsighttype"
    icon="fa-solid fa-magnifying-glass"
    text="Returns the definition of a single Insight type, including its expected input schema."
  />

  <CoolTile
    header="Payees API"
    href="https://api.basiq.io/reference/payees"
    icon="fa-solid fa-users"
    text="Manage and retrieve payee information including domestic, biller, international, and digital wallet payments."
  />

  <CoolTile
    header="Expense Ratio Insights"
    href="https://api.basiq.io/reference/getexpenseratioinsights"
    icon="fa-solid fa-chart-pie"
    text="Analyze spending patterns and category distribution across user transactions."
  />

  <CoolTile
    header="Verify Income Insight"
    href="https://api.basiq.io/reference/verifyincomeinsight"
    icon="fa-solid fa-money-bill-wave"
    text="Verify whether a user's income falls within a specified range using min and max values."
  />

  <CoolTile
    header="Identity Insights API"
    href="https://api.basiq.io/reference/getidentityinsights/"
    icon="fa-solid fa-id-card"
    text="Identity insights are coming soon."
  />

  <CoolTile
    header="Account Insights"
    href="https://api.basiq.io/reference/getaccountinsights#/"
    icon="fa-solid fa-lightbulb"
    text="Retrieve detailed account insights via /users/{userId}/insights/account."
  />

  <CoolTile
    header="Account Balance Verification"
    href="https://api.basiq.io/reference/getbalanceinsights"
    icon="fa-solid fa-scale-balanced"
    text="Query account balance insights with optional min and max filters."
  />

  <CoolTile
    header="Connection Analytics"
    href="https://api.basiq.io/reference/getconnectionanalytics#/"
    icon="fa-solid fa-chart-line"
    text="View analytics about user connections for reporting and dashboards."
  />

  <CoolTile
    header="Merchant Search"
    href="https://api.basiq.io/reference/merchantsearch"
    icon="fa-solid fa-store"
    text="Search and retrieve merchant data to enrich transaction insights."
  />

  <CoolTile
    header="Basiq Demo App"
    href="https://demo.basiq.io"
    icon="fa-solid fa-display"
    text="Explore Basiq APIs and workflows through the interactive demo app."
  />
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
