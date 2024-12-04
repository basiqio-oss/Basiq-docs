---
title: Customise UI
excerpt: >-
  Customise your ConsentUI effortlessly to tailor the user experience according
  to your preferences and requirements.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/ORXaNWBnJhAtawgwJSu4?embed" title="Basiq - Consent UI Customisation" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

## Introduction:

Partners utilising the ConsentUI have the ability to customise various aspects of the interface through the Layout tab. This tab enables partners to adjust fonts, colors, text size, and the appearance of different elements within the ConsentUI.

## Importance:

It's important to note that these customisations are instantly applied to all screens under the consent.basiq.io domain. This includes screens related to Consent Manage, Extend, Connect, and others.

Please be aware that the **AuthUI** project screens **(found at connect.basiq.io)** are not affected by these customisation options. The changes made in the Layout tab exclusively apply to the ConsentUI.

Partners can conveniently preview the live changes they make to the ConsentUI by utilising the Dashboard's editing feature. This allows partners to visualize the modifications and ensure they meet their desired design requirements.

## Failures:

In the event of an error, such as the failure to load configuration values, the ConsentUI will gracefully fallback to default values. This ensures that the interface remains functional and consistent even if there are issues with the customisation settings.

Certain elements within the ConsentUI cannot be customised to maintain compliance. For example, the CDR logo will always remain on a white background, preserving the required branding standards.

Additional user interface (UI) elements, including shadows, divider lines, and loaders, are not customisable. However, they utilize a neutral black color with opacity. This design choice ensures that these elements stylistically blend with any color values chosen for customisation.

Icons within the ConsentUI inherit the color of their parent div. For instance, the 'info' button on the home screen will adopt the color of the paragraph text it is associated with. This behavior ensures a cohesive and consistent visual presentation throughout the interface.

Input fields within the ConsentUI inherit the 'accent' and 'inactive' color values. These fields are dynamic elements with multiple states, and their colors adapt accordingly. This design approach maintains visual harmony and provides clear visual cues to users based on the states of the input fields.

## Glimpse

