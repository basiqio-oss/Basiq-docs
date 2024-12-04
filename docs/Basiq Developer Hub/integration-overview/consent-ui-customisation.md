---
title: Consent UI Customisation
excerpt: >-
  Discover how the Consent UI from Basiq simplifies and streamlines user consent
  management for your application, ensuring seamless integration, compliance,
  and an enhanced user experience.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: getting-started
      title: Getting started
---
<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/ORXaNWBnJhAtawgwJSu4?embed" title="Basiq - Consent UI Customisation" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

## Introduction

The Consent UI is a key feature of the Basiq platform, designed to make it easy for you to get and handle user consents — a crucial part of effectively using data and payment services. It blends smoothly into your app with a simple URL redirect and offers a range of customization options through the Basiq Dashboard. With these tools, you can tailor the Consent UI to match your app's look and feel, providing a seamless and familiar experience for your users. Here is a list of features and benefit of the Consent UI:

* **Seamless Integration and Customisation**: Easily embeddable into applications via URL redirect with a customisable interface through the Basiq Dashboard, allowing for seamless integration and alignment with your application's branding.

* **Efficient Consent and Data Management**: Streamlines the process of obtaining and managing user consents in a compliant manner, while also enabling secure connectivity with financial institutions and facilitating payment setup if using Basiq payment services.

* **Enhanced User Experience and Control**: Provides a user-friendly interface that enhances the overall experience, coupled with features that allow users to view, manage, and extend their consents, offering greater transparency and control.

* **Regulatory Compliance and Data Security**: Ensures adherence to regulatory standards like the Consumer Data Rights, reducing the risk of non-compliance in data access and payment services, and upholds data security and privacy norms.

* **Time Efficiency and Market Readiness**: Reduces development time and resources by providing a ready-to-use, compliant solution, accelerating the market readiness of applications and offering developers flexibility and control over the user interface.

### Key Interfaces

The Consent UI is composed of several key screens, each designed to facilitate a different aspect of user interaction:

* **Consent Capture Screen**: This is the initial touchpoint where users are informed about the data access request. It is crucial for transparency and user trust, detailing the type of data accessed and its intended use.

* **Institution Selection Screen**: Users select their financial institution from a comprehensive list on this screen. This step is vital for establishing a secure and reliable connection for data retrieval.

* **Data Holder Screens**: These screens are controlled by the financial institutions themselves. They handle crucial steps such as user authorisation and account selection. While these screens are integral to the process, they remain under the purview of the respective financial institutions, ensuring security and compliance in user authentication and data access.

* **Consent Management Screen**: This interface allows users to view and manage their existing consents. It's a critical component for maintaining user control over their data.

* **Consent Extension Screen**: In cases where consent is nearing its expiration, this screen facilitates the extension process, ensuring uninterrupted service and data access.

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

      </td>

      <td style={{ textAlign: "left" }}>
        Reference name
      </td>

      <td style={{ textAlign: "left" }}>
        When a user attempts to cancel out of our consent UI, a confirmation pop-up appears to ensure the user intends to leave the consent process. This pop-up provides a message indicating the action the system will take if the user confirms the cancelation. For example: If the partner name is "ExamplePartner", the confirmation pop-up will now display:  

        "Are you sure you want to leave? You will be taken back to ExamplePartner."
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

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        Manage consent url
      </td>

      <td style={{ textAlign: "left" }}>
        A publicly hosted page with details on Consent management for your users.
      </td>
    </tr>
  </tbody>
</Table>

## Consent UI Integration

> 🚧 Important Notice:
>
> Embedding the Consent UI is not supported. Due to bank security policies, the Consent UI cannot be embedded using methods such as iframes. Instead, you must implement the full redirect provided by Basiq.

### Redirect Method:

To integrate the Consent UI, follow these steps to implement the full redirect:

1. **Initiate the Consent Process**: Start by creating a consent request through Basiq's API.
2. **Redirect to Consent UI**: Use the URL provided in the response to redirect the user to the Consent UI.
3. **Complete the Consent**: Once the user completes the consent process, they will be redirected back to your application with the job id's.

This approach ensures compliance with bank security requirements and maintains the integrity of the user's financial data.
