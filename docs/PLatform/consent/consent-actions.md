---
title: Consent Actions
excerpt: Consent Actions in Basiq Consent UI
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Create Consent (No action parameter or action=null)

This is the default flow for first-time onboarding or for users without existing valid consent. It involves the user consenting to connect their financial institutions and sharing data. No specific action parameter is needed in the URL.

In the default onboarding flow, users without prior consent or existing valid connections are required to provide their consent. This process is facilitated through the Basiq Consent UI, which is initialised without a specific action parameter (action=null or no action). This default mode is designed for new user onboarding where initial consent to connect to financial institutions is required.

### When `action=null` is Triggered

The `action=null` parameter, or the absence of an action parameter in the URL, signifies that the Consent UI should open in its default state, which is designed for first-time user consent. This parameter is used in the following scenarios:

1. **New User Onboarding**: When a user is newly created and has not yet provided any consent to access their financial data.
2. **Re-consenting**: If previous consents have expired or become invalid, and the user needs to consent again to continue accessing their financial data.

### Implementing Default Consent Flow

To implement this flow, you must redirect the user to the Basiq Consent UI with a URL formatted as follows:

```json URL
window.location = `https://consent.basiq.io/home?token={{client_token_bound_to_userId}}&action=null`;
```

Here, `{{client_token_bound_to_userId}}` should be replaced with the actual client token that is bound to the user’s ID. This token is important as it authenticates the user’s session in the Consent UI.

### Example Use Case

* **Scenario**: You have just created a user via the Basiq API using your server token and then obtained a client token bounded with that created user. The next step is to initiate the consent process to allow the user to connect their financial accounts.
* **Action**: Redirect the user to the Consent UI using the URL format specified above. This initiates the default consent flow where the user can authorise the connection to their financial institutions.

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/y4I4runGiUDlzUVZO90r?embed" title="Basiq Consent | action=null" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

## Connect Institutions (action=connect)

If a user already has valid consent, they can directly add more financial institutions without needing to provide additional consent.

### When to Use `action=connect`

The `action=connect` parameter is beneficial in the following situations:

1. **Existing Consent**: When a user already has valid consent established for accessing their financial data.
2. **Adding Connections**: If users wish to add more connections to their existing set of connected financial institutions without re-consenting.

### Implementing action=connect

To implement this flow, redirect the user to the Consent UI with the following URL format:

```json URL
window.location = `https://consent.basiq.io/home?token={{client_token_bound_to_userId}}&action=connect`;
```

Replace `{{client_token_bound_to_userId}}` with the actual client token bound to the user's ID, ensuring proper authentication of the user's session in the Consent UI.

### Example Use Case

* **Scenario**: A user who has previously consented to connect their primary bank account now wishes to add connections from other financial institutions without having to re-consent.
* **Action**: Redirect the user to the Consent UI using the URL format specified above, including the `action=connect` parameter. This allows the user to bypass the consent step and directly proceed to adding additional connections.

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/65BYh2YL4VuCBy5Kqaqz?embed" title="Basiq | action=manage" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

### Alternative Approach

Alternatively, users can utilise the flow tab feature within the Customise UI to enable multiple connections from different financial institutions.

#### How to Enable Allow Multiple Connections

The docs on enabling the "Allow Multiple Connections" flow tab feature within the Customise UI can be found [here](https://api.basiq.io/docs/consent-ui-customisation). This customisation option allows users to connect multiple bank accounts from different financial institutions within the same session, streamlining the process of aggregating financial data.

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/LIYnWtOVoK6fI9g4gj32?embed" title="Basiq - Dashboard" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

<br />

> 👍 This skips re-consenting and moves directly to connecting institutions.

## Manage Consent (action=manage)

Allows users to view and manage their existing consents, including details about expiry and connected institutions. Users can delete connections individually or revoke consent entirely.

### When to Use action=manage

The `action=manage` parameter is useful when users wish to:

* **View Consent Details**: Users want to review their current consent status, including expiry dates and connected institutions.
* **Manage Connections**: Users desire to delete specific connections or revoke consent entirely from your organisation.

### Implementing action=manage

To implement this functionality, redirect the user to the Consent UI with the following URL format:

```json URL
window.location = `https://consent.basiq.io/home?token={{client_token_bound_to_userId}}&action=manage`;
```

Replace `{{client_token_bound_to_userId}}` with the actual client token bound to the user's ID, ensuring proper authentication of the user's session in the Consent UI.

### Example Use Case

* **Scenario**: A user wishes to review their current consent settings and manage the connections they have authorised.
* **Action**: Redirect the user to the Consent UI using the URL format specified above, including the `action=manage` parameter. This allows the user to access a screen where they can view their consent details and manage their connections.

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/Wad1ic93gwfM3NQFdMJ3?embed" title="Basiq | action=manage" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

### Consent History

On the Consent Management screen, you can now view the history of previously expired/revoked consents. Additionally, if you trigger action=manage with no active consent, a list of all previously revoked or expired consents will be displayed.

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/RT2oVGipLNLvmhDwgksF?embed" title="action=manage | List of expired/revoked consents" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

### Customised UI: Manage Consent URL Field

In the customised UI's Flow tab, a new field called "Manage Consent URL" has been introduced. This field allows customers to provide a URL that directs consumers to detailed instructions on how they can revoke their consent. Ensuring this URL is populated is crucial for compliance and enhances the consumer experience by clearly outlining the steps to manage consent.

<Image align="center" src="https://files.readme.io/3dbb584-Screenshot_2024-06-12_at_3.06.02_PM.png" />

### Functionality

**When the "Manage Consent URL" field is populated**:

* **Consumer Experience**: On the consent UI screen, under the "Manage your data sharing" section, consumers will see the message: "You can revoke your consent at any time by following these instructions." This message will include a link to the provided URL, directing consumers to the customer's guide on revoking consent.

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/5CZ5ezxsyJsXtqysLypS?embed" title="Basiq - Manage Consent URL " frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

**When the "Manage Consent URL" field is not populated:**

* **Default Message**: Consumers will see the default message: "You can revoke your consent at any time by visiting the settings area."

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/mlUzYryo7DgdEGQIGghv?embed" title="Basiq - Manage consent URL" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

### Guidelines for Partners

Partners are responsible for creating and maintaining the guide linked through the "Manage Consent URL." The following points outline what the guide should include:

* **Accessibility**: The guide should be easy to find for consumers and available as a public page so that users can read it before giving consent.
* **Content Requirements**: 
  * Clearly describe the process for revoking consent.
  * Provide direct access to consent management functionalities.
  * Ensure the instructions are straightforward and easy to follow.
* **Compliance Adherence**:
  * The guide must comply with CDR rules regarding the handling of CDR data post-consent expiry/revoke.
  * Any amendments or revoking of consent must be communicated to Basiq through the relevant API calls if the Consent UI action is set to "manage."

Partners should ensure that the guide is effective, functional, and user-friendly.

> 📘 Additional Support
>
> For any questions or further clarification, customers can reach out to their account manager or contact our support team. Partners are also welcome to submit their guides for review to ensure they meet the required standards.

## Extend Consent (action=extend)

Used when the user's consent is nearing expiry. This action extends the duration of consent so that the application can continue accessing the user's data.

### When to Use action=extend

The `action=extend` parameter is appropriate when:

* **Consent Expiration**: A user's consent is nearing its expiration date, and they need to extend it to maintain uninterrupted access to their financial data.
* **Application Requirement**: Your application requires ongoing access to the user's financial data, and their consent needs to be extended to ensure continuity.

### Implementing action=extend

To implement consent extension, redirect the user to the Consent UI with the following URL format:

```json
window.location = `https://consent.basiq.io/home?token={{client_token_bound_to_userId}}&action=extend`;
```

Replace `{{client_token_bound_to_userId}}` with the actual client token bound to the user's ID, ensuring proper authentication of the user's session in the Consent UI.

### Example Use Case

#### Scenario:

Max, a user of your financial management application, receives a notification that his consent for accessing financial data is due to expire soon. He wants to extend his consent to ensure uninterrupted access to his financial information.

#### User Interaction:

1. **Notification**: Max receives a notification within the application informing him that his consent is nearing expiry.
2. **Consent Management**: Max clicks on the provided link to manage his consent settings.
3. **Consent Extension**: In the Consent UI, Max selects the option to extend his consent. Upon confirming, Max's consent is extended for an additional period.
4. **Confirmation**: Max receives a confirmation message indicating that his consent has been successfully extended and the new expiration date.

#### Customisation:

* **Duration Configuration**: As a developer, you have configured the consent extension duration to be X days from the current date using the Customise UI.
* **Data Retrieval Span**: Additionally, you have set the data retrieval span to be 730 days from the current date to retrieve transaction data for a sufficient historical period.

Both of these elements, the duration of consent extension and the duration for data retrieval, can be configured from the Customize UI. On the right side, under "Consent" > "Data", you can adjust the durations in days for both consent extension and data retrieval span. Detailed instructions on customising these elements can be found [here](https://api.basiq.io/docs/consent-ui-customisation).

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/Whbv6znUNLivsS16J9Yr?embed" title="Basiq | action=extend" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

<br />

> ❗️ An error occurs if this action is used without active user consent.

## Update Consent (action=update)

Necessary when there are changes to the consent policy that require users to re-authorise. This might happen if there's an increase in the scope of data access needed by the application. Old consents are revoked, and connections are deleted, prompting users to consent a new under the updated terms.

### When to Use action=update

The `action=update` parameter is suitable when:

* **Consent Policy Amendment**: The application's consent policy has been updated, either due to changes in scope or other policy amendments.
* **Re-Authorisation Required**: Users need to re-authorise their consent to align with the updated consent policy.

### How It Works

* **Initiating action=update**: When initiating the action=update, the current consent policy on the application is compared with the active consent.
* **Policy Comparison**: If the consent policy remains the same, the process automatically falls back to action=extend, which extends the existing consent.
* **Scope Changes**: If the scopes in the consent policy have changed, users are prompted to re-consent, agreeing to the updated consent.
* **Re-Consent Implications**: During the re-consent process, the old consent is revoked, resulting in the deletion of all existing connections. Previously connected institutions are displayed prominently for the user's reference.

> ❗️ Note
>
> Using action=update when a user does not have active consent will result in an error. Ensure that users have provided consent before attempting to update it.Be aware that executing this action will result in the revocation of all existing connections.

## Reauthorise Consent (action=reauthorise)

Enhances user experience by addressing expiring connections. It focuses on extending the consent duration for connections that are about to expire soon. Includes functionality such as the "Renew" button, which helps prolong the connection without changing Basiq account IDs.

> ⚠️ Expiring Soon Connections
>
> For open banking type connections with an expiryDate less than 7 days away, they will be categorised under the 'Expiring soon' section, and a 'Renew' button will be visible as per the below screenshot.

### When to Use action=Reauthorise

After initiating a consent extension using action=extend, users need to reauthorise their connections with individual data holders to ensure continuity in data access. In this context, `action=reauthorise` facilitates the reauthorisation process specifically for each data holder.

To trigger the reauthorisation process, users can follow these steps:

* **Identify Expiring Connections**: Users can identify connections with expiry dates less than 7 days away, categorised under the "Expiring soon" section in the Basiq platform.
* **Click Renew Button**: Upon identifying an expiring connection, users can click the "Renew" button associated with that connection.
* **Initiate Authorisation Flow**: Clicking the "Renew" button redirects users to the data holder's platform to extend the duration of their connections for the currently shared accounts.

### Implementing Action=Reauthorise

To implement the reauthorisation flow using `action=reauthorise`, follow these steps:

* Redirect the user to the Consent UI with the appropriate URL format.
* Include the `action=reauthorise` parameter in the URL to trigger the reauthorisation process.

```json URL
window.location = `https://consent.basiq.io/home?token={{client_token_bound_to_userId}}&action=reauthorise`;
```

Replace `{{client_token_bound_to_userId}}` with the actual client token bound to the user's ID, ensuring proper authentication of the user's session in the Consent UI.

### Authorisation Flow for Extension

During the authorisation renewal process, users may observe a minor modification in the flow. Data holders will pre-select the accounts that users are currently sharing, streamlining the reauthorisation process. However, it's essential to note that this process may vary among different data holders.

### Post-Renewal Account IDs

After following the renewal flow, users can rest assured that the Basiq account IDs on their side will remain unchanged. Users can continue accessing their financial data using the same account IDs after the renewal process, ensuring continuity and consistency in data access.

### Close Button Functionality

The "Close" button within the reauthorisation flow navigates users to the redirect URL page. If the redirect URL isn’t defined in the application configuration, the button remains invisible. The URL includes any state parameter provided, as well as jobId and jobIds values cached from authorisations done during the session.

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/B08VfAgCBF2Aa90rvdXH?embed" title="Basiq | action=reauthorise" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

### Alternative: ConnectionId Parameter for Reauthorisation

In situations where users need to renew authorization for specific connections without waiting for the default 7-day expiry period, the connectionId parameter offers a direct and immediate solution. This parameter allows users to initiate reauthorisation for individual connections seamlessly within the Basiq Consent UI.

#### URL Structure

To utilise the `connectionId` parameter for reauthorisation, construct the Basiq Consent URI with the following structure:

```json URL
https://consent.basiq.io/home?&token=${token}&connectionId=${connectionId}
```

#### Implementation Steps

* **Retrieve Connection ID**: Obtain the specific connectionId associated with the connection that requires reauthorisation. This ID uniquely identifies the connection within the Basiq platform.
* **Construct URL**: Use the obtained connectionId to construct the Consent UI URL, ensuring to include the user's authentication token (token) for proper session authentication.
* **Redirect User**: Redirect the user to the constructed URL, initiating the reauthorisation process for the specified connection directly within the Consent UI.

> 👍 Notes:
>
> These actions can be initiated by appending the appropriate action parameter in the Basiq Consent UI URL, providing a seamless way to manage user consents and data connections through the platform.
