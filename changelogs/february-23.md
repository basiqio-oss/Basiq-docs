---
title: February '23
author: Ashman Malik
hidden: false
published_at: '2023-02-10T05:57:40.527Z'
type: improved
---
# February '23 :sunny:

## :star2: What's new?

## Trusted Advisor Model Update

Trusted Advisor update is live on Consent UI. We will always display Application name. 

## :moneybag: Payments UI

Payments UI has been updated to use [action=payments](https://api.basiq.io/docs/collect-workflow#steps) parameter instead of `Capture payment accounts` toggle

## :information_source: Consent Scopes

* Removed Direct Debits and Saved Payee scopes from consent permission list. We do not support retrieval of these via open banking

* Updated scope requirements so that `account.basic` is required when adding `account.detail`.