---
title: March '23
author: Ashman Malik
hidden: false
published_at: '2023-02-28T23:35:28.196Z'
type: added
---
# March '23 :sunny:

## :star2: What's new? 🌱

We are excited to announce that partners will now have access to additional customization options in the [layout tab](https://dashboard.basiq.io/customise-ui). These new features will allow partners to have more control over the appearance of their content, and include the ability to set a custom paragraph line height and change icon colors. These customization options are designed to help partners achieve their desired visual style and enhance the overall user experience. We hope these new features will provide partners with more flexibility and creative freedom to make their content stand out.

Here's a screenshot of what it's looking like. 

<Image title="Screenshot 2023-03-01 at 10.17.22 am.png" alt={1373} border={true} src="https://files.readme.io/35055a1-Screenshot_2023-03-01_at_10.17.22_am.png">
  Customise UI (Layout Tab)
</Image>

## Error Handling 🪝

We are pleased to announce that ConsentUI has been updated to handle and display certain errors more effectively. With this update, ConsentUI will now correctly handle and display the following errors:

**Disconnected**: If the client's internet connection is lost, ConsentUI will display an appropriate message to indicate that the connection has been lost and the user may need to try again later.

<Image title="Screenshot 2023-03-01 at 11.52.47 am.png" alt={430} width="80%" border={true} src="https://files.readme.io/e1b84cf-Screenshot_2023-03-01_at_11.52.47_am.png">
  Disconnected
</Image>

**Data deletion in progress**: If data deletion is in progress, ConsentUI will display a message to inform the user that their data is being deleted and to try again later.

<Image title="Screenshot 2023-03-01 at 12.00.15 pm.png" alt={425} width="80%" border={true} src="https://files.readme.io/efc063f-Screenshot_2023-03-01_at_12.00.15_pm.png">
  Data Deletion in Progress
</Image>

**Connections not enabled for a specific partner API key**: If a partner API key does not have connections enabled, ConsentUI will display an error message indicating that connections need to be enabled for that partner API key.

**Payments not enabled**: If a partner tries to use the payment parameter but payments are not enabled, ConsentUI will display an error message indicating that payments need to be enabled.

We believe these improvements will provide a better user experience for partners and users alike, by providing more specific and informative error messages in these scenarios. We are committed to continuing to improve the functionality and usability of ConsentUI, and we look forward to sharing further updates in the near future. 💙

## Consent UI Updates 📣

We are excited to announce that ConsentUI has been updated to display an expiry countdown for MFA (multi-factor authentication) connections, as well as providing the ability for users to retry or go back if the MFA connection expires.

With this update, users will be able to see the remaining time before the MFA connection expires, which will help them better manage their session and prevent any unexpected disconnections. In addition, if the MFA connection does expire, the user will be presented with options to retry or go back to the previous screen, making the overall experience more seamless and user-friendly.

We believe that these new features will provide a more streamlined and intuitive experience for users, particularly those who rely on MFA connections for added security. We are committed to continually improving the functionality and usability of ConsentUI, and look forward to sharing further updates in the future.

## Consent Scopes Updates 🚀

We would like to inform our partners that, as part of our compliance with open banking requirements, it is no longer possible to add the **account.detail** scope without also including the **account.basic** scope.

This means that partners will need to include both the **account.detail** and **account.basic** scopes in any requests that require access to account information. This requirement is designed to ensure that partners are only accessing the minimum amount of data necessary to provide their services, while also maintaining a high level of security and compliance.

We understand that this may require partners to update their existing integrations, and we apologize for any inconvenience this may cause. However, we believe that this change is necessary to ensure that we are complying with industry standards and regulations, and maintaining the highest level of security and trust for our users.

We are committed to providing our partners with the necessary support to make this transition as smooth as possible. If you have any questions or concerns about this change, please do not hesitate to contact our support team. We appreciate your cooperation and understanding.

## Discontinued Support ☔

We would like to inform our partners that as part of our ongoing efforts to improve the security and compliance of our platform, it is no longer possible to request unsupported scopes such as **Direct Debits** and **Saved Payees**.

This change is designed to ensure that partners are only requesting the minimum amount of data necessary to provide their services, while also ensuring compliance with industry standards and regulations. We believe that this change will help to maintain a high level of security and trust for our users, and reduce the risk of unauthorized access to sensitive data.

We understand that this may require partners to update their existing integrations, and we apologize for any inconvenience this may cause. However, we believe that this change is necessary to ensure the continued reliability and security of our platform.

We are committed to providing our partners with the necessary support to make this transition as smooth as possible.

> 📘 Future Updates
>
> If you have any questions or concerns about this change, please do not hesitate to contact our support team at [support@basiq.io.](mailto:support@basiq.io.) We appreciate your cooperation and understanding.