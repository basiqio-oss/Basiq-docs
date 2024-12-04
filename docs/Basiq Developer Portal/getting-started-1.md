---
title: Getting Started
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
# Getting Started with Basiq API: Quick Setup Guide

Welcome to Basiq, your gateway to swiftly implement and utilize our API. This guide has been designed to streamline the setup process, getting you ready to delve into coding without delay.

## 1. Application Registration via Dashboard

Begin by registering your application through our [dashboard](https://dashboard.basiq.io/). Make sure to bookmark this page, as it will serve as your central hub for application management. Here, you can handle tasks like inviting team members, assigning roles and permissions, generating API keys, and managing application-level settings and configurations.

## 2. Configure Your Application

Customize your application's settings to suit your needs:

  * **Application Details**: Specify your application's name, region, and logo. These details will be presented to your end users when they connect their financial institutions.

  * **Consent Policy**: Craft a consent policy outlining data access scope, consent duration, and intention. This policy will be presented to end users when they grant consent and connect their financial institutions. While a default policy is provided, it's essential to tailor it to your application's context.

  * **Institutions**: Define which institutions will be displayed to end users through the Basiq Consent UI. Partners can choose connection methods (Direct Debit Control or Open Banking) for each institution. Note that only partners enabled for Open Banking can select Open Banking connectors.

More information on this application config can be found **[here](https://api.basiq.io/docs/dash-configuration)**.

## 3. Generate Your API Key

Head over to the developers tab to generate a new API key. Remember:

  * You can create multiple API keys, making it possible to use keys across various applications and environments.
  * Assign meaningful names to each API key to easily distinguish between them.
  * Copy and securely store the provided key immediately, as it will only be fully exposed once.
  * Safeguard your API keys diligently, as they come with significant privileges. Never share them in public spaces like GitHub or client-side code.

## 4. Enable Open Banking for Your Application

For those interested in accessing Open Banking data, consider enabling your application:

**Optional Upgrade**: All partners can transition to v3.0 as it becomes available. However, to fully unlock the potential of Basiq API 3.0 and Open Banking, partners must collaborate with our <a onclick="messenger('show') >customer success team </a>. This ensures compatibility with the access models supported by Basiq, in accordance with CDR legislation.

Embark on your journey with Basiq API by following these steps. Should you encounter any questions or hurdles, our support team is here to assist you every step of the way.