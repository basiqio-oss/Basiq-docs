---
title: Consent Management Policy Template
deprecated: false
hidden: true
metadata:
  robots: index
---
This document explains how partners can integrate and present a Consent Management Portal on their websites, ensuring compliance with the Consumer Data Right (CDR) requirements. This guide includes details on managing user consents, data retention policies, data deletion, and de-identification.

## Introduction to the Consumer Data Right (CDR)

The Consumer Data Right (CDR) regulates the collection and handling of CDR data in line with privacy safeguards and rules that:

* Ensure your data is managed securely.
* Provide you with control over how your data is shared and used.

<Cards columns={2} style={{ marginTop: '20px' }}>
  <Card title="What is an Accredited Data Recipient (ADR)?" icon="fa-shield-alt" style={{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '20px', animation: 'fadeIn 1s ease-out' }}>
    <p style={{ fontSize: '16px', color: '#003366' }}>
      An **Accredited Data Recipient (ADR)** is an organization approved under the CDR framework to receive and manage consumer data securely. ADRs are required to adhere to strict privacy and security rules, ensuring that the consumer's data is used only with their consent.
    </p>

    <ul>
      <li>Adhere to transparent disclosure of data usage.</li>
      <li>Ensure secure storage and transfer of consumer data.</li>
      <li>Implement privacy safeguards for data sharing based on user consent.</li>
    </ul>
  </Card>

  <Card title="Key User Benefits" icon="fa-check-circle" style={{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '20px', animation: 'fadeIn 2s ease-out' }}>
    <ul>
      <li><strong>Choice and Control:</strong> Users decide what data to share, how it’s used, and who can access it.</li>
      <li><strong>Manage Consent:</strong> Users can view, modify, or revoke their consents at any time.</li>
      <li><strong>Data Deletion Requests:</strong> Users can request deletion or de-identification of their personal data.</li>
    </ul>
  </Card>

  <Cards />

  <Cards columns={2} style={{ marginTop: '20px' }} />

  <Card title="How Data is Used" icon="fa-cogs" style={{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '20px', animation: 'fadeIn 3s ease-out' }}>
    <div style={{ fontSize: '16px', fontWeight: 'bold', color: '#003366' }}>
      Data collected under the CDR framework is used for various purposes, all based on user consent.
    </div>

    <ul>
      <li><strong>Personalized Solutions:</strong> Tailoring recommendations based on user activities.</li>
      <li><strong>Operational Purposes:</strong> Detecting fraud, preventing abuse, and performing analytical reporting using de-identified data.</li>
      <li><strong>Communication:</strong> Sending updates, notifications, or support for services related to the user's preferences.</li>
    </ul>
  </Card>

  <Card title="" icon="fa-user">
    <img src="https://i0.wp.com/greener.com.au/wp-content/uploads/2023/06/CDR-2.png" />
  </Card>
</Cards>

<Accordion title="Data Security" icon="fa-lock" style={{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px', animation: 'fadeIn 2s ease-out' }}>
  <div style={{ fontSize: '16px', fontWeight: 'bold', color: '#003366' }}>
    It’s important to ensure that data is securely managed, following strict protocols for storage, encryption, and access.
  </div>

  <ul style={{ color: '#003366', listStyleType: 'circle', paddingLeft: '20px' }}>
    <li><strong>Storage:</strong> All data must be securely stored in Australia.</li>
    <li><strong>Encryption:</strong> Encrypt all CDR data in transit and at rest.</li>
    <li><strong>Access Control:</strong> Limit data access to authorized personnel only.</li>
    <li><strong>Audits:</strong> Regular audits ensure compliance with data security practices.</li>
  </ul>
</Accordion>

## Consent Management

To support the proper management of user consent in compliance with the Consumer Data Right (CDR) regulations, partners are required to provide at least two methods for users to manage their consents. These methods can be implemented in various ways to ensure flexibility and convenience for users.

Partners have three main options for implementing consent management:

<Tabs style={{ animation: 'fadeIn 3s ease-out' }}>
  <Tab title="Basiq Dashboard">
    <Accordion title="A. Partner Revoking Consent on Behalf of Users" icon="fa-user-cog" style={{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px', animation: 'fadeIn 3s ease-out' }}>
      <p style={{ fontSize: '16px', color: '#003366' }}>
        Partners can access the Basiq dashboard and revoke consent on behalf of users when needed.
      </p>

      <ul style={{ color: '#003366', listStyleType: 'circle', paddingLeft: '20px' }}>
        <li>Log into the Basiq dashboard.</li>
        <li>Navigate to the "Users" section.</li>
        <li>Locate the user whose consent needs to be revoked.</li>
        <li>Click to revoke consent.</li>
      </ul>

      <HTMLBlock>{`
                                                                                                                                                                          <div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;">
                                                                                                                                                                            <iframe
                                                                                                                                                                              src="https://demo.arcade.software/xfi9ECT8ilSRYF2gzsHb?embed&embed_mobile=tab&embed_desktop=inline"
                                                                                                                                                                              title="Partners Revoking Consent"
                                                                                                                                                                              frameborder="0"
                                                                                                                                                                              loading="lazy"
                                                                                                                                                                              webkitallowfullscreen
                                                                                                                                                                              mozallowfullscreen
                                                                                                                                                                              allowfullscreen
                                                                                                                                                                              allow="clipboard-write"
                                                                                                                                                                              style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;"
                                                                                                                                                                            />
                                                                                                                                                                          </div>
      `}</HTMLBlock>
    </Accordion>

    <Accordion title="B. User Revoking Consent Directly" icon="fa-user" style={{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px', animation: 'fadeIn 4s ease-out' }}>
      <p style={{ fontSize: '16px', color: '#003366' }}>
        Partners can send a URL to the user from the Basiq dashboard, allowing them to revoke consent independently.
      </p>

      <ul style={{ color: '#003366', listStyleType: 'circle', paddingLeft: '20px' }}>
        <li>Generate a URL link from the Basiq dashboard.</li>
        <li>Send the link to the user (via email or other methods).</li>
        <li>The user reviews their consents and revokes them.</li>
      </ul>

      <HTMLBlock>{`
                                                                                                                                                                          <div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;">
                                                                                                                                                                            <iframe
                                                                                                                                                                              src="https://demo.arcade.software/4SusPv6H3COu7a0MG3G2?embed&embed_mobile=tab&embed_desktop=inline"
                                                                                                                                                                              title="User Revoking Consent"
                                                                                                                                                                              frameborder="0"
                                                                                                                                                                              loading="lazy"
                                                                                                                                                                              webkitallowfullscreen
                                                                                                                                                                              mozallowfullscreen
                                                                                                                                                                              allowfullscreen
                                                                                                                                                                              allow="clipboard-write"
                                                                                                                                                                              style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;"
                                                                                                                                                                            />
                                                                                                                                                                          </div>
      `}</HTMLBlock>
    </Accordion>
  </Tab>

  <Tab title="action=manage Parameter">
    <Accordion title="How it Works" icon="fa-link" style={{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px', animation: 'fadeIn 2s ease-out' }}>
      <p style={{ fontSize: '16px', color: '#003366' }}>
        The action=manage parameter directs users to the Consent Management Portal (CMP), where they can manage and revoke their consents directly.
        Partners can:
      </p>

      <ul style={{ color: '#003366', listStyleType: 'circle', paddingLeft: '20px' }}>
        <li>Integrate the CMP view into their web or mobile application for a seamless user experience.</li>
        <li>Provide a link from their app or website to the CMP.</li>
        <li>Replicate certain consent management functionalities within their app and redirect users to Basiq for more advanced operations.</li>
      </ul>

      <HTMLBlock>{`
                                                                                                                                                                          <div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;">
                                                                                                                                                                            <iframe
                                                                                                                                                                              src="https://demo.arcade.software/Wad1ic93gwfM3NQFdMJ3?embed"
                                                                                                                                                                              title="Basiq | action=manage"
                                                                                                                                                                              frameborder="0"
                                                                                                                                                                              loading="lazy"
                                                                                                                                                                              webkitallowfullscreen
                                                                                                                                                                              mozallowfullscreen
                                                                                                                                                                              allowfullscreen
                                                                                                                                                                              allow="clipboard-write"
                                                                                                                                                                              style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;"
                                                                                                                                                                            />
                                                                                                                                                                          </div>
      `}</HTMLBlock>
    </Accordion>
  </Tab>

  <Tab title="Alternative Methods">
    <Accordion title="Additional Options" icon="fa-phone" style={{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px', animation: 'fadeIn 3s ease-out' }}>
      <p style={{ fontSize: '16px', color: '#003366' }}>
        Partners should also provide alternative ways for users to manage their consents, such as:
      </p>

      <ul style={{ color: '#003366', listStyleType: 'circle', paddingLeft: '20px' }}>
        <li>Offering a support email for consent-related requests.</li>
        <li>Providing a phone number for users to contact support.</li>
        <li>Ensuring access to a publicly available resource (e.g., a webpage or downloadable PDF) explaining consent management policies and procedures.</li>
      </ul>

      <p style={{ fontSize: '16px', color: '#003366' }}>
        Ensure your company policies align with the Consent Policy configured in the Basiq customizer. Refer to the official <a href="https://www.oaic.gov.au/consumer-data-right/consumer-data-right-guidance-for-business/privacy-obligations/consumer-consent,-authorisation-and-dashboards" target="_blank" style={{ color: '#003366' }}>ACCC/CDR rules</a> for further guidance.
      </p>
    </Accordion>
  </Tab>
</Tabs>

## Consent Management Details

Users can view and manage their existing consents, including expiry details and connected institutions.

<Cards columns={3}>
  <Card title="View Consent" href="/consent/view" icon="fa-eye">
    Review active consents and details.
  </Card>

  <Card title="Revoke Consent" href="/consent/manage" icon="fa-times-circle">
    Revoke individual or all consents.
  </Card>

  <Card title="Support" href="/contact" icon="fa-envelope">
    Contact support for assistance.
  </Card>
</Cards>

<Accordion title="Data Retention and De-identification" icon="fa-cogs" style={{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px', animation: 'fadeIn 2s ease-out' }}>
  <Accordion title="Data Deletion Process" icon="fa-trash" style={{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px' }}>
    <p><strong>Request Deletion of Your Data</strong></p>
    <p>We respect your privacy and only collect data necessary for providing our services. You have the right to request the deletion of any redundant data we hold at any time. If you withdraw your consent, we will promptly delete your data or de-identify it, ensuring it can no longer be linked to you.</p>

    <p><strong>Handling Redundant Data</strong></p>
    <p>When your data is no longer needed for any legally permitted purpose, we follow a secure process to handle it:</p>

    <ul>
      <li>We will delete, destroy, or de-identify redundant data, unless required to retain it by law.</li>
      <li>If there are legal obligations (e.g., court orders or reporting), we will retain data as necessary.</li>
      <li>We will assess whether to delete or de-identify data based on its relevance and necessity, unless you've explicitly requested deletion.</li>
    </ul>

    <p><strong>What Happens When Your Data is Deleted?</strong></p>
    <p>When your data is deleted:</p>

    <ul>
      <li>It is fully and securely removed from our storage systems.</li>
      <li>Any copies of the data are securely destroyed.</li>
      <li>If shared with third-party processors, we will ensure they delete or destroy their copies as well.</li>
    </ul>

    <p>Your privacy is our priority, and we ensure your data is inaccessible once deleted.</p>

    <p><strong>Contact Us</strong></p>
    <p>If you have questions or want to request the deletion of your data, please contact us:</p>

    <ul>
      <li><strong>Email:</strong> \[Support Email Address]</li>
      <li><strong>Phone:</strong> \[Phone Number]</li>
    </ul>

    <p>We are committed to assisting you and will handle your request promptly.</p>
  </Accordion>

  <Accordion title="De-identification Process" icon="fa-user-secret" style={{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px' }}>
    <p><strong>What Does De-identification Mean?</strong></p>
    <p>De-identification involves removing identifiable information (e.g., user ID, timestamps) while retaining only aggregated, anonymized data. This ensures that personal details are completely stripped out, making the data anonymous.</p>

    <p>We may de-identify CDR (Call Data Record) data that has not become redundant during analytics creation. These anonymized insights help us improve our products and services. We may also share this data with merchants we partner with, or provide it to you as general insights about \[partner]'s users and for invoicing purposes. Additionally, we may share de-identified CDR data with third-party fraud prevention tools to detect and prevent fraud.</p>

    <p>If a service no longer requires the use of your de-identified CDR data, you have the option to request its deletion. This can be decided when you first give consent and anytime during the consent lifecycle.</p>

    <p><strong>How We De-identify CDR Transaction Data</strong></p>
    <p>When we de-identify CDR transaction data, we take the following steps to ensure it becomes completely anonymous:</p>

    <ul>
      <li>Removing the transaction's user ID, ensuring no link to any specific individual.</li>
      <li>Stripping the time portion from the transaction date and time to prevent tracking of exact timestamps.</li>
      <li>Eliminating any transaction description that could reveal the merchant's location or other identifying information.</li>
    </ul>

    <p>Once these steps are completed, the data is fully anonymous and cannot be re-identified or traced back to an individual.</p>
  </Accordion>

  <Accordion title="Retention Policy" icon="fa-clipboard-check" style={{ backgroundColor: '#ffffff', color: '#003366', borderRadius: '8px', padding: '15px' }}>
    <p>Partners are required to ensure that all user data is deleted from their systems when the retention toggle is turned OFF. Additionally, Basiq will ensure the complete deletion of user data upon request, in accordance with this policy. It is essential for partners to follow this protocol to maintain data privacy and compliance standards.</p>
  </Accordion>
</Accordion>

This document provides you with a starting point for understanding and implementing our data de-identification process. You are free to use and adapt this information as needed to align with your use cases. Our team is here to assist and will be happy to review and approve any modifications you make.

We encourage you to tailor the content to your specific needs and feel confident knowing that any changes you propose will be carefully evaluated by our experts. Should you have any questions or need further clarifications, don't hesitate to reach out. Our team is always ready to collaborate and support you throughout this process.