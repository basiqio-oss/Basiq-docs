---
title: Delete an auth_link
excerpt: >-
  <blockquote>Note that this action cannot be undone.</blockquote>


  <blockquote>The auth_link is a URL that directs a User to Basiq's hosted
  consent workflow to link banks and securely share data. When the user selects
  'I have disclosed all my accounts' the auth_link is automatically
  deleted.</blockquote>


  Returns an empty body if the delete succeeded. Otherwise, this call returns an
  error in the event of a failure.
api:
  file: .referencecore.json
  operationId: deleteAuthLink
hidden: false
---