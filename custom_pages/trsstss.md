---
title: Consent Management Policy
fullscreen: false
hidden: true
---
<Accordion title="Introduction to the Consumer Data Right (CDR)" icon="fa-info-circle">
  The Consumer Data Right (CDR) regulates the collection and handling of CDR data in line with privacy safeguards and rules that:

  * Ensure your data is managed securely.
  * Provide you with control over how your data is shared and used.
</Accordion>

<Cards columns={2}>
  <Card title="Key User Benefits" icon="fa-check-circle">
    * **Choice and Control**: Users decide what data to share, how it’s used, and who can access it.
    * **Manage Consent**: Users can view, modify, or revoke their consents at any time.
    * **Data Deletion Requests**: Users can request deletion or de-identification of their personal data.
  </Card>

  <Card title="What is an Accredited Data Recipient (ADR)?" icon="fa-shield-alt">
    An **Accredited Data Recipient (ADR)** is an organization approved under the CDR framework to receive and manage consumer data securely.

    * Transparent disclosure of how data is used.
    * Secure storage and transfer of consumer data.
    * Privacy safeguards ensuring data is only used as consented by the user.
  </Card>
</Cards>

<Accordion title="Types of Data Collected" icon="fa-database">
  With user consent, ADRs may collect the following types of data:

  * **Personal Information**: Full Name, Contact Details, Occupation
  * **Transaction Data**: Details about purchases, payments, associated metadata.
  * **De-Identified Data**: Data stripped of personally identifiable information for analytics and reporting.
</Accordion>

<Accordion title="How Data is Used" icon="fa-cogs">
  Example framework for the usage of CDR data:

  * **Providing Personalised Solutions**: Tailoring recommendations based on user activities.
  * **Operational Purposes**: Fraud detection, prevention, and analytical reporting using de-identified data.
  * **Communication**: Sending updates, notifications, or support for services.
</Accordion>

<Accordion title="Data Security" icon="fa-lock">
  Ensure compliance with these practices:

  * **Storage**: All data must be stored securely in Australia.
  * **Encryption**: Encrypt all CDR data in transit and at rest.
  * **Access Control**: Limit data access to authorized personnel or systems.
  * **Audits**: Regularly audit data handling practices.
</Accordion>

<Tabs>
  <Tab title="1. Using the Basiq Dashboard for Consent Management">
    <Accordion title="A. Partner Revoking Consent on Behalf of Users" icon="fa-user-cog">
      Partners can access the Basiq dashboard and revoke consent on behalf of users when they are unable to do so themselves.

      * **Steps**:
        1. Log into the Basiq dashboard.
        2. Navigate to the "Users" section.
        3. Locate the user whose consent needs to be revoked.
        4. Click to revoke consent.
    </Accordion>

    <Accordion title="B. User Revoking Consent Directly" icon="fa-user">
      Partners can send a URL to the user from the Basiq dashboard, directing them to the consent management interface where they can revoke consent independently.

      * **Steps**:
        1. Generate a URL link from the Basiq dashboard.
        2. Send the link to the user (via email or other methods).
        3. The user reviews their consents and revokes them.
    </Accordion>
  </Tab>

  <Tab title="2. Using the action=manage Parameter for Consent Management">
    <Accordion title="How it Works" icon="fa-link">
      Partners can send a link with the `action=manage` parameter to allow users to manage their consents directly.

      * **Demo**:
        <HTMLBlock>{`
        <div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/Wad1ic93gwfM3NQFdMJ3?embed" title="Basiq | action=manage" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
        `}</HTMLBlock>
    </Accordion>
  </Tab>
</Tabs>

<Cards columns={4}>
  <Card title="Consent Management Details" href="/consent/manage" icon="fa-info-circle">
    Users can view and manage their existing consents, including expiry details and connected institutions.
  </Card>

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

<Accordion title="Data Retention and De-identification" icon="fa-cogs">
  <Accordion title="Deletion Process" icon="fa-trash">
    * Securely delete user data when consent is withdrawn.
    * Inform third-party data processors to delete or de-identify shared data.
  </Accordion>

  <Accordion title="De-identification" icon="fa-paint-brush">
    * Stripping identifiable information (e.g., user ID, timestamps).
    * Retaining only aggregated, anonymised insights.
  </Accordion>

  <Accordion title="Retention Policy" icon="fa-clipboard-check">
    * Partner Responsibility: If the retention toggle is OFF, partners must delete the data from their systems while ensuring Basiq deletes user data.
  </Accordion>
</Accordion>

<Accordion title="User Rights" icon="fa-user-shield">
  Ensure your platform enables the following:

  * **Access to Data**: Users can request a copy of their data.
  * **Correction of Errors**: Users can correct inaccuracies.
  * **Control**: Allow users to manage consents and data sharing preferences.
  * **Deletion Requests**: Users can request permanent deletion of their data.
</Accordion>