---
title: Get User Analytics
excerpt: >-
  Retrieve user analytics, such as number of users and connections created for
  an application over a given time interval.
api:
  file: analytics.json
  operationId: getUserAnalytics
hidden: false
icon: 🆕
---
<SimpleStepper>
  <SimpleStep header="Step 1: Understand the data">
    <i> 🚧 The displayed number of billable users may not match your actual billing total.\
    For precise billing information, please reach out to support. </i>
  </SimpleStep>

  <SimpleStep header="Step 2: Use the correct interval">
    ℹ️ Billable user counts are only returned when the interval is set to <code>monthly</code>.
  </SimpleStep>
</SimpleStepper>