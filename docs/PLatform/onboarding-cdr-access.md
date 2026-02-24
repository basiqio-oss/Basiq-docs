---
title: Onboarding & Accessing CDR
excerpt: >-
  Understand the complete onboarding journey, timeline, and requirements before
  integrating with Basiq. Set expectations upfront to avoid integration
  surprises.
deprecated: false
hidden: true
metadata:
  robots: index
---
# Onboarding with the Basiq API & Accessing CDR

Before you start integrating with Basiq, it's critical to understand the complete onboarding journey. This isn't just an API integration—it's a structured process that includes security assessments, compliance verification, and due diligence.

**This page exists to set expectations upfront.** Many companies discover mid-integration that there are requirements they weren't aware of. We want you to have full clarity before you invest engineering time.

***

## The Reality: What You Need to Know

<Callout theme="default">
  **You cannot move directly from "building" to "live"** without completing several prerequisite steps. The timeline from starting integration to accessing live CDR data typically ranges from 2-6 months depending on your company size and complexity.

  Without this clarity upfront, teams often:

  * Begin full integration without completing prerequisites
  * Discover mid-build that they need ACCC accreditation
  * Reach go-live only to find commercial terms need discussion
  * Experience frustration when timelines don't align with expectations

  This page eliminates that confusion.
</Callout>

***

## The Four Onboarding Stages

### Stage 1: Prerequisites & Due Diligence (Weeks 1-2)

Before any integration begins, you must confirm you meet baseline requirements. This is where many organizations realize they need additional setup or can't proceed yet.

**What we assess:**

* [ ] ACCC Data Recipient Accreditation status (or pathway to accreditation)
* [ ] Compliance infrastructure (data handling, privacy, security)
* [ ] Technical capability (API integration experience, secure infrastructure)
* [ ] Commercial alignment (pricing tier, feature access, SLA requirements)

**Who's involved:** You (business & legal), Basiq (business development & compliance)

**Why this matters:** This step prevents wasted engineering time on both sides. If accreditation isn't complete, you can still build in Sandbox, but live access won't be possible until it's done.

<Callout theme="default">
  **Not accredited yet?** No problem. You can begin sandbox integration in parallel while pursuing accreditation. However, we need to discuss this openly upfront to align timelines.
</Callout>

***

### Stage 2: Architecture & Build Planning (Weeks 2-4 for fintech | Weeks 2-8 for enterprise)

Now that we've confirmed you're ready to proceed, we move to the technical build phase.

**What happens:**

* API credentials generated for Sandbox
* Your team reviews Basiq API documentation
* Integration architecture documented (how Basiq fits into your systems)
* Data flow diagrams created
* Development begins in non-production environments

**Who's involved:** Your engineering team (primarily)

**Your responsibility:**

* Design how consent flows through your application
* Integrate core Basiq endpoints (accounts, transactions, identity, etc.)
* Implement secure token management
* Build error handling for API failures

**Basiq support:** Docs, API guides, developer support via email/Slack

<Callout theme="default">
  **Sandbox is production-grade.** The only difference is you're working with test data. Use this phase to build properly—error handling, logging, monitoring, rate limit handling.
</Callout>

***

### Stage 3: CDR Security Assessment (1-2 weeks, concurrent with Stage 2)

This is the critical gating item that often surprises teams. We conduct a detailed security and compliance assessment with your technical team.

**What we review:**

* Data encryption at rest and in transit
* Access control—who has access to customer data and why
* Your incident response & breach notification procedures
* Third-party vendor risk (any tools touching customer data)
* Audit trail capabilities (can you log who accessed what data when?)

**Who's involved:** Basiq security team + your Dev/SecOps/CTO

**Why 1-2 weeks?** The timing depends on your team's availability. We ask detailed questions; you need the right people to answer them thoroughly.

**Important:** This assessment isn't optional—it's mandatory for live access. It's also not a pass/fail; if gaps are found, we work with you to address them.

