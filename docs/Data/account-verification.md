---
title: Account Verification
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
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/33aac0b-2dcf482-DevHub_StarterKit_1080x800.png",
        "",
        "Account Verification"
      ],
      "align": "center"
    }
  ]
}
[/block]


Account verification through BASIQ provides a secure and regulatory-compliant solution for businesses to access and verify user financial information, crucial for operations like credit scoring, risk assessment, and general financial services.

## Account Verification Made Easy

Using Basiq's API for account verification offers several benefits:

- **Streamlined Onboarding**: Speed up the account verification process, reducing drop-offs during customer sign-up.
- **Instant Verification**: Quickly verify identities and accounts for deposits and withdrawals.
- **Enhanced User Experience**: Display relevant financial data, like bank balances, within your app.
- **Efficiency**: Access real-time financial data to eliminate time-consuming manual processes.

## Setting Up Your Account Verification App

With Basiq's API, verifying accounts is quick and secure. The data comes directly from banks, which means:

- Faster customer onboarding.
- Instant verification for deposits and withdrawals.
- Real-time access to accurate financial data.

<br />

## Step by Step Guide

### Step 1: Sign Up with Your Email

- To begin the verification process, sign up using your email address. This email is necessary to create a BASIQ user, which will be essential for the next steps. When you sign up, a user is created with the following information:
  - Email: The email address you provide (e.g., [gavin@hooli.com](mailto:gavin@hooli.com)).
  - Mobile: Your mobile phone number (e.g., +61410888666).
  - First Name: Your first name (e.g., Gavin).
  - Middle Name: Your middle name, if applicable (e.g., leave blank if not applicable).
  - Last Name: Your last name (e.g., Belson).

> 🚧 You must provide either a mobile number or an email address to create the user and continue.

<br />

### Step 2: Pre-Consent Screen ( Optional )

- Review the pre-consent information. This step is optional. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2aaad68-image.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


<br />

### Step 3: Consent UI

- Provide your consent to proceed. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/25ddc7c-image.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


<br />

### Step 4: Select Institution

- Choose your financial institution from the list provided. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/128bb1c-image.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


<br />

### Step 5: Connection to DataHolder

- Steps 5 involve connecting to your DataHolder, which includes additional screens for account selection, reviewing consent from the DataHolder's end, and redirection back to BASIQ. These steps may vary depending on the specific bank or DataHolder. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a930cb1-image.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


<br />

### Step 6: Redirection Back to BASIQ

- You'll see a connection screen confirming the successful linkage between your account and the service. If the connection is unsuccessful, an error message will be displayed. Once confirmed, this screen indicates that your account is verified. You can then poll the job after clicking "Done," which will redirect you back to your client application. 

```erlang URL
https://example./account-verification?jobId=d684c882-fb9c-4284-98a0-d3b65334922e&jobIds=d684c882-fb9c-4284-98a0-d3b65334922e
```

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/40504ba-image.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


<br />

## Basiq's Starter Kits

[Our starter kits](https://api.basiq.io/docs/starter-kit-account-verification) simplify the integration process. We've already set up the API for you, following best practices. This means you can quickly start without worrying about the technical details.

### IAV Tutorial

Check out our [Account Verification (IAV)](doc:starter-kit-account-verification) tutorial to see how the the account verification starter-kit works. This app is for testing and use sandbox accounts only.

### Customising Your App

You can easily customise the starter kit to match your brand. Just update the colors and fonts in the configuration files, and replace the logos with your own to maintain a consistent brand image.

### Following Best Practices

Our starter kits follow Basiq's best practices, ensuring:

- Secure handling of tokens.
- Efficient processing of tasks.
- Clear consent flow and trust-building measures.
- Use of modern technology.

### Complete Demo

[block:html]
{
  "html": "<div style=\"position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;\"><iframe src=\"https://demo.arcade.software/PMpsn5g5aMhHzqn3ApMe?embed\" title=\"Account Name Validation Demo\" frameborder=\"0\" loading=\"lazy\" webkitallowfullscreen mozallowfullscreen allowfullscreen allow=\"clipboard-write\" style=\"position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;\"></iframe></div>"
}
[/block]


> 👍 Tutorial
> 
> [Account Verification. ](https://api.basiq.io/docs/starter-kit-account-verification)