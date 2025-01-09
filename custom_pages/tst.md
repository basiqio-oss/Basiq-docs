---
title: '# Consent Management Policy Template'
fullscreen: false
hidden: true
---
<Accordion title="Consent Management Portal" icon="fa-info-circle">
  The Consent Management Portal (CMP) provides users with the ability to:

  * **View Consent Details**: Review expiry dates, connected institutions, and consent status.
  * **Manage Connections**: Delete specific connections or revoke consent entirely.
  * **Submit Requests**: Contact support for data-related actions, including withdrawal or deletion.

  Use the URL format:\
  `https://[YOUR_DOMAIN]/consent?action=manage`\
  to integrate the CMP into your system.
</Accordion>

<Cards columns={2}>
  <Card title="Key Features" icon="fa-list-alt">
    **View Consent**: Display user consent details and allow updates or deletions.\
    **Support Options**: Provide an email or contact form for data-related queries.
  </Card>

  <Card title="Implementation Steps" icon="fa-code">
    1. Add CMP link to your dashboard.
    2. Use `action=manage` for user access to the CMP.
    3. Include demo functionality to showcase features.
  </Card>
</Cards>

<Accordion title="Data Retention and De-identification" icon="fa-database">
  Partners should implement a toggle to manage data retention:

  * **Toggle ON**: Partners store the data; Basiq deletes user data.
  * **Toggle OFF**: Partners delete the data; Basiq also deletes user data.

  This ensures compliance and aligns with redundancy rules.
</Accordion>

<Columns layout="auto">
  <Column>
    **Scenario**:\
    A user wants to review consent and delete redundant data.\
    **Process**:

    1. Access CMP via `action=manage`.
    2. Revoke consent for an institution.
    3. Request data deletion.
  </Column>

  <Column>
    **Types of Data**:

    * Personal Information (Name, Contact)
    * Financial Data (Transactions)\
      **Usage Examples**:
    * Displaying carbon footprints.
    * Providing personalized recommendations.
  </Column>
</Columns>

<Tabs>
  <Tab title="What is an ADR?">
    **Accredited Data Recipient (ADR)**:\
    Entities that handle CDR data per privacy safeguards.

    * **User Benefits**:
      * Control data sharing.
      * Withdraw consent anytime.
      * Request data deletion.
  </Tab>

  <Tab title="Secure Data Practices">
    * Store data in Australia (e.g., Microsoft Azure).
    * Encrypt data in transit and at rest.
    * Share data only with user consent.
  </Tab>

  <Tab title="Deletion and De-identification">
    **Deletion**:

    * Fully erase data from systems.
    * Remove redundant data unless required by law.\
      **De-identification**:
    * Remove identifiable attributes.
    * Use for aggregated analytics and fraud detection.
  </Tab>
</Tabs>

<Accordion title="Transparency and User Control" icon="fa-lightbulb">
  Partners should ensure transparency by:

  * Explaining data collection and usage.
  * Disclosing third-party sharing (e.g., Basiq, Experian).
  * Allowing users to submit requests easily.

  **Contact Details**:\
  Provide a support email for additional assistance.
</Accordion>