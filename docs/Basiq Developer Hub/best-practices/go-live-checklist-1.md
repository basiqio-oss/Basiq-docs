---
title: Go live checklist
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
<Image width="80%" src="https://files.readme.io/cd58628-dev_guide_hero.svg" />

Once you’ve integrated with the Basiq API using our sandbox environment, and you’re ready to be enabled for live data, there are a few things to tick off to ensure it all runs smoothly. Here is a checklist covering everything you need to make your application production-ready. 

All of the **best practice** implementation details for the following requirements can be found [here](#basiq-best-practices). 

# Housekeeping

with the Basiq [dashboard](https://dashboard.basiq.io/)\
 \
✅      Invite **team members** to your account

✅      Setup Basiq **applications** to keep environments separate and manage **API keys**

✅      For further instructions, see this [video tutorial](https://www.loom.com/share/6cb661d752db4fda932871dccce9133b). 

# The basics

 \
✅      **Cache your token**, don't re-authenticate for every request. Token lasts 1 hr

✅      Use **correct token scope** eg. use `CLIENT_ACCESS` token for **all** client side requests. 

✅      **Handle jobs correctly**, including [happy and unhappy paths](#handling-failed-jobs)

# **Need data updated daily**?

 \
✅      [Enable smart cache](https://api.basiq.io/docs/basiq-best-practices-1#section-when-refreshing-a-connection) for **daily** fresh data

✅      Check **user jobs daily** and handle any failures

✅      Only manually refresh connections on an **ad hoc** basis

# **Built your own UI**?

 \
✅      Check **correct login fields** for [each bank](https://api.basiq.io/docs/#institutions) e.g. St George requires an additional security code. 

✅      **Never store users credentials**, post directly to the Basiq API using `CLIENT_ACCESS` token

# Support

 \
✅      Ensure **error logging** includes `userId`, `connectionId`, and `jobId`, for reporting issues

✅      Use `/institutions` to [dynamically](https://api.basiq.io/docs/#basiq-best-practices) determine **current stage and status** of all connectors 

✅      Subscribe to **notifications** from [our status page](https://status.basiq.io/) for larger, ongoing outages

✅      Reach out to us anytime via the intercom chat bubble on our site, or at [support@basiq.io](mailto:support@basiq.io).

 \
 

> 📘 Download this checklist
>
> If you would like a PDF of this checklist to hand off to your developers, you can get one [here](https://drive.google.com/uc?id=12mRQZlOBVjzWVFec-zZPKMHp4xO0JnfB\&export=download).
