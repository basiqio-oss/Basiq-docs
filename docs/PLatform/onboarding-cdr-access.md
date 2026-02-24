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
# Your Journey to Going Live with Basiq

You've decided to integrate with Basiq. Great. But before you task your engineering team with building, you need to know something critical:**Getting from "let's do this" to "we're live with real data" isn't a straight line.**

Most companies don't realise this until they're 3 weeks into integration. This page exists to show you the real journey so you can plan accordingly.

***

## The Thing Nobody Tells You

You're about to discover that integrating with Basiq isn't just about connecting an API. It's about security assessments, compliance verification, commercial discussions, and regulatory coordination. It sounds heavy because it is. But there's a reason.

Every piece of data flowing through Basiq is someone's financial information. Transactions, account balances, identity data. That's not light stuff. The process exists to ensure it's handled properly.

**Here's what we're going to walk through:**

The realistic steps from today to go-live, who gets involved at each stage, where surprises typically happen, and how long this actually takes.

***

## Week 1-2: The First Conversation (The Qualification Phase)

Your first call with our team isn't about APIs. It's about reality-checking.

**We're asking:**

* Are you ACCC-accredited, or on the path to accreditation? (This is the biggest one. If the answer is "we don't know," that's where the conversation starts.)
* What does your compliance infrastructure look like?
* What's your timeline actually looking like?
* What are we charging you, and does that fit your budget?

**Why this matters to you:**

If you don't have ACCC accreditation, live data access isn't possible. Period. But here's the thing—you can still build in Sandbox while pursuing accreditation. We need to discuss this openly so you don't waste 3 months of engineering time on something you can't go live with.

<Callout theme="default">
  **This is where frustrated founders often say later: "I wish I'd known this before we started."** We're telling you now. If you're not accredited, that's the first item on your to-do list. We can help, but it needs to happen before live access is possible.
</Callout>

If everything checks out—accreditation is on track, budget aligns, timeline is realistic—you move forward.

**Who's involved:** You (founders/business + legal), Basiq (business development + compliance)

**How long:** 1-2 weeks of conversations and approvals

***

## Week 2-4: Your Team Gets Started (The Build Planning Phase)

Now your engineers get involved. This is where the actual work begins.

**What your team is doing:**

* Getting Sandbox API credentials (instant)
* Reading our API docs and integrating documentation
* Drawing diagrams of how Basiq fits into your system
* Writing the code that'll handle consent flows, API calls, error handling
* Setting up secure token management (you're handling customer data now)

**Why this takes longer than you think:**

Most teams estimate this at 1 week. It usually takes 2-4 weeks for smaller teams, 6-8+ weeks for larger organizations. Why? Because you're doing it right. You're building error handling (what happens when the API is down?), logging (how will you debug issues?), monitoring (how will you know if something breaks?).

<Callout theme="default">
  **Use Sandbox aggressively here.** This isn't a "quick test" environment. It's where you learn the API, find edge cases, and build properly. Teams that rush through Sandbox always regret it in production.
</Callout>

Your engineering team is mostly on their own here, but you've got Basiq support via email and Slack if things get stuck.

**Who's involved:** Your engineering team (primary), Basiq (support role)

**How long:** 2-4 weeks (fintech) to 6-8+ weeks (enterprise)

***

## Week 2-3: The Security Audit (Happening Simultaneously)

While your team is building, something else is happening that often surprises people.

**The Basiq security team is asking your security/engineering leadership detailed questions:**

* How do you encrypt customer data?
* Who has access to it and why?
* What's your process if there's a data breach?
* How do you audit who's touched customer data?
* Any third-party tools processing this data? We need to review those.

**Why this takes time:**

This isn't a checkbox exercise. It's a real conversation with your technical and security team. If your security person is in-between roles, or if you don't have one, this phase extends. If gaps are found (and often they are), you need to fix them.

<Callout theme="default">
  **This is where most projects slip.** Not because it's impossible to fix, but because it requires the right people to be available and engaged. Your CTO or lead engineer needs to be in these conversations.
</Callout>

By the end of this phase, we've either:

* Given you a green light to proceed
* Identified gaps and worked with you on fixes (which might add 2-4 weeks)

**Who's involved:** Your security/engineering team + Basiq security team

**How long:** 1-2 weeks (if your team is responsive) to 4+ weeks (if gaps need fixing)

***

## Week 4-6: Testing & Final Push (The Integration Testing Phase)

Your build is complete. Time to make sure it actually works.

**What happens:**

* End-to-end testing in Sandbox (real scenarios, not just happy paths)
* Load testing (your system shouldn't crash at 1000 users)
* Error scenario testing (what happens when Basiq is down? When API requests time out?)
* Monitoring & alerting configured (because you can't manage what you can't see)
* Go-live checklist reviewed (do you have all the pieces?)

**Common breakdown points:**

* "We didn't build retry logic" → Your app crashes when the API hiccups
* "We're not logging API calls" → When something breaks, you have no idea what happened
* "We didn't test rate limits" → You hit API limits in production and weren't prepared
* "Security assessment revealed gaps" → You're now fixing things while trying to go live

<Callout theme="default">
  **This is where good preparation in Week 2-4 pays off.** Teams that built properly in Sandbox rarely hit surprises here.
</Callout>

**Who's involved:** Your team (testing, monitoring setup) + Basiq (production credentials provisioning)

**How long:** 1-2 weeks of focused testing

***

## Weeks 4-6 (Parallel): The CDR Registry & ACCC Coordination

While you're testing, something else is happening behind the scenes.

Basiq is working with ACCC to register your organization for live CDR access. This is regulatory coordination, not technical work. It just takes time.

<Callout theme="default">
  **This is automatic if accreditation is complete.** If it's not, this phase waits. That's why accreditation status matters so much upfront.
</Callout>

**Who's involved:** Basiq + ACCC (you don't need to be hands-on here, but you're in the loop)

**How long:** 2-4 weeks depending on ACCC processing

***

## Week 6-8: You're Live

All pieces aligned. Accreditation verified. Security assessment green-lit. Integration tested. ACCC registration complete.

Your live API credentials are provisioned. Your data is flowing. You're live.

**But here's the thing:** Going live isn't the end. It's the beginning of monitoring, supporting customers through it, and handling the inevitable questions that come up.

***

## Timeline Reality Check by Company Size

Here's what this actually looks like in practice:

<Tabs>
  <Tab title="Small Fintech (10-30 people)">
    **Real timeline: 4-6 weeks to go live**

    **Week 1-2:** Qualification call, accreditation check, commercial approval
    **Week 2-4:** Build in Sandbox, security assessment conversations
    **Week 4-6:** Final testing, credential provisioning
    **Week 4-6 (parallel):** ACCC coordination

    **Why this timeline works:**

    * Smaller teams move faster, fewer approval layers
    * Direct communication with security person
    * Assumes accreditation is already complete or very close

    **Where it usually slips:**

    * Accreditation not actually complete (adds 4-8 weeks minimum)
    * Security person unavailable during assessment
    * ACCC processing slower than expected
  </Tab>

  <Tab title="Mid-Market (50-200 people)">
    **Real timeline: 8-12 weeks to go live**

    **Week 1-2:** Qualification, accreditation verification, legal review
    **Week 2-6:** Build in Sandbox, security/compliance assessment
    **Week 6-10:** Testing, integration refinement, monitoring setup
    **Week 4-10 (parallel):** ACCC coordination
    **Week 10-12:** Final go-live prep and credential provisioning

    **Why this takes longer:**

    * Multiple approval layers (legal, security, engineering leadership)
    * More complex integrations (legacy systems, multiple data sources)
    * Security assessment takes longer (more people to coordinate)

    **Where it usually slips:**

    * Accreditation takes longer than expected
    * Security gaps requiring rework
    * Integration complexity underestimated
  </Tab>

  <Tab title="Enterprise (500+ people)">
    **Real timeline: 3-6 months to go live**

    **Week 1-3:** Qualification, accreditation confirmation, extensive legal/compliance review
    **Week 2-10:** Build Phase 1 + security assessment Phase 1
    **Week 8-16:** Build Phase 2 + security assessment Phase 2 + vendor reviews
    **Week 16-20:** Integration testing, monitoring, compliance final review
    **Week 4-20 (parallel):** ACCC coordination and regulatory verification
    **Week 20-24:** Final go-live prep

    **Why this takes significantly longer:**

    * Enterprise security & compliance are thorough (as they should be)
    * Multiple systems integration (not just one API)
    * Vendor risk assessments (any third-party tools touching data)
    * Internal change management & approvals

    **Where it slips:**

    * Accreditation still being processed
    * Major security gaps requiring significant rework
    * Multiple rounds of assessment needed
    * Internal stakeholder alignment
  </Tab>
</Tabs>

***

## What Actually Changes When You Go Live

You might be thinking: "This all seems like a lot for an API integration."

Here's why it matters:

**In Sandbox:** You're testing with fake data. No one's real financial information is at stake. If something breaks, it's a learning moment.

**In Production:** You're handling real transactions, real account balances, real identity data. If something breaks, someone can't see their money. If data isn't encrypted properly, someone's financial life is exposed. If you don't have proper logging, you can't prove what happened.

The process exists because the stakes are real.

***

## The Commercial Piece (The Part That Surprises People)

Here's something to know: Basiq's pricing isn't a fixed website number.

It depends on:

* How much data you're pulling (transactions per month)
* Which features you're using
* How much support you need
* Your company size and stage
* Any custom work

<Callout theme="default">
  **Don't assume you know the price.** We discuss this during Week 1-2 so there are no surprises when you're ready to go live.
</Callout>

***

## The Honest Reality

**What happens with teams who skip these steps:**

* They integrate without confirming accreditation status, then discover mid-build they can't go live
* They skip the security assessment, then face it later when everything needs rework
* They don't discuss commercial terms until they're ready to go live (now there's negotiation pressure)
* They don't build proper error handling or monitoring, so production is a nightmare
* They end up frustrated because expectations weren't set upfront

**What happens with teams who do it right:**

* They integrate with full clarity on accreditation, timeline, and cost
* Security assessment happens alongside build, not as a surprise
* Build is solid because they tested thoroughly in Sandbox
* Go-live is boring (in the best way) because everything's been planned
* No surprises. No LinkedIn complaints. No rushed rework.

***

## Before You Reach Out: What to Prepare

If you're seriously considering Basiq, here's what you should get straight first:

<Cards>
  <Card title="Accreditation Status" icon="✓">
    Are you ACCC-accredited? On the path? Don't know? Find out. This is the first question.
  </Card>

  <Card title="Your Technical Lead" icon="👤">
    Who owns this project on your side? They need to be real, not delegated to a junior engineer.
  </Card>

  <Card title="Your Timeline" icon="📅">
    When do you actually need live access? Be realistic. Most teams add 4-8 weeks to their first estimate.
  </Card>

  <Card title="Your Integration Scope" icon="🏗️">
    Is this one API integration or are you integrating across multiple systems?
  </Card>

  <Card title="Your Security Story" icon="🔐">
    Do you have security practices in place? Who's your security person?
  </Card>
</Cards>

***

## FAQ: Questions From Other Teams Like You

<Callout theme="default">
  Yes, absolutely. Sandbox access is instant. Start building while we sort out accreditation and commercial terms. Just don't assume you'll be live quickly if accreditation isn't complete.
</Callout>

<Callout theme="default">
  You can build in Sandbox (really good idea to start here). But live access won't happen until accreditation is complete. We need to be honest about that upfront.
</Callout>

<Callout theme="default">
  No. It's not negotiable. It's not arbitrary. It protects your customers' data and your business. Every company goes through it.
</Callout>

<Callout theme="default">
  Yes, and you should. Start both immediately. If the assessment reveals gaps, you'll fix them while you're integrating.
</Callout>

<Callout theme="default">
  It's not pass/fail. It's discovery. If problems are found, we work with you to fix them. Most teams do, and they end up with a more secure integration.
</Callout>

<Callout theme="default">
  It varies. We discuss it during Week 1-2 based on your use case. No surprises later.
</Callout>

<Callout theme="default">
  Migration support is available. We can help transition existing integrations. Discuss this upfront so we can factor it into timeline and pricing.
</Callout>

***

## The Reality

This process is longer than a typical API integration. It's also better.

By the time you go live, you'll have:

* Verified your system is secure
* Tested everything thoroughly
* Aligned expectations with your team
* Built it the right way, not the fast way

Will it take longer than you initially thought? Probably. Is it worth it? Absolutely.

***

## Ready to Start?

If this timeline works for you and you're ready to have an honest conversation about where you actually are (vs. where you hope to be), let's talk.

Get in touch with the following:

* Your organization name & size
* Your ACCC accreditation status (or timeline to it)
* Your primary technical contact
* When you actually need live access
* Any migration context (if moving from somewhere else)

**Contact:** [onboarding@basiq.io](mailto:onboarding@basiq.io)

We'll schedule a call, give you a realistic timeline based on your situation, and answer the specific questions you have.

No surprises. No wasted engineering time. Just honest conversations about what's actually involved.
