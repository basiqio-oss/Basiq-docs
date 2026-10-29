---
title: Redirect to App
deprecated: false
hidden: true
metadata:
  robots: index
---
i want to add this but i want you to use MDX

Redirect to App for Mobile Applications

Overview

Redirect to App (R2A) is a CDR authentication flow that allows a consumer to authenticate with their Data Holder using the Data Holder's native mobile application.

For Basiq integrations, this means that a consumer who starts a consent journey from a native mobile application may be transferred from the Basiq consent experience to their Data Holder's mobile application to authenticate and authorise the CDR data sharing request.

Once the Data Holder completes authentication and authorisation, the consumer is returned to the Basiq/ADR application through the registered mobile redirect URI.

Redirect to App is part of the CDR authentication standards and must be supported by Data Recipients from 10 May 2027. Data Recipients and Data Holders may implement the capability earlier.

When should I use Redirect to App?

Redirect to App is intended for integrations where the consumer starts the CDR consent journey from a native mobile application.

The flow allows the consumer to use the authentication experience they are already familiar with in their Data Holder's mobile banking app, such as their existing app authentication mechanisms.

For example:

Partner mobile app

→ Basiq Consent UI

→ Data Holder

→ Data Holder mobile app

→ Consumer authenticates

→ Consumer authorises CDR consent

→ Partner mobile app

The Data Holder is responsible for authenticating the consumer. Basiq does not collect or handle the consumer's Data Holder credentials.

End-to-end flow

A typical Basiq mobile integration follows this pattern:

┌──────────────────────┐
│   Partner Mobile App │
└──────────┬───────────┘
│
│ Start Basiq consent
▼
┌──────────────────────┐
│    Basiq Consent UI  │
└──────────┬───────────┘
│
│ CDR authentication
▼
┌──────────────────────┐
│     Data Holder      │
│      CDR service     │
└──────────┬───────────┘
│
│ Redirect to App
▼
┌──────────────────────┐
│ Data Holder Mobile   │
│        App           │
└──────────┬───────────┘
│
│ Authenticate
│ + Authorise
▼
┌──────────────────────┐
│ Data Holder completes │
│ CDR authorisation     │
└──────────┬───────────┘
│
│ Redirect URI
▼
┌──────────────────────┐
│   Partner Mobile App │
│   / Basiq callback   │
└──────────────────────┘

The exact consumer experience is determined by the Data Holder and the CDR standards.

What happens during Redirect to App?

1. Consumer starts the consent journey

The consumer starts the Basiq consent journey from the partner's native mobile application.

Basiq presents the consumer with the relevant consent and Data Holder selection experience.

2. Consumer selects their Data Holder

The consumer selects the Data Holder they want to connect.

Basiq then initiates the CDR authentication and authorisation flow with that Data Holder.

3. Data Holder initiates Redirect to App

Where the Data Holder supports Redirect to App, the consumer is transferred to the Data Holder's native application.

The mobile operating system handles the transition from the current application/browser context to the registered Data Holder application.

Data Holders supporting Redirect to App must support the CDR-defined Claimed HTTPS URI mechanism for this app-to-app transition.

4. Consumer authenticates in the Data Holder app

The consumer authenticates using the Data Holder's supported authentication mechanism.

For example, this may involve the authentication already used by the consumer when accessing their banking application.

The CDR standards require the authentication experience not to involve more steps than the consumer would reasonably encounter when logging into the Data Holder's app for non-CDR purposes, unless otherwise specified by the standards.

5. Consumer authorises the CDR request

Authentication does not itself grant access to the consumer's data.

After authentication, the Data Holder continues the CDR authorisation flow within its mobile application.

The consumer reviews and authorises the requested data sharing.

6. Consumer returns to the partner application

After successful authorisation, the Data Holder redirects the consumer back using the registered redirect URI.

For an ADR that initiates consent from a mobile application, the ADR must support a Claimed HTTPS Scheme URI for its app redirect URI. Data Recipients must also register separate redirect URIs when they provide both app-based and web-based redirection.

The partner application can then resume the Basiq integration using the result of the consent flow.

Basiq's role

Basiq provides the consent and CDR integration layer between the partner and the Data Holder.

Basiq is responsible for:

Providing the consent experience.

Initiating the CDR connection with the selected Data Holder.

Managing the CDR integration and authorisation flow.

Providing the appropriate redirect/callback mechanism.

Returning the consumer to the partner's application following the CDR flow.

Managing the resulting CDR connection and data access according to the Basiq integration.

Basiq does not authenticate the consumer with the Data Holder.

Basiq should never request or collect a consumer's Data Holder username, password, PIN or other Data Holder authentication credentials.

The CDR standards also require consumer-facing interactions to make clear that third parties do not need the consumer's password to access CDR data.

Partner responsibilities

When integrating Basiq into a native mobile application, the partner is responsible for ensuring its application can correctly handle the mobile redirect flow.

The partner should:

Initiate the Basiq consent experience from the mobile application.

Configure the appropriate Basiq redirect URI.

Support the mobile application's claimed HTTPS redirect URI.

Ensure the operating system can route the redirect back to the correct application.

Handle successful, cancelled and failed consent journeys.

Resume the application flow when the consumer returns from the Data Holder.

