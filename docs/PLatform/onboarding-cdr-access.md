---
title: Onboarding & CDR Access
excerpt: >-
  Complete guide to integrating with Basiq API and accessing Consumer Data Right
  (CDR) data
deprecated: false
hidden: true
metadata:
  robots: index
---
***

# Onboarding & CDR Access Checklist

Your complete guide to preparing for integration with Basiq and enabling Consumer Data Right (CDR) access. This checklist covers all four stages of the onboarding journey.

## Pre-Integration Requirements

<Callout type="info">
Before you start building, ensure your organization meets these foundational requirements. This typically takes 1-2 weeks to confirm.
</Callout>


### Stage 1: Prerequisites & Assessment

* [ ] **ACCC Data Recipient Accreditation** - Confirm your organization is accredited or in the accreditation process
  * [ ] **Legal & Compliance Review** - CDR compliance obligations reviewed by legal team
    * [ ] **Data Handling Infrastructure** - You have secure API infrastructure (HTTPS, encryption standards)
      * [ ] **Privacy Policy Updated** - Consumer data handling practices documented publicly
        * [ ] **Designated Contact** - Identify primary technical contact for security assessment
          * [ ] **Technical Documentation** - Current tech stack, architecture, and data flows documented
            <Callout type="warning">
            Without ACCC accreditation, you can only access Sandbox mode. Live data access requires full Data Recipient status.
            </Callout>

## Integration Phase Checklist

### Stage 2: Build ETA & Architecture Review

**Duration:** 2-4 weeks (Small Fintech) | 3-6 months (Enterprise)

* [ ] **API Keys Generated** - Sandbox keys created in Basiq Dashboard
  * [ ] **Development Environment Setup** - Local/staging environment configured
    * [ ] **Architecture Documented** - How you'll integrate Basiq API into your stack
      * [ ] **Data Flow Diagram** - Document how customer data flows through your system
        * [ ] **Error Handling Plan** - Define how you'll handle API failures and edge cases
          * [ ] **Team Onboarded** - Dev team reviewed Basiq API documentation



### Stage 3: Integration & Development

<br />

**Who:** You manage this | **Duration:** 2-4 weeks

* [ ] **Consent UI Implemented** - Customer consent flow built and tested
  * [ ] **API Integration Complete** - Core endpoints integrated (accounts, transactions, identity)
    * [ ] **Token Management** - Refresh token handling implemented securely
      * [ ] **Testing in Sandbox** - Full end-to-end flow tested with test data
        * [ ] **Error Handling Verified** - Rate limits, timeouts, and failures handled gracefully
          * [ ] **Logging & Monitoring** - API requests/responses logged for debugging



### Stage 4: CDR Security Assessment

<br />

**Who:** Basiq Security + Your Team | **Duration:** 1-2 weeks | **Best fit:** Dev/SecOps/CTO

<Callout type="warning">
This assessment is critical. The timing depends on your team's availability to answer detailed security and compliance questions. Have your technical and security personnel available.
</Callout>


<br />

* [ ] **Security Team Assigned** - Dev/SecOps person assigned to answer assessment questions
  * [ ] **Data Protection Review** - Your encryption and secure storage practices reviewed
    * [ ] **Access Control Documentation** - Who has access to customer data and why documented
      * [ ] **Incident Response Plan** - How you'll respond to data breaches documented
        * [ ] **Third-Party Vendors Assessed** - Any third-party tools handling data reviewed for compliance
          * [ ] **Audit Trail Capability** - Ability to log/audit all data access confirmed


            ***




## Pre-Go-Live Checklist

<br />

<br />

### Stage 5: ACCC & CDR Setup

<br />

**Who:** Basiq + ACCC | **Duration:** 2 weeks (pending accreditation)

* [ ] **ACCC Coordination** - Basiq works with ACCC to register your live access
  * [ ] **Accreditation Verified** - Your organization's Data Recipient status confirmed
    * [ ] **Live Credentials Generated** - Production API keys received
      * [ ] **Rate Limits Configured** - Your account tier and rate limits set appropriately



### Stage 6: Go-Live Preparation

<br />

Before you enable live access, complete this final checklist:

<Cards>
  <Card title="Infrastructure" icon="🔒">
    - [ ] Production environment hardened
    - [ ] SSL/TLS certificates valid
    - [ ] DDoS protection enabled
    - [ ] Database backups configured
  </Card>
  <Card title="Monitoring" icon="📊">
    - [ ] Error tracking (Sentry, DataDog, etc.) set up
    - [ ] API performance monitoring active
    - [ ] Alert thresholds configured
    - [ ] Logs shipping to central location
  </Card>
  <Card title="Security" icon="🛡️">
    - [ ] Secrets management (env vars) secured
    - [ ] API keys rotated
    - [ ] Rate limiting configured
    - [ ] Request validation implemented
  </Card>
  <Card title="Documentation" icon="📝">
    - [ ] Customer documentation ready
    - [ ] Support runbook prepared
    - [ ] Incident response plan shared with team
    - [ ] Training completed
  </Card>
</Cards>

## Timeline by Company Size

<Tabs>
  <Tab title="Small Fintech">
    **Total Timeline: 2-4 weeks**
    
    Prerequisites: 1 week
    Build ETA: 2 weeks
    Integration: 2-3 weeks
    Security Assessment: 1 week
    CDR Setup: 2 weeks (parallel)
    ────────────
    Total: ~4-5 weeks
    
    **Best for:** Companies with {'<'}20 employees, simple integration requirements
  </Tab>

  <Tab title="Mid-Market">
    **Total Timeline: 2-3 months**
    
    Prerequisites: 1-2 weeks
    Build ETA: 3-4 weeks
    Integration: 3-4 weeks
    Security Assessment: 1-2 weeks
    CDR Setup: 2-3 weeks (parallel)
    ────────────
    Total: 8-12 weeks
    
    **Best for:** Companies with 50-200 employees, moderate integration scope
  </Tab>

  <Tab title="Enterprise">
    **Total Timeline: 3-6 months**
    
    Prerequisites: 2-3 weeks
    Build ETA: 6-8 weeks
    Integration: 6-8 weeks
    Security Assessment: 2-3 weeks
    CDR Setup: 3-4 weeks (parallel)
    ────────────
    Total: 16-24 weeks
    
    **Best for:** Companies with 500+ employees, complex multi-system integration
  </Tab>
</Tabs>

## Key Contacts & Support

<Callout type="success">
**Having issues?** Here's who to reach out to at each stage:
</Callout>

| Stage | Question | Contact |
|-------|----------|---------|
| Prerequisites | ACCC accreditation questions | support@basiq.io |
| Build ETA | Integration approach | developers@basiq.io |
| Security Assessment | Compliance requirements | security-team@basiq.io |
| Go-Live | Production credentials | onboarding@basiq.io |

## Common Questions

<Callout type="info" title="Can we access Sandbox immediately?">
Yes! Sandbox access is instant. No accreditation required. Perfect for testing and development.
</Callout>

<Callout type="info" title="What if we're not yet ACCC accredited?">
You can still build and test in Sandbox. Live access requires full accreditation, which you can pursue in parallel with development.
</Callout>

<Callout type="info" title="Can the security assessment happen during integration?">
Yes, in fact we recommend it. You can start integration work while the security assessment is underway. They run in parallel.
</Callout>

<Callout type="info" title="What if we change solutions mid-process?">
No problem. Migration support is available as an optional add-on. Reach out to discuss your situation.
</Callout>

<br />
