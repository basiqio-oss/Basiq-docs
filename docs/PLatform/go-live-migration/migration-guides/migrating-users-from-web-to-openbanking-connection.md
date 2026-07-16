---
title: Web to OpenBanking
excerpt: >-
  This guide outlines the process for transitioning users from a Web connection
  to an OpenBanking (OB) connection.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
If you're looking to transition your users from a traditional Web-based connection to an OpenBanking (OB) connection, follow these straightforward steps to ensure a smooth migration.

## Step-by-Step Migration Process:

### **Prepare for Migration:**

* **Verify OpenBanking Configuration:** Ensure that the institution is set to OpenBanking in your [application’s configuration](https://dashboard.basiq.io/customise-ui). This is a prerequisite for migrating to an OB connection.

### **Purge Existing Data:**

* **Data Clean-Up:** Prior to the migration, it's essential to remove the existing user data for the specific institution. To achieve this, use the ['Purge Connection Data' endpoint](https://api.basiq.io/reference/purgeconnectiondata). This step is a necessary prerequisite to ensure a seamless transition to the OB connection.

> 📘 Note: This action must be performed before deleting the Web connection as the purge function only works for active connections.

### **Delete Existing Web Connection:**

* **Remove Current Connection:** [Delete the user's existing Web connection](https://api.basiq.io/reference/deleteconnection). It's important to note that a user cannot have both Web and OB connections active simultaneously for the same institution. This step is crucial to avoid conflicts and ensure compliance with connection policies.

### **Establish New OB Connection:**

* **Create the OB Connection:** Once the Web connection is deleted and data is purged, you can proceed to establish a new OB connection for the user.

***

### Reminders and Tips:

* **Follow the Order:** It’s crucial to follow these steps in the order presented to avoid any data or connection conflicts.
* **Inform Your Users:** Keep your users informed about these changes. Clear communication can help them understand the benefits of migrating to an OpenBanking connection and what to expect during the process.
* **Support and Assistance:** If you encounter any issues or have questions during the migration process, feel free to reach out for support. 

We’re here to assist you in making this transition as smooth as possible.
