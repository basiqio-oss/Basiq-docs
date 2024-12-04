---
title: Income Verification (IAV)
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1daec9fc906bc8b1f6b83221ef0436c6e37d5124c93d713406e68a369574a6db-Apple_Macbook_Pro.png",
        "",
        "Income Verification StarterKit"
      ],
      "align": "center",
      "caption": "Income Verification StarterKit"
    }
  ]
}
[/block]


# Overview: What is Income Verification?

The Income Verification [Starter Kit](https://iv-demo.basiq.io/) streamlines the process of verifying a user's income. By securely connecting their bank account, this kit automatically generates an income verification report through our **[Reports API](https://api.basiq.io/reference/createreport)**. The report encompasses both user-level and group-level analyses, detailed in the sections below.

## Creating an Income Verification Report

To generate an income verification report, make a POST request to the following endpoint::

```Text REPORT API Endpoint
POST https://au-api.basiq.io/reports
```

### Required Headers

When making the request, ensure you include the following headers:

- `Accept`: Specify the response format you expect, typically application/json.
- `Authorization`: Include your `Bearer token` for authentication.
- `Content-Type`: Indicate that you're sending JSON data with application/json.

#### Example Request Headers:

```Text Http
Accept: application/json
Authorization: Bearer your_access_token
Content-Type: application/json
```

## Constructing Your Request

When constructing your request, you'll need to prepare a JSON payload that specifies the type of report you want to generate, along with any filters relevant to the income verification.

### Required Payload Structure

The payload should include:

- `reportType`: The type of report you are generating. For income verification, use `"CON_AFFOR_01"`.
- `title`: A descriptive title for the report.
- `filters`: An array of filter objects that specify the parameters for your report.

### Example Payload:

```json
{
  "reportType": "CON_AFFOR_01",
  "title": "John Smith Affordability Report 2022-03-26",
  "filters": [
    { "name": "fromDate", "value": "2022-01-01" },
    { "name": "toDate", "value": "2023-01-01" },
    { "name": "accounts", "value": ["ag829sj", "aj82gka"] },
    { "name": "users", "value": ["272af9fa-0f4a-44dc-bf88-a63bec2d0662"] },
    { "name": "includeMetrics", "value": ["ME002", "ME003", "ME004"] },
    { "name": "includeGroups", "value": ["INC-001", "INC-002", "EXP-001"] }
  ]
}
```

### Relevant Metrics and Groups

For income verification, the following metrics and income groups are relevant for this use-case:

| ID    | Title                                      |
| ----- | ------------------------------------------ |
| ME001 | # OF IDENTIFIED SALARY SOURCES             |
| ME002 | AVERAGE MONTHLY AMOUNT FROM SALARY         |
| ME003 | SALARY HAS BEEN STABLE FOR (MONTHS)        |
| ME004 | OTHER POSSIBLE INCOME MONTHLY              |
| ME022 | HAS RECENT CHANGES TO SALARY CIRCUMSTANCES |
| ME033 | AVERAGE INCOME MONTHLY                     |
| ME035 | TOTAL INCOME HAS BEEN STABLE FOR (MONTHS)  |
| ME036 | MEDIAN MONTHLY AMOUNT FROM SALARY          |
| ME037 | MEDIAN INCOME MONTHLY                      |
| ME040 | AVERAGE MONTHLY CREDITS                    |
| ME042 | # OF RECENT INCOME SOURCES                 |
| ME043 | # OF ONGOING REGULAR INCOME SOURCES        |
| ME045 | TOTAL INCOME HAS BEEN SECURE FOR (MONTHS)  |

### Including All Income Groups

To ensure that your report includes all income groups, even those without data (displaying a value of 0), make sure to specify all relevant groups in the includeGroups filter. This is beneficial as it provides a more comprehensive view of the income landscape.

| ID      | Title                  |
| ------- | ---------------------- |
| INC-001 | Benefits               |
| INC-002 | Child Support Income   |
| INC-003 | Insurance Credits      |
| INC-004 | Interest Income        |
| INC-005 | Investment Income      |
| INC-006 | Other Earnings         |
| INC-007 | Other Credits          |
| INC-008 | Rent & Board Income    |
| INC-009 | Salary                 |
| INC-010 | Superannuation Credits |
| INC-012 | Youth Allowance        |
| INC-013 | Rental Assistance      |
| INC-014 | Centrelink             |
| INC-015 | Medicare               |
| INC-016 | Jobseeker              |
| INC-018 | Pension                |
| INC-019 | Carers                 |
| INC-020 | Education              |
| INC-021 | Crisis Support         |

## Use Case: Verifying User Income for Lending

Let's take you through a use case.

### Scenario:

A lender needs to verify a user’s income before approving a loan. The user, John, has multiple sources of income that must be considered.

### Example:

John is seeking a loan due to financial pressures. He has four distinct sources of income:

- **Salary:** 
  - Paid monthly.
  - Received $6,000 from January 2023 to May 2023.
  - Promoted in June 2023, increasing salary to $8,000 per month (ongoing).
- **Rental Income:**
  - Receives $1,500 fortnightly from a tenant.
  - Rental income started in mid-June 2023 due to rising interest rates.
- **Child Support:**
  - Previously received monthly child support.
  - Payments stopped after October 2023.
- **Interest Income:**
  - Receives monthly interest from a savings account.

### User-Level Analysis:

- **Average Monthly Income**: John’s average monthly income is $10,061.78.
- **Income Stability (Past 12 Months)**: John’s income has been secure, received generally on time, with minimal fluctuations.
- **Income Stability (Past 7 Months)**: Income has remained stable, with consistent payments and minor variability.
- **Current Salary Stability**: His salary has been stable for the past 7 months, with no recent changes.
- **Projected Income**: Based on historical income, three stable income streams are expected to continue, with John projected to earn $11,145 next month.

### Metrics:

Below the analysis, display key metric data points like:

- Total monthly income.
- Source-specific income history.
- Projections for next month's income.

This can be seen in this example below: 

[block:html]
{
  "html": "<!--ARCADE EMBED START--><div style=\"position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;\"><iframe src=\"https://demo.arcade.software/575cLC6XcgySwdSrgYx7?embed&embed_mobile=tab&embed_desktop=inline\" title=\"BASIQ Income Verification\" frameborder=\"0\" loading=\"lazy\" webkitallowfullscreen mozallowfullscreen allowfullscreen allow=\"clipboard-write\" style=\"position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;\" ></iframe></div><!--ARCADE EMBED END-->"
}
[/block]


### Group-Level Analysis:

For each income source (salary, rent, child support, interest), list detailed group results in a drill-down format. Each section should be expandable for further exploration of the data, allowing the developer to access more granular insights on each income stream.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ea5952eb9c8bec04097926480a1f10dde7b2de07468aa9d0cddceddc78692766-groups.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


## Income Verification Starter Kit

The **[Income Verification Starter Kit](https://iv-demo.basiq.io/)** automates the process of verifying a user’s income. By securely connecting their bank account, the kit generates a comprehensive income verification report using our **[Reports API](https://api.basiq.io/reference/createreport)**, which includes user-level and group-level analysis.

### Process Flow:

- **User Bank Account Connection**: Users securely connect their bank accounts.
- **Generate Income Report**: After connection, the [Reports API](https://api.basiq.io/reference/createreport) will be used to generate a detailed report of the user's income.
- **Analysis Metrics**: 
  - The generated report will automatically perform the **user-level analysis**:
    - **Average Monthly Income** calculation.
    - **Income Stability** for the past 12 months and 7 months.
    - **Current Salary Stability** and projected future income.
  - The report will also generate **group-level analysis**:
    - Income breakdown by source (salary, rental, child support, interest).
    - Drill-down functionality for each income source, allowing further exploration.

### Try It Out:

Visit our [demo](https://iv-demo.basiq.io/) to connect a sample bank account and see the income verification process in action.

## Demo Application Performance

Our **[Income Verification Demo\*\*](https://iv-demo.basiq.io/) is optimised to ensure a high-quality user experience. Below are the results from a **Lighthouse audit\*\* conducted on Google Chrome, reflecting top-tier performance in several key areas:

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/01e43f0a88f01bc4d3a3ae99f797dca52656e1457f913e92bba55b3c24bbf733-Screenshot_2024-09-19_at_11.16.42_AM.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


- Performance: 100
- Accessibility: 95
- Best Practices: 100
- SEO: 100

These scores demonstrate the application’s focus on speed, accessibility, and adherence to web standards, ensuring a seamless experience across devices.

> 👍 Quick Links
> 
> - [Report API](https://api.basiq.io/reference/createreport)
> - Income Verification Starter Kit [Demo](https://iv-demo.basiq.io/) 

If you have any questions or need assistance, feel free to reach out to our support team.