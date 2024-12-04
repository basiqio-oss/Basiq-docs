---
title: API key management
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> 📘 API Key Rotation
> 
> Rotating API keys regularly is a recommended practice to minimise the risk of key exposure and misuse. It is advised that API keys are rotated every 90 days to ensure that the keys remain secure. Below is a step-by-step guide on how to rotate API keys.

# Step-by-Step Guide for API Key Rotation

## Step 1: Schedule the Rotation

Mark your calendar for regular API key rotations every 90 days. Setting up reminders can help ensure compliance with this security best practice.

## Step 2: Generate a New API Key

To rotate an API key, you must first generate a new key:

1. Log into the dashboard.
2. Navigate to the 'API Keys' section.
3. Click on 'Generate New API Key'.

## Step 3: Implement the New API Key

Once a new API key is generated, update your applications or integrations with the new key:

- Replace the old API key with the new key in all your applications.

## Step 4: Verify the Integration

After updating the API key, verify that all systems are functioning as expected with the new key:

1. Test all endpoints to ensure they are operational.
2. Check application logs for any unauthorised or failed attempts.

## Step 5: Revoke the Old API Key

Once the new API key is confirmed to be working correctly:

1. Return to the 'API Keys' section in the dashboard.
2. Select the old API key and click on 'Revoke'.
3. Confirm the revocation to remove the old key from the system.

> 👍 Recommendations for Maintaining Security
> 
> 1. **Limit API Key Access**: Only provide access to API keys to team members who absolutely need it.
> 2. **Assign Appropriate Permissions**: When creating API keys, assign appropriate permissions to them based on the needs of the respective teams.
> 3. **Use Environment Variables**: Store API keys in environment variables instead of hard coding them in your applications.
> 4. **Regular Audits**: Conduct regular audits of API key usage and access rights.
> 5. **Secure Storage**: Use secure vaults or key management systems to store your API keys.