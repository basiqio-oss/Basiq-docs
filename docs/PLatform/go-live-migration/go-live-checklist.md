---
title: Go live checklist
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
<Image align="center" width="80%" src="https://files.readme.io/cd58628-dev_guide_hero.svg" />

Once you’ve integrated with the Basiq API using our sandbox environment, and you’re ready to be enabled for live data, there are a few things to tick off to ensure it all runs smoothly. Here is a checklist covering everything you need to make your application production-ready. 

All of the **best practice** implementation details for the following requirements can be found [here](https://api.basiq.io/docs/best-practices). 

# Housekeeping

with the Basiq [dashboard](https://dashboard.basiq.io/) \
✅      Invite **team members** to your account

✅      If you wish to access Open Banking data, reach out to customer success to ensure you are enabled

✅      Setup Basiq **applications** to manage **API keys**, configure your **consent policy, and\
select your** offered institutions\*\*. 

✅      Before being enabled for access to live data, ensure you have **cleaned up any test users** as these will become billable once you are switched on. 

# The basics

 \
✅      **Cache your token**, don't re-authenticate for every request. Token lasts 1 hr

✅      Use **correct token scope** eg. use `CLIENT_ACCESS` token for **all** client side requests. 

✅      **Handle jobs correctly**, including [happy and unhappy paths](https://api.basiq.io/docs/handling-jobs#possible-job-failure-scenarios)

# **Need data updated daily**?

 \
✅      [Enable smart cache](https://api.basiq.io/docs/best-practices#when-refreshing-a-connection) for **daily** fresh data

✅      Check **user jobs daily** and handle any failures

✅      Only manually refresh connections on an **ad hoc** basis

# Support

 \
✅      Ensure **error logging** includes `userId`, `connectionId`, and `jobId`, for reporting issues

✅      Use `/connectors` to [dynamically](https://api.basiq.io/docs/migration-guide-from-institutions-ep-to-connectors-ep) determine **current stage and status** of all connectors 

✅      Subscribe to **notifications** from [our status page](https://status.basiq.io/) for larger, ongoing outages

✅      Reach out to us anytime via the intercom chat bubble on our site, or at [support@basiq.io](mailto:support@basiq.io).

# Additional Recommendations

✅      Inform the end user that they can manage their consent at any point. You can utilise the `action=manage` to do so, which you can read more about [here](https://api.basiq.io/docs/consent-actions#manage-consent-actionmanage).

✅      Utilise the “Manage Consent URL” field in the flow section of our Consent UI customizer. You can put the URL to your consent management guide so we can show it to consumers within the "Manage your data sharing" section.

✅      Get in touch with the onboarding team to walkthrough your UX journey and integration.

✅      Enable SmartCaching.

✅      Enable 2FA.

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/dovS6GmzDt1tXBDnsdPe?embed" title="Basiq - 2FA " frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>
