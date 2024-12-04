---
title: Upgrading to v3.0
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
## What's new

There have been some fundamental changes to how the Basiq platform manages consent and data governance for our partners. This have largely been due to the rules defined in the CDR Open Banking Australian Government legislation. Although the CDR requirements and architecture are complex, Basiq has been able to abstract that complexity away, leaving just a few key areas for partners to consider. *Major changes can be seen in the following areas:*

* **Consent definition** - Partners need to define their [Consent Policy](https://api.basiq.io/docs/consent-ui) which will determine the consent agreement with their Consumers.

* **Institutions:** There are now two methods of connecting financial institutions: Digital Data Capture and Open Banking. For each institution partners will now need to configure which data connection method to use [via the dashboard](https://api.basiq.io/docs/dash-configuration#2-configuring-your-available-institutions).

* **Consent UI:** CDR has mandated a very detailed and granular consent model. The Basiq platform simplifies the consent process by providing a [Consent UI](https://api.basiq.io/docs/consent-ui) for our partners to use in their applications. Basiq also provides a consumer consent management solution.

* **Data Governance:** CDR has strict rules around how the granular consent is applied to data persisted both in the Basiq and in our Partner platforms. Basiq provides a fully managed data governance solution.

* **Open Banking data:** In order to access Open Banking data our partners need to work with Basiq to enable one of the access models available under CDR. Only once this is done can our Partners fully unlock the potential of the Basiq API 3.0 and Open Banking. *More information to come around the different access models...* 

<Image width="80%" src="https://files.readme.io/1a93039-openbankingcomponents_1.svg" />

> 📘 Upgrading to v3.0 does not automatically enable you for Open Banking data access
>
> Partners are able to upgrade to access v3.0 of the API without being enabled for Open Banking. If you would like to be enabled for Open Banking please reach out to [support@basiq.io](mailto:support@basiq.io) where the team can assist in registering your application.

## Migrating to 3.0

In order to help existing partners easily migrate to v3.0, and to minimise the technical maintenance across two systems, Basiq will upgrade all partners data to ensure that it is inline with the new data model requirements. This includes the creation of application policies and user consents.

#### All existing partners will have their data structures updated to be compatible with API 3.0

Basiq will ensure that the existing implied user consents will be used to generate the following:

* **Creation of a consent policy per application:** Creating a consent Policy object for each application fitting the new consent schema

* **Creation of a consent record per user:** Creating a user consent object for each user fitting the new consent schema

* **Update application records to incorporate new attributes** e.g. A `displayName` for each Application generated from the existing Partner Name. 

### UI updates

For v3.0 of the API, **partners are required to redirect their users to the Basiq Consent UI** for them to provide consent and create new connections instead - they will not be able to do this using the API. See our [User Consent UI](https://api.basiq.io/docs/consent-ui) for more information. 

### Data governance

Notification services are critical to ensuring that all the parties (Basiq and Partners) adhere to and respect the user consent. To assist parties in adhering to the granted consent - Basiq provides a series of notification services that will inform partners when there is a change of state with the consent object. **Partners are required to provide Basiq with an event web-hook (coming soon!) to receive these event notifications and provide it in their[application configuration](https://api.basiq.io/docs/dash-configuration#3-configuring-your-data-governance-web-hook).**

## Step by step guide

### Dashboard

**1.** Your Application is already enabled for 3.0 but we need to perform some [Consent UI Configuration](https://api.basiq.io/docs/dash-configuration) first. Head to the [Basiq dashboard](dashboard.basiq.io) and navigate to the [Customise UI](https://dashboard.basiq.io/customise-ui) page for your Basiq Application\
 

![1880](https://files.readme.io/f398f3c-Customise_UI.png "Customise UI.png")

 \
**2.** Once you're here input your own branding in the header image and configure your redirection url!

![2738](https://files.readme.io/672076b-ConsentUI-HeaderImage.png "ConsentUI-HeaderImage.png")

 

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        New fields
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Header Image
      </td>

      <td style={{ textAlign: "left" }}>
        Your products brand image that will be presented to the end user when they view the Consent UI
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Redirection URL
      </td>

      <td style={{ textAlign: "left" }}>
        The URL you would like your users to be redirected to on completing their bank connections
      </td>
    </tr>
  </tbody>
</Table>

**3.** Now we can edit the Consent Policy. Here you will see a pre-filled, generic consent policy which your user will be presented with when they connect their accounts. Consider what you update here carefully as any changes will not apply to existing customers until they re-consent.\
 

![2728](https://files.readme.io/158e134-Screen_Shot_2022-09-02_at_3.31.18_pm.png "Screen Shot 2022-09-02 at 3.31.18 pm.png")

 \
**4.** Navigate to the Institutions tab. This is where you are able to decide which institutions you will offer to your end user, and by which method (Open Banking or Web Connectors) once you are enabled for access to Open Banking data. By default you will have all Institutions selected.\
 \
 

![2016](https://files.readme.io/a3aea15-Screen_Shot_2022-09-02_at_3.33.33_pm.png "Screen Shot 2022-09-02 at 3.33.33 pm.png")

 \
**5.** Once you have configured everything via the dashboard you can click save and you are ready to implement application changes. 

### Code changes

**6.** Update **all** of your `/token` requests to include the new version in the header.\
 

```http
POST /token HTTP/1.1
Host: au-api.basiq.io
Authorization: Basic YOUR_API_KEY
Content-Type: application/x-www-form-urlencoded
basiq-version: 3.0
Content-Length: 19

scope={SCOPE}
```

**7.** Update your applications UI to accomodate the new Consent UI. If you are using the previous Simple UI (our `npm` package) you will just need to trigger a window redirect instead of rendering the old component. You will need to include the `userId`, and the client token *(which should now also be bound to the userId - see previous step)*.\
 

```javascript
// Redirect to the external Basiq Consent UI to connect
  async function goToConsent(action = null) {
    let userId = sessionStorage.getItem("userId")
    const token = await getClientToken(userId);
    window.location = (`https://consent.basiq.io/home?token=${token}&action=${action}`);
  }

<Button onClick={goToConsent}>Connect your accounts</Button>
```

When your user has finished with connecting their institutions, they will be redirected back to the URL defined in your dashboard back in step 2, and from there you will be able to access their financial data as normal.
