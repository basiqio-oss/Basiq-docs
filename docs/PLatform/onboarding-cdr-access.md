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
# Onboarding with the Basiq API & Accessing CDR

This guide provides a comprehensive overview of the onboarding process for integrating with Basiq and gaining access to live Consumer Data Right (CDR) data.

## Key Concepts

<Callout theme="default">
  **Basiq Enables Live Access** - You will be enabled for access to live data via web connectors. Open Banking data access will be enabled once you have completed the required steps and assessments.
</Callout>

<Callout theme="default">
  **CDR Security Assessment** - This is conducted jointly by Basiq and your team. The timing depends on having the correct person or people assisting with assessment questions. It requires understanding of your technical application environment. Your Dev/Sec Ops or CTO would be best suited for this.
</Callout>

<Callout theme="default">
  **CDR Set Up** - Basiq will work with the ACCC to begin establishing your access to CDR data. This process depends on the ACCC and its verification processes.
</Callout>

<Callout theme="default">
  **Migration** - The Basiq team is able to assist in migrating users from an existing solution. This is an optional add-on which will be outlined in your MSA.
</Callout>

## Onboarding Timeline Overview

The total onboarding timeline depends on your organization size and complexity:

### Small Fintech

* **Duration:** 2-4 weeks
* **Process:** Streamlined for smaller teams
* **Requirements:** Basic tech assessment, compliance readiness verification

### Large Enterprise

* **Duration:** 3-6 months
* **Process:** Extended due diligence, multiple stakeholder coordination
* **Requirements:** Comprehensive security review, compliance assessment, integration planning

## The Four-Stage Onboarding Process

```
┌─────────────────────────────────────────────────────────────┐
│                    ONBOARDING JOURNEY                       │
└─────────────────────────────────────────────────────────────┘

Stage 1: Build ETA
  ↓
Stage 2: Integrate with the Basiq API
  ↓
Stage 3: Develop & Test
  ↓
Stage 4: Support & Go Live
  ↓
Parallel: CDR Security Assessment → CDR Set Up → Enable Institutions
  ↓
Final: Go Live & Optional Migration
```

### Stage 1: Build ETA

**Owner:** Customer  
**Duration:** Varies by company size  
**Key Activities:**

* Architecture review and assessment of your business
* Review of current tech stack and development approach
* Understanding of integration requirements and dependencies
* Timeline estimation for implementation

**What Happens Next:** Once ETA is established, you move to integration planning.

***

### Stage 2: Integrate with the Basiq API

**Owner:** Customer (Basiq provides support)  
**Duration:** 2-4 weeks typical  
**Key Activities:**

* Build API application using Basiq endpoints
* Set up authentication and authorization
* Configure data connectors for required financial institutions
* Implement consent management UI

**Requirements:**

* Development team availability
* API key and sandbox credentials
* Familiarity with REST APIs and authentication patterns

**Next Steps:** Begin development and testing phase.

***

### Stage 3: Develop & Test

**Owner:** Customer  
**Duration:** 2-4 weeks typical  
**Key Activities:**

* Configure your application and consent UI
* Test integrations in sandbox environment
* Validate data flows and error handling
* Prepare for compliance review

**Basiq Support:** Documentation, guides, and technical assistance available for questions.

**Next Steps:** Ready for security assessment and production deployment.

***

### Stage 4: Support & Production Access

**Owner:** Basiq + Customer  
**Duration:** Ongoing  
**Key Activities:**

* Technical documentation and guidance
* Troubleshooting and optimization
* Monitoring and support

**Requirements:** Completed security assessment and compliance verification.

***

## Parallel Process: CDR Security & Compliance

While you're building and testing, the CDR compliance process runs in parallel:

### CDR Security Assessment

**Owner:** Basiq + Your Team  
**Duration:** 1-2 weeks  
**Who Should Be Involved:** Dev/SecOps, CTO, or equivalent technical leadership

**Assessment Covers:**

* Data security practices and encryption standards
* Data handling and storage procedures
* Access controls and authentication mechanisms
* Compliance with CDR requirements
* API security and rate limiting
* Logging and audit trails
* Incident response procedures

