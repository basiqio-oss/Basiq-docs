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

> 📘 Application configuration
>
> How the Basiq Consent UI is presented to users is defined by the applications consent policy and institutions selection. Partners can manage this in the [dashboard configuration](ref:dash-configuration).

## Basiq Consent UI flow

 \
 

<Image width="80%" src="https://files.readme.io/664ba00-Group_2674.png" />

 \
 

## Using the Basiq Consent UI

The Consent UI is hosted by Basiq, so the user flow will be as follows: 

1. User is presented with the applications pre consent (**in partner app**)
2. On accepting the pre consent, partners should then redirect their users to:`https://consent.basiq.io/home?userId={{userId}}&token={{client_token_bound_to_userId}}`
3. Upon confirmation from the user they they have finished connecting their institutions, they will be redirected back to the partners application. The redirect URL can be configured via the dashboard, but will default to the origin if this is not set. 

> 🚧 Authentication params
>
> Authentication params are required and include: 
>
> * `userId`, and 
> * `CLIENT_SCOPE` access token. **Note:  The userId must*also* be bound to this token to access the Consent UI for security reasons**
>
> These can be created and obtained via the Basiq API (See the [quick start guide](ref:quickstart-part-1))

## Action parameters

Partners can pass an optional `action` param for alternate flows. The action you pass will be determined by the state of the user and what the user needs to do via the Consent UI. 

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Action
      </th>

      <th style={{ textAlign: "left" }}>
        When to use
      </th>

      <th style={{ textAlign: "left" }}>
        Screen
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        No action parameter (default state)
      </td>

      <td style={{ textAlign: "left" }}>
        Your user is **onboarding** for the first time so will need to complete the user journey from giving consent to connecting their institutions in its entirety. 
      </td>

      <td style={{ textAlign: "left" }}>
        **[F1]**
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `action=manage`
      </td>

      <td style={{ textAlign: "left" }}>
        Your user needs to **manage** the consent they have granted for your application. This state allows them to view and manage their current consent including the connections that have been made under this and also.

        *Using this action when a user does not have an active user consent will result in an error.*
      </td>

      <td style={{ textAlign: "left" }}>
        **[F2]**
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `action=connect`
      </td>

      <td style={{ textAlign: "left" }}>
        Your user already has an existing valid consent, but would like to **make additional connections**.
      </td>

      <td style={{ textAlign: "left" }}>
        **[F3]**
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `action=update`
      </td>

      <td style={{ textAlign: "left" }}>
        Your user needs to **update their consent** or connection details. E.g. The applications consent policy has been amended.
      </td>

      <td style={{ textAlign: "left" }}>
        **Coming soon......**
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `action=extend`
      </td>

      <td style={{ textAlign: "left" }}>
        Your user's consent is **about to expire** and they need to extend it in order to allow your application to continue to access their data.
      </td>

      <td style={{ textAlign: "left" }}>
        **Coming soon......**
      </td>
    </tr>
  </tbody>
</Table>

 

### Consent UI Actions Flow

<Image width="smart" src="https://files.readme.io/d07d24b-Group_2733_1.svg" />

 

### Alternative UI flows

![924](https://files.readme.io/6f6b0a3-Group_2734_1.svg "Group 2734 (1).svg")
