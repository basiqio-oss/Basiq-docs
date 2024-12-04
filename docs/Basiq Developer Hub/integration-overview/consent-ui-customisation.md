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
[block:html]
{
  "html": "<div style=\"position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;\"><iframe src=\"https://demo.arcade.software/ORXaNWBnJhAtawgwJSu4?embed\" title=\"Basiq - Consent UI Customisation\" frameborder=\"0\" loading=\"lazy\" webkitallowfullscreen mozallowfullscreen allowfullscreen allow=\"clipboard-write\" style=\"position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;\"></iframe></div>"
}
[/block]


## Introduction

The Consent UI is a key feature of the Basiq platform, designed to make it easy for you to get and handle user consents — a crucial part of effectively using data and payment services. It blends smoothly into your app with a simple URL redirect and offers a range of customization options through the Basiq Dashboard. With these tools, you can tailor the Consent UI to match your app's look and feel, providing a seamless and familiar experience for your users. Here is a list of features and benefit of the Consent UI:

- **Seamless Integration and Customisation**: Easily embeddable into applications via URL redirect with a customisable interface through the Basiq Dashboard, allowing for seamless integration and alignment with your application's branding.

- **Efficient Consent and Data Management**: Streamlines the process of obtaining and managing user consents in a compliant manner, while also enabling secure connectivity with financial institutions and facilitating payment setup if using Basiq payment services.

- **Enhanced User Experience and Control**: Provides a user-friendly interface that enhances the overall experience, coupled with features that allow users to view, manage, and extend their consents, offering greater transparency and control.

- **Regulatory Compliance and Data Security**: Ensures adherence to regulatory standards like the Consumer Data Rights, reducing the risk of non-compliance in data access and payment services, and upholds data security and privacy norms.

- **Time Efficiency and Market Readiness**: Reduces development time and resources by providing a ready-to-use, compliant solution, accelerating the market readiness of applications and offering developers flexibility and control over the user interface.

### Key Interfaces

The Consent UI is composed of several key screens, each designed to facilitate a different aspect of user interaction:

- **Consent Capture Screen**: This is the initial touchpoint where users are informed about the data access request. It is crucial for transparency and user trust, detailing the type of data accessed and its intended use.

- **Institution Selection Screen**: Users select their financial institution from a comprehensive list on this screen. This step is vital for establishing a secure and reliable connection for data retrieval.

- **Data Holder Screens**: These screens are controlled by the financial institutions themselves. They handle crucial steps such as user authorisation and account selection. While these screens are integral to the process, they remain under the purview of the respective financial institutions, ensuring security and compliance in user authentication and data access.

- **Consent Management Screen**: This interface allows users to view and manage their existing consents. It's a critical component for maintaining user control over their data.

- **Consent Extension Screen**: In cases where consent is nearing its expiration, this screen facilitates the extension process, ensuring uninterrupted service and data access.

#### Consent Tab Settings

| Section                           | Feature                                  | Description                                                                                                                                                                                                                      |
| --------------------------------- | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Title and Subtitle                | Brand name                               | Identifies your service in the consent UI, establishing a clear brand presence for users during the consent process. This should be recognisable and consistent with your other branding.                                        |
|                                   | Title                                    | Custom text fields for setting the main title hat appear in the consent UI, which can be used to communicate the purpose of the data sharing to the user effectively.                                                            |
|                                   | Subtitle                                 | Custom text fields for setting the subtitle that appear in the consent UI, which can be used to communicate the purpose of the data sharing to the user effectively.                                                             |
| Purposes                          | [Your Purpose]                           | Defines the specific reasons for data collection. This section is to articulate the scope and intent of the data retrieval to users, ensuring transparency in data usage.                                                        |
| [Permissions](doc:consent-scopes) |                                          | Detailed control over the types of financial data the application will access, such as account names, balances, and transaction details. This ensures users are informed about what data is being accessed and for what purpose. |
|                                   | Name and occupation                      | [Checkbox - unchecked]                                                                                                                                                                                                           |
|                                   | Name, occupation, contact details        | [Checkbox - checked]                                                                                                                                                                                                             |
|                                   | Organisation profile                     | [Checkbox - unchecked]                                                                                                                                                                                                           |
|                                   | Organisation profile and contact details | [Checkbox - unchecked]                                                                                                                                                                                                           |
|                                   | Account name, type and balance           | [Checkbox - checked]                                                                                                                                                                                                             |
|                                   | Account balance and details              | [Checkbox - checked]                                                                                                                                                                                                             |
|                                   | Transaction details                      | [Checkbox - checked]                                                                                                                                                                                                             |
| Data                              | Duration (days)                          | Determines the validity period of user consent for data sharing. A standard setting is 365 days, but it can be adjusted according to specific business needs or regulatory requirements.                                         |
|                                   | Data retrieval span (days)               | Specifies the extent of historical financial data that users allow to access upon giving consent. This can range from a recent few days to an extensive span of up to two years, enabling detailed financial analysis.           |
|                                   | Retain data by default                   | When enabled, the system will automatically retain the retrieved financial data for the set duration. This setting is essential for maintaining continuous data access for analysis without prompting users for re-consent.      |

#### Appearance Tab Settings

| Section      | Feature                     | Description                                                                                                                                                         |
| ------------ | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Header Image | Image selection             | Manage the upload and display of a custom header image for brand visibility. The recommended size for header image is **1372x256**.                                 |
|              | Always display header image | Check this option to always display headers on all screens.                                                                                                         |
| Font         | Font                        | Select the font style that will be used throughout the UI, aiding in brand consistency. If you have a custom font, please contact Basiq to discuss its integration. |
|              | Primary color               | Use this to change primary color. E.g # 130F26                                                                                                                      |
|              | Secondary color             | Use this to change secondary color. E.g # 130F26                                                                                                                    |
|              | Inactive color              | Use this to change inactive color. E.g # 7F888C                                                                                                                     |
|              | Heading size (px)           | Adjust the size of heading texts in pixels.                                                                                                                         |
|              | Paragraph size (px)         | Adjust the size of paragraph texts in pixels.                                                                                                                       |
|              | Line height (px)            | Adjust the height of lines in pixels for readability.                                                                                                               |
| Buttons      | Primary button              | Customise text and background color, along with border radius for primary buttons.                                                                                  |
|              | Secondary button            | Customise text and background color, along with border radius for secondary buttons.                                                                                |
|              | Border radius (px)          | Customise the border radius of your buttons.                                                                                                                        |
| Colors       |                             | Control the UI's overall appearance, including background color and the colors used for messages indicating success, failure, or warnings.                          |
|              | Success                     | # 4FC35A                                                                                                                                                            |
|              | Warning                     | # FABE34                                                                                                                                                            |
|              | Failure                     | # FE493F                                                                                                                                                            |
|              | Background                  | # FFFFFF                                                                                                                                                            |
|              | Links                       | # 0459A8                                                                                                                                                            |
|              | Accreditation               | # 2784DA                                                                                                                                                            |
| Wrapper      | Desktop width (px)          | Define the width of the desktop UI wrapper in pixels to ensure proper layout fitting.                                                                               |

#### Institution Tab Settings

| Section             | Description                                                                                                                                                           |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Select all Checkbox | Facilitates the selection or deselection of all financial institutions in the list for ease of management.                                                            |
| Institution List    | A list where you can select which financial institutions will be available for users to connect with, tailored to the services and regions your application supports. |

#### Flow Tab Setting

[block:parameters]
{
  "data": {
    "h-0": "Section",
    "h-1": "Feature",
    "h-2": "Description",
    "0-0": "Preferences",
    "0-1": "Skip success screen",
    "0-2": "A toggle to bypass the confirmation screen after successful consent, offering a more streamlined experience for users. Useful for repeat users who are familiar with the process and do not require additional confirmation.",
    "1-0": "",
    "1-1": "Allow multiple connections",
    "1-2": "Permits users to connect multiple bank accounts from different financial institutions, broadening the scope of data aggregation for a more comprehensive financial overview.",
    "2-0": "",
    "2-1": "Analytics (GTM)",
    "2-2": "This field accepts a Google Tag Manager tracking code, which allows for the collection of analytics on how users interact with the consent UI, providing insights into user behaviour and potential areas for UI improvement.",
    "3-0": "",
    "3-1": "Reference name",
    "3-2": "When a user attempts to cancel out of our consent UI, a confirmation pop-up appears to ensure the user intends to leave the consent process. This pop-up provides a message indicating the action the system will take if the user confirms the cancelation. For example: If the partner name is \"ExamplePartner\", the confirmation pop-up will now display:  \n  \n\"Are you sure you want to leave? You will be taken back to ExamplePartner.\"",
    "4-0": "External URLs",
    "4-1": "Redirect URL",
    "4-2": "The web address users will be redirected to after the consent process is completed. This URL is critical for maintaining a seamless user journey through the consent procedure, whether granting or revoking consent.",
    "5-0": "",
    "5-1": "Manage consent url",
    "5-2": "A publicly hosted page with details on Consent management for your users."
  },
  "cols": 3,
  "rows": 6,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


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