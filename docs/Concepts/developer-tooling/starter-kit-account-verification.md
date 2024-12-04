---
title: Pending and Posted Transaction
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
        "https://files.readme.io/2dcf482-DevHub_StarterKit_1080x800.png",
        "2dcf482-DevHub_StarterKit_1080x800.png",
        1080,
        700,
        "#000000"
      ],
      "sizing": "original"
    }
  ]
}
[/block]
Basiq's starter kits were created to **accelerate time to production**. We’ve done the full API integration and user flow, closely following all our best practices, so partners can focus on their innovation. Focusing on both user- and developer- experience, the app is easily tailored to create a native user experience that aligns with any application's product and brand guidelines, and can be used standalone, incorporated into your own application, or simply as reference code for **what "great" looks like**. 

## Account Verification
[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FAsQl_IlcWRM%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DAsQl_IlcWRM&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FAsQl_IlcWRM%2Fhqdefault.jpg&key=f2aa6fc3595946d0afc3d76cbbd25dc3&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=AsQl_IlcWRM",
  "title": "Basiq's account verification starter kit",
  "favicon": "https://www.google.com/favicon.ico",
  "image": "https://i.ytimg.com/vi/AsQl_IlcWRM/hqdefault.jpg"
}
[/block]
Integrating with the Basiq API means account verification can become seamless, and more secure, as the data is coming direct from the bank. It also allows partners to: 

- Reduce application abandonment through streamlined customer onboarding and a faster, more effective account verification process.
- Instantly verify ID and accounts for deposits and withdrawals
- Create authentic eye catching user experiences by surfacing and displaying things like bank balances within your solution
- Cut out time-consuming, cumbersome merchant processes with real-time access to financial data. 

The **Account Verification** Starter Kit is a template project that partners can use to generate their own project  get to market - fast. **All you need is your API key to spin up a fully functional account verification app.** Check it out [here](https://github.com/basiqio/account-verification-API-v3.0). 

# Style and brand configuration
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f9a1157-Group_2682.png",
        "Group 2682.png",
        1920,
        2375,
        "#817fbb"
      ],
      "sizing": "smart"
    }
  ]
}
[/block]

[block:parameters]
{
  "data": {
    "0-0": "Brand colours and typeface",
    "0-1": "Our starter kits are configurable to fit all brand guidelines, mainly by updating the `tailwind.config.js` with your brands colours and typeface. *Importing fonts can be done via `styles.css`*",
    "1-1": "You'll also want to replace the following logos with your own, maintaining the naming convention: \n- `public/product-logo-full.svg`\n- `public/product-logo-square.svg`",
    "2-1": "All product specific copy is noted as `PRODUCT_COPY` - in order to highlight exactly what should be updated based on your applications intentions and value proposition.",
    "1-0": "Logos",
    "2-0": "Copy",
    "h-0": "Config"
  },
  "cols": 2,
  "rows": 3
}
[/block]

# Gold standard

Our starter kits maintain all of the [Basiq best practices](https://api.basiq.io/docs/best-practices) around areas such as: 

- Token management
- Job handling - both happy and unhappy paths
- Strong pre consent flow - Clearly defined **value proposition** and a focus on **building trust**
-  *& more.. *

As well as being built on a **modern tech stack** using React, Next.js and Tailwind. 


### Check out our sample apps! 

Real life examples of how the starter kits look *and* feel. Check them out [here](https://av-demo.basiq.io/). 

[block:callout]
{
  "type": "info",
  "title": "Sample apps will only work for test banks and sandbox accounts",
  "body": "**We have disabled connecting to live banks for our sample apps.** You can login to our test banks using all of the sandbox credentials (for both happy and unhappy path scenarios) found [here](https://api.basiq.io/reference/testing#unhappy-path-test-users). *We recommend using Hooli bank for testing*"
}
[/block]
# Spinning up the starterKit **under 5 mins**

When developers start a new project, they often begin by using a starter kit or demo app as a foundation for their work. This starting point provides a pre-existing code base, which can be tailored to fit their specific needs. To use this code base, the developer needs to make a copy of it, either by downloading it from a repository or cloning it from a version control system. 

Here's a demo of how to spin up the starterKit in under 5 mins. 
[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FBljMvHvYckM%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DBljMvHvYckM&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FBljMvHvYckM%2Fhqdefault.jpg&key=f2aa6fc3595946d0afc3d76cbbd25dc3&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=BljMvHvYckM",
  "title": "Basiq Starter Kits - Developer demo",
  "favicon": "http://www.google.com/favicon.ico",
  "image": "https://i.ytimg.com/vi/BljMvHvYckM/hqdefault.jpg"
}
[/block]

[block:callout]
{
  "type": "success",
  "title": "Quick Links",
  "body": "* [Live Application](https://av-demo.basiq.io/) to test out\n* [Public Git Repo](https://github.com/basiqio/account-verification-API-v3.0) for your use\n* [Test Credentials](https://api.basiq.io/reference/testing) for our Sandbox users"
}
[/block]
:wrench: Questions? Please reach out to [support@basiq.io](mailto:support@basiq.io).