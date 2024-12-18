---
title: Reporting
excerpt: Reporting API
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The Reporting API for Consumer Affordability is a powerful tool designed to provide lenders with comprehensive insights into the financial health and affordability of their customers. Leveraging a combination of data from various sources including Consumer Data Rights (CDR), Web connectors, and Statement uploads, this feature enables lenders to make informed lending decisions while ensuring regulatory compliance and enhancing the overall customer experience.

## Key Features:

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

### BASIQ Dashboard Demo to Support Multiple Users:

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(50.10741138560687% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/WKGWSWQpYiCeNANWPuIj?embed" title="Basiq - Support Multiple Users in Reports" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

### Export Options:

You can export reports in PDF or CSV formats for record-keeping and detailed transaction analysis. Currently, the option to export in CSV and PDF is only available via the API.

When you click on the Print option in the Insights reports, you can choose the "Save as PDF" option.

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(54.55861070911722% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/dDGbKIIfrIypiqWanzA6?embed" title="Basiq - Dashboard Print / Export to PDF" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

### Bank Statement Export Capability:

Easily export [bank statements](https://api.basiq.io/docs/bank-statements) to support lending decisions.

## Resources:

### Video: Generating a Consumer Affordability Insights Report:

This video demonstrates how to generate a Consumer Affordability Insights report via the dashboard, providing a preview of the final PDF report.

<Embed url="https://www.youtube.com/watch?v=AM_0rBRC8O8" title="Generating a consumer affordability insights report" favicon="https://www.google.com/favicon.ico" image="https://i.ytimg.com/vi/AM_0rBRC8O8/hqdefault.jpg" provider="youtube.com" href="https://www.youtube.com/watch?v=AM_0rBRC8O8" typeOfEmbed="youtube" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252FAM_0rBRC8O8%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DAM_0rBRC8O8%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252FAM_0rBRC8O8%252Fhqdefault.jpg%26key%3D7788cb384c9f4d5dbbdbeffd9fe4b92f%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />

### Video: How Basiq's Reporting API Works:

An animated video showcasing how the reporting API cleans, normalizes, and enriches large datasets when integrated with customer applications.

<Embed url="https://www.youtube.com/watch?v=twqmjz0Aoo8" title="How Basiq's Reporting API works" favicon="https://www.google.com/favicon.ico" image="https://i.ytimg.com/vi/twqmjz0Aoo8/hqdefault.jpg" provider="youtube.com" href="https://www.youtube.com/watch?v=twqmjz0Aoo8" typeOfEmbed="youtube" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252Ftwqmjz0Aoo8%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253Dtwqmjz0Aoo8%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252Ftwqmjz0Aoo8%252Fhqdefault.jpg%26key%3D7788cb384c9f4d5dbbdbeffd9fe4b92f%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22640%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />

### Reports: Implementation Guide:

Detailed guide covering all steps required for successful implementation of the Basiq Affordability solution, including project steps and customer considerations.

<Embed url="https://basiq-hosted-files.s3.ap-southeast-2.amazonaws.com/docs-resources/Basiq%20-%20Platform%20Implementation_guide.pdf" provider="basiq-hosted-files.s3.ap-southeast-2.amazonaws.com" href="https://basiq-hosted-files.s3.ap-southeast-2.amazonaws.com/docs-resources/Basiq%20-%20Platform%20Implementation_guide.pdf" typeOfEmbed="pdf" title="undefined" html="%3Ciframe%20src%3D%22https%3A%2F%2Fdrive.google.com%2Fviewerng%2Fviewer%3Furl%3Dhttps%253A%2F%2Fbasiq-hosted-files.s3.ap-southeast-2.amazonaws.com%2Fdocs-resources%2FBasiq%252520-%252520Platform%252520Implementation_guide.pdf%26embedded%3Dtrue%22%20width%3D%22600%22%20height%3D%22780%22%20style%3D%22border%3A%20none%3B%22%3E%3C%2Fiframe%3E" />

You can also follow up our API reference [here](https://api.basiq.io/reference/createreport). 

## Reports: Groups & Metrics:

Customer-facing document displaying groups and metrics with definitions for the insights reporting solution.

### Metrics

| Section               | ID    | Title                                                 | Type    | Description                                                                                                                                           |
| --------------------- | ----- | ----------------------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Expenses              | ME015 | % of spend on discretionary expenses                  | percent | Mean monthly spend on discretionary expenses as a percentage of total outgoings                                                                       |
| Expenses              | ME013 | % of spend on non-discretionary expenses              | percent | Mean monthly spend on non-discretionary expenses as a percentage of total outgoings                                                                   |
| Expenses              | ME034 | Average Outgoings monthly                             | money   | Mean monthly total outgoings                                                                                                                          |
| Expenses              | ME039 | Average outgoings excluding liabilities               | money   | Mean monthly total outgoings excluding liability payments                                                                                             |
| Expenses              | ME014 | Monthly spend on discretionary expenses               | money   | Mean monthly spend on discretionary expenses                                                                                                          |
| Expenses              | ME012 | Monthly spend on non-discretionary expenses           | money   | Mean monthly spend on non-discretionary expenses                                                                                                      |
| Expenses              | ME016 | Monthly spend on other expenses                       | money   | Mean monthly spend on other expenses                                                                                                                  |
| Financial Commitments | ME008 | Average monthly amount                                | money   | Mean monthly repayments to lenders                                                                                                                    |
| Financial Commitments | ME009 | # of identified companies                             | integer | Number of relationships with lending merchants                                                                                                        |
| Financial Commitments | ME010 | Total credit card limit                               | money   | Total limits on available credit card accounts                                                                                                        |
| Financial Commitments | ME011 | Total credit card balance                             | money   | Total of latest available balances on available credit card accounts                                                                                  |
| Financial Commitments | ME046 | Average monthly ongoing amount to lenders             | money   | Ongoing monthly repayments to lenders                                                                                                                 |
| Financial Commitments | ME048 | Ongoing Monthly Mortgage Repayment                    | money   | Projected ongoing monthly mortgage repayments                                                                                                         |
| Government Services   | ME007 | Misc Government services monthly                      | money   | Mean monthly income through government benefits other than Rental Assistance and Youth Allowance                                                      |
| Government Services   | ME006 | Rental Assistance monthly                             | money   | Mean monthly income from Rental Assistance                                                                                                            |
| Government Services   | ME005 | Youth Allowance monthly                               | money   | Mean monthly income from Youth Allowance                                                                                                              |
| Summary               | ME040 | Average Monthly Credits                               | money   | Mean monthly credits excluding internal transfers                                                                                                     |
| Summary               | ME041 | Average Monthly Debits                                | money   | Mean monthly debits excluding internal transfers                                                                                                      |
| Income Sources        | ME001 | # of identified salary sources                        | integer | Number of recent salary income sources                                                                                                                |
| Income Sources        | ME002 | Average monthly amount from salary                    | money   | Mean monthly amount from salary income sources over the reporting period                                                                              |
| Income Sources        | ME003 | Salary has been stable for (months)                   | integer | Number of months within report over which salary has been stable                                                                                      |
| Income Sources        | ME004 | Other possible income monthly                         | money   | Mean monthly income from sources not covered within Salary and Benefits                                                                               |
| Income Sources        | ME033 | Average Income monthly                                | money   | Total forward looking monthly total income excluding tax, insurance, superannuation credits                                                           |
| Income Sources        | ME035 | Total Income has been stable for (months)             | integer | Number of months within report over which total income has been stable                                                                                |
| Income Sources        | ME036 | Median monthly amount from Salary                     | money   | Median of the monthly sum of transaction amounts for all transactions in Group INC009                                                                 |
| Income Sources        | ME037 | Median Income monthly                                 | money   | Sum of the individual group medians for all INC groups used in Metric ME033                                                                           |
| Income Sources        | ME042 | # of recent income sources                            | integer | Number of recent income sources across all income groups                                                                                              |
| Income Sources        | ME043 | # of ongoing regular income sources                   | integer | Number of recent income sources across all income groups where an income frequency has been detected                                                  |
| Income Sources        | ME045 | Total Income has been secure for (months)             | integer | Number of months within report over which total ongoing income has been stable or improving (secure)                                                  |
| Risk Flags            | ME022 | Has recent changes to salary circumstances            | boolean | Indicates new salary source in 2 months before end of reporting period or salary source stopping in 2 months prior to end of reporting period         |
| Risk Flags            | ME023 | Has received crisis support payments                  | boolean | Indicates if any crisis support income has been received during reporting period                                                                      |
| Risk Flags            | ME024 | Has superannuation credits                            | boolean | Indicates if any superannuation income has been received during reporting period                                                                      |
| Risk Flags            | ME025 | Has cash advances                                     | boolean | Indicates cash withdrawals from credit card accounts during reporting period                                                                          |
| Risk Flags            | ME026 | Has redraws                                           | boolean | Indicates transfers from mortgage accounts during reporting period                                                                                    |
| Risk Flags            | ME027 | Has High-Cost Finance                                 | boolean | Indicates repayments (during reporting period) to lenders that may charge high interest rates                                                         |
| Risk Flags            | ME028 | Missing non-discretionary expenses: groceries         | boolean | no instances of non-discretionary expenses: groceries detected                                                                                        |
| Risk Flags            | ME029 | Missing non-discretionary expenses: telecommunication | boolean | no instances of non-discretionary expenses: telecommunication detected                                                                                |
| Risk Flags            | ME030 | Missing non-discretionary expenses: utilities         | boolean | no instances of non-discretionary expenses: utilities detected                                                                                        |
| Risk Flags            | ME031 | Has Unemployment Benefit                              | boolean | Indicates if Jobseeker payments have been received                                                                                                    |
| Risk Flags            | ME032 | Receives Child Support                                | boolean | Indicates if child support payments have been detected                                                                                                |
| Risk Flags            | ME047 | Has unshared mortgage account                         | boolean | Indicates if mortgage payments are detected without a mortgage account having been shared                                                             |
| Risk Metrics          | ME019 | # of financial dishonours                             | integer | Number of financial dishonour transactions detected during reporting period                                                                           |
| Risk Metrics          | ME017 | # of SACC loans                                       | integer | Number of relationships with SACC lenders                                                                                                             |
| Risk Metrics          | ME020 | % of income spent on High Risk Activities             | percent | Percentage of income withdrawn at ATM's (including from credit cards), spent on gambling and credit card interest, and withdrawn via redraws          |
| Risk Metrics          | ME018 | % of income withdrawn via ATM                         | percent | Percentage of income withdrawn as cash at ATM's over the reporting period                                                                             |
| Risk Metrics          | ME021 | Total spend on High Risk Activities                   | money   | Total withdrawn at ATM's (including from credit cards), spent on gambling and credit card interest, and withdrawn via redraws during reporting period |

### Groups

| ID      | Title                         | Description                                                                                                        | Sections                                     |
| ------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- |
| EXP-001 | ATM Withdrawals               | Cash withdrawals from all account types other than credit-card                                                     | Other Expenses, High Risk Activities         |
| EXP-002 | Automotive                    | Automotive repair and service expenses                                                                             | Discretionary Expenses                       |
| EXP-003 | Cash Advances                 | Cash withdrawals from credit-cards                                                                                 | Other Expenses, High Risk Activities         |
| EXP-004 | Childrens Retail and Gaming   | Toys and games expenses                                                                                            | Discretionary Expenses                       |
| EXP-005 | Collection Agencies           | Repayments to collection agencies                                                                                  | Liabilities                                  |
| EXP-006 | Debt Interest Accrual         | Debit interest payments on credit-card and transaction accounts                                                    | Other Expenses, High Risk Activities         |
| EXP-007 | Department Stores             | Department store expenses                                                                                          | Discretionary Expenses                       |
| EXP-008 | Dining Out                    | Cafe, restaurant and fast food expenses                                                                            | Discretionary Expenses                       |
| EXP-009 | Dishonours                    | Dishonour fees                                                                                                     | Other Expenses, High Risk Activities         |
| EXP-010 | Donations                     | Donation expenses                                                                                                  | Discretionary Expenses                       |
| EXP-011 | Education and Childcare       | Educational and childcare expenses                                                                                 | Non-Discretionary Expenses                   |
| EXP-012 | Entertainment                 | Entertainment expenses including amusement parks, pubs, parks, arts                                                | Discretionary Expenses                       |
| EXP-013 | External Transfers            | Transfers to non-shared accounts                                                                                   | Other Expenses                               |
| EXP-014 | Gambling                      | Gambling expenses                                                                                                  | Discretionary Expenses, High Risk Activities |
| EXP-015 | Government & Council Services | Payments to government entities                                                                                    | Discretionary Expenses                       |
| EXP-016 | Groceries                     | Groceries and food retailing expenses                                                                              | Non-Discretionary Expenses                   |
| EXP-017 | Gyms and memberships          | Payments to gyms and fitness centres                                                                               | Discretionary Expenses                       |
| EXP-018 | Medical                       | Payments for medical services                                                                                      | Non-Discretionary Expenses                   |
| EXP-019 | Home Improvement              | Trade service expenses                                                                                             | Discretionary Expenses                       |
| EXP-020 | Insolvency                    | Payments to insolvency firms                                                                                       | Liabilities                                  |
| EXP-021 | Insurance                     | Insurance payments including health, life, motor and general                                                       | Non-Discretionary Expenses                   |
| EXP-023 | Motor Finance                 | Payments to vehicle lenders                                                                                        | Liabilities                                  |
| EXP-024 | Online Retail                 | Online retail expenses                                                                                             | Discretionary Expenses                       |
| EXP-025 | Other Finance                 | Payments to non-depository institutions including BNPL, payday lending, mortgage providers, and short term lending | Liabilities                                  |
| EXP-026 | Peer to Peer Finance          | Payments to peer-to-peer lenders                                                                                   | Liabilities                                  |
| EXP-027 | Personal Care                 | Personal care expenses                                                                                             | Discretionary Expenses                       |
| EXP-028 | Pet Care                      | Payments to pet stores or vets                                                                                     | Discretionary Expenses                       |
| EXP-029 | Redraws                       | Any debits from mortgage accounts                                                                                  | Other Expenses, High Risk Activities         |
| EXP-030 | Rent                          | Rental payments                                                                                                    | Non-Discretionary Expenses                   |
| EXP-031 | Retail                        | General retail expenses including furniture, electronics, clothing, footwear                                       | Discretionary Expenses                       |
| EXP-032 | Returns & Refunds             | Refunds (credits)                                                                                                  | Other Expenses                               |
| EXP-033 | Small Amount Lending          | Payments to SACC lenders                                                                                           | Liabilities                                  |
| EXP-035 | Subscription Media & Software | Payments for subscription media                                                                                    | Discretionary Expenses                       |
| EXP-036 | Telecommunication             | Telecoms expenses                                                                                                  | Non-Discretionary Expenses                   |
| EXP-038 | Travel                        | Travel expenses including hotels and flights                                                                       | Discretionary Expenses                       |
| EXP-039 | Uncategorised Debits          | Payments not categorised by Basiq Enrichment                                                                       | Discretionary Expenses                       |
| EXP-040 | Utilities                     | Payments to utility providers e.g. gas water and electricity                                                       | Non-Discretionary Expenses                   |
| EXP-041 | Vehicle and Transport         | Fuel and public transport expenses                                                                                 | Discretionary Expenses                       |
| EXP-051 | Alcohol and Tobacco           | Alcohol and tobacco expenses                                                                                       | Discretionary Expenses                       |
| EXP-052 | Sports and Hobbies            | Payments to sport retailers and sport clubs                                                                        | Discretionary Expenses                       |
| EXP-054 | Other Categorised             | Other categorised discretionary expenses not falling into any other discretionary groups                           | Discretionary Expenses                       |
| EXP-055 | Clothing and Footwear         | Clothing and footwear expenses                                                                                     | Discretionary Expenses                       |
| EXP-056 | Mortgage Repayments           | Credits on mortgage accounts                                                                                       | Liabilities                                  |
| EXP-057 | Loan Repayments               | Credits on loan accounts                                                                                           | Liabilities                                  |
| EXP-058 | Mortgage Transfers            | Transfers and Payments to mortgage accounts that have not been shared/declared                                     | Liabilities                                  |
| EXP-061 | Credit Card Repayments        | Credits on credit cards                                                                                            | Liabilities                                  |
| EXP-062 | Credit Card Transfers         | Transfers and Payments to credit cards that have not been shared/declared                                          | Liabilities                                  |
| EXP-063 | Loan Transfers                | Transfers and Payments to loan accounts that have not been shared/declared                                         | Liabilities                                  |
| INC-001 | Benefits                      | Government benefit payments including Centrelink, youth allowance, jobseeker                                       | Income                                       |
| INC-002 | Child Support Income          | Child support income                                                                                               | Income                                       |
| INC-003 | Insurance Credits             | Credits from insurance companies                                                                                   | Income                                       |
| INC-004 | Interest Income               | Interest credits over $50 on any shared accounts                                                                   | Income                                       |
| INC-005 | Investment Income             | Dividend income                                                                                                    | Income                                       |
| INC-006 | Other Earnings                | Income sources not falling into other income groups where credits are over $300                                    | Income                                       |
| INC-007 | Other Credits                 | Income sources not falling into other income groups where credits are under $300                                   | Income                                       |
| INC-008 | Rent & Board Income           | Rental income                                                                                                      | Income                                       |
| INC-009 | Salary                        | Salary income where credits are over $100 and salary keywords or phrases are detected                              | Income                                       |
| INC-010 | Superannuation Credits        | Superannuation credits                                                                                             | Income                                       |
| INC-012 | Youth Allowance               | Income from government youth allowance program                                                                     | Income                                       |
| INC-013 | Rental Assistance             | Income from government rental assistance program                                                                   | Income                                       |
| INC-014 | Centrelink                    | Income from government Centrelink program - excludes any Centrelink income that may be specific to other groups    | Income                                       |
| INC-015 | Medicare                      | Income from Medicare rebates                                                                                       | Income                                       |
| INC-016 | Jobseeker                     | Income from government Jobseeker program                                                                           | Income                                       |
| INC-018 | Pension                       | Pension income                                                                                                     | Income                                       |
| INC-019 | Carers                        | Income from government carers assistance program                                                                   | Income                                       |
| INC-020 | Education                     | Income from government education assistance program                                                                | Income                                       |
| INC-021 | Crisis Support                | Income from government crisis support program                                                                      | Income                                       |

## Conclusion:

The Report Consumer Affordability feature within Basiq Insights empowers lenders with robust tools and resources to assess consumer affordability accurately and efficiently. By leveraging a combination of advanced data analytics, comprehensive reporting, and user-friendly interfaces, Basiq Insights revolutionises lending practices, setting new standards for data-driven decision-making in the financial industry.

> 👍 Quick Links
>
> * [The Evolution of Lending - Basiq Blog Post ](https://basiq.io/blog/the-evolution-of-lending-introducing-basiq-insights/)
> * [Get Started?](https://api.basiq.io/reference/createreport)