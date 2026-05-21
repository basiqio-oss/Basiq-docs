---
title: Introduction to Basiq
excerpt: >-
  Basiq is a Consumer Data Right accredited API platform that provides the
  building blocks of financial services.
deprecated: false
hidden: false
icon: fad fa-hand-wave
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## What is Basiq?

Basiq is a <a href="https://blog.basiq.io/basiq-launches-cdr-data-holder-and-data-recipient-solution/">Consumer Data Right accredited</a> API platform that enables secure access to customer-consented financial data.

It provides a single integration point to access banking and financial data, and to generate insights that power lending, payments, wealth, and digital finance products.

## API Products

Basiq APIs are grouped into core product areas. Each maps directly to an OpenAPI specification.

<Grid columns="3" gapX="30px" gapY="30px" paddingY="1.5em" style={{ gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))' }}>
  <CoolTile header="Connect" href="https://raw.githubusercontent.com/basiqio-oss/Basiq-docs/refs/heads/v3.0/reference/connect.json" icon="fa-duotone fa-link" text="Customer-consented accounts, transactions, connections, consent, jobs, and users." />

  <CoolTile header="Enrich" href="https://raw.githubusercontent.com/basiqio-oss/Basiq-docs/refs/heads/v3.0/reference/enrich.json" icon="fa-duotone fa-chart-line" text="Merchant enrichment, categorisation, and transaction classification." />

  <CoolTile header="Insights" href="https://raw.githubusercontent.com/basiqio-oss/Basiq-docs/refs/heads/v3.0/reference/insights.json" icon="fa-duotone fa-magnifying-glass-chart" text="Income, expense, balance, identity, and affordability insights." />

  <CoolTile header="Reporting" href="" icon="fa-duotone fa-file-chart-column" text="Generate and manage financial reports across supported report types." />

  <CoolTile header="Identity" href="" icon="fa-duotone fa-id-card" text="Identity verification data and identity records linked to users." />

  <CoolTile header="Platform" href="https://raw.githubusercontent.com/basiqio-oss/Basiq-docs/refs/heads/v3.0/reference/platform.json" icon="fa-duotone fa-layer-group" text="Auth links, connectors, analytics, payees, statements, and system resources." />

  <CoolTile header="Webhooks" href="https://raw.githubusercontent.com/basiqio-oss/Basiq-docs/refs/heads/v3.0/reference/webhooks.json" icon="fa-duotone fa-webhook" text="Event-driven updates for jobs, connections, and data changes." />

  <CoolTile header="Affordability" href="https://raw.githubusercontent.com/basiqio-oss/Basiq-docs/refs/heads/v3.0/reference/affordability.json" icon="fa-duotone fa-scale-balanced" text="Income, expense, and affordability assessments (legacy APIs)." />
</Grid>

## API Overview

Start here to understand how Basiq fits together.

<Grid columns="3" gap="20px">
  <CoolCard header="Data Access" icon="fa-duotone fa-database" text="Access bank, transaction, and account data via secure consented connections." />

  <CoolCard header="Insights Layer" icon="fa-duotone fa-brain" text="Transform raw financial data into income, expense, and affordability insights." />

  <CoolCard header="Platform Services" icon="fa-duotone fa-sitemap" text="Manage consent, connectors, webhooks, and system configuration." />
</Grid>

## System Status

<Grid columns="2" gap="20px">
  <CoolTile header="Supported Regions" icon="fa-duotone fa-globe" text="Australia & New Zealand — full coverage of supported financial institutions." />

  <CoolTile header="Platform Status" icon="fa-duotone fa-signal" href="https://dashboard.basiq.io/status" text="Real-time API health, connectors, and system status." />
</Grid>
