---
title: Dec’25 🎄 – New API Endpoint
author: amalik@cuscal.com.au
hidden: false
published_at: '2025-12-23T00:26:49.087Z'
type: added
---
<p style={{ marginBottom: '2em', color: '#555' }}>
  Wrapping up the year with some exciting updates to the Basiq Platform! This month, we have released improvements to the Income Verification API. 
</p>

<div style={{ display: 'flex', flexWrap: 'wrap', gap: '30px' }}>
  {[
            {
              title: 'Verify Income Insights',
              url: 'https://api.basiq.io/reference/verifyincomeinsight',
              icon: 'fa-money-bill-wave',
              desc: 'Verifies if a user’s income falls within a specified range using a required `min` and optional `max` value. Returns a match result with confidence level based on financial data.',
              badge: 'New',
              example: 'Check if a user earns at least $5,000 for a loan application, or verify if income is sufficient to cover a proposed rent.'
            },
          ].map(({ title, url, icon, desc, badge, example }) => (
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
              <ul style={{ marginTop: '0.5em', color: '#555', paddingLeft: '20px' }}>
                <li><strong>Body Params:</strong> Income range to verify against user's financial data</li>
                <li><strong>income object:</strong>
                  <ul>
                    <li><strong>min</strong> (string, required) – Minimum income value as a numeric string</li>
                    <li><strong>max</strong> (string, optional) – Maximum income value as a numeric string</li>
                  </ul>
                </li>
              </ul>
              <p style={{ marginTop: '0.5em', color: '#555', fontStyle: 'italic' }}>
                Use Cases: {example}
              </p>
            </a>
          ))}
</div> <p>
Happy Holidays and a Happy New Year! 🎉
</p>