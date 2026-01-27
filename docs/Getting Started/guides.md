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

     <div style={{ display: 'flex', flexWrap: 'wrap', gap: '30px' }}>
        {[
          {
            title: 'Payees API',
            url: 'https://api.basiq.io/reference/payees',
            icon: 'fa-users',
            desc: 'Manage and retrieve payee information with support for multiple payee types including domestic, biller, international, and digital wallet payments. List all payees with advanced filtering and pagination.',
            badge: 'New',
            example: 'Retrieve all domestic payees, filter payees by connection, or get detailed information for a specific payee including bank details.',
            params: [
              { name: 'GET /users/{userId}/payees', desc: 'List all payees with pagination and filtering support' },
              { name: 'GET /users/{userId}/payees/{payeeId}', desc: 'Get detailed payee information by payee ID' },
              { name: 'Query Parameters', desc: 'limit (1-500), filter by type, connectionId, or created date' }
            ]
          },
          {
            title: 'Expense Ratio Insights',
            url: 'https://api.basiq.io/reference/getexpenseratioinsights',
            icon: 'fa-chart-pie',
            desc: 'Analyze spending patterns and expense distribution across categories. Get insights into how much users are spending on different expense categories relative to their income.',
            badge: 'New',
            example: 'Analyze expense ratios for budgeting applications, identify spending trends, or provide personalized financial recommendations based on expense categories.',
            params: [
              { name: 'Body Params', desc: 'Period and category filters for expense analysis' },
              { name: 'expense object', desc: 'Configuration for expense ratio calculation and filtering' },
              { name: 'Response', desc: 'Returns expense breakdown by category with ratio percentages' }
            ]
          },
        ].map(({ title, url, icon, desc, badge, example, params }) => (
          <a
            key={title}
            href={url}
            style={{
              flex: '1 1 250px',
              border: '1px solid #ddd',
              borderRadius: '12px',
              padding: '20px',
              textDecoration: 'none',
              color: '#333',
              boxShadow: '0 2px 8px rgba(0,0,0,0.05)',
              transition: 'box-shadow 0.2s',
            }}
            onMouseEnter={(e) => e.currentTarget.style.boxShadow = '0 4px 16px rgba(0,0,0,0.1)'}
            onMouseLeave={(e) => e.currentTarget.style.boxShadow = '0 2px 8px rgba(0,0,0,0.05)'}
          >
            <div style={{ marginBottom: '0.5em', fontSize: '1.2em' }}>
              <i
                className={`fa-duotone fa-solid ${icon}`}
                style={{ marginRight: '10px' }}
              ></i>
              {title}
              {badge && (
                <span
                  style={{
                    marginLeft: '8px',
                    fontSize: '0.75em',
                    backgroundColor: '#28a745',
                    color: '#fff',
                    padding: '2px 6px',
                    borderRadius: '6px',
                  }}
                >
                  {badge}
                </span>
              )}
            </div>
            <p style={{ margin: 0, color: '#555' }}>{desc}</p>
            <ul style={{ marginTop: '0.5em', color: '#555', paddingLeft: '20px' }}>
              {params.map(({ name, desc: paramDesc }) => (
                <li key={name}>
                  <strong>{name}:</strong> {paramDesc}
                </li>
              ))}
            </ul>
            <p style={{ marginTop: '0.5em', color: '#555', fontStyle: 'italic' }}>
              Use Cases: {example}
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
