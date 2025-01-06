---
title: Upcoming Changes
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
# Manage Consent Integration Guide for Partners

## What is Manage Consent?

<Accordion title="What is Manage Consent?" icon="fa-info-circle">
  The **Manage Consent** feature allows users to view and manage their consent preferences for data sharing with your platform. Users can check which institutions are connected, delete connections, or revoke consent entirely. This is a vital feature for compliance with the
  [Consumer Data Right (CDR)](https://www.accc.gov.au/business/consumer-data-right/cdr-rules#Consent-Management).
</Accordion>

## Consent Policy Configuration

<Tabs>
  <Tab title="Data Collection">
    The data you wish to collect from the user (e.g., account details, transaction history). Partners need to define exactly what data they are seeking permission to access.
  </Tab>

  <Tab title="Data Retention">
    Defines how long user-consented data is stored. Data will be deleted after consent expiration or revocation, but partners may need to retain de-identified data based on legal obligations. [More about data retention in CDR](https://www.accc.gov.au/business/consumer-data-right/cdr-rules#Data-Retention-and-Disclosure).
  </Tab>

  <Tab title="Data Usage">
    Describes how the user's data will be used (e.g., for analytics, product enhancement, etc.). Be sure to clarify the intent behind data usage in the consent policy.
  </Tab>

  <Tab title="Data Sharing">
    Lists any third parties that the data will be shared with (e.g., affiliates, analytics companies). Full transparency about this is required under the CDR rules.
  </Tab>
</Tabs>

## How the Consent UI Works

<Accordion title="Overview of Consent UI" icon="fa-info-circle">
  The **Consent UI** is a user interface that dynamically renders consent policies based on the configuration you define for your platform. It ensures a streamlined user experience for both Open Banking and traditional data collection methods.
</Accordion>

<Accordion title="Features of Consent UI" icon="fa-cogs">
  <ul>
    <li><strong>User-friendly Interface:</strong> The UI provides an easy-to-use interface for consumers to manage their consents.</li>
    <li><strong>Dynamic Switching:</strong> Compatible with both Open Banking and traditional data collection methods.</li>
  </ul>
</Accordion>

## Implementing the Manage Consent Flow

<Columns layout="auto">
  <Column>
    <h5>Redirect URL Format</h5>
    <p>To implement the "Manage Consent" functionality, use the following URL format:</p>

    <pre>
      window\.location = `https://consent.basiq.io/home?token={{client_token_bound_to_userId}}&action=manage`;
    </pre>

    <p>Replace <code>client\_token\_bound\_to\_userId</code> with the actual client token bound to the user's ID.</p>
  </Column>
</Columns>

## Data Disclosure

<Accordion title="Data Disclosure" icon="fa-warning">
  If your application retains any form of user data (e.g., de-identified data) or creates copies of the data, it is necessary to include a detailed <strong>Data Disclosure</strong> section in your consent management policy. This section must inform users on how the data is collected, held, used, and disclosed.
  For further guidance, please refer to the [CDR Data Disclosure requirements](https://www.accc.gov.au/business/consumer-data-right/cdr-rules#Data-Disclosure).
</Accordion>

## Additional Resources

<Cards columns={4}>
  <Card title="Learn More about CDR Rules" href="https://www.accc.gov.au/business/consumer-data-right/cdr-rules" icon="fa-book" target="_blank">
    Read through the full Consumer Data Right rules to understand compliance.
  </Card>

  <Card title="Open Banking Overview" href="https://www.openbanking.org.uk/" icon="fa-bank" target="_blank">
    An overview of Open Banking principles and implementation in the UK.
  </Card>

  <Card title="Best Practices" icon="fa-check-circle">
    Learn about best practices for managing data and user consent.
  </Card>

  <Card title="Consent UI Details" href="https://www.basiq.io/docs" icon="fa-cogs">
    Dive deeper into the Basiq Consent UI and its integration.
  </Card>
</Cards>