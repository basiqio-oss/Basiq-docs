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

## Recent Releases;

     <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '30px', marginBottom: '2em' }}>
        {[
          {
            title: 'Payees API',
            url: 'https://api.basiq.io/reference/payees',
            icon: 'fa-users',
            desc: 'Manage and retrieve payee information with support for multiple payee types including domestic, biller, international, and digital wallet payments.',
            badge: 'NEW'
          },
          {
            title: 'Expense Ratio Insights',
            url: 'https://api.basiq.io/reference/getexpenseratioinsights',
            icon: 'fa-chart-pie',
            desc: 'Analyze spending patterns and expense distribution across categories with detailed financial insights.',
            badge: 'NEW'
          },
          {
            title: 'Verify Income Insights',
            url: 'https://api.basiq.io/reference/verifyincomeinsight',
            icon: 'fa-money-bill-wave',
            desc: 'Verifies if a user\'s income falls within a specified range using a required min and optional max value.',
            badge: 'NEW'
          },
          {
            title: 'Identity API - Insights',
            url: 'https://api.basiq.io/reference/getidentityinsights/',
            icon: 'fa-id-card',
            desc: 'Identity features are on the way — stay tuned for updates.',
            badge: 'NEW'
          },
          {
            title: 'Insights API – Account Details',
            url: 'https://api.basiq.io/reference/getaccountinsights#/',
            icon: 'fa-lightbulb',
            desc: 'Get detailed account insights via /users/{userId}/insights/account to build richer account experiences.',
            badge: 'NEW'
          },
          {
            title: 'Account Balance Verification',
            url: 'https://api.basiq.io/reference/getbalanceinsights#/',
            icon: 'fa-scale-balanced',
            desc: 'Query account balance insights with flexible filtering (min/max parameters).',
            badge: 'NEW'
          },
          {
            title: 'Analytics API – Connection Analytics',
            url: 'https://api.basiq.io/reference/getconnectionanalytics#/',
            icon: 'fa-chart-line',
            desc: 'Retrieve insights about user connections to build stronger analytics dashboards.'
          },
          {
            title: 'Merchant Search & Retrieve',
            url: 'https://api.basiq.io/reference/merchantsearch',
            icon: 'fa-store',
            desc: 'Enrich your transactions by searching and retrieving merchant info.'
          },
          {
            title: 'Basiq Demo App',
            url: 'https://demo.basiq.io',
            icon: 'fa-display',
            desc: 'A one-stop demo app to explore Basiq\'s APIs and end-to-end workflows.'
          }
        ].map(({ title, url, icon, desc, badge }) => (
          <a
            key={title}
            href={url}
            style={{
              border: '1px solid #ddd',
              borderRadius: '12px',
              padding: '20px',
              textDecoration: 'none',
              color: '#333',
              boxShadow: '0 2px 8px rgba(0,0,0,0.05)',
              transition: 'box-shadow 0.2s',
              display: 'flex',
              flexDirection: 'column'
            }}
            onMouseEnter={(e) => e.currentTarget.style.boxShadow = '0 4px 16px rgba(0,0,0,0.1)'}
            onMouseLeave={(e) => e.currentTarget.style.boxShadow = '0 2px 8px rgba(0,0,0,0.05)'}
          >
            <div style={{ marginBottom: '0.8em' }}>
              <h3 style={{ margin: '0 0 0.5em 0', fontSize: '1.1em' }}>
                {title}
                {badge && (
                  <span
                    style={{
                      marginLeft: '8px',
                      fontSize: '0.75em',
                      color: '#f59e0b',
                      fontWeight: 'bold'
                    }}
                  >
                    {badge}
                  </span>
                )}
              </h3>
              <i
                className={`fa-duotone fa-solid ${icon}`}
                style={{ fontSize: '1.5em', color: '#f59e0b' }}
              ></i>
            </div>
            <p style={{ margin: 0, color: '#555', fontSize: '0.95em', lineHeight: '1.5' }}>
              {desc}
            </p>
          </a>
        ))}
      </div>

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
