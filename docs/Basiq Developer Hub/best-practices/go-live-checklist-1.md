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
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/cd58628-dev_guide_hero.svg",
        "dev_guide_hero.svg",
        690,
        385,
        "#00b3ff"
      ],
      "sizing": "80"
    }
  ]
}
[/block]
Once you’ve integrated with the Basiq API using our sandbox environment, and you’re ready to be enabled for live data, there are a few things to tick off to ensure it all runs smoothly. Here is a checklist covering everything you need to make your application production-ready. 

All of the **best practice** implementation details for the following requirements can be found [here](#basiq-best-practices). 

# Housekeeping 
with the Basiq [dashboard](https://dashboard.basiq.io/)
&nbsp;
✅&nbsp;   &nbsp; Invite **team members** to your account

✅&nbsp;   &nbsp; If you wish to access Open Banking data, reach out to customer success to ensure you are enabled

✅&nbsp;   &nbsp; Setup Basiq **applications** to manage **API keys**, configure your **consent policy, and 
select your **offered institutions**. 

# The basics
&nbsp;
✅&nbsp;   &nbsp; **Cache your token**, don't re-authenticate for every request. Token lasts 1 hr

✅&nbsp;   &nbsp; Use **correct token scope** eg. use `CLIENT_ACCESS` token for **all** client side requests. 

✅&nbsp;   &nbsp; **Handle jobs correctly**, including [happy and unhappy paths](#handling-failed-jobs)

# **Need data updated daily**? 
&nbsp;
✅&nbsp;   &nbsp; [Enable smart cache](https://api.basiq.io/docs/basiq-best-practices-1#section-when-refreshing-a-connection) for **daily** fresh data

✅&nbsp;   &nbsp; Check **user jobs daily** and handle any failures

✅&nbsp;   &nbsp; Only manually refresh connections on an **ad hoc** basis

# Support
&nbsp;
✅&nbsp;   &nbsp; Ensure **error logging** includes `userId`, `connectionId`, and `jobId`, for reporting issues

✅&nbsp;   &nbsp; Use `/institutions` to [dynamically](https://api.basiq.io/docs/#basiq-best-practices) determine **current stage and status** of all connectors 

✅&nbsp;   &nbsp; Subscribe to **notifications** from [our status page](https://status.basiq.io/) for larger, ongoing outages

✅&nbsp;   &nbsp; Reach out to us anytime via the intercom chat bubble on our site, or at [support@basiq.io](mailto:support@basiq.io).

&nbsp;
&nbsp;
[block:callout]
{
  "type": "info",
  "title": "Download this checklist",
  "body": "If you would like a PDF of this checklist to hand off to your developers, you can get one [here](https://drive.google.com/uc?id=12mRQZlOBVjzWVFec-zZPKMHp4xO0JnfB&export=download)."
}
[/block]