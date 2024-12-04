---
title: List float accounts
excerpt: ''
api:
  file: payments.json
  operationId: listFloatAccounts
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
When list float accounts, you will receive a below response. 
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"type\": \"list\",\n    \"count\": 1,\n    \"data\": [\n        {\n            \"type\": \"floataccount\",\n            \"id\": \"786ffcce-a112-43d8-8bad-b38393fe0a9f\",\n            \"bankBranchCode\": \"802919\",\n            \"accountNumber\": \"1111111\",\n            \"availableBalance\": 14733.15,\n            \"status\": \"active\",\n            \"links\": {\n                \"self\": \"https://au-api.basiq.io/payments/float-accounts/786ffcce-a112-43d8-8bad-b38393fe0a9f\"\n            }\n        }\n    ],\n    \"links\": {\n        \"self\": \"https://au-api.basiq.io/payments/float-accounts\"\n    }\n}",
      "language": "json"
    }
  ]
}
[/block]