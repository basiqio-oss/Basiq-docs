---
title: Create a report
excerpt: >-
  Use this endpoint to create a new report. Report creation is an asynchronous
  task, meaning a job will be returned to let you know the progress of the
  report generation.

  You can poll the job to know when the report has been generated. You can
  create any supported report (see reportTypes for a list of supported reports).
  Ensure you provide the necessary filters when generating a report.

  All created reports, will store a copy of the data as a snapshot - this
  ensures that you have access to the raw data that was used to create the
  report.
api:
  file: reporting.json
  operationId: post_reports
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---