<Callout theme="default">
  **This is where timelines often slip.** If your security person is unavailable or if critical gaps are discovered, this phase can extend. Plan accordingly.
</Callout>

***

### Stage 4: Integration Testing & Go-Live (Weeks 3-6 into the process)

Once architecture is solid and security assessment is progressing, you move to serious testing.

**What happens:**

* Full end-to-end testing in Sandbox
* Load testing (how does your system handle 1000+ concurrent users?)
* Error scenarios tested (network timeouts, rate limits, API downtime)
* Monitoring & alerting configured in production
* Go-live checklist completed

**Common blockers at this stage:**

* Logging/monitoring not configured (you can't debug without logs)
* Rate limiting not handled (your app crashes when API rate limits are hit)
* No retry logic (transient failures aren't retried)
* Security gaps discovered during assessment (requires rework)

***

## Timeline by Company Size

The journey length depends heavily on your organization's complexity and accreditation status.

<Tabs>
  <Tab title="Small Fintech (10-30 people)">
    **Typical timeline: 2-4 weeks to live CDR access**

    **Phase breakdown:**

    * Prerequisites & due diligence: 1 week
    * Build ETA & architecture: 1-2 weeks
    * Integration & development: 2 weeks
    * CDR security assessment: 1 week (concurrent)
    * CDR setup with ACCC: 2 weeks (concurrent)

    **Key assumption:** You have ACCC accreditation or are on the path to it.

    **Risk factors:**

    * Security assessment delayed if key person unavailable
    * ACCC approval slower than expected
  </Tab>

  <Tab title="Mid-Market (50-200 people)">
    **Typical timeline: 2-3 months to live CDR access**

    **Phase breakdown:**

    * Prerequisites & due diligence: 1-2 weeks
    * Build ETA & architecture: 3-4 weeks
    * Integration & development: 3-4 weeks
    * CDR security assessment: 1-2 weeks (concurrent)
    * CDR setup with ACCC: 2-3 weeks (concurrent)

    **Key assumption:** Moderate integration complexity, security assessment requires cross-functional coordination.

    **Risk factors:**

    * Accreditation process slower than expected
    * Security gaps discovered during assessment requiring rework
    * Integration complexity higher than anticipated
  </Tab>

  <Tab title="Enterprise (500+ people)">
    **Typical timeline: 3-6 months to live CDR access**

    **Phase breakdown:**

    * Prerequisites & due diligence: 2-3 weeks
    * Build ETA & architecture: 6-8 weeks
    * Integration & development: 6-8 weeks
    * CDR security assessment: 2-3 weeks (concurrent)
    * CDR setup with ACCC: 3-4 weeks (concurrent)
    * Additional: Vendor risk assessments, policy updates, training

    **Key assumption:** High integration complexity, multiple systems, extensive compliance requirements.

    **Risk factors:**

    * Internal approval processes
    * Accreditation still in progress
    * Major security gaps requiring significant rework
    * Multiple rounds of assessment needed
  </Tab>
</Tabs>

***

## What Happens at Each Stage: Ownership & Responsibility

This table clarifies who does what to prevent confusion:

| Stage                   | Activity                        | Basiq Owns                | You Own                        | Timeline  |
| ----------------------- | ------------------------------- | ------------------------- | ------------------------------ | --------- |
| **Prerequisites**       | ACCC accreditation verification | Compliance review         | Obtaining accreditation        | 1-3 weeks |
| **Prerequisites**       | Commercial terms discussion     | Proposal & pricing        | Approval & sign-off            | 1-2 weeks |
| **Build ETA**           | API credentials generation      | Provisioning              | Integration setup              | 1 day     |
| **Build ETA**           | Architecture review             | Guidance & best practices | Design & implementation        | 1-2 weeks |
| **Integration**         | API documentation & support     | Support & updates         | Building & testing             | 2-4 weeks |
| **Integration**         | Sandbox support                 | Troubleshooting           | Integration work               | Ongoing   |
| **Security Assessment** | Assessment process              | Conducting assessment     | Answering questions thoroughly | 1-2 weeks |
| **Security Assessment** | Gap remediation                 | Advisory                  | Implementation                 | Variable  |
| **CDR Setup**           | ACCC registration               | Coordination with ACCC    | Providing accreditation proof  | 2-4 weeks |
| **Go-Live**             | Production credentials          | Provisioning              | Configuration & testing        | 1 day     |

***

## The Commercial Piece

This is often the surprise. API access isn't one-size-fits-all.

**Pricing & terms depend on:**

* Data volume (transactions per month)
* Feature set (which Basiq features you're using)
* Support level (email vs. priority support)
* Company size & stage
* Custom requirements

<Callout theme="default">
  **Don't assume pricing from the website applies to you.** Every implementation is unique. We discuss commercials during Stage 1 (Prerequisites) so there are no surprises later.
</Callout>

***

## How to Prepare Right Now

If you're considering Basiq, here's what you should do before reaching out:

<Cards>
  <Card title="1. Verify ACCC Status" icon="✓">
    Confirm whether your organization is ACCC-accredited or what the path to accreditation looks like. This is the foundational question.
  </Card>

  <Card title="2. Identify Your Technical Contact" icon="👤">
    Who's the primary engineer who'll own the Basiq integration? They should understand your data architecture.
  </Card>

  <Card title="3. Map Your Tech Stack" icon="🏗️">
    How will Basiq fit into your existing systems? What integrations are needed downstream?
  </Card>

  <Card title="4. Plan Your Timeline" icon="📅">
    When do you *actually* need live access? Be realistic. Most teams underestimate by 4-8 weeks.
  </Card>

  <Card title="5. Security Review" icon="🔐">
    Have your security/compliance person review the CDR requirements. They'll be involved anyway.
  </Card>
</Cards>

***

## FAQ: The Questions We Hear Most

<Callout theme="default">
  No. It's mandatory for any organization accessing live CDR data. It exists to protect your customers' data and your business.
</Callout>

<Callout theme="default">
  Yes. Sandbox access is instant. You don't need ACCC accreditation to test—use this time to build properly and prepare for the assessments ahead.
</Callout>

<Callout theme="default">
  You can still build in Sandbox. But live access won't be possible until accreditation is complete. Discuss this with us upfront so we can align on realistic timelines.
</Callout>

<Callout theme="default">
  Yes, and we recommend it. Start development in parallel with the assessment. That said, if the assessment reveals gaps, rework may delay your timeline.
</Callout>

<Callout theme="default">
  It's not pass/fail—it's a discovery process. If gaps are identified, we work with you to address them. Most gaps are fixable; it just takes additional work and time.
</Callout>

<Callout theme="default">
  Yes. Pricing varies based on volume, features, and complexity. We discuss this during Stage 1 so you're not surprised later.
</Callout>

<Callout theme="default">
  Migration support is available. We can help transition your existing integrations to Basiq. Discuss this during the commercial conversation.
</Callout>

***

## The Bottom Line

Integrating with Basiq isn't a simple API integration—it's a structured onboarding process with security, compliance, and commercial components. **This is by design.** It protects your customers' data and ensures a solid foundation for your business.

**We share this to set expectations upfront.** If you're ready to have this conversation with full clarity on what's ahead, let's talk. We'd rather have realistic timelines and aligned expectations than surprise you mid-project.

***

## Ready to Get Started?

Contact us with the following information and we'll schedule an initial conversation:

* Organization name & size
* Your ACCC accreditation status
* Primary technical contact
* Approximate timeline for needing live access
* Any migration context (if moving from another provider)

**Email:** [onboarding@basiq.io](mailto:onboarding@basiq.io)

We'll set up a call to discuss your situation specifically and give you a realistic timeline based on your circumstances.
