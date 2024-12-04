---
title: Migration checklist
excerpt: Quick Guide to Upgrading to Basiq API 3.0
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Key Updates

### Consent & CDR Integration

With the release of Basiq API 3.0, we've aligned our platform with the CDR Open Banking regulations. While the CDR rules may seem complex, we've simplified the process to ensure a smooth transition for partners. Below are the main changes you need to be aware of:

* **Consent Policy:** Partners must define their [Consent Policy](https://api.basiq.io/docs/consent-ui) to establish a consent agreement with consumers.

* **Institutions:** Two connection methods are now available for financial institutions: Digital Data Capture and Open Banking. You must configure which method to use for each institution via the [dashboard](https://api.basiq.io/docs/dash-configuration#2-configuring-your-available-institutions).

* **Consent UI:** The CDR requires a granular consent model. Basiq simplifies this with a [Consent UI](https://api.basiq.io/docs/consent-ui) that partners can integrate into their applications, ensuring a smooth consent process for users.

* **Data Governance:** The platform now supports CDR’s strict rules on consent for data storage and governance. We offer a managed solution for this.

* **Open Banking Data Access:** To access Open Banking data, partners need to work with Basiq to enable the appropriate access model under CDR. Contact [support@basiq.io](mailto:support@basiq.io) for more information.

<HTMLBlock>{`
<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(66.66666666666666% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/oLJlGfYDq85CogD5rfaK?embed&embed_mobile=tab&embed_desktop=inline" title="Platform Components" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->
`}</HTMLBlock>

<br />

> 📘 Upgrading to v3.0 does not automatically enable you for Open Banking data access
>
> Partners are able to upgrade to access v3.0 of the API without being enabled for Open Banking. If you would like to be enabled for Open Banking please reach out to [support@basiq.io](mailto:support@basiq.io) where the team can assist in registering your application.

## Migrating to API 3.0

We’ve streamlined the upgrade process to minimise technical overhead for partners. Your data will be upgraded to meet the new 3.0 requirements. This includes:

* **Consent Policies:** A consent policy will be created for each of your applications.
* **User Consents:** A consent record will be created for each user to fit the new schema.
* **Application Updates:** Attributes such as `displayName` will be added to your applications.

## Required UI Changes

To comply with API 3.0, you must redirect users to the Basiq Consent UI to manage consent and establish connections. Connection creation using API-only methods are no longer supported. Visit our [User Consent UI](https://api.basiq.io/docs/consent-ui) documentation for more details.

## Notifications & Data Governance

Basiq provides event notifications to keep you updated on changes to user consents. You will need to set up an [event web-hook](https://api.basiq.io/docs/webhooks) and configure it in your application settings.

## Step-by-Step Guide to Upgrading

### 1. Configure Consent UI

Head to the [Basiq dashboard](dashboard.basiq.io) and customize the Consent UI. Add your brand’s header image and configure the redirection URL.

* **Brand Name:** Adding Brand name is mandatory. 
* **Header Image:** This will be shown to users on the Consent UI.
* **Redirection URL:** Define where users will be redirected after connecting their accounts.

<HTMLBlock>{`
<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(50.18807092960774% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/1HCla91Hn0l7IQrV7Jq6?embed&embed_mobile=tab&embed_desktop=inline" title="Customise UI " frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->
`}</HTMLBlock>

### 2. Set Up Institutions

Choose which institutions to offer to users and configure the connection method (Open Banking or Web Connectors) from the Institutions tab.

<HTMLBlock>{`
<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(50.18807092960774% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/SWY8ewzJMwlWvI1CccQJ?embed&embed_mobile=tab&embed_desktop=inline" title="Institutin Selection" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->
`}</HTMLBlock>

### 3. Save Changes

After configuring everything in the dashboard, click "Save" to apply the changes.

<HTMLBlock>{`
<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(50.18807092960774% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/VDnntCkjgmsyxhgZMQoR?embed&embed_mobile=tab&embed_desktop=inline" title="Basiq - Customise UI " frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->
`}</HTMLBlock>

Once you have configured everything via the dashboard you can click save and you are ready to implement application changes.

### 4. Update API Requests

For all `/token` requests, include the new version header:

```http
POST /token HTTP/1.1
Host: au-api.basiq.io
Authorization: Basic YOUR_API_KEY
Content-Type: application/x-www-form-urlencoded
basiq-version: 3.0
Content-Length: 19

scope={SCOPE}
```

### 5. Update Your UI

If you used the previous Simple UI, replace it with a redirect to the new Consent UI. Here’s an example of how to trigger the redirect:

```javascript
// Redirect to the external Basiq Consent UI to connect
  async function goToConsent(action = null) {
    let userId = sessionStorage.getItem("userId");
    const token = await getClientToken(userId);
    window.location = (`https://consent.basiq.io/home?&token=${token}&action=${action}`);
  }

<Button onClick={goToConsent}>Connect your accounts</Button>
```

Once users connect their institutions, they will be redirected to the URL defined in your dashboard, and their financial data will be accessible as usual.
