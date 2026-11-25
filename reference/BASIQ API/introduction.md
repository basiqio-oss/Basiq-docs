---
title: Introduction to Basiq
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
Choose a Basiq product below to find API documentation for accessing financial data, generating insights, or managing platform services.

## What is Basiq?

Basiq is a <a href="https://blog.basiq.io/basiq-launches-cdr-data-holder-and-data-recipient-solution/">Consumer Data Right accredited</a> API platform that enables secure access to customer-consented financial data.

It provides a single integration point to access banking and financial data, and to generate insights that power lending, payments, wealth, and digital finance products.

## Products

Basiq groups its APIs into core product areas. Each maps directly to an OpenAPI specification (a machine-readable description of API endpoints, requests, and responses).

Select a product card to open its API reference. Each card includes a product name and a description of the available capabilities.

<Grid columns={3} style={{ gap: '24px', paddingBlock: '1.5em' }}>
  <CoolCard header="Connect" href="https://api.basiq.io/reference/posttoken" icon="far fa-link" text="Customer-consented accounts, transactions, connections, consent, jobs, and users." />

  <CoolCard header="Enrich" href="https://api.basiq.io/reference/enrich" icon="far fa-chart-line" text="Merchant enrichment, categorisation, and transaction classification." />

  <CoolCard header="Insights" href="https://api.basiq.io/reference/createinsight" icon="far fa-magnifying-glass-chart" text="Income, expense, balance, identity, and affordability insights." />

  <CoolCard header="Reporting" href="https://api.basiq.io/reference/createreport" icon="far fa-file-chart-column" text="Generate and manage financial reports across supported report types." />

  <CoolCard header="Identity" href="https://api.basiq.io/reference/getuseridentities" icon="far fa-id-card" text="Identity verification data and identity records linked to users." />

  <CoolCard header="Platform" href="https://api.basiq.io/reference/postauthlink" icon="far fa-layer-group" text="Auth links, connectors, analytics, payees, statements, and system resources." />

  <CoolCard header="Webhooks" href="https://api.basiq.io/reference/listappwebhooks" icon="far fa-webhook" text="Event-driven updates for jobs, connections, and data changes." />

  <CoolCard header="Affordability" href="https://api.basiq.io/reference/getaffordabilitylist" icon="far fa-scale-balanced" text="Income, expense, and affordability assessments (legacy APIs)." />
</Grid>

## API Overview

Select Data Access to access financial data with customer permission, Insights Layer to analyse that data, or Platform Services to manage your integration.

<Grid columns={3} style={{ gap: '24px', paddingBlock: '1em' }}>
  <CoolTile header="Data Access" href="https://api.basiq.io/reference/posttoken" icon="far fa-database" text="Access bank, transaction, and account data through secure connections that customers authorise." />

  <CoolTile header="Insights Layer" href="https://api.basiq.io/reference/createinsight" icon="far fa-brain" text="Transform raw financial data into income, expense, and affordability insights." />

  <CoolTile header="Platform Services" href="https://api.basiq.io/reference/postauthlink" icon="far fa-sitemap" text="Manage consent, connectors, webhooks, and system configuration." />
</Grid>

## System Status

**Supported Regions:** Australia & New Zealand — full coverage of supported financial institutions.

Select Platform Status to check API health and system status.

<CoolTile header="Platform Status" icon="far fa-signal" href="https://dashboard.basiq.io/status" text="Real-time API health, connectors, and system status." />

<br />