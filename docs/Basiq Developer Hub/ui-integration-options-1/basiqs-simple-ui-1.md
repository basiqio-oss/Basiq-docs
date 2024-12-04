---
title: Basiq's simple UI
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
The Basiq Connect Control is a UI component that allows applicants to securely connect their bank accounts. It's written in React, however it exposes a vanilla JavaScript interface ensuring it can be used across all frameworks. You can see an example of how it looks in production here: 
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7597e9e-ezgif.com-gif-maker.gif",
        "ezgif.com-gif-maker.gif",
        800,
        419,
        "#f9fafc"
      ]
    }
  ]
}
[/block]
## Installation 
Regardless of the JS framework you are using (Angular, VueJS), you will need to install `react` and `react-dom`.

Install `basiq-connect-control` and it's dependencies:

`$ npm install react react-dom`
`$ npm install @basiq/basiq-connect-control`
[block:callout]
{
  "type": "info",
  "title": "Optional",
  "body": "If you are concerned about your app supporting Internet Explorer you may also install polyfill libraries such as `core-js` and `react-app-polyfill`."
}
[/block]
## Usage

The package exports a single function which takes a config object as a parameter. Calling this function will render the bank picker to the user.

### Where to call `BasiqConnect()`

If you’re using vanilla JavaScript, you can call `BasiqConnect()` anywhere after the host DOM element is loaded. If you are using React to build your application you should call it either in `componentDidMount`, or, if you are using React Hooks, in `useEffect`.
[block:code]
{
  "codes": [
    {
      "code": "import React, { useEffect } from 'react';\nimport BasiqConnect from \"@basiq/basiq-connect-control\"\n\nexport const BasiqConnectModal = (() => {\n  let config = {\n    containerId: \"basiq-control\",\n  \tuserID: userId,\n    token: access_token\n  }\n  \n  useEffect(() => {\n          BasiqConnect(config)\n      }, [])\n      \n      return <div id=\"basiq-control\"></div>\n})",
      "language": "javascript",
      "name": "Rendering the BasiqConnect UI"
    }
  ],
  "sidebar": true
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "A common place for the BasiqConnect picker is in a modal, attaching the open method to a button such as “Connect your accounts”."
}
[/block]
### The config object 

A number of parameters can be passed through the config object. Most are optional values however authentication params are required and can be provided by:

- Sending the `userId` and `access_token`, which can be obtained via the BasiqAPI (See the [quick start guide](https://api.basiq.io/docs/getting-started-1)); or

- Sending the `connectLinkId`, which can be obtained from the [auth_link endpoint](https://api.basiq.io/reference#auth-links) 
[block:code]
{
  "codes": [
    {
      "code": "{\n    // required fields\n    containerId: String, // ID of the DOM element to which Basiq Connect Control will be rendered; \n\n    // and either\n    token: String, // CLIENT_ACCESS scope \n    userID: String, \n    // or\n    connectLinkId: String, \n\n    // optional fields\n    upload: Boolean, // should uploading statements be enabled\n    connect: Boolean, // should connecting to bank with credentials be enabled\n    companyName: String, // company name to be shown, will default to Basiq Dashboard name \n    regionOfInstitutions: String, // valid values: Australia, New Zealand\n    hideTestBanks: Boolean, // should test banks (Basiq, Hooli) be hidden from user\n    hideBetaBanks: Boolean // should beta banks be hidden from user\n}",
      "language": "json",
      "name": "The config object"
    }
  ],
  "sidebar": true
}
[/block]

[block:callout]
{
  "type": "warning",
  "title": "Handling Jobs",
  "body": "A connection is created via the Basiq UI control when a user submits their login credentials. This kicks off a job in the background and triggers a custom `jobCreated` event in the browser, passing your application that `jobId`. If you want to subscribe to this event, you just need to add a listener to subscribe to it. \n\nYou can now poll the `jobs/{jobId} `endpoint to check the status of each step: \n```\nconst handleNewJob = async (event) => {\n  let jobId = await event.detail.id;\n  pollJob(jobId)\n}\n\nwindow.addEventListener(\"jobCreated\", handleNewJob);\n```\nThis allows you to:  \n\n- Perform actions as soon as the step you rely on is complete without waiting for the following steps,\n- Allow your user to carry on with their flow, keeping them engaged, and\n- **Effectively manage any failed jobs**, which is crucial to your application. See the best practices for managing failed jobs."
}
[/block]
And that’s it, Basiq now handles all the connections within that UI component!
[block:callout]
{
  "type": "info",
  "title": "Source code",
  "body": "You can check out the [Github repo](https://github.com/basiqio/basiq-connect-control) and our [NPM registry](https://www.npmjs.com/package/@basiq/basiq-connect-control) for more info."
}
[/block]