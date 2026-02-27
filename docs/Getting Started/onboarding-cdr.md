---
title: Onboarding & Accessing CDR
excerpt: >-
  Understand the complete onboarding journey, timeline, and requirements
  before   integrating with Basiq. Set expectations upfront to avoid
  integration   surprises.
deprecated: false
hidden: true
icon: fad fa-person-snowboarding
metadata:
  robots: index
---
# Your Journey to Going Live with Basiq

You've decided to integrate with Basiq. Great! Before your engineering team starts building, it helps to understand the path from "let’s do this" to "we're live with real data."

This page shows the typical journey, so you can plan effectively and make the most of your integration.

## What to Expect

Integrating with Basiq is more than connecting an API. It includes security, compliance, commercial considerations, and regulatory coordination.

Every piece of data flowing through Basiq is sensitive—transactions, account balances, identity data.

**Here's what we're going to walk through:**

* The realistic steps from today to go-live
* Who gets involved at each stage
* How to stay on track
* Typical timelines

## &#x20;The First Conversation (The Qualification Phase)

Your first call with our team sets the foundation.

**We're asking:**

* What's your usecase? 
* Whats your intent to use the data for? 
* Do you currently consume openbanking from another vendor? 
* What sort of business are you? (Startup, scaleup, mid, enterprise, bank etc).
* Other qualification question to ensure, Basiq is a good fit and more importantly you meet open banking requirements 

**Why this matters to you:**

This initial conversation is extremely important to have prior to building integration across our API to ensure the alignment from the begin. 

Accreditation enables live data access, but you can start building in Sandbox immediately while working toward accreditation. Discussing it upfront ensures your team is productive and focused on the right tasks.

<Callout icon="🚀" theme="info">
  **Planning early helps you move efficiently.** If accreditation is in progress, you can keep building in Sandbox and be ready to go live when the approval is complete.
</Callout>

If everything aligns—accreditation, budget, and timeline—you move forward.

**Who's involved:** You (founders/business + legal), Basiq (business development + compliance)

**How long:** 1-2 weeks of conversations and approvals (Integration timeline will strictly depends on the resource your business has or this piece of work). 

## Your Team Gets Started (The Build Planning Phase)

Now your engineers get involved. This is where the actual work begins.

**What your team is doing:**

* Getting Sandbox API credentials (instant)
* Reading API docs and integration guides
* Mapping how Basiq fits into your system
* Writing code for consent flows, API calls, and error handling
* Setting up secure token management

**Why this matters:**

Proper handling of error flows, logging, and monitoring ensures a smooth live launch.

<Callout icon="📘" theme="info">
  **Use Sandbox fully.** It’s where you learn the API, explore edge cases, and build with confidence. Teams who test carefully here go live more smoothly.
</Callout>

Your engineering team leads this phase, with Basiq support via email and Jira as needed.

**Who's involved:** Engineering team (primary), Basiq (support)

## The Security Audit (Happening Simultaneously)

While your team builds, Basiq’s security team collaborates with yours to review. Basiq must do a due diligence on all businesses wanting access to the platform/openbanking data. In many cases Basiq holds majority of the risk in this relationship due to us been the license holder. This is the reasoning for the due diligence. 

* Encryption of customer data
* Access control and auditing
* Procedures for data incidents
* Third-party tools handling data

**Why this matters:**

This ensures your integration is secure and aligned with best practices. If adjustments are needed, you can address them during the build.

<Callout icon="🔐" theme="info">
  **Security discussions run alongside building.** Having your lead engineer or CTO involved helps move things along smoothly.
</Callout>

By the end, we either:

* Give a green light to proceed
* Identify minor adjustments and work with you on fixes

**Who's involved:** Security/engineering team + Basiq security team

## Testing & Final Push, Commercials Agreed

Your build is complete. Time to validate it works as expected and move towards executing and agreed MSA. 

Please note commercials differ depending on a myriad of factors. Our pricing, product and services are aimed at mid to large size businesses.

**What happens:**

