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
Set up your Basiq integration, explore the APIs, and check service status using the links below.

<Grid columns="3" gap="20px" style={{ gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))' }}>
  <CoolCard header="Quick Start" href="https://api.basiq.io/docs/getting-started" icon="fa-duotone fa-solid fa-rocket-launch" text="Register your application, get API keys, authenticate, and create a user." />

  <CoolCard header="API Reference" href="https://api.basiq.io/reference/introduction" icon="fa-duotone fa-solid fa-code-simple" text="Explore API endpoints for Connect, Enrich, Reporting, Webhooks, and Affordability." />

  <CoolCard header="Consent Management" href="https://api.basiq.io/docs/consent" icon="fa-duotone fa-solid fa-brush" text="Configure the consent interface, policies, institutions, and branding." />
</Grid>

{/* Note to editors: Consider moving Recent Releases to Basics as they’re demoted */}

## Recent Releases

Explore insights (results derived from financial data for analysis or verification) and other API features.

<Grid
  columns="3"
  gapX="30px"
  gapY="30px"
  paddingY="1.5em"
  style={{ gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))" }}
>
  <CoolTile
    header={<span>Account Identity Verification <span style={{ display: 'inline-block', marginLeft: '0.4em', padding: '0.15em 0.55em', border: '1px solid currentColor', borderRadius: '999px', fontSize: '0.65em', fontWeight: 700, lineHeight: 1.4, verticalAlign: 'middle', whiteSpace: 'nowrap' }}>New</span></span>}
    href="https://api.basiq.io/reference/createinsight"
    icon="far fa-address-card"
    text="Match a bank branch code (BSB) and account number against shared accounts. Retrieve identity information for the customer who authorised consent."
  />

  <CoolTile
    header="Create Insight"
    href="https://api.basiq.io/reference/createinsight"
    icon="fa-solid fa-plus-circle"
    text="Create account, balance, identity, income, or expense-ratio verification insights. Only expense-ratio verification supports multiple users per request."
  />

  <CoolTile
    header="List Insight Types"
    href="https://api.basiq.io/reference/getinsighttypes"
    icon="fa-solid fa-list"
    text="List supported insight types and their input schemas (definitions of accepted data)."
  />

  <CoolTile
    header="Retrieve Insight Type"
    href="https://api.basiq.io/reference/getinsighttype"
    icon="fa-solid fa-magnifying-glass"
    text="Retrieve an insight type's definition and required input structure."
  />

  <CoolTile
    header="Payees API"
    href="https://api.basiq.io/reference/payees"
    icon="fa-solid fa-users"
    text="Retrieve and manage payee details for domestic, biller, international, and digital wallet payments."
  />

  <CoolTile
    header="Expense Ratio Insights"
    href="https://api.basiq.io/reference/getexpenseratioinsights"
    icon="fa-solid fa-chart-pie"
    text="Analyse spending patterns and spending by category across user transactions."
  />

  <CoolTile
    header="Verify Income Insight"
    href="https://api.basiq.io/reference/verifyincomeinsight"
    icon="fa-solid fa-money-bill-wave"
    text="Check whether a user's income falls within minimum and maximum values."
  />

  <CoolTile
    header="Identity Insights API"
    href="https://api.basiq.io/reference/getidentityinsights/"
    icon="fa-solid fa-id-card"
    text="Compare a user's name, phone number, email, and address to retrieve identity insights."
  />

  <CoolTile
    header="Account Insights"
    href="https://api.basiq.io/reference/getaccountinsights#/"
    icon="fa-solid fa-lightbulb"
    text="Retrieve account insights using /users/{userId}/insights/account."
  />

  <CoolTile
    header="Account Balance Verification"
    href="https://api.basiq.io/reference/getbalanceinsights"
    icon="fa-solid fa-scale-balanced"
    text="Retrieve account balance insights with optional minimum and maximum filters."
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
    text="Search for merchants and retrieve details to add context to transactions."
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
  <CoolTile header="Developer Hub" href="https://api.basiq.io/reference/developer-hub" icon="fa-duotone fa-solid fa-layer-group" text="Explore guides, best practices, software development kits (SDKs), and command-line interface (CLI) tools." />

  <CoolTile header="Access Methods" href="https://api.basiq.io/docs/access-method" icon="fa-duotone fa-solid fa-link" text="Compare web connector, Open Banking, and statement upload options for accessing financial data." />

  <CoolTile header="Connections & Sync" href="https://api.basiq.io/docs/data-connections" icon="fa-duotone fa-solid fa-code-branch" text="Manage user connections, refresh data, and cache results for reuse." />

  <CoolTile header="Reports & Affordability APIs" href="https://api.basiq.io/docs/consumer-affordability/" icon="fa-duotone fa-solid fa-chart-simple" text="Create and retrieve statements, affordability summaries, and expense summaries." />

  <CoolTile header="Webhooks & Real‑time" href="https://api.basiq.io/reference/addwebhook/" icon="fa-duotone fa-solid fa-bell" text="Receive webhooks (event notifications sent to your application) for jobs, connections, and data updates." />

  <CoolTile header="SDK / CLI" href="https://api.basiq.io/reference/developer-hub" icon="fa-duotone fa-solid fa-terminal" text="Generate a JavaScript or TypeScript SDK using the CLI and OpenAPI (a machine-readable API definition)." />
</Grid>

## Integration Guides

<Grid columns="3" gapX="30px" gapY="30px" paddingY="1.5em" style={{ gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))' }}>
  <CoolTile header="Activate Your Account" href="https://api.basiq.io/docs/activate-your-account" icon="fa-duotone fa-solid fa-user-check" text="Verify and activate your Basiq account." />

  <CoolTile header="Application Setup" href="https://api.basiq.io/docs/application-setup" icon="fa-duotone fa-solid fa-gears" text="Register your application and generate API keys." />

  <CoolTile header="Consent Interface Customisation" href="https://api.basiq.io/docs/consent-ui-customisation" icon="fa-duotone fa-solid fa-palette" text="Customise the consent flow, branding, and policies." />
</Grid>

## API & Connector Health

[Check API and connector status on the Basiq status page](https://status.basiq.io/).

<StatusPage title="API & Connectors" url="https://status.basiq.io/" />

<br />