---
title: 'Quickstart: code free'
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
<Image align="left" src="https://files.readme.io/b7047cff27f0ab4fa4471ae43382d4aa2bd46e432c365c9b704f3e6ff8f7b6ac-1a04ca3-Group_1496.png" />

<br />

<p> </p>

The following guide will help you to get up and running with the Basiq API without writing any application code. It uses [Postman](https://www.postman.com) and is suitable for both technical and non-technical audiences.

If you would prefer to integrate your application with the API directly, and aren't afraid to get your hands dirty writing some code, you might be more interested in our [Quickstart](ref:quickstart-part-1). <br />

> 🚧 Postman app required
>
> Postman is an API development tool which gives users a platform to make requests to any API. It's often used by developers to test out their own API's, however many of their consumers come from a non-technical background wanting to interact with a public API. We have curated a Postman collection for this use case, which features all of our API endpoints and makes it simple to get up and running using the platform.
>
> If you don't already have the app you can [download it here.](https://www.getpostman.com/downloads)

## STEP 1: Register

Register your application via our [dashboard](https://dashboard.basiq.io/) and create a *new* application (do not use the demo app that is created by default). All applications in dashboard are using v3.0 by default. When you have created and [configured](ref:dash-configuration) your new application, generate an API key under the Developers tab.

> 📘 API Keys
>
> You can create as many API keys as you want, which allows you to use keys across different applications and environments. It’s a good idea to give each API key a meaningful name in order to differentiate between them.
>
> Make sure you copy and save the key we give you straight away, as it will only be exposed it in full once. Your API keys carry many privileges, so be sure to keep them secret!

## STEP 2: Grab our sample code

Go to [our sample code](https://documenter.getpostman.com/view/16249946/UVktosia?version=latest) (also known as the Postman Collection) and click Run in Postman: <br />

<Image align="center" width="80%" src="https://files.readme.io/c20e2e5-Group_2710.png" />

*Make sure you select the Postman app that was installed earlier (the option will display your operating system, e.g. Mac/Windows).* <br />

<Image align="center" width="80%" src="https://files.readme.io/4f282a8-postmanStep8" />

## STEP 3: Authenticate

In Postman click on the menu options \[ 1 ], \[ 2 ], \[ 3 ] & \[ 4 ]

\[ 5 ] Then replace XXXXXX with the API Key you generated via the dashboard in Step 1

\[ 6 ] Click Save, then Send to make the request. <br />

<Image align="center" width="80%" src="https://files.readme.io/07eec60-postmanstep9.png" />

> 📘 Your access token will last an hour
>
> Don't forget: Your access token will expire every 60 minutes, so refresh as you need to.

## STEP 3: Create a user

Creating a user gives you a "bucket" to store all your financial data. Upon successful creation of a user, you will receive a `userId`. Hold onto this for the next step.

*Creating a user requires a SERVER\_ACCESS scoped token* <br />

## STEP 4: Create your first User Consent and Connection

All consent management and connection creation is done via the Basiq Consent UI. Once you have your `userId` and `access_token`, access the Consent UI via:

`https://consent.basiq.io/home?token={{client_token_bound_to_userId}}`

> 📘 Consent UI URL
>
> The token must not be enclosed in parenthesis `{{}}`

to start aggregating data. You can use our sandbox environment to replicate real life data. Find the credentials [here](https://api.basiq.io/reference/testing).

*Note: The Consent UI requires the token to be bound to a specific user by attaching the userId as well as CLIENT\_ACCESS scope to the request* <br />

## STEP 5: Make your requests!

Basiq's full suite of products are available when you use the Postman collection, ready for you start making all of your requests.

In order to connect to Basiq's test banks, you will need to use the sandbox user logins. You can find the credentials for all scenarios [here](https://api.basiq.io/reference/testing).

**Note:** You are free to make as many request as you like, however we cap the connections for sandbox users at 500 per account. If you would like to increase this quote, please email us at [support@basiq.io](mailto:support@basiq.io).

<br />

<br />

<Image align="left" src="https://files.readme.io/b7047cff27f0ab4fa4471ae43382d4aa2bd46e432c365c9b704f3e6ff8f7b6ac-1a04ca3-Group_1496.png" />

<Accordion title="Introduction" icon="fa-info-circle">
  Learn how to get started with the Basiq API using Postman. This guide is designed for both technical and non-technical users.
</Accordion>

<Cards columns={2}>
  <Card title="Overview" icon="fa-book">
    This guide will walk you through the steps needed to integrate with the Basiq API using Postman.
  </Card>

  <Card title="Requirements" icon="fa-cogs">
    > 🚧 Ensure you have Postman installed to proceed. You can [download it here](https://www.getpostman.com/downloads).
  </Card>
</Cards>

<Card title="Quick Integration" icon="fa-play-circle">
  Prefer coding directly? Check out our [Quickstart](ref:quickstart-part-1) for a more hands-on approach.
</Card>

<Columns layout="auto">
  <Column>
    <strong>Note:</strong> This guide emphasizes ease of use with Postman for streamlined API interactions.
  </Column>

  <Column>
    Postman is an essential tool that allows you to test and interact with APIs effectively.
  </Column>
</Columns>

<Cards columns={2}>
  <Card title="STEP 1: Register" icon="fa-user">
    <p>
      To start, register your application on our <a href="https://dashboard.basiq.io/">dashboard</a> and create a *new* application (avoid using the default demo app). When you're done, generate an API key under the Developers tab.
    </p>

    <Accordion title="API Key Details" icon="fa-key">
      You can create as many API keys as needed. Name them in a way that makes them easy to manage. Be sure to copy your key immediately as it will only be exposed once.
    </Accordion>
  </Card>

  <Card title="STEP 2: Grab Sample Code" icon="fa-code">
    <p>
      Go to <a href="https://documenter.getpostman.com/view/16249946/UVktosia?version=latest">our sample code</a> and click *Run in Postman*.
    </p>

    <Image align="center" src="https://files.readme.io/c20e2e5-Group_2710.png" width="80%" />

    <p>Make sure to select the installed Postman app that corresponds to your operating system (e.g., Mac/Windows).</p>

    <Image align="center" src="https://files.readme.io/4f282a8-postmanStep8" width="80%" />
  </Card>
</Cards>

<Cards columns={2}>
  <Card title="STEP 3: Authenticate" icon="fa-lock">
    <p>Follow these steps in Postman:</p>

    <ol>
      <li>Navigate through the necessary menu options.</li>
      <li>Replace `XXXXXX` with your API key from Step 1.</li>
      <li>Click *Save* and then *Send*.</li>
    </ol>

    <Image align="center" src="https://files.readme.io/07eec60-postmanstep9.png" width="80%" />

    <Accordion title="Token Expiry Info" icon="fa-clock">
      Remember, your access token expires every 60 minutes. Refresh it as needed to maintain seamless API interaction.
    </Accordion>
  </Card>

  <Card title="STEP 4: Create a User" icon="fa-user-plus">
    <p>Create a user to establish a space for storing your financial data. After successful creation, save the `userId` for the next steps. This step requires a `SERVER_ACCESS` scoped token.</p>
  </Card>
</Cards>

<Cards columns={2}>
  <Card title="STEP 5: User Consent and Connection" icon="fa-check-circle">
    <p>Use the following URL to access the Consent UI:</p>
    <p><code>[https://consent.basiq.io/home?token=\{\{client\_token\_bound\_to\_userId}}](https://consent.basiq.io/home?token=\{\{client_token_bound_to_userId}})</code></p>

    <Accordion title="Important Note" icon="fa-exclamation-triangle">
      The token should not be enclosed in curly braces `{{}}`. Ensure it's bound to a specific user by attaching the `userId` and `CLIENT_ACCESS` scope.
    </Accordion>

    <p>For testing purposes, you can use our sandbox environment. Find testing credentials <a href="https://api.basiq.io/reference/testing">here</a>.</p>
  </Card>

  <Card title="STEP 6: Make Your Requests" icon="fa-paper-plane">
    <p>Start making API requests using the Postman collection. Connect with Basiq's test banks using the sandbox user logins.</p>

    <Accordion title="Sandbox Limits" icon="fa-limit">
      The sandbox user connections are capped at 500 per account. To increase this limit, contact <a href="mailto:support@basiq.io">[support@basiq.io](mailto:support@basiq.io)</a>.
    </Accordion>
  </Card>
</Cards>