* End-to-end testing in Sandbox
* Load testing for higher traffic scenarios
* Error scenario testing (API downtime, timeouts)
* Monitoring and alerting configuration
* Review of go-live checklist

<Callout icon="👍" theme="okay">
  **Teams that prepared carefully in Sandbox see fewer surprises.** This phase confirms everything runs smoothly in production.
</Callout>

**Who's involved:** Your team (testing, monitoring setup) + Basiq (production credentials provisioning)

**How long:** 1-2 weeks of focused testing

## Weeks 4-6 (Parallel): The CDR Registry & ACCC Coordination

While testing, Basiq works with ACCC to register your organization for live CDR access. This is a regulatory step that runs alongside testing.

<Callout icon="✅" theme="info">
  **If accreditation is complete, this runs automatically.** You stay in the loop while approvals proceed.
</Callout>

**Who's involved:** Basiq + ACCC (your involvement is minimal)

**How long:** 2-4 weeks depending on processing

## Week 6-8: You're Live

All pieces are aligned. Accreditation confirmed. Security assessment complete. Integration tested. ACCC registration complete.

Your live API credentials are provisioned, and your data flows securely. Going live marks the start of monitoring and supporting your customers effectively.

## Timeline Reality Check by Company Size

<Tabs>
  <Tab title="Small Fintech (10-30 people)">
    **Real timeline: 4-6 weeks to go live**

    **Week 1-2:** Qualification call, accreditation check, commercial approval\
    **Week 2-4:** Build in Sandbox, security assessment conversations\
    **Week 4-6:** Final testing, credential provisioning\
    **Week 4-6 (parallel):** ACCC coordination

    **Why this timeline works:**

    * Smaller teams move quickly
    * Direct communication with security lead
    * Accreditation nearly complete or in progress
  </Tab>

  <Tab title="Mid-Market (50-200 people)">
    **Real timeline: 8-12 weeks to go live**

    **Week 1-2:** Qualification, accreditation verification, legal review\
    **Week 2-6:** Build in Sandbox, security/compliance assessment\
    **Week 6-10:** Testing, integration refinement, monitoring setup\
    **Week 4-10 (parallel):** ACCC coordination\
    **Week 10-12:** Final go-live prep and credential provisioning

    **Why this takes longer:**

    * Multiple approval layers
    * More complex integrations
    * Security assessment coordination
  </Tab>

  <Tab title="Enterprise (500+ people)">
    **Real timeline: 3-6 months to go live**

    **Week 1-3:** Qualification, accreditation confirmation, legal/compliance review\
    **Week 2-10:** Build Phase 1 + security assessment Phase 1\
    **Week 8-16:** Build Phase 2 + security assessment Phase 2 + vendor reviews\
    **Week 16-20:** Integration testing, monitoring, compliance final review\
    **Week 4-20 (parallel):** ACCC coordination\
    **Week 20-24:** Final go-live prep

    **Why this takes longer:**

    * Thorough enterprise security & compliance
    * Multiple system integrations
    * Vendor risk assessments
    * Internal approvals & change management
  </Tab>
</Tabs>

## What Actually Changes When You Go Live

**In Sandbox:** You test with simulated data safely.  
**In Production:** You handle real transactions, balances, and identity data with secure logging, monitoring, and error handling in place.

The process ensures reliability and confidence when going live.

## The Commercial Piece (The Part That Surprises People)

Basiq's pricing varies depending on:

* Data usage (transactions per month)
* Features you’re using
* Level of support
* Company size and stage
* Any custom work

<Callout icon="📘" theme="info">
  **Discuss pricing early.** This ensures you know what to expect and can plan your budget confidently.
</Callout>

## Before You Reach Out: What to Prepare

<Cards>
  <Card title="Accreditation Status" icon="✓">
    Are you ACCC-accredited or on the path? This is the first question to clarify.
  </Card>

  <Card title="Your Technical Lead" icon="👤">
    Identify who owns this project on your side—they should be empowered to make technical decisions.
  </Card>

  <Card title="Your Timeline" icon="📅">
    When do you need live access? Be realistic and plan accordingly.
  </Card>

  <Card title="Your Integration Scope" icon="🏗️">
    Are you integrating a single API or multiple systems?
  </Card>

  <Card title="Your Security Story" icon="🔐">
    What security practices are in place? Who is your security point of contact?
  </Card>
