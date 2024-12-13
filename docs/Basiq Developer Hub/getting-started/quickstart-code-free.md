---
title: 'Quickstart: code free'
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

<div
  style={{
    border: "2px solid #4e9ccf", // Classic blue border
    borderRadius: "8px",
    backgroundColor: "#e3f2fd", // Light blue background (cascade effect)
    padding: "16px",
    margin: "16px 0",
    fontFamily: "Arial, sans-serif",
    color: "#333", // Dark text for readability
  }}
>
  <strong style={{ color: "#1e88e5" }}>📢 Attention!</strong> If you have any issues, please reach out to our amazing support team.

  <div style={{ display: 'flex', alignItems: 'center' }}>
    <button
      onClick={() => Intercom('showNewMessage', 'issues on FAQs:')}
      style={{
        padding: '12px 30px',
        backgroundColor: '#1e88e5', // Classic blue button color
        color: '#ffffff',
        border: 'none',
        borderRadius: '50px',
        fontSize: '16px',
        fontWeight: '600',
        textTransform: 'uppercase',
        cursor: 'pointer',
        boxShadow: '0 4px 10px rgba(30, 136, 229, 0.2)', // Soft blue shadow
        transition: 'background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease',
        outline: 'none',
        display: 'flex',
        justifyContent: 'center',
        height: '45px',
        position: 'relative',
        overflow: 'hidden',
        marginLeft: '10px', // Add space between text and button
        minWidth: '150px', // Ensure the button has enough width for the text
      }}
      onMouseEnter={(e) => {
        e.target.style.transform = 'scale(1.1)';
        e.target.style.boxShadow = '0 6px 15px'; // Darker shadow on hover
        e.target.style.backgroundColor = '#1565c0'; // Darker blue on hover
      }}
      onMouseLeave={(e) => {
        e.target.style.transform = 'scale(1)';
        e.target.style.boxShadow = '0 4px 10px';
        e.target.style.backgroundColor = '#1e88e5'; // Original blue
      }}
    >
      Support team
    </button>
  </div>
</div>