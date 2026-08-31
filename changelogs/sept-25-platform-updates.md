---
title: Sept '25 - Platform Updates
author: amalik@cuscal.com.au
hidden: false
published_at: '2025-09-29T00:16:54.422Z'
type: added
---
<h2 style={{ fontSize: '1.5em', marginBottom: '0.5em' }}>
  🚀 September Changelog
</h2>

<p style={{ marginBottom: '2em', color: '#555' }}>
  Stay up to date with the latest additions to the Basiq Platform. This month we’re excited to bring you new APIs to supercharge insights and analytics for your apps.
</p>

<div style={{ display: 'flex', flexWrap: 'wrap', gap: '30px' }}>
  {[
                {
                  title: 'Insights API – Account Details',
                  url: 'https://api.basiq.io/reference/getaccountinsights#/',
                  icon: 'fa-lightbulb',
                  desc: 'Get detailed account insights via /users/{userId}/insights/account. Perfect for building richer account experiences.',
                },
                {
                  title: 'Account Balance Verification',
                  url: 'https://api.basiq.io/reference/getbalanceinsights#/',
                  icon: 'fa-scale-balanced',
                  desc: 'Query account balance insights with flexible filtering (min/max parameters) via /users/{userId}/insights/balance.',
                },
                {
                  title: 'Identity - Identity Insights',
                  url: 'https://api.basiq.io/reference/getidentityinsights/',
                  icon: 'fa-id-card',
                  desc: 'Identity Insights are released, please check out the docs for more details.',
                },
                {
                  title: 'Analytics API – Connection Analytics',
                  url: 'https://api.basiq.io/reference/getconnectionanalytics#/',
                  icon: 'fa-chart-line',
                  desc: 'Retrieve insights about user connections to build stronger analytics dashboards.',
                },
              ].map(({ title, url, icon, desc, badge }) => (
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
                  }}
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
                          backgroundColor: '#f0ad4e',
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
                </a>
              ))}
</div>