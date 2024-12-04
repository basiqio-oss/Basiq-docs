---
title: Getting started
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
Basiq makes it easy for you to get up and running with the API quickly. This guide will get you setup and ready to dive into some code. 

### 1. Register your application via our [dashboard](https://dashboard.basiq.io/)

**Bookmark this page:** This will be where you manage your application moving forward, including things like inviting team members and assign roles or permissions, generating API keys, and managing any application level settings or configuration.

### 2. Configure your application, including:

- **Application details:** Including your application name, region and logo. This information will be presented to your end users when they connect their institutions. 

- **Consent policy:** Your consent policy defines the scope, consent duration, intention for data access, and will be presented to your end user when they give consent and connect their institutions. *Note: A generic consent policy will be predefined for each application, but it is important to carefully consider the most appropriate policy for your application*

- **Institutions:** Define which institutions will be displayed to the end-user when connecting via the Basiq Consent UI. Partners are able to select a specific connection method (DDC or Open Banking) for each institution. *Note: Only partners enabled for Open Banking will be able to select Open Banking connectors.*

More information on this application config can be found [here](https://api.basiq.io/docs/dash-configuration). 

### 3. Generate a new API key under the developers tab. 
[block:callout]
{
  "type": "warning",
  "title": "API keys",
  "body": "- You can create as many API keys as you want, which allows you to use keys across different applications and environments. It’s a good idea to give each API key a meaningful name in order to differentiate between them.\n\n- Make sure you copy and save the key we give you straight away, as it will only be exposed in full once. Your API keys carry many privileges, so be sure to keep them secret! \n\n*Do not share your API keys in publicly accessible areas such GitHub, client-side code, etc.*"
}
[/block]
### 4. Enable your application for Open Banking
*Optional: For partners who wish to access Open Banking data: *

All partners are able to upgrade to v3.0 as soon as it is available, however due to CDR legislation if they wish to fully unlock the potential of the Basiq API 3.0 and Open Banking they will need to work with the customer success team to enable one of the access models supported by Basiq.