---
title: 'Quickstart: code free'
excerpt: >-
  No programming experience? No worries! Get a feel for the full suite of Basiq
  products without writing a single line of code thanks to our Postman
  collection.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
<img align="left" src="https://files.readme.io/1a04ca3-Group_1496.svg" >
<br />
<br />

The following guide will help you to get up and running with the Basiq API without writing any application code. It uses [Postman](https://www.postman.com) and is suitable for both technical and non-technical audiences.

If you would prefer to integrate your application with the API directly, and aren't afraid to get your hands dirty writing some code, you might be more interested in our [Quickstart](https://api.basiq.io/docs/quickstart-part-1).
[block:callout]
{
  "type": "warning",
  "body": "Postman is an API development tool which gives users a platform to make requests to any API. It's often used by developers to test out their own API's, however many of their consumers come from a non-technical background wanting to interact with a public API. We have curated a Postman collection for this use case, which features all of our API endpoints and makes it simple to get up and running using the platform. \n\nIf you don't already have the app you can [download it here.](https://www.getpostman.com/downloads)",
  "title": "Postman app required"
}
[/block]
## STEP 1: Register
<img align="left" src="https://files.readme.io/546c6d2-Group_7_1.svg" >
<br />
<br />

Register your application via our [dashboard](https://dashboard.basiq.io/) and create a new API key under the Developers tab.
<br />
[block:callout]
{
  "type": "info",
  "body": "You can create as many API keys as you want, which allows you to use keys across different applications and environments. It’s a good idea to give each API key a meaningful name in order to differentiate between them.\n\nMake sure you copy and save the key we give you straight away, as it will only be exposed it in full once. Your API keys carry many privileges, so be sure to keep them secret!",
  "title": "API Keys"
}
[/block]
## STEP 2: Grab our sample code
<img align="left" src="https://files.readme.io/546c6d2-Group_7_1.svg" >
<br />
<br />

Go to [our sample code](https://documenter.getpostman.com/view/2889361/S1LyVTQP?version=latest) (also known as the Postman Collection) and click Run in Postman:
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d674435-postmanstep7.png",
        "postmanstep7.png",
        1228,
        592,
        "#a5a4a3"
      ],
      "sizing": "80"
    }
  ]
}
[/block]
*Make sure you select the Postman app that was installed earlier (the option will display your operating system, e.g. Mac/Windows).* 
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4f282a8-postmanStep8",
        "postmanStep8",
        810,
        558,
        "#f9f7f7"
      ],
      "sizing": "80"
    }
  ]
}
[/block]
## STEP 3: Authenticate

<img align="left" src="https://files.readme.io/546c6d2-Group_7_1.svg" >
<br />
<br />
<br />
In Postman click on the menu options [ 1 ], [ 2 ], [ 3 ] & [ 4 ]

[ 5 ] Then replace XXXXXX with the API Key you generated via the dashboard in Step 1

[ 6 ] Click Save
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/07eec60-postmanstep9.png",
        "postmanstep9.png",
        2566,
        1348,
        "#e9e8e9"
      ],
      "sizing": "80"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "Don't forget: Your access token will expire every 60 minutes, so refresh as you need to.",
  "title": "Your access token will last an hour"
}
[/block]
#### Testing the collection

Before you start making calls to the API, it's a good idea to run the tests to ensure everything is in working order.

To run the tests, simply click Run from the collection menu:
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4ec6f15-postmanstep10.png",
        "postmanstep10.png",
        2566,
        1348,
        "#e8e8e8"
      ],
      "sizing": "80"
    }
  ]
}
[/block]
The Collection Runner window will open. Click Run:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/105b527-postmanstep11.png",
        "postmanstep11.png",
        2560,
        1600,
        "#ebebec"
      ],
      "sizing": "80"
    }
  ]
}
[/block]
You will then see the results in the "Collection Runner" window.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f6c0755-postmanstep12",
        "postmanstep12",
        1600,
        1002,
        "#efefef"
      ]
    }
  ]
}
[/block]
## STEP 4: Make your calls 

&nbsp;

Basiq's full suite of products are available when you use the Postman collection, ready for you start making requests! 

In order to connect to Basiq's test banks, you will need to use the sandbox user logins. You can find the credentials for all scenarios [here](https://api.basiq.io/reference/connect). 

**Note:** You are free to make as many request as you like, however we cap the connections for sandbox users at 500 per account. If you would like to increase this quote, please email us at support@basiq.io.
[block:callout]
{
  "type": "info",
  "title": "Environment Variables",
  "body": "You will notice our Postman collection uses lots of environment variables. These are set with postman scripts and are all set automatically so you don't need to worry about copying and pasting for each request."
}
[/block]