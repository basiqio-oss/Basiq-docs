---
title: Oct '25 - Connector Updates, Dashboard UI, and Government Payment Tags
author: Ashman Malik
hidden: false
published_at: '2025-10-30T04:11:47.632Z'
type: improved
---
<h2 style={{ fontSize: '1.5em', marginBottom: '0.5em' }}>
  🚀 October Changelog
</h2>

<p style={{ marginBottom: '2em', color: '#555' }}>
  Stay up to date with the latest updates to the Basiq Platform. This month we’re excited to share connector removals, UI updates, and enhanced tagging for government payments.
</p>

<div style={{ display: 'flex', flexWrap: 'wrap', gap: '30px' }}>
  {[
    {
      title: 'Removal of Illawarra Credit Union Limited Connector',
      url: 'https://cuscal.atlassian.net/browse/DSRV-3063',
      icon: 'fa-university',
      desc: `Illawarra Credit Union Limited has been removed from the CDR register.`,
    },
    {
      title: 'Dashboard UI Update',
      url: 'https://dashboard.basiq.io/',
      icon: 'fa-palette',
      desc: `Visual update to the Dashboard UI to align with Cuscal branding.

No functional changes or API modifications.`,
    },
    {
      title: 'Enhanced governmentPayment Tags',
      url: 'https://api.basiq.io/reference/enrich/',
      icon: 'fa-tags',
      desc: `We’re excited to announce the addition of new government benefits categories to our CDR enrichment capabilities. This enhancement enables more granular and accurate classification of consumer transactions related to government support programs via the CDR.

This improvement to enrichment will provide a better understanding of government benefits for downstream use cases including more precise affordability assessment and any offering that requires a detailed understanding of government income. New categories introduced include: familyTaxBenefit, stillbornPymt, childCareSubsidy, parentalLeavePymt, parentingPymt, disabilitySupport, pensionerEducationSupplement, farmAllowance, disasterPymt. Improved coverage for familyAllowance, jobseekerPymt, education, and youthAllowance.`,
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
        <i className={`fa-solid ${icon}`} style={{ marginRight: '10px' }}></i>
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
      {desc.split('\n\n').map((paragraph, idx) => (
        <p key={idx} style={{ margin: '0 0 1em 0', color: '#555' }}>
          {paragraph}
        </p>
      ))}
    </a>
  ))}
</div>