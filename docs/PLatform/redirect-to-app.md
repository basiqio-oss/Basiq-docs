---
title: Redirect to App
deprecated: false
hidden: true
metadata:
  robots: index
---
## Overview

Redirect to App (R2A) is a CDR authentication flow that allows a consumer to authenticate with their Data Holder using the Data Holder's native mobile application.

For Basiq integrations, this means that a consumer who starts a consent journey from a native mobile application may be transferred from the Basiq consent experience to their Data Holder's mobile application to authenticate and authorise the CDR data sharing request.

Once the Data Holder completes authentication and authorisation, the consumer is returned to the Basiq/ADR application through the registered mobile redirect URI.

Redirect to App is part of the CDR authentication standards and must be supported by Data Recipients from 10 May 2027. Data Recipients and Data Holders may implement the capability earlier.