This is how the customiser UI looks like, loaded with an editor on the right hand side. The details are below: 

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(54.55861070911722% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/nd6vv0GcUDqCd5BPOGqu?embed" title="Basiq - Glimpse Customise UI" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

**Analytics (GTM)**

In order to configure Google Tag Manager (GTM), the process begins with the utilisation of the Customiser feature. Through Customiser UI, partners are able to incorporate their own custom tags into the Analytics field of Google Tag Manager (GTM). This allows for a personalised and tailored tracking system.

Once the configuration is complete, additional code snippets are added to the ConsentUI. At present, the tracking setup primarily focuses on entire pages rather than individual elements such as buttons or links. This means that the tracking and analytics capabilities of the system are designed to monitor the navigation patterns of users, particularly their access to specific screens or pages.

However, it's important to note that the current setup does not include the identification of distinct actions within those pages. In other words, while the system can track user movement and interactions on a broader scale, it is unable to differentiate between different types of clicks or actions performed by users within those pages.

## Customisable fields

#### Consent Tab Settings

<Table>
  <thead>
    <tr>
      <th>
        Section
      </th>

      <th>
        Feature
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Title and Subtitle
      </td>

      <td>
        Brand name
      </td>

      <td>
        Identifies your service in the consent UI, establishing a clear brand presence for users during the consent process. This should be recognisable and consistent with your other branding.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Title
      </td>

      <td>
        Custom text fields for setting the main title hat appear in the consent UI, which can be used to communicate the purpose of the data sharing to the user effectively.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Subtitle
      </td>

      <td>
        Custom text fields for setting the subtitle that appear in the consent UI, which can be used to communicate the purpose of the data sharing to the user effectively.
      </td>
    </tr>

    <tr>
      <td>
        Purposes
      </td>

      <td>
        [Your Purpose]
      </td>

      <td>
        Defines the specific reasons for data collection. This section is to articulate the scope and intent of the data retrieval to users, ensuring transparency in data usage.
      </td>
    </tr>

    <tr>
      <td>
        [Permissions](doc:consent-scopes)
      </td>

      <td>

      </td>

      <td>
        Detailed control over the types of financial data the application will access, such as account names, balances, and transaction details. This ensures users are informed about what data is being accessed and for what purpose.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Name and occupation
      </td>

      <td>
        [Checkbox - unchecked]
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Name, occupation, contact details
      </td>

      <td>
        [Checkbox - checked]
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Organisation profile
      </td>

      <td>
        [Checkbox - unchecked]
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Organisation profile and contact details
      </td>

      <td>
        [Checkbox - unchecked]
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Account name, type and balance
      </td>

      <td>
        [Checkbox - checked]
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Account balance and details
      </td>

      <td>
        [Checkbox - checked]
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Transaction details
      </td>

      <td>
        [Checkbox - checked]
      </td>
    </tr>

    <tr>
      <td>
        Data
      </td>

      <td>
        Duration (days)
      </td>

      <td>
        Determines the validity period of user consent for data sharing. A standard setting is 365 days, but it can be adjusted according to specific business needs or regulatory requirements.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Data retrieval span (days)
      </td>

      <td>
        Specifies the extent of historical financial data that users allow to access upon giving consent. This can range from a recent few days to an extensive span of up to two years, enabling detailed financial analysis.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Retain data by default
      </td>

      <td>
        When enabled, the system will automatically retain the retrieved financial data for the set duration. This setting is essential for maintaining continuous data access for analysis without prompting users for re-consent.
      </td>
    </tr>
  </tbody>
</Table>

#### Appearance Tab Settings

<Table>
  <thead>
    <tr>
      <th>
        Section
      </th>

      <th>
        Feature
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Header Image
      </td>

      <td>
        Image selection
      </td>

      <td>
        Manage the upload and display of a custom header image for brand visibility. The recommended size for header image is 

        **1372x256**

        .
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Always display header image
      </td>

      <td>
        Check this option to always display headers on all screens.
      </td>
    </tr>

    <tr>
      <td>
        Font
      </td>

      <td>
        Font
      </td>

      <td>
        Select the font style that will be used throughout the UI, aiding in brand consistency. If you have a custom font, please contact Basiq to discuss its integration.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Primary color
      </td>

      <td>
        Use this to change primary color. E.g # 130F26
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Secondary color
      </td>

      <td>
        Use this to change secondary color. E.g # 130F26
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Inactive color
      </td>

      <td>
        Use this to change inactive color. E.g # 7F888C
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Heading size (px)
      </td>

      <td>
        Adjust the size of heading texts in pixels.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Paragraph size (px)
      </td>

      <td>
        Adjust the size of paragraph texts in pixels.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Line height (px)
      </td>

      <td>
        Adjust the height of lines in pixels for readability.
      </td>
    </tr>

    <tr>
      <td>
        Buttons
      </td>

      <td>
        Primary button
      </td>

      <td>
        Customise text and background color, along with border radius for primary buttons.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Secondary button
      </td>

      <td>
        Customise text and background color, along with border radius for secondary buttons.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Border radius (px)
      </td>

      <td>
        Customise the border radius of your buttons.
      </td>
    </tr>

    <tr>
      <td>
        Colors
      </td>

      <td>

      </td>

      <td>
        Control the UI's overall appearance, including background color and the colors used for messages indicating success, failure, or warnings.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Success
      </td>

      <td>
        \# 4FC35A
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Warning
      </td>

      <td>
        \# FABE34
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Failure
      </td>

      <td>
        \# FE493F
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Background
      </td>

      <td>
        \# FFFFFF
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Links
      </td>

      <td>
        \# 0459A8
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Accreditation
      </td>

      <td>
        \# 2784DA
      </td>
    </tr>

    <tr>
      <td>
        Wrapper
      </td>

      <td>
        Desktop width (px)
      </td>

      <td>
        Define the width of the desktop UI wrapper in pixels to ensure proper layout fitting.
      </td>
    </tr>
  </tbody>
</Table>

#### Institution Tab Settings

| Section             | Description                                                                                                                                                           |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Select all Checkbox | Facilitates the selection or deselection of all financial institutions in the list for ease of management.                                                            |
| Institution List    | A list where you can select which financial institutions will be available for users to connect with, tailored to the services and regions your application supports. |

#### Flow Tab Setting

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Section
      </th>

      <th style={{ textAlign: "left" }}>
        Feature
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Preferences
      </td>

      <td style={{ textAlign: "left" }}>
        Skip success screen
      </td>

      <td style={{ textAlign: "left" }}>
        A toggle to bypass the confirmation screen after successful consent, offering a more streamlined experience for users. Useful for repeat users who are familiar with the process and do not require additional confirmation.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        Allow multiple connections
      </td>

      <td style={{ textAlign: "left" }}>
        Permits users to connect multiple bank accounts from different financial institutions, broadening the scope of data aggregation for a more comprehensive financial overview.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        Analytics (GTM)
      </td>

      <td style={{ textAlign: "left" }}>
        This field accepts a Google Tag Manager tracking code, which allows for the collection of analytics on how users interact with the consent UI, providing insights into user behaviour and potential areas for UI improvement.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        External URLs
      </td>

      <td style={{ textAlign: "left" }}>
        Redirect URL
      </td>

      <td style={{ textAlign: "left" }}>
        The web address users will be redirected to after the consent process is completed. This URL is critical for maintaining a seamless user journey through the consent procedure, whether granting or revoking consent.
      </td>
    </tr>
  </tbody>
</Table>

## Preview Screens

The Customise UI Preview feature allows partners to view and test different ConsentUI flows within your application. Partners can preview the appearance and functionality of three specific flows: Connect, Manage, Extend.

## Available Flows

### Connect Flow (Default)

The Connect Flow is the default ConsentUI flow. It is designed to help users connect their bank accounts to your platform. It typically involves selecting financial institutions, entering credentials, and providing consent for data access. With the Customise UI Preview, you can test the appearance and functionality of this flow.

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(54.55861070911722% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/tu8WgieBNdiIE2ejHxNJ?embed" title="Basiq - Connect Flow" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

### Manage Consent

The Manage Consent Flow allows users to review and manage their existing consents. It's a user-friendly way for them to see which accounts they've connected, what data you have access to, and the ability to revoke or modify consents along with connections. The Customise UI Preview for this flow enables you to check how this management interface appears and functions.

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(54.55861070911722% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/wP7ec9EeDs6JL7zHiw9l?embed" title="Basiq - Manage Consent" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

### Extend Consent

The Extend Consent Flow is used when users need to extend or renew their consent for data access. It's an important part of maintaining data access permissions. This feature in Customise UI Preview lets you review how the extension process works and how it's presented to the users.

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(54.55861070911722% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/LJ1AcCN6PLFFpP18N0Um?embed" title="Basiq - Extend Consent Customise UI" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

## Quick Links

You can get started [here](https://dashboard.basiq.io/customise-ui) and let us know if you have any feedback for us to improve.

> ❗️ Mandatory Brand Name
>
> We've made Brand name a mandatory value for all applications, including non-Business Consumer Changes (BCC). Partners who haven't defined it yet will be prompted to do so the next time they edit ConsentUI. Once Brand Name is added, the partners are able to 'save' their consent policy in the customise UI.
