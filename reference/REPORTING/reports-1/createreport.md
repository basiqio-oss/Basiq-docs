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

  This API allows generating reports with various filters. The `filters` field
  in the report request enables you to specify parameters for customizing the
  report content.

  > 📘 Note: The report title cannot be longer than 50 characters.


  > 📘 **Reminder:** When Enrich data is updated, the transactions' Enrich
  results won’t automatically reflect these updates. To ensure your report
  reflects the latest Enrich data, purge and refresh connections before
  generating a new report.


  ### Filters 

  Filters are used to narrow down the data included in the report. The available
  filters are:

  - `fromDate`: Specifies the start date for the report data (format:
  YYYY-MM-DD).

  - `toDate`: Specifies the end date for the report data (format: YYYY-MM-DD).

  - `accounts`: List of account IDs to include in the report.

  - `users`: List of user IDs to include in the report.

  - `includeMetrics`: List of metric codes to include in the report. Supported
  values are specific to the report type. Rules for `includeMetrics`:
    - If the array is empty (`"value": []`), all metrics will be shown.
    - If no filter is provided, all metrics will be shown.
    - If an array of codes is provided, only these specific metrics will be shown.
    - If the value is `null`, no metrics will be shown.

  - `includeGroups`: List of group codes to include in the report. Supported
  values are specific to the report type. Rules for `includeGroups`:
    - If the array is empty (`"value": []`), all groups will be shown.
    - If no filter is provided, all groups will be shown.
    - If an array of codes is provided, only these specific groups will be shown.
    - If the value is `null`, no groups will be shown.
api:
  file: reporting.json
  operationId: createreport
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---