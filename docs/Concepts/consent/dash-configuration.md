---
title: Account Balance vs Available Funds
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
        "https://files.readme.io/d89e07a-customiseUi.gif",
        "customiseUi.gif",
        1440,
        810,
        "#e4dfe7"
      ],
      "sizing": "80"
    }
  ]
}
[/block]
&nbsp;

Partners are able to setup and configure their applications via the `customise-ui` tab in the [basiq dashboard](https://dashboard.basiq.io). Partners will also be able to see a live preview of the [Consent UI](doc:consent-ui) while they make these changes. 

## 1. Configuring your applications consent policy 

By default, each application is assigned a Consent Policy when it is created, however this can be updated to more accurately reflect your applications needs by updating values including: 
- Duration,
- Title & Subtitle,
- Purposes,
- [Permissions](doc:consent-scopes), and
- Supporting parties

&nbsp;
&nbsp;
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bec0ea4-Screen_Shot_2022-08-24_at_1.17.35_pm.png",
        "Screen Shot 2022-08-24 at 1.17.35 pm.png",
        2880,
        1582,
        "#e7ebf0"
      ],
      "sizing": "80"
    }
  ]
}
[/block]
&nbsp;
When defining these fields, you should keep in mind the rules and requirements as proposed by the CDR, and defined within the latest [CX Guidelines](https://consumerdatastandards.gov.au/guidelines-and-conventions/consumer-experience-guidelines/).

&nbsp;

## 2. Configuring your available institutions 

As Open Banking becomes more widely adopted, the number of available institutions will increase, and in some cases there may be multiple ways to connect to a single institution - *such as ING Open Banking and ING Digital Data Capture*. 
&nbsp;
&nbsp;
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/cc2b27e-Screen_Shot_2022-08-31_at_10.07.10_am.png",
        "Screen Shot 2022-08-31 at 10.07.10 am.png",
        2756,
        1530,
        "#e3e7ed"
      ],
      "sizing": "80"
    }
  ]
}
[/block]
&nbsp;
By selecting from the list of institutions, partners can configure which institutions they would like to present to their end users. *Note: The application dashboard Institution picker will only show Open Banking data sources for institutions if the partner is enabled. See [enablement](https://api.basiq.io/docs/open-banking#enabling-your-application-for-open-banking) for more information.*

**E.g.** Partners may choose to exclude any that specifically relate to business banking as they are irrelevant for their use case, or to only have Open Banking supported institutions available.

&nbsp;

## 3. Add your own Branding in the Header Image

You can now add your own branding in the header image. This will be shown to your end users.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/12cdc15-ConsentUI-HeaderImage.png",
        "ConsentUI-HeaderImage.png",
        2738,
        1464,
        "#000000"
      ]
    }
  ]
}
[/block]
&nbsp;
## 4. Configuring any optional fields

There a number of other additional fields that partners can configure, depending on how they would like the Consent UI to behave for their end users, including 
- **Redirect URL: **Where your user will be redirected to when they have finished with their banking portal
- **Skip success page:** If you are looking to reduce the number of screens you may choose to skip the final "Successfully connected to..." page and instead redirect straight back to your own application 
- **Allow multiple connections:** If your end user should be able to connect more than one institution at a time
- **Retain data by default:** This will decide the default behaviour of data retention for your users