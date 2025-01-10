---
title: '# Consent Management Policy Template'
fullscreen: false
hidden: true
---
This document explains how partners can integrate and present a Consent Management Portal on their websites, ensuring compliance with the Consumer Data Right (CDR) requirements. This guide includes details on managing user consents, data retention policies, data deletion, and de-identification.

## Introduction to the Consumer Data Right (CDR)

The Consumer Data Right (CDR) regulates the collection and handling of CDR data in line with privacy safeguards and rules that:

* Ensure your data is managed securely.
* Provide you with control over how your data is shared and used.

## Key User Benefits

* **Choice and Control**: Users decide what data to share, how it’s used, and who can access it.
* **Manage Consent**: Users can view, modify, or revoke their consents at any time.
* **Data Deletion Requests**: Users can request deletion or de-identification of their personal data.

# Features of the Consent Management Portal

## What is an Accredited Data Recipient (ADR)?

An **Accredited Data Recipient (ADR)** is an organization approved under the CDR framework to receive and manage consumer data securely. ADRs must comply with strict rules, including:

* Transparent disclosure of how data is used.
* Secure storage and transfer of consumer data.
* Privacy safeguards ensuring data is only used as consented by the user.

## Types of Data Collected

With user consent, ADRs may collect:

1. **Personal Information**:
   1. Full Name
   2. Contact Details (address, email, phone number)
   3. Occupation
2. **Transaction Data**:
   1. Details about purchases or payments.
   2. Associated metadata (merchant, category).
3. **De-Identified Data**:
   1. Data stripped of personally identifiable information for analytics and reporting.

## How Data is Used

Your organization must transparently outline the use of CDR data. Below is an example framework:

* **Providing Personalised Solutions**:
  * Tailoring recommendations based on user activities.
* **Operational Purposes**:
  * Fraud detection and prevention.
  * Analytical reporting (using de-identified data).
* **Communication**:
  * Sending updates, notifications, or support for services.

## Data Security

Ensure compliance with these practices:

* **Storage**: All data must be stored securely in Australia.
* **Encryption**: Encrypt all CDR data in transit and at rest.
* **Access Control**: Limit data access to authorised personnel or systems.
* **Audits**: Regularly audit data handling practices.

## Consent Management

To support the proper management of user consent in compliance with the Consumer Data Right (CDR) regulations, partners have two main options for implementing consent management:

### 1. Using the Basiq Dashboard for Consent Management

Basiq provides a built-in dashboard where users and partners can manage consent details efficiently. This method enables two ways of handling consent revocation:

#### A. Partner Revoking Consent on Behalf of Users:

* **How it works**: Partners can access the Basiq dashboard and revoke consent on behalf of users. This is useful when users are unable or unwilling to manage their consents directly but need assistance from the partner.
* **Steps**:
  * The partner logs into the Basiq dashboard.
  * Navigate to the "**Users**" section.
  * Locate the user whose consent needs to be revoked.
  * Click to revoke consent and follow the prompts to complete the action.

#### B. User Revoking Consent Directly:

* **How it works**: Partners can send a URL to the user from the Basiq dashboard, directing them to the consent management interface where they can revoke their consent independently.
* **Steps**:
  * The partner generates a URL link from the Basiq dashboard.
  * The partner sends the URL to the user (via email or other communication methods).
  * The user clicks the link and is directed to the Basiq consent management portal.
  * The user reviews their consents and decides to revoke consent for specific data or institutions.
  * This method gives users more direct control over their consent settings and enables partners to support users in a seamless way.

### 2. Using the action=manage Parameter for Consent Management

The second method for consent management involves redirecting users to the Consent Management Portal via the `action=manage` parameter. This method allows users to view, manage, and revoke their consents via a specific URL.

#### How it Works:

* **action=manage**: This is the URL parameter that directs users to the Consent Management Portal (CMP), where they can view and manage their consents.

**Demo**:

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/Wad1ic93gwfM3NQFdMJ3?embed" title="Basiq | action=manage" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>  
`}</HTMLBlock>

<br />

<Accordion title="Consent Management Details" icon="fa-info-circle">
  Users can view and manage their existing consents, including expiry details and connected institutions.
</Accordion>

<Cards columns={4}>
  <Card title="View Consent" href="/consent/view" icon="fa-eye">
    Review active consents and details.
  </Card>

  <Card title="Revoke Consent" href="/consent/manage" icon="fa-times-circle">
    Revoke individual or all consents.
  </Card>

  <Card title="Support" href="/contact" icon="fa-envelope">
    Contact support for assistance.
  </Card>

  <Card title="Learn More" href="/info" icon="fa-book">
    Understand how we use your data.
  </Card>
</Cards>

### Data Retention and De-identification

#### Deletion Process:

* Securely delete user data when consent is withdrawn.
* Inform third-party data processors to delete or de-identify shared data.

#### De-identification:

De-identified data should:

* Be stripped of all identifiable information (e.g., user ID, timestamps).
* Retain only aggregated, anonymised insights.

#### Retention Policy:

* Partner Responsibility: If the retention toggle is OFF, partners must delete the data from their systems while ensuring Basiq deletes user data.

### User Rights

Ensure your platform enables the following:

* **Access to Data**: Users can request a copy of their data.
* **Correction of Errors**: Users can correct inaccuracies.
* **Control**: Allow users to manage consents and data sharing preferences.
* **Deletion Requests**: Users can request permanent deletion of their data.