Avoid attempting to authenticate the consumer with the Data Holder directly.

The mobile application should treat the Data Holder authentication experience as an external authentication step and should not attempt to reproduce or embed the Data Holder's authentication screens.

Redirect URI requirements

For mobile applications, the redirect URI is particularly important because it determines how the consumer returns to the partner application.

Where an ADR provides both web-based and app-based redirection, separate redirect URIs must be registered.

For app-based consent initiation, the ADR must support the CDR's Claimed HTTPS URI mechanism for the application redirect URI.

The purpose of this mechanism is to allow the mobile operating system to associate the HTTPS URI with the partner's application and route the consumer back into that application.

The partner should therefore ensure that:

The redirect URI is correctly registered.

The mobile application is configured to claim the relevant HTTPS URI.

The iOS and Android application configuration is correctly implemented.

The application can resume the consent flow when the redirect is received.

The application handles cases where the consumer does not return successfully.

WebView considerations

Redirect to App should not be treated as a requirement to embed the entire CDR authentication journey inside a WebView.

The Data Holder controls its own authentication experience.

In particular, the partner should not attempt to embed the Data Holder's native authentication experience inside the partner's WebView.

A mobile integration should instead allow the CDR flow to transition between the partner application and the Data Holder's application where Redirect to App is supported.

The resulting experience is therefore:

Partner App
│
▼
Basiq Consent
│
▼
Data Holder
│
▼
Data Holder App
│
▼
Authentication + Authorisation
│
▼
Partner App

This is different from a traditional WebView-based flow where the entire journey remains within the partner application.

Redirect to App vs Redirect to Web

<br />

Redirect to App

Redirect to Web

Consumer starts from

Native mobile app

Web or mobile

Authentication

Data Holder mobile app

Data Holder web experience

Data Holder app required

Yes, where applicable

No

Native app-to-app transition

Yes

No

Partner mobile callback

Required for app flow

Web redirect

Consumer credentials

Entered/authenticated with Data Holder

Entered/authenticated with Data Holder

Basiq handles credentials

No

No

Redirect to App is specifically designed to provide an app-based authentication experience where the Data Holder provides a mobile application.

What if Redirect to App cannot be used?

Redirect to App is not expected to work in every circumstance.

Where Redirect to App cannot be used and Decoupled Authentication is not supported, the CDR fallback framework requires Data Holders to continue supporting Redirect to Web with One Time Password (OTP).

This means a mobile application should be designed to handle the possibility that the consumer completes authentication through an alternative CDR authentication flow.

The partner should not assume that every Data Holder will always result in an app-to-app transition.

Example customer journey

A customer is using a partner's mobile application and wants to connect their bank account.

Step 1

The customer selects Connect bank account.

Step 2

The partner launches the Basiq Consent UI.

Step 3

The customer selects their Data Holder.

Step 4

The Data Holder's CDR flow determines that Redirect to App can be used.

Step 5

The customer is transferred to the Data Holder's mobile application.

Step 6

The customer authenticates using the Data Holder's supported authentication method.

Step 7

The customer reviews and authorises the CDR data-sharing request.

Step 8

The Data Holder completes the CDR authorisation flow.

Step 9

The customer is returned to the partner's mobile application using the registered app redirect URI.

Step 10

The partner application resumes the Basiq journey and can continue using the resulting Basiq connection.

Important considerations for partners

Do not collect Data Holder credentials

The partner should never ask the customer for their bank username, password or authentication credentials.

Do not assume authentication happens in Basiq

Basiq facilitates the CDR consent journey. Authentication is performed by the Data Holder.

Do not assume every Data Holder behaves identically

The consumer experience may vary depending on the Data Holder, whether the consumer has its mobile application installed, and which authentication flow is available.

Support returning to the mobile application

The partner application must be able to receive and process the registered app redirect URI.

Support cancellation and failure

The customer may cancel authentication or authorisation, close the Data Holder app, or encounter an authentication failure. The partner should handle these outcomes without leaving the customer in an incomplete state.

Implementation checklist

Before releasing a mobile Basiq integration, confirm that:

Basiq Consent UI can be launched from the native application.

The appropriate mobile redirect URI is configured.

The application supports the CDR Claimed HTTPS URI requirements.

iOS application association is configured correctly.

Android application association is configured correctly.

The application can resume after returning from a Data Holder.

Success, cancellation and failure states are handled.

The application does not collect Data Holder credentials.

The integration does not assume that every Data Holder supports the same authentication experience.

The integration can handle the applicable fallback authentication flow.

Summary

For a native mobile Basiq integration, Redirect to App allows the consumer to leave the Basiq/partner journey temporarily and authenticate and authorise through their Data Holder's native mobile application before returning to the partner application.

Basiq remains responsible for facilitating the CDR consent and connection flow, while the Data Holder remains responsible for consumer authentication and authorisation.

The key requirement for the partner is to correctly support the mobile redirect URI and app-to-app return journey, rather than attempting to embed or reproduce the Data Holder's authentication experience.

Redirect to App is a CDR requirement for relevant Data Recipients and Data Holders from 10 May 2027, although participants can implement it earlier.

Official CDR reference: [https://cx.dsb.gov.au/authenticate/redirect-to-app](https://cx.dsb.gov.au/authenticate/redirect-to-app)
