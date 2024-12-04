---
title: Create a statement
excerpt: >-
  Create a new statement by uploading an official PDF bank statement or CSV
  file. The server will create a job that processes the following steps:

  1. **verify-credentials**: Verify the file, validate the layout, and attempt
  to parse the statement.

  2. **retrieve-accounts**: Retrieve the list of accounts and their details
  (account number, name, balances).

  3. **retrieve-transactions**: Fetch the transactions for each account.


  The status of each step can be checked by querying the Retrieve a job. 


  > Note that this function is not supported in sandbox environments (AU00000).


  For CSV file format specifications, please contact our support team.


  > 🚧 

  > 

  > Note that the time it takes to complete the processes above will vary
  depending on the volume of data along with the complexity of the bank
  statement. As a rough guide this entire process could take anywhere between 10
  - 30 secs. Upload multiple statements in parallel to provide the best user
  experience
api:
  file: data.json
  operationId: createStatement
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---