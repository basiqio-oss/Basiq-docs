---
title: Consent UI
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
For a data recipient (Basiq) to collect, use and disclose CDR data they must have consent from the consumer to do so. The Basiq Consent UI renders the defined application consent policy within a flow that aligns with the rules and requirements proposed by the CDR, and the latest CX Guidelines. *Partners wishing to access v3.0 of the Basiq API are required to use the Basiq Consent UI in their application.*

Once a user has given consent, the Consent UI flow will take them to the institution picker to continue connecting their accounts, and on completion will be redirected back to the partner application. Consumers can manage all of their provided consents through a consent dashboard owned by Basiq.
[block:callout]
{
  "type": "info",
  "body": "How the Basiq Consent UI is presented to users is defined by the applications consent policy and institutions selection. Partners can manage this in the [dashboard configuration](ref:dash-configuration).",
  "title": "Application configuration"
}
[/block]
## Basiq Consent UI flow

&nbsp;
&nbsp;
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/664ba00-Group_2674.png",
        "Group 2674.png",
        3429,
        1907,
        "#dde4e6"
      ],
      "sizing": "80"
    }
  ]
}
[/block]
&nbsp;
&nbsp;

## Using the Basiq Consent UI

The Consent UI is hosted by Basiq, so the user flow will be as follows: 

1. User is presented with the applications pre consent (**in partner app**)
2. On accepting the pre consent, partners should then redirect their users to:`https://consent.basiq.io/home?userId={{userId}}&token={{client_token_bound_to_userId}}`
3. Upon confirmation from the user they they have finished connecting their institutions, they will be redirected back to the partners application. The redirect URL can be configured via the dashboard, but will default to the origin if this is not set. 
[block:callout]
{
  "type": "warning",
  "body": "Authentication params are required and include: \n\n- `userId`, and \n- `CLIENT_SCOPE` access token. **Note:  The userId must *also* be bound to this token to access the Consent UI for security reasons**\n\nThese can be created and obtained via the Basiq API (See the [quick start guide](ref:quickstart-part-1))",
  "title": "Authentication params"
}
[/block]
## Action parameters

Partners can pass an optional `action` param for alternate flows. The action you pass will be determined by the state of the user and what the user needs to do via the Consent UI. 
[block:parameters]
{
  "data": {
    "h-0": "Action",
    "h-1": "When to use",
    "h-2": "Screen",
    "0-0": "No action parameter (default state)",
    "0-1": "Your user is **onboarding** for the first time so will need to complete the user journey from giving consent to connecting their institutions in its entirety. ",
    "1-0": "`action=manage`",
    "1-1": "Your user needs to **manage** the consent they have granted for your application. This state allows them to view and manage their current consent including the connections that have been made under this and also.\n\n*Using this action when a user does not have an active user consent will result in an error.*",
    "0-2": "**[F1]**",
    "1-2": "**[F2]**",
    "2-0": "`action=connect`",
    "2-1": "Your user already has an existing valid consent, but would like to **make additional connections**.",
    "2-2": "**[F3]**",
    "3-0": "`action=update`",
    "4-0": "`action=extend`",
    "3-2": "**Coming soon......**",
    "4-2": "**Coming soon......**",
    "3-1": "Your user needs to **update their consent** or connection details. E.g. The applications consent policy has been amended.",
    "4-1": "Your user's consent is **about to expire** and they need to extend it in order to allow your application to continue to access their data."
  },
  "cols": 3,
  "rows": 5
}
[/block]
&nbsp;
### Consent UI Actions Flow
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d07d24b-Group_2733_1.svg",
        "Group 2733 (1).svg",
        2708,
        833,
        "#ff9790"
      ],
      "sizing": "smart"
    }
  ]
}
[/block]
&nbsp;
### Alternative UI flows
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6f6b0a3-Group_2734_1.svg",
        "Group 2734 (1).svg",
        924,
        895,
        "#333333"
      ]
    }
  ]
}
[/block]