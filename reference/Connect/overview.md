---
title: OpenAPI specification
deprecated: false
hidden: true
icon: fad fa-download
metadata:
  robots: index
---
Use the Connect openapi spec to authenticate with Basiq, manage users, link financial institutions, retrieve account and transaction data, and monitor asynchronous jobs.

<Callout icon="📘" theme="info">
  **OpenAPI specification**

  Download or inspect the Connect OpenAPI file: <Anchor label="`connect.json`" target="_blank" href="https://raw.githubusercontent.com/basiqio-oss/Basiq-docs/refs/heads/v3.0/reference/connect.json">`connect.json`</Anchor>
</Callout>

## What’s included

The Connect specification includes endpoints for:

* Generating API access tokens with `POST /token`
* Creating, retrieving, updating, and deleting users
* Listing, retrieving, refreshing, deleting, and purging user connections
* Retrieving consents and deleting user consents
* Listing and retrieving accounts
* Listing and retrieving transactions
* Tracking asynchronous jobs
* Submitting MFA responses for connection jobs

Use this specification when you are building account-linking, transaction retrieval, consent management, or connection refresh workflows.
