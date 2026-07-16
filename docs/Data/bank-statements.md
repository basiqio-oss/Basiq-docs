---
title: Statements
excerpt: Bank Statements
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Introduction:

Statements play a crucial role in financial transactions, especially in the lending and brokerage sectors. They provide detailed records of account activity and are often required as supporting documentation for various financial processes.

## Business Case:

The need for statements primarily arises from the requirements of lenders and brokers. These entities are obligated to submit bank statements to bank lenders as part of supporting documentation. Despite the availability of other financial reports like the Consumer Affordability Report, banks still necessitate bank statements for several reasons.

## Importance of Statements:

* **Comprehensive Record:** Statements offer a comprehensive overview of account activities, including deposits, withdrawals, and balances over a specified period. This level of detail is important for assessing an individual's financial health and credibility.
* **Verification:** Bank statements serve as a means of verification for the information provided in other financial reports. They offer tangible evidence of financial transactions and can corroborate the data presented in other documents.
* **Risk Assessment:** Lenders and brokers use bank statements to conduct thorough risk assessments before extending credit or entering into financial agreements. The patterns and trends observed in the statement help in evaluating the borrower's ability to repay loans and manage finances responsibly.
* **Regulatory Compliance:** In many jurisdictions, regulatory authorities mandate the submission of bank statements as part of the loan approval process. Compliance with these regulations is essential for both lenders and borrowers to avoid legal issues and ensure transparency.

## Statements in Financial Processes:

* **Loan Applications:** Bank statements are commonly required during the loan application process to verify income, assets, and financial stability.
* **Mortgage Applications:** Mortgage lenders often request bank statements to assess the borrower's financial capacity and evaluate the risk associated with the loan.
* **Credit Assessments:** Statements play a crucial role in credit assessments, helping lenders determine the creditworthiness of applicants and set appropriate terms and conditions.

# How to Create and Retrieve Statements via Basiq API

This guide will walk you through the process of creating and retrieving statements via our API. Statements provide a comprehensive summary of financial transactions and account activity over a specified period.

## Creating a Statement

To create a statement, follow these steps:

### Make a POST Request

Send a POST request to the endpoint for reports:

```Text CURL
POST https://au-api-basiq.io/reports
```

### Include Body Parameters

Include the following body parameters:

```json
{
   "reportType": "STATEMENT_01",
   "title": "Statement",
   "filters": [
      {
         "name": "fromDate",
         "value": "2022-01-01"
      },
      {
         "name": "account",
         "value": "121221c"
      },
      {
         "name": "user",
         "value": "2323323r"
      }
   ]
}
```

#### Mandatory Parameters:

* **reportType**: Specifies the type of report. Must be "STATEMENT\_01".
* **account**: Unique identifier for the account.
* **user**: Unique identifier for the user.

### Optional Parameters:

**title**: Title of the statement. If not provided, defaults to `STMT-dd.mm.yyyy-dd.mm.yyyy`.

**fromDate**: Start date of the statement period. Defaults to the last update of the account and goes back 13 months if not provided.

### Receive Confirmation

If the request is successful, you will receive a response containing a job ID:

```json
{
    "type": "job",
    "id": "<jobID>",
    "links": {
        "self": "https://au-api.basiq.io/jobs/jobId"
    }
}
```

## Retrieving the Statement

To retrieve the statement:

### Use Job ID

Use the received job ID to fetch the report ID. Keep polling the following endpoint to get "success" status:

```Text CURL
GET https://au-api-basiq.io/jobs/jobId
```

### Job Confirmation

If the request is successful, you will receive a response with report ID:

```json
{
    "type": "job",
    "id": "a2a17e84",
    "createdDate": "2024-03-21T23:51:37Z",
    "updatedDate": "2024-03-21T23:51:48Z",
    "jobType": "report",
    "sourceId": "a2a17e84",
    "steps": [
        {
            "title": "create-report",
            "status": "success",
            "result": {
                "type": "report",
                "url": "/reports/a2a17e84"
            }
        }
    ],
    "links": {
        "self": "https://au-api.basiq.io/jobs/a2a17e84",
        "source": "https://au-api.basiq.io/reports/a2a17e84"
    }
}
```

### Use Report ID

Use the received `id` as report ID to fetch the statement. Send a GET request to the following endpoint:

```json cURL
GET https://au-api-basiq.io/reports/<reportId>
```

* Replace `<reportId>` with the report ID received in the previous step.

### Include Authorization

Include the Bearer token in the request header for authorization:

```Text cURL
Authorization: Bearer token
```

### Specify Accept type

Specify the `accept` as application/json for JSON format:

```Text cURL
accept: application/json
```

### Retrieving PDF Format

To retrieve the statement in PDF format, follow the same steps as retrieving the JSON format, but set the accept accordingly:

```Text cURL
accept: application/pdf
```

## Retrieving Transactions

Transactions associated with the statement are listed separately via the following endpoint:

```json
GET https://au-api-basiq.io/reports/<reportId>/transactions
```

* Replace `<reportId>` with the report ID obtained earlier.

# How to Create & Export Statements via Dashboard

This guide will walk you through the process of creating and downloading statements via our Basiq Dashboard. The detail video demonstration is below, and you can interact with the demo as well.

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(54.0520984081042% + 41px); height: 0; width: 100%;">
<iframe src="https://demo.arcade.software/9VWzGum68A5oSDKGwwJY?embed" title="Basiq - Statements" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe>
</div>
`}</HTMLBlock>

> 📘 Statements
>
> If you don't see this option in your dashboard. Please reach out to our support team for enablement or you can email us at [support@basiq.io.](mailto:support@basiq.io)

> 👍 Quick Links
>
> * [Create Statements](https://api.basiq.io/reference/createreport)
> * [List Statements](https://api.basiq.io/reference/listallreports)
> * [Retrieve Statements](https://api.basiq.io/reference/retrievereport)
> * [Basiq Dashboard](https://dashboard.basiq.io/)