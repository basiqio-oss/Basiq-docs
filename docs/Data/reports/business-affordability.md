---
title: Business Affordability Report
excerpt: Business Affordability Report API
deprecated: false
hidden: false
icon: 🆕
metadata:
  robots: index
---
The Business Affordability Report API is designed to give lenders and financial institutions deep insights into the financial health of business entities. Building on the foundation of our Consumer Affordability Report, this new report type offers a comprehensive financial snapshot tailored specifically for businesses—supporting better credit decisioning across all business sizes, from sole traders to large enterprises.

By leveraging business financial data and consent-based access, this feature empowers our partners to deliver smarter, faster, and more inclusive B2B lending and financial services.

## Key Features

### Business-Centric Financial Insight

* Purpose-built for analysing business finances—including income, expenses, account balances, and cash flow.
* Offers relevant groups and metrics focused on operational trends and financial viability.

### API and Dashboard Access

Available via:

* **API**: Accessible only to organisation-type users.
* **Dashboard**: Accessible via Reports Tab.

Supports JSON and PDF report formats for flexibility across technical and non-technical use cases.

> 📘 Enablement
>
> Please contact our support team for enablement for our Business Consumer Affordability Report.

### Purpose-Aligned Data Points

* Designed to reflect real-world business financial operations.
* Includes:
  * Balance history and trends.
  * Categorised income and expenses.
  * Financial ratios and liquidity indicators.
  * Risk profiling metrics.

### Smarter Decisioning for B2B Use Cases

* Reduces complexity and time in B2B lending workflows.
* Optimised for use cases such as:
  * Business loan origination.
  * Trade credit assessments.

### Competitive and Future-Ready

* Ensures your organisation stays ahead by offering a full-spectrum affordability solution across both consumers and businesses.
* Built to scale with new features and integrations as Open Banking for business evolves.

### Use Cases

The Business Affordability Report is ideal for:

* Lenders and Banks evaluating SME and enterprise applicants.
* Fintechs offering B2B credit, cash flow tools, or working capital services.
* Alternative Credit Providers needing enriched and fast business profiling.
* Embedded Finance Providers integrating lending into business platforms.

### Access to Data Sources:

* Future-proof your solution by accessing data from Consumer Data Rights (CDR), Web connectors, and Statement uploads.
* Seamlessly transition from screen scraping to Open Banking as banks adopt newer data access methods.

### Extensive Data Library:

* Access thousands of data points, over 60 groups, 50+ metrics, and more than 500 merchant categories for comprehensive reporting.

### Comprehensive Transaction Data Access:

* Gain access to over 12 months of transaction data from multiple financial institutions, offering a detailed view of a customer’s financial health.

### Advanced Data Categorisation:

* Enriched transaction details including merchant, location, and category, with expenses categorised into more than 500 categories based on ANZSIC classifications for detailed spend behavior analysis.

### Customisable Reporting:

* Generate custom reports tailored to meet unique decisioning criteria using a growing library of data points and metrics.

### Enhanced Decisioning Tools:

* Utilise an expanding set of groups and metrics to refine decision-making processes.

### Consolidated Multi-Account Reporting:

* Enable consolidated reporting across multiple bank accounts with integrated consent UI, allowing for individual or combined reports for multiple applicants.

### Predefined Risk Flags:

Benefit from an extensive library of risk flags designed for comprehensive decisioning, aiding in identifying gaps in financial information for thorough and accurate assessments.

### Powerful Enrichment Overlay Services:

Utilise machine learning for transaction cleansing and categorisation, enhancing data quality for deeper insights.

### Allow Multiple Users in Reports:

* **Modification of API**: The API will now accommodate requests for reports involving up to **five users**. Incorporate logic to manage requests with multiple users, ensuring avoidance of duplicate accounts.
* **Error Handling**: Proper error messages will be returned if duplicate accounts are detected or if a user/account is entered more than once.

### Business Affordability Dashboard Demo

<HTMLBlock>{`
<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(50.18807092960774% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/z8mv9NcBFMyJ2Dk1pkem?embed&embed_mobile=tab&embed_desktop=inline&show_copy_link=true" title="Basiq - Dashboard" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->
`}</HTMLBlock>

### Export Options:

You can export reports in PDF or CSV formats for record-keeping and detailed transaction analysis. Currently, the option to export in CSV and PDF is only available via the API.

<HTMLBlock>{`
<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(50.18807092960774% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/lCgdCtaQWmDJPzrskErt?embed&embed_mobile=tab&embed_desktop=inline&show_copy_link=true" title="Basiq - Export Business Affordability" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->
`}</HTMLBlock>

> 👍 Quick Links
>
> * [Create a Business Report? ](https://api.basiq.io/reference/createreport#/)
> * [List Report Types](https://api.basiq.io/reference/listreporttypes#/)