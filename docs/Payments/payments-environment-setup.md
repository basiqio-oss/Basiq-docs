---
title: Environments & setup
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Payments are the first “write” behaviour offered via the Basiq platform (traditionally it was restricted to read access of records only). For this reason, it’s important that we ensure partners now have adequate setup and separation for their development and production environments. 

## Processing environments

Basiq payments can be processed in one of two modes: `sandbox`, and `production`. These are what we call processing environments, and they mean you will need two applications setup - one for each mode. Luckily, it’s easy to do this in your application management via the dashboard. 

### :hammer: Sandbox: For development

* Payments processed in the sandbox environment are **simulated** (not using real funds). They will not reach real payment networks and therefore will not affect any institutions. 
* All payments are **simulated** and will progress through each of the different states at the hour mark (e.g if you send a payrequest at 6:45pm the payrequest will be updated at 7pm), allowing partners to test within a reasonable timeframe.

### :rocket: Production: When you're ready to go live

* Payments in the production environment are processed **using real funds** and are communicated using live payment networks, with external payment providers, and institutions.
* When using this mode, you may also access a `restricted` production mode, in which you are restricted to processing a certain number of payments with low denominational amounts for a certain period (e.g. daily). This is to allow for lower risk production testing. 
* Production mode is only able to be accessed once compliance verification has been finalised.

> 📘 Get the ball rolling
>
> To start accessing either of these payment environments, or if you have any questions, please get in touch with us at [support@basiq.io](mailto:support@basiq.io) where we will be able to set you up for payments