**Key Point:** This assessment requires someone with deep technical knowledge of your infrastructure and security practices.

***

### CDR Set Up

**Owner:** Basiq + ACCC  
**Duration:** 2 weeks typical  
**Status Trigger:** Added to CDR Registry (approximately 1 week from assessment completion)

**What Happens:**

* Basiq works with the ACCC to register your Data Recipient status
* CDR data access is provisioned
* Your app is added to the ACCC's central registry
* Live CDR data becomes accessible

***

### Enable Institutions for Open Banking

**Owner:** Customer  
**Duration:** Instant to variable  
**Key Activities:**

* Via dashboard: Enable individual financial institutions
* Configure which data types to access per institution
* Set up webhook handlers for data updates
* Test live connections

***

## Complete Journey: From Application to Go Live

```
Start: Building your API Application
  ├─ Build ETA (Customer)
  ├─ Integrate with Basiq API (Customer) ───────────┐
  ├─ Develop & Test (Customer) ──────────────────┐  │
  │                                              │  │
  ├─ CDR Security Assessment (Basiq + Customer)  │  │
  │  └─ Added to CDR Registry (1 week)           │  │
  │                                              │  │
  ├─ CDR Set Up (Basiq + ACCC)                   │  │
  │  └─ Timing: 2 weeks                          │  │
  │                                              │  │
  ├─ Support Phase (Basiq) ──────────────────────┘  │
  │                                                 │
  └─ Go Live ◄──────────────────────────────────────┘
     (Instant when all steps complete)
  
  Optional: Migration from existing solution (TBA)
```

***

## Access Progression

### Sandbox Access

* **Available:** Immediately upon registration
* **Requirements:** API key only
* **Use Case:** Testing and development
* **Data:** Test data from sandbox environment

### Live Access (Web Connectors)

* **Available:** After security assessment completion
* **Requirements:** Compliant infrastructure
* **Use Case:** Production data from live financial institutions
* **Data:** Real account and transaction data

### CDR Access

* **Available:** After full onboarding completion
* **Requirements:** ACCC accreditation and security approval
* **Use Case:** Open Banking data access
* **Data:** Authorized by end-user through consent flow

***

## Typical Timeline Summary

| Phase               | Small Fintech | Large Enterprise |
| ------------------- | ------------- | ---------------- |
| Build ETA           | 2-4 weeks     | 3-6 months       |
| Integration         | 2-4 weeks     | 1-3 months       |
| Testing             | 1-2 weeks     | 2-4 weeks        |
| Security Assessment | 1 week        | 2-3 weeks        |
| CDR Registry Setup  | 1 week        | 1 week           |
| CDR Set Up          | 2 weeks       | 2 weeks          |
| **Total**           | **2-4 weeks** | **3-6 months**   |

***

## Icon Legend

Throughout this documentation and the onboarding dashboard, you'll see these indicators:

* **🔧 Basiq manages for you** - Basiq handles this step
* **👤 Customer input required** - Your team needs to take action
* **⏱️ Approximate timings** - These are estimates; actual times may vary

***

## What Comes After Go Live

Once you're live, you have two optional paths:

### Ongoing Support

* Technical support and documentation
* API monitoring and optimization
* Update notifications for new features
* Performance analytics

### Migration (Optional)

* Migrate existing users from legacy solutions
* Basiq team assistance available
* Timeline: TBA (included in MSA if selected)

***

## Getting Help

During your onboarding journey:

* **Documentation:** Check our comprehensive guides and API reference
* **Support:** Reach out to our support team with technical questions
* **Security Questions:** Contact your assigned security assessment lead
* **General Inquiries:** Connect with your account manager

## Next Steps

1. **Start Here:** Review the [Integration Overview](link-to-integration-overview)
2. **Quickstart:** Get up and running with our [Quickstart Guide](link-to-quickstart)
3. **Technical Docs:** Dive into the [API Reference](link-to-api-reference)
4. **Security:** Understand requirements in our [CDR Compliance Guide](link-to-compliance)
