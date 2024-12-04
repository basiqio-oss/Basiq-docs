---
title: Retrieve a report
excerpt: >-
  Use this endpoint to retrieve a specific report. Ensure you check the

  documentation for the schema of each report type.


  | Request Header |
  Description                                                             | 

  |----------------|-----------------------------------------------------------------------------|

  | Accept         | Specifies the format of the response. Use
  `application/json` or `application/pdf` | 


  If you want to generate the PDF, make sure to change `content-type`

  in the CURL request to `application/pdf` for PDF generation.
api:
  file: reporting.json
  operationId: retrieveReport
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---