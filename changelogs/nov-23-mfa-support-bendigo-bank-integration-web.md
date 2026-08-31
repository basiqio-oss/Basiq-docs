---
title: Nov '23 - MFA Support - Bendigo Bank Integration (Web)
author: Ashman Malik
hidden: false
published_at: '2023-11-08T00:26:50.456Z'
type: improved
---
# New Features:

* Added MFA (Multi-Factor Authentication) support for Bendigo Bank, enhancing security for user interactions with the bank's services.

# MFA Job Flow:

* [Introduced a new job flow](https://api.basiq.io/v2.1/reference/upgrading-to-v21#support-for-mfa) for Bendigo Bank that requires a slightly different approach compared to the standard job.
* Users can now identify if they are encountering an MFA challenge by checking the number of steps in the job process, as an MFA challenge typically consists of four steps.

# Recommended Actions:

* We recommend users to verify the number of steps in the job process to determine if they are facing an MFA challenge.
* Adjust your workflow accordingly when dealing with MFA challenges specific to Bendigo Bank.

# Non-UI Usage:

* For cases where you do not utilise our user interface (UI) when interacting with Bendigo Bank, it is essential to return "confirmed" (as a string) as an MFA response.
* This "confirmed" response indicates that your end user has opened an app, and Bendigo Bank relies on this response when establishing a connection.

## Updated MFA Response for Bendigo Bank:

To respond to the MFA challenge when interacting with Bendigo Bank, you should use the following format:

```json POST Create MFA Response
POST /jobs/61723/mfa HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json

{
  "mfa-response": ["confirmed"]
}

```

If you have any questions or encounter any issues, please don't hesitate to reach out to our support team.