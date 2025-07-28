---
title: Welcome to Basiq
excerpt: >-
  Basiq is a Consumer Data Right accredited API platform that provides the
  building blocks of financial services.
deprecated: false
hidden: true
metadata:
  robots: index
---
<Grid columns="3" gap="20px" style={{ gridTemplateColumns: 'repeat(auto‑fit, minmax(200px, 1fr))' }}>
  <CoolCard header="Quick Start" href="https://api.basiq.io/docs/getting-started" icon="fa-duotone fa-solid fa-rocket-launch" text="Register your app, get API keys, authenticate, and create a user" />

  <CoolCard header="API Reference" href="https://api.basiq.io/reference/introduction" icon="fa-duotone fa-solid fa-code-simple" text="Full OpenAPI specification & endpoints for Connect, Enrich, Reporting, Webhooks, Affordability" />

  <CoolCard header="Customize UI Consent" href="https://api.basiq.io/docs/access-method" icon="fa-duotone fa-solid fa-brush" text="Configure consent UI, customize policy, institutions and branding" />
</Grid>

{/* Note to editors: Consider moving Recent Releases to Basics as they’re demoted */}

## Recent Releases

<Grid columns="3" gapX="30px" gapY="30px" paddingY="1.5em" style={{ gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))' }}>
  <CoolTile header="Analytics API" href="https://api.basiq.io/reference/getuseranalytics" icon="fa-duotone fa-solid fa-chart-line" isBeta text="Access categorised insights and financial behavior patterns" />

  <CoolTile header="Merchant Search & Retrieve" href="https://api.basiq.io/reference/merchantsearch" icon="fa-duotone fa-solid fa-store" text="Enrich your transactions by searching and retrieving merchant info" />

  <CoolTile header="PFM App Update" href="https://api.basiq.io/docs/demo-pfm" icon="fa-duotone fa-solid fa-mobile-screen" text="New PFM demo app with budgeting, transactions and affordability" />

  <CoolTile header="Consent Status Filters" href="https://api.basiq.io/reference/getconsents" icon="fa-duotone fa-solid fa-filter-circle-xmark" text="Retrieve consents using status filters: active, expired, revoked" />

  <CoolTile header="Business Affordability Report" href="https://api.basiq.io/docs/business-affordability" icon="fa-duotone fa-solid fa-file-invoice-dollar" text="Assess a business’s financial capacity with downloadable JSON or PDF reports." />

  <CoolTile header="Dashboard MFA & Team Invites" href="https://api.basiq.io/docs/quickstart-basiq-dashboard/editing-profile-account-settings-and-enabling-2fa" icon="fa-duotone fa-solid fa-user-lock" text="Multi‑factor authentication, team permissions and app environment setup" />
</Grid>

## Developer Basics

<Grid columns="3" gapX="30px" gapY="30px" paddingY="1.5em">
  <CoolTile header="Developer Hub" href="https://api.basiq.io/reference/developer-hub" icon="fa-duotone fa-solid fa-layer-group" text="Guides, best practices, SDK & CLI support" />

  <CoolTile header="Access Methods" href="https://api.basiq.io/docs/access-method" icon="fa-duotone fa-solid fa-link" text="Web connector, Open Banking, statement upload options" />

  <CoolTile header="Connections & Sync" href="https://api.basiq.io/docs/data-connections" icon="fa-duotone fa-solid fa-code-branch" text="Manage user connections, refresh patterns, caching" />

  <CoolTile header="Reports & Affordability APIs" href="https://api.basiq.io/reference/introduction#reporting" icon="fa-duotone fa-solid fa-chart-simple" text="Create and retrieve statements, affordability and expense summaries" />

  <CoolTile header="Webhooks & Real‑time" href="https://api.basiq.io/reference/introduction#webhooks" icon="fa-duotone fa-solid fa-bell" text="Post‑back events for jobs, connections or data updates" />

  <CoolTile header="SDK / CLI" href="https://api.basiq.io/reference/developer-hub" icon="fa-duotone fa-solid fa-terminal" text="Generate JavaScript / TypeScript SDK from OpenAPI or use CLI" />
</Grid>

## Integration Guides

<Grid columns="3" gapX="30px" gapY="30px" paddingY="1.5em" style={{ gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))' }}>
  <CoolTile header="Activate Your Account" href="https://api.basiq.io/docs/activate-your-account" icon="fa-duotone fa-solid fa-user-check" text="Steps to verify and activate your Basiq account." />

  <CoolTile header="Application Setup" href="https://api.basiq.io/docs/application-setup" icon="fa-duotone fa-solid fa-gears" text="Register your application and generate API keys." />

  <CoolTile header="Consent UI Customisation" href="https://api.basiq.io/docs/access-method" icon="fa-duotone fa-solid fa-palette" text="Tailor the consent flow, branding, and policies." />
</Grid>

<br />

<Grid columns={2} gap="20px">
  <CoolImageCard header="PFM Starter Kit" href="https://api.basiq.io/docs/pfm-overview" src="https://files.readme.io/843b303b4f8eaa9f02ffb0abec834798a08f6f8439889db0506828090a2c09fa-PFM-1080x700.png" text="Help users better manage their finances with Basiq’s Personal Finance Management tools." />

  <CoolImageCard header="Income Verification Kit" href="https://api.basiq.io/docs/income-verification" src="https://example.basiq.io/income-verification.png" text="Verify user income streams to support lending and affordability workflows." />
</Grid>