</Cards>

## FAQ: Questions From Other Teams Like You

<Accordion title="Can we start building today?" icon="fa-code">
  <p>
    <strong>Yes, absolutely.</strong> Sandbox access is instant. You can start building while accreditation and commercial discussions progress.
  </p>
</Accordion>

<Accordion title="What if we're not accredited yet?" icon="fa-question-circle">
  <p>
    <strong>You can build in Sandbox</strong> safely while working toward accreditation. Live access follows once approvals are complete.
  </p>
</Accordion>

<Accordion title="Can we skip the security assessment?" icon="fa-shield">
  <p>
    <strong>All teams complete a security review.</strong> It ensures your integration is secure and reliable for customers.
  </p>
</Accordion>

<Accordion title="Can we run the security assessment and build at the same time?" icon="fa-sync">
  <p>
    <strong>Yes, and it’s recommended.</strong> Running both in parallel keeps your project efficient and ensures a smooth go-live.
  </p>
</Accordion>

<Accordion title="What if the security assessment finds adjustments?" icon="fa-exclamation-triangle">
  <p>
    <strong>Adjustments are part of the process.</strong> Basiq works with your team to address them efficiently, leading to a stronger integration.
  </p>
</Accordion>

<Accordion title="How much is this going to cost?" icon="fa-dollar-sign">
  <p>
    <strong>It varies.</strong> Discussed early in Week 1-2, pricing is clear based on your setup and expected usage.
  </p>
</Accordion>

<Accordion title="What if we're switching from another provider?" icon="fa-exchange-alt">
  <p>
    <strong>Migration support is available.</strong> We help transition existing integrations smoothly and plan timelines accordingly.
  </p>
</Accordion>

## The Reality

This process is longer than a typical API integration, but it ensures:

* Your system is secure
* Everything is tested thoroughly
* Expectations are aligned
* Integration is built the right way

The result: a smooth go-live with confidence.

## Ready to Start?

If this timeline works for you and you're ready for an honest conversation about where you are, reach out with:

* Organization name & size
* ACCC accreditation status (or timeline)
* Primary technical contact
* Target go-live date
* Any migration context

**Contact:** [onboarding@basiq.io](mailto:onboarding@basiq.io)

We'll provide a realistic timeline, answer questions, and guide you through a smooth integration.

<div
  style={{
    border: "2px solid #1E1E1E",
    borderRadius: "8px",
    backgroundColor: "#1E1E1E",
    padding: "16px",
    margin: "16px 0",
    fontFamily: "Arial, sans-serif",
    color: "#ffffff",
  }}
>
  📢 For any questions, reach out to our support team.

  <div style={{ display: 'flex', alignItems: 'center' }}>
    <button
      onClick={() => Intercom('showNewMessage', 'issues on FAQs:')}
      style={{
        padding: '12px 30px',
        backgroundColor: '#1E1E1E',
        color: '#ffffff',
        border: '2px solid #ffffff',
        borderRadius: '50px',
        fontSize: '16px',
        fontWeight: '600',
        textTransform: 'uppercase',
        cursor: 'pointer',
        transition: 'background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease',
        outline: 'none',
        display: 'flex',
        justifyContent: 'center',
        height: '45px',
        position: 'relative',
        overflow: 'hidden',
        marginLeft: '10px',
        minWidth: '150px',
      }}
      onMouseEnter={(e) => {
        e.target.style.transform = 'scale(1.1)';
        e.target.style.backgroundColor = '#333333';
      }}
      onMouseLeave={(e) => {
        e.target.style.transform = 'scale(1)';
        e.target.style.backgroundColor = '#1E1E1E';
      }}
    >
      Support team
    </button>
  </div>
</div>
