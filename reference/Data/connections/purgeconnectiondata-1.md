---
title: Purge connection data
excerpt: >-
  Use this endpoint to remove all user data related to a specific institution.
  Purging is only applicable for active user connections.


  When Enrich data is updated, the Enrich results under transactions won’t
  automatically reflect these updates. To ensure the latest Enrich results are
  available, partners should first purge and then refresh connections. Without
  this step, any new insight reports generated will not include the latest
  enriched data.


  > 📘 **Note:** Remember to purge and refresh connections to keep Enrich
  insights current.
api:
  file: .referencedata.json
  operationId: purgeConnectionData
hidden: false
---