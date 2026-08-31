---
title: July '25 - API & Dashboard Updates
author: Ashman Malik
hidden: false
published_at: '2025-07-24T01:21:34.548Z'
type: improved
---
<h2 style={{ fontSize: '1.5em', marginBottom: '0.5em' }}>
  🚀 What's New in the Basiq Platform
</h2>

<p style={{ marginBottom: '2em', color: '#555' }}>
  Discover the latest enhancements across our APIs and tools. Build smarter with new insights, search features, and updated app experiences.
</p>

<div style={{ display: 'flex', flexWrap: 'wrap', gap: '30px' }}>
  {[
        {
          title: 'Analytics API',
          url: 'https://api.basiq.io/reference/getuseranalytics',
          icon: 'fa-chart-line',
          badge: 'Beta',
          desc: 'Access categorised insights and financial behavior patterns',
        },
        {
          title: 'Merchant Search & Retrieve',
          url: 'https://api.basiq.io/reference/merchantsearch',
          icon: 'fa-store',
          desc: 'Enrich your transactions by searching and retrieving merchant info',
        },
        {
          title: 'PFM App Update',
          url: 'https://api.basiq.io/docs/demo-pfm',
          icon: 'fa-mobile-screen',
          desc: 'New PFM demo app with budgeting, transactions and affordability',
        },
        {
          title: 'Consent Status Filters',
          url: 'https://api.basiq.io/reference/getconsents',
          icon: 'fa-filter-circle-xmark',
          desc: 'Retrieve consents using status filters: active, expired, revoked',
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
            <i className={`fa-duotone fa-solid ${icon}`} style={{ marginRight: '10px' }}></i>
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