---
title: Extended Metadata
excerpt: >-
  For a data recipient (Basiq) to collect, use and disclose CDR data, they must
  have consent from the consumer to do so. For this reason, *partners wishing to
  access v3.0 of the Basiq API are required to use the Basiq Consent UI in their
  application.*
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
 \
 

<Image width="40%" src="https://files.readme.io/6b64555-ezgif.com-gif-maker_2.gif" />

 \
 

## The Consent UI

The Basiq Consent UI is designed to handle all of the complexity behind **CDR legislation**, **consent management**, and **CX guidelines**, so partners can fast track their access to Open Banking data, and focus on innovation. 

The Consent UI is driven by the application's own [Consent Policy](ref:dash-configuration#1-configuring-your-applications-consent-policy), which acts as a contract for end users to agree to before proceeding to connect their institution/s.

## Dynamic switching

The Consent UI focuses on providing a seamless user experience no matter the method of data retrieval. What this means, is that it can be used for both web, and Open Banking, connections. Consent applies to the application/user level, so all connections made under this will be handled the same way. The institutions presented to the user are decided by the partner and can be configured at any point via the [dashboard](ref:dash-configuration#2-configuring-your-available-institutions). Everything else is handled by the UI. 

## Implementation

The Consent UI is hosted by Basiq, and can be accessed by passing a `CLIENT_SCOPE`. This token must also be bound to the `userId` as a security measure, to ensure nobody is consenting on your users behalf. E.g. 

`https://consent.basiq.io/home?token={{client_token_bound_to_userId}}`

Your access token and userId can be obtained via the Basiq API (See the [quick start guide](ref:quickstart-part-1)).

## The Consent flow

The Consent UI will grant a different user flow, depending on the action required. This is handled by partners passing additional parameters in the URL.

### Create consent *(No action parameter, default)*

Not passing any action parameters will present the user with the default Consent Flow, and should be used for first time onboarding and users that do not have an existing, valid consent against their account. This flow will cover consent as well as connecting their institutions.\
 \
 

![370](https://files.readme.io/df3d930-DefaultFlow.svg "DefaultFlow.svg")

 \
 

### Manage consent `action=manage`

Your user would like to manage their consent. This includes viewing their current consent including expiry, and connections they have made that your application now has access to. This screen will allow them to delete connections individually or entirely revoke the consent they have given to your organisation.

*Note: Using this action when a user does not have an active user consent will result in an error.*\
  

![185](https://files.readme.io/223c673-Group_2742.svg "Group 2742.svg")

 \
 

### Connect institutions `action=connect`

If your end user has an existing, valid consent, they do not need to re-consent and instead can skip straight to connect any institutions. E.g. if a user has decided they would like to add more connections after already exiting the flow. 

 \
 

![247](https://files.readme.io/c1b5b57-actionConnect.svg "actionConnect.svg")

 \
 

### Extend consent `action=extend`

Your user's consent is due to expire soon, and are required to extend it in order for your application to continue to access their data.

*Note: Using this action when a user does not have an active user consent will result in an error.*\
 \
 

![184](https://files.readme.io/ebd9e10-extendConsent.svg "extendConsent.svg")

 \
 

### Update consent `action=update`

Your user needs to update their consent. E.g. The applications consent policy has been amended due to an increase in scope and they are required to re-authorise. *A change in scope will not invalidate your users consent, however it will restrict your application from accessing data under the additional scopes until they have accepted the new consent policy.*

*Note: Using this action when a user does not have an active user consent will result in an error.*\
 \
 

![291](https://files.readme.io/a58af47-updateConsent.svg "updateConsent.svg")

 \
 

## `State` Parameter

This release enables our partners when launching the frontend flow, We allow our partners to pass a state parameter which is included in the BASIQ Consent URI when the user returns to our application. This state parameter can be decoded on the partners application side and be used to determine where to direct the user back to.

*Note: The BASIQ Consent URI will look like this:[https://consent.basiq.io/home?\&token=$\{token}\&action=$\{action}\&state=\{yourState}](#)*

 \
 

 \
 

## Institution parameters

If a partner knows which institution they wish to obtain credentials for, they can add an `institutionId` parameter to the URL. This will bypass the "Select Institution" screen and is applicable for the following flows: 

* Create consent: `default`
* Connect institutions: `action=connect`
* Update consent: `action=update`

*Note: The BASIQ Consent URI will look like this:[https://consent.basiq.io/home?\&token=$\{token}\&action=$\{action}\&state=\{yourState}\&institutionId=\{institutionId}](#)*

 \
 

 \
 

## Update credentials via Consent UI

Partners can now pass a `connectionId` parameter in the URL to initiate a credential update flow. This only works for non-CDR connections.

*Note: The BASIQ Consent URI will look like this:[https://consent.basiq.io/home?\&token=$\{token}\&connectionId=$\{connectionId}\&state=\{yourState}](#)*

![424](https://files.readme.io/0ddc104-image-20220915-015203_1.png "image-20220915-015203 (1).png")

 \
 

## `jobIds` parameter

Basiq allows your users to create multiple connections within a single flow when the `Allow multiple connections` feature is enabled in the Basiq dashboard. With the new `jobIds` parameter, you can retrieve all the `jobIds` from connection attempts appended to the `Redirect URL`.

This parameter makes it easier and more streamlined for you to track the progress of multiple connections within the same session. The `Redirect URL` contains all `jobIds` from that session, including the newest `jobId` like so: 

```text Sample Redirect URL with jobIds
http://www.your-redirect-url.com/?jobIds=123,456,789
```

Refer to the [Dashboard configuration](https://api.basiq.io/docs/dash-configuration#4-configuring-any-optional-fields) page for more information on how to enable the Allow multiple connections feature.

 \
 

## Error scenarios

<Image width="25%" src="https://files.readme.io/3d11bfb-Group_2743.svg" />

 \
 

### Payments consent `action=payment`

Passing in this value would result in showing the payments consent UI. If the user has not consented to sharing data accounts then they will be directed to that step first. If the user has already shared data accounts then the payments consent will be shown.

<Image width="smart" src="https://files.readme.io/8c7653a-cac6b5b-paymentspage2_1.png" />

 \
 

#### Resource not found

You will be met with a `resource-not-found` error if your user does not have a current consent and you are attempting to enter a flow that requires one such as `action=manage`. This can be avoided by performing a check for your user's consent prior to initiating this flow. If they do not have one they should go to the default flow and give consent. 

#### Missing attributes

A `missing-attributes` error may occur if your access token has not been bound to a `userId`. You can try use [this JWT app](https://jwt.io/) to decode your token and confirm if it has been bound correctly. Read more about tokens [here](ref:posttoken).  

 

### Full consent flow diagram

 \
 

<Image width="smart" src="https://files.readme.io/563467a-Frame_2.svg" />
