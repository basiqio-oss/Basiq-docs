---
title: Retrieve a report
excerpt: >
  Use this endpoint to retrieve a specific report. Ensure you check the

  documentation for the schema of each report type.


  | Request Header |
  Description                                                             | 

  |----------------|-----------------------------------------------------------------------------|

  | Accept         | Specifies the format of the response. Use `application/pdf`
  | 


  If you want to generate the PDF, make sure to change `accept`

  in the CURL request to `application/pdf` for PDF generation.
api:
  file: .referencereporting.json
  operationId: retrieveReport
hidden: false
---