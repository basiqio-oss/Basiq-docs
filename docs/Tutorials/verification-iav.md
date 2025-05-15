---
title: Income/Expense Verification (IEV)
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
<Image align="center" alt="Income Verification StarterKit" border={false} caption="Income/Expense Verification StarterKit" src="https://files.readme.io/88fc8ac887132e1a095a02367f990af654547c3ace1f0bfed07badcc4c6329a8-ssvve.png" />

# Overview: What is Income & Expense Verification?

This Verification streamlines the process of verifying a user's income. By securely connecting their bank account, this demo automatically generates a verification report through our **[Reports API](https://api.basiq.io/reference/createreport)**. The report includes user-level, metrics and group-level analyses, with details tailored to the verification type selected by the user (income or expense).

## Creating an Income or Expense Verification Report

To generate an income or expense verification report, make a POST request to the following endpoint::

```Text REPORT API Endpoint
POST https://au-api.basiq.io/reports
```

### Required Headers

When making the request, ensure you include the following headers:

* `Accept`: Specify the response format you expect, typically application/json.
* `Authorization`: Include your `Bearer token` for authentication.
* `Content-Type`: Indicate that you're sending JSON data with application/json.

#### Example Request Headers:

```Text Http
Accept: application/json
Authorization: Bearer your_access_token
Content-Type: application/json
```

## Constructing Your Request

When constructing your request, you'll need to prepare a JSON payload that specifies the type of report you want to generate, along with any filters relevant to the your desired income or expense verification.

### Required Payload Structure

The payload should include:

* `reportType`: The type of report you are generating. For income verification, use `"CON_AFFOR_01"`.
* `title`: A descriptive title for the report.
* `filters`: An array of filter objects that specify the parameters for your report.
* `reportSubType`: it can be either `income` or `expense` based on your use case.

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
    { "name": "includeGroups", "value": ["INC-001", "INC-002", "EXP-001"] },
    { "name": "reportSubType", "value": "income" }
  ]
}
```

### Relevant Metrics and Groups

For income verification, the following metrics and income groups are relevant for this use-case:

<Table>
  <thead>
    <tr>
      <th>
        ID
      </th>

      <th>
        Title
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ME001
      </td>

      <td>
        # OF IDENTIFIED SALARY SOURCES
      </td>
    </tr>

    <tr>
      <td>
        ME002
      </td>

      <td>
        AVERAGE MONTHLY AMOUNT FROM SALARY
      </td>
    </tr>

    <tr>
      <td>
        ME003
      </td>

      <td>
        SALARY HAS BEEN STABLE FOR (MONTHS)
      </td>
    </tr>

    <tr>
      <td>
        ME004
      </td>

      <td>
        OTHER POSSIBLE INCOME MONTHLY
      </td>
    </tr>

    <tr>
      <td>
        ME022
      </td>

      <td>
        HAS RECENT CHANGES TO SALARY CIRCUMSTANCES
      </td>
    </tr>

    <tr>
      <td>
        ME033
      </td>

      <td>
        AVERAGE INCOME MONTHLY
      </td>
    </tr>

    <tr>
      <td>
        ME035
      </td>

      <td>
        TOTAL INCOME HAS BEEN STABLE FOR (MONTHS)
      </td>
    </tr>

    <tr>
      <td>
        ME036
      </td>

      <td>
        MEDIAN MONTHLY AMOUNT FROM SALARY
      </td>
    </tr>

    <tr>
      <td>
        ME037
      </td>

      <td>
        MEDIAN INCOME MONTHLY
      </td>
    </tr>

    <tr>
      <td>
        ME040
      </td>

      <td>
        AVERAGE MONTHLY CREDITS
      </td>
    </tr>

    <tr>
      <td>
        ME042
      </td>

      <td>
        # OF RECENT INCOME SOURCES
      </td>
    </tr>

    <tr>
      <td>
        ME043
      </td>

      <td>
        # OF ONGOING REGULAR INCOME SOURCES
      </td>
    </tr>

    <tr>
      <td>
        ME045
      </td>

      <td>
        TOTAL INCOME HAS BEEN SECURE FOR (MONTHS)
      </td>
    </tr>
  </tbody>
</Table>

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

Let's take you through a use case for income, you can also try it for expense.

### Scenario:

A lender needs to verify a user’s income before approving a loan. The user, John, has multiple sources of income that must be considered.

### Example:

John is seeking a loan due to financial pressures. He has four distinct sources of income:

* **Salary:**
  * Paid monthly.
  * Received $6,000 from January 2023 to May 2023.
  * Promoted in June 2023, increasing salary to $8,000 per month (ongoing).
* **Rental Income:**
  * Receives $1,500 fortnightly from a tenant.
  * Rental income started in mid-June 2023 due to rising interest rates.
* **Child Support:**
  * Previously received monthly child support.
  * Payments stopped after October 2023.
* **Interest Income:**
  * Receives monthly interest from a savings account.

### User-Level Analysis:

* **Average Monthly Income**: John’s average monthly income is $10,061.78.
* **Income Stability (Past 12 Months)**: John’s income has been secure, received generally on time, with minimal fluctuations.
* **Income Stability (Past 7 Months)**: Income has remained stable, with consistent payments and minor variability.
* **Current Salary Stability**: His salary has been stable for the past 7 months, with no recent changes.
* **Projected Income**: Based on historical income, three stable income streams are expected to continue, with John projected to earn $11,145 next month.

### Metrics:

Below the analysis, display key metric data points like:

* Total monthly income.
* Source-specific income history.
* Projections for next month's income.

This can be seen in this example below:

<HTMLBlock>{`
<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(50.18807092960774% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/MrytPCJ3deoPlgj9VKEH?embed&embed_mobile=tab&embed_desktop=inline" title="Income/Expense Verification" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->
`}</HTMLBlock>

### Group-Level Analysis:

For each income source (salary, rent, child support, interest), list detailed group results in a drill-down format. Each section should be expandable for further exploration of the data, allowing the developer to access more granular insights on each income stream.

<Image align="center" src="https://files.readme.io/ea5952eb9c8bec04097926480a1f10dde7b2de07468aa9d0cddceddc78692766-groups.png" />

## Income Verification Starter Kit

The **[Income Verification Starter Kit](https://iv-demo.basiq.io/)** automates the process of verifying a user’s income. By securely connecting their bank account, the kit generates a comprehensive income verification report using our **[Reports API](https://api.basiq.io/reference/createreport)**, which includes user-level and group-level analysis.

### Process Flow:

* **User Bank Account Connection**: Users securely connect their bank accounts.
* **Generate Income Report**: After connection, the [Reports API](https://api.basiq.io/reference/createreport) will be used to generate a detailed report of the user's income.
* **Analysis Metrics**:
  * The generated report will automatically perform the **user-level analysis**:
    * **Average Monthly Income** calculation.
    * **Income Stability** for the past 12 months and 7 months.
    * **Current Salary Stability** and projected future income.
  * The report will also generate **group-level analysis**:
    * Income breakdown by source (salary, rental, child support, interest).
    * Drill-down functionality for each income source, allowing further exploration.

### Try It Out:

Visit our [demo](https://iv-demo.basiq.io/) to connect a sample bank account and see the income verification process in action.

## Demo Application Performance

Our **[Income Verification Demo\*\*](https://iv-demo.basiq.io/) is optimised to ensure a high-quality user experience. Below are the results from a** Lighthouse audit\*\* conducted on Google Chrome, reflecting top-tier performance in several key areas:

<Image align="center" src="https://files.readme.io/cc2335309b0a21572f3e0d150c822b380c69aae227cd373508e833325106be1d-Screenshot_2025-03-14_at_8.27.53_am.png" />

* Performance: 100
* Accessibility: 95
* Best Practices: 100
* SEO: 100

These scores demonstrate the application’s focus on speed, accessibility, and adherence to web standards, ensuring a seamless experience across devices.

> 👍 Quick Links
>
> * [Report API](https://api.basiq.io/reference/createreport)
> * Income Verification Starter Kit [Demo](https://iv-demo.basiq.io/)

<div
  style={{
    border: "2px solid #1E1E1E", // Dark border
    borderRadius: "8px",
    backgroundColor: "#1E1E1E", // Dark background
    padding: "16px",
    margin: "16px 0",
    fontFamily: "Arial, sans-serif",
    color: "#ffffff", // Light text for contrast
  }}
>
  <strong style={{ color: "#ffffff" }}>📢 Attention!</strong> If you have any issues, please reach out to our amazing support team.

  <div style={{ display: 'flex', alignItems: 'center' }}>
    <button
      onClick={() => Intercom('showNewMessage', 'issues on FAQs:')}
      style={{
        padding: '12px 30px',
        backgroundColor: '#1E1E1E',
        color: '#ffffff',
        border: '2px solid #ffffff', // Add contrast border if needed
        borderRadius: '50px',
        fontSize: '16px',
        fontWeight: '600',
        textTransform: 'uppercase',
        cursor: 'pointer',
        transition: 'background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease',
        outline: 'none',
        display: 'flex',
        justifyContent: 'center',
        height: '45px',
        position: 'relative',
        overflow: 'hidden',
        marginLeft: '10px',
        minWidth: '150px',
      }}
      onMouseEnter={(e) => {
        e.target.style.transform = 'scale(1.1)';
        e.target.style.backgroundColor = '#333333'; // Slightly lighter dark on hover
      }}
      onMouseLeave={(e) => {
        e.target.style.transform = 'scale(1)';
        e.target.style.backgroundColor = '#1E1E1E'; // Original dark
      }}
    >
      Support team
    </button>
  </div>
</div>