---
title: Trusted Advisor
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
The Trusted Advisor access model allows qualified professionals to access consumer data for the purpose of providing financial advice. Please read this guide carefully to understand the requirements and steps for onboarding on the Trusted Advisor model.

# Overview

The Trusted Advisor access model allows organisations or individuals to access consumer data for providing financial advice. Partners who qualify as Trusted Advisors can be granted access to the Consumer Data Right (CDR) platform under Basiq.

A Trusted Advisor can be an organisation or an individual who meets the following qualifications:

## Organisation TA Access

Organisations that clearly fit the definition of a Trusted Advisor (e.g., mortgage broker firms). The Trusted Advisor details will be visible on the Consent screen before consent is provided, as well as on the Consent Management and Consent Extension screens for users who previously provided consent with an Individual or Organisation TA.

For existing consents, Trusted Advisor details are read from the Consent object.

Integration with the API for Organisation level TA access works in the same way as a standard integration. However, the Consent UI will render the organisation being named as a Trusted Advisor. The Trusted Advisor information is obtained from the provided token.

Token Specification for Organisation TA Access  
The Trusted Advisor (TA) is passed to the consent UI on launch via the Client Token. The following claims should be added to the token based on the JWT Specs:

- **orgName**: The name of the Trusted Advisor organisation (e.g., Accountants XYZ Pty Ltd).
- **orgRefID**: The reference ID of the organisation (e.g., 0123456789).
- **orgRefType**: The type of reference ID (no specific validation; can be ABN, ACN, or any identifier)
- **orgType**: The type of the Trusted Advisor organisation (e.g., Accountant, Financial Broker, Financial Advisor, Legal Professional, Tax Agent, Financial Counselling Agency).
- **abnAcn**: ABN or ACN number (optional, must follow ABN/ACN format if included)

## Individual TA Access

Suited to organisations that fit the definition of a Trusted Advisor, but their business model does not allow organisation-level access (e.g., mortgage aggregator firms). The consent process is identical for both the individual Trusted Advisor access model and the Organization TA access model. However, in the individual access model, the Trusted Advisor details pertain to an individual, such as: 

- **orgName**: The name of the Trusted Advisor (e.g., John Doe).
- **orgRefID**: The reference ID of the Trusted advisor (e.g., 0123456789).
- **orgRefType**: The type of reference ID (no specific validation; can be ABN, ACN, or any identifier)
- **orgType**: The type of the Trusted Advisor Individual (e.g., Accountant, Financial Broker, Financial Advisor, Legal Professional, Tax Agent, Financial Counselling Agency).
- **abnAcn**: ABN or ACN number (optional, must follow ABN/ACN format if included)

# Token Endpoint Extension

In order to support the Trusted Advisor model for partners, Basiq has extended the POST /token endpoint for requests with the scope "CLIENT_ACCESS." The new organisation fields should be included in the request body as follows:

```yaml body
{
    "scope": "CLIENT_ACCESS", 
    "userId": "10be99c6-1944-4552-bd6f-08d893875179",
    "orgName": "Accountants XYZ Pty Ltd",
    "orgRefID": "0123456789",
    "orgRefType": "Mortgage Broker",
    "orgType": "Financial Broker",
    "abnAcn": "51824753556"
}
```

> **Note: ** `orgRefType` can accept any string without specific validation. **abnAcn** is optional but must be a valid ABN/ACN if included.

The supported values for the orgType field are `Accountant`, `Financial Broker`, `Financial Advisor`, `Legal Professional`, `Tax Agent`, and `Financial Counselling Agency`.

You can use this token to initiate your consent UI and resume the operation. If you have any questions or need further assistance, please contact our support team.

## ConsentUI - Trusted Adviser

- Updated the appearance of the TA banner and popup.
- Added a TA disclaimer message above the consent confirmation button.

### Demo

[block:html]
{
  "html": "<div style=\"position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;\"><iframe src=\"https://demo.arcade.software/5FZJ6bqKc5r5aqotc60W?embed\" title=\"Trusted Advisor Model Demo\" frameborder=\"0\" loading=\"lazy\" webkitallowfullscreen mozallowfullscreen allowfullscreen allow=\"clipboard-write\" style=\"position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;\"></iframe></div>"
}
[/block]