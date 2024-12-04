---
title: Account Types
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
<Image title="120db64-Typography.jpg" alt={2058} src="https://files.readme.io/120db64-Typography.jpg">
  Basiq Customise UI
</Image>

## Introduction:

Partners utilising the ConsentUI have the ability to customize various aspects of the interface through the Layout tab. This tab enables partners to adjust fonts, colors, text size, and the appearance of different elements within the ConsentUI.

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

<Image title="32a604c-Screenshot_2023-06-29_at_4.16.03_pm.png" alt={2766} src="https://files.readme.io/32a604c-Screenshot_2023-06-29_at_4.16.03_pm.png">
  Customise UI
</Image>

**Analytics (GTM)**

In order to configure Google Tag Manager (GTM), the process begins with the utilisation of the Customiser feature. Through Customiser UI, partners are able to incorporate their own custom tags into the Analytics field of Google Tag Manager (GTM). This allows for a personalised and tailored tracking system.

Once the configuration is complete, additional code snippets are added to the ConsentUI. At present, the tracking setup primarily focuses on entire pages rather than individual elements such as buttons or links. This means that the tracking and analytics capabilities of the system are designed to monitor the navigation patterns of users, particularly their access to specific screens or pages.

However, it's important to note that the current setup does not include the identification of distinct actions within those pages. In other words, while the system can track user movement and interactions on a broader scale, it is unable to differentiate between different types of clicks or actions performed by users within those pages.

## Customisable fields

**Header Image**

The header image, which includes the logo displayed at the top of the ConsentUI homepage, has been relocated to the Layout tab. Partners can upload their desired logo image to be used as the header image.

**Font Family**

Partners have the flexibility to choose from a variety of open-source Google Fonts. By selecting a font family, partners can apply a consistent font style to all elements throughout the ConsentUI. Additionally, the text is set to either bold or regular by default, depending on whether the selected font supports it.

**Font Size**

The ConsentUI allows partners to configure the sizes of both headings and paragraphs. Heading size affects the titles displayed on most screens, such as the "Select institution" title. On the other hand, paragraph size applies to all other text elements, including buttons, subtext, popups, and more.

**Heading Color**

Partners can modify the font color of all heading text elements within the ConsentUI. This customisation option allows for the selection of a preferred font-face color, enabling partners to align the appearance of the headings with their brand identity.

**Paragraph Color**

The ConsentUI also provides the ability to change the font color of all paragraph text elements, excluding disabled elements and links. By customizing the paragraph color, partners can ensure a consistent visual style throughout the text content within the ConsentUI.

**Inactive Color**

Partners have the option to modify the font color of disabled elements, subtext, and disclaimers within the ConsentUI. This customization feature enables partners to select a specific font-face color that distinguishes inactive or non-interactive elements from the rest of the interface.

**Links**

Partners can customize the font color of all clickable elements, including links, back buttons, and active inputs. This allows partners to create visual consistency and highlight interactive elements within the ConsentUI.

**Buttons**

The ConsentUI supports customisation of buttons, including their background color, text color, and border radius. Partners can individually configure these properties for Primary and Secondary buttons, allowing for differentiation between button types based on their visual appearance.

**Background**

Partners have the ability to set the background color of the entire ConsentUI page container. This customisation option allows for the selection of a specific color that aligns with the partner's branding and overall design aesthetic.

**Accreditation (only for Open Banking enabled applications)**

![2766](https://files.readme.io/20d19f5-Screenshot_2023-06-29_at_4.16.13_pm.png "20d19f5-Screenshot_2023-06-29_at_4.16.13_pm.png")

For Open Banking enabled applications, partners can modify the background and text colors of the Consumer Data Right (CDR) accreditation badge. This customisation feature ensures that the badge seamlessly integrates with the partner's chosen color scheme.

**Consent Policy - Data We Will Collect**

Partners can select from different pre-configured scopes to determine the specific data they wish to fetch from the Data Holders. The ConsentUI provides a straightforward way to manage these consent scopes. Partners can refer to the Consent Scopes documentation for further information on configuring and utilising consent scopes within the ConsentUI.

This comprehensive documentation outlines the various customisation options available within the ConsentUI, empowering partners to create a customised and branded experience for their users while maintaining functionality and compliance with data consent policies.

## Quick Links

You can get started [here](https://dashboard.basiq.io/customise-ui) and let us know if you have any feedback for us to improve.
