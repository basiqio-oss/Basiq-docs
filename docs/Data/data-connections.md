---
title: Connections
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
## Overview:

Connection objects are created when a user connects their financial institution with your app. These connections act as channels that fetch and store account holders' data, such as accounts and transactions, against the User object. To maintain data integrity and simplify management, it is recommended to interact with account data through the User object rather than directly via the connection.

## Connection Status:

### **Active (Web & <<glossary:OB>>)**:

The connection is fully functional and has completed all necessary job steps.

### **Deleted (Web & <<glossary:OB>>)**:

Indicates the connection has been terminated by the partner.

### **Invalid (Web & <<glossary:OB>>)**:

The connection is not operational due to issues in one or more of the job steps. It can be refreshed manually, and a successful refresh will restore it to "Active."

### **Pending (Web)**:

The connection is new and waiting to determine if it will become active or remain invalid. This status signifies the start of the process.

### **Init (<<glossary:OB>>)**:

The connection has successfully passed the open banking authorization and is temporarily in this state.

### **Pre-init (<<glossary:OB>>)**:

Similar to the Pending status, this is assigned at the creation of an open banking connection and marks the beginning of the job. Connections stuck in pre-init state are usually a result of user leaving the authorisation flow before finishing it. The first step in resolving this is appointing the user to go through the whole flow again. There’s no need to delete a pre-init connection beforehand.

## Data Fetching and Sync

Once established, a connection allows for the retrieval of data added after its creation by refreshing it. This keeps your system up-to-date with the financial institution's latest information. Using the Smart Cache is advisable as it optimises data access and minimises system strain.

## Managing Connections

### Ad Hoc Refreshes:

Limit these to avoid excessive load on bank servers, which can lead to user account issues or bank-imposed restrictions.

### Connection Monitoring:

Creating a new connection with the same credentials as an existing one will cause the new one to pause for six minutes to avoid account lockouts.

### Bulk Refreshes:

Avoid scheduling massive simultaneous refreshes, which can overload bank systems. Instead, rely on Smart Cache for regular updates.

### Refresh Frequency:

Check the [last refresh](https://api.basiq.io/reference/refreshconnection) time either through detailed job records or by examining the `connection.lastUsed` attribute before performing a refresh.

## Managing Connection Data

When a connection is deleted, the existing data for accounts and transactions remains within the User object. If you need to completely remove all data associated with a connection:

### Purge Existing Data

- **Data Clean-Up**: Before you can fully remove an institution's data, use the '[Purge Connection Data](https://api.basiq.io/reference/purgeconnectiondata)' endpoint to delete all existing user data for that specific institution. This is crucial for ensuring a clean transition.

> 📘 Note:
> 
> The purge function must be executed while the connection is still active, as it does not work on deleted connections.

### Delete Existing Web Connection

- **Remove Current Connection**: It is necessary to delete the existing connection if transitioning to an <<glossary:OB>> connection. This prevents conflicts since a user cannot have both Web and OB connections active at the same time for the same institution.

### Establish New OB Connection

- **Create the <<glossary:OB>> Connection**: After the connection is deleted and the data is purged, you can establish a new <<glossary:OB>> or web connection for the user. This ensures continuity and compliance with updated connection protocols.