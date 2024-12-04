---
title: Enrich
excerpt: >-
  Enrich converts your banking transaction data into actionable insights by
  securely applying advanced tagging, cleaning, and enrichment processes to help
  you manage your finances effectively.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Overview

The Enrich resource provides detailed transaction data enrichment by enhancing bank transaction descriptions with additional attributes. The service categorises transactions and returns merchant information, location details, and industry-standard categorisation.

The data enrichment process on the Basiq platform involves four key steps:

* **Data Access**
* **Data Tagging, Cleaning, and Tokenization**
* **Data Enrichment**
* **Machine Learning and Final Output**

### Step 1: Data Access

Access a customer's transaction data by linking their bank accounts through Basiq Connect. Customers must provide consent to securely link their accounts and share their transaction information.

<Image align="center" src="https://files.readme.io/32cc5aaff084259cd8fdb45f14c298cdd43fcd3eedbe40bac925d7ba90fd7233-Connect.png" />

### Step 2: Data Tagging, Cleaning, and Tokenization

Once the raw transaction data is collected, it is categorised into debits and credits. Transactions are then tagged, cleaned, and standardised for enrichment. For instance:

* **Debit Transactions**: Bank fees, cash withdrawals, loan interest.
* **Credit Transactions**: Payments to merchants, refunds, interest earned, loan repayments.

Transactions are standardised to handle inconsistent formats across banks, ensuring reliable and accurate enrichment.

<Image align="center" src="https://files.readme.io/5dfc649473d62455c4eb2fd6d5b1f2c51ccfb63d8e971032b5cc09377765c85b-enrich_02-1024x111.png" />

<Image align="center" src="https://files.readme.io/e0241506d018400badbe27e32923f3670e74fe7b11bbfe5b0ef560bfc78dea8a-enrich_03-1024x282.png" />

### Step 3: Data Enrichment

Enriched data is matched against Basiq’s curated merchant database, which includes merchant identity, location, and categorisation details. 

Enrichment provides:

* **Merchant Information**: Business name, website, ABN, and contact details.
* **Location Information**: Address and geocode location.
* **Category Information**: A 4-level hierarchy of industry-standard categorisation.

<Image align="center" src="https://files.readme.io/09c6fffc4599bfc7531be8b6b96173424d7ac3ccaf7419e2691f294bab963715-enrich_04-1024x282.png" />

### Step 4: Machine Learning and Final Output

When a transaction cannot be immediately categorised, Basiq's machine learning model steps in. This model analyses transactions using additional data sources to ensure accurate categorisation and enrichment. It continuously improves through dynamic learning with each transaction processed.

<Image align="center" src="https://files.readme.io/6e3b72baa5e1635e7532c5345b888d76b63cf1182dc5f94885bc172774b47bd3-enrich_05-1024x178.png" />

<Image align="center" src="https://files.readme.io/6ae18a5fccb9da7adb901d027aaa2aedef62d59a90e64adffb887d72dbea9b46-enrich_06-1024x383.png" />

You can read complete blog post [here](https://www.basiq.io/blog/back-to-basics-what-is-data-enrichment/). 

## Enrich API

The Enrich resource enables you to retrieve details by passing in a search query containing a bank transaction description. The service enriches transaction data with multiple attributes, returning a transaction classification and three metadata components. The transaction classification will first determine if the transaction is of type payment, transfer, cash-withdrawal, bank-fee etc. The engine then derives merchant information, purchase location, and prescribes an industry standard categorisation for each payment transaction.

You can subscribe to one or all of the following three core datasets returned depending on your use case:

### Data

* **Merchant**: Details relating to the store or merchant such as business name, website, ABN, and contact details.
* **Location**: Details relating to the location of the entity such as address and geocode location.
* **Category**: Industry standard categorisation with a 4-level hierarchy for banking transactions.
* **Links**: Provides direct link to the original query and master and thumb merchant logos.

<Image align="center" src="https://files.readme.io/4cd1806802ba0d90402c51425e1f19af47147b56aa68c319c202bcf01b8b6097-enrich_07-1024x535.png" />

## Tags

The `tags` field is an array of strings that represents the classification of transactions based on various criteria. Here are the available tags and their use cases:

* **Card**: Represents card transactions. Example: `card:4615` (last four digits of the card number).
* **conduct**: Includes various keywords such as `card`, `overdrawn`, `cheque`, `atm`, `currency`, `late`, `admin`, `dishonour`, `interest`.
* **governmentPayment**: Includes keywords like `centrelink`, `crisisSupport`, `education`, `familyAllowance`, `jobseekerPymt`, `medicare`, `newstart`, `pension`, `rentalAssistance`, `vetAffairs`, `youthAllowance`.
* **income**: Includes tags such as `childSupport`, `insurance`, `investment`, `rent`, `salary`, `superannuation`.
* **liability**: Includes keywords like `afterpay`, `arl collect pty ltd`, `australian recoveries`, `axess`, `azora`, `baycorp`, `beforepay`, `brighte`, `bundll`, `cash converters`, `cash direct`, `cashngo`, `cash stop`, `cash train`, `ccc`, `cfmg pty ltd`, `charter mercantile`, `cigno`, `collectau`, `collection house`, `complete credit solutions`, `credit collection services`, `credit corp`, `creditline`, `deferit`, `dun and bradstreet`, `earnd`, `edstart`, `finance one`, `fundo`, `fupay`, `gem visa`, `humm`, `indebted`, `klarna`, `latitude`, `laybuy`, `limepay`, `lion finance`, `money3`, `moneyloop`, `mypaynow`, `nimble`, `nine25`, `openpay`, `panthera`, `payitlater`, `payright`, `pioneer credit`, `plenti`, `probe`, `q card`, `quickapay`, `spotmenow`, `sunshine loans`, `tapmypay`, `wagetap`, `wallet wizard`, `zip pay`.
* **third-party**: Includes tags like `apple pay`, `google`, `paypal`,` sp`, `sq`.
* **creditCard**: Represents credit card transactions.
* **expense**: Includes tags like rent.
* **loan**: Includes tags related to `loan` repayments.
* **mortgage**: Includes various mortgage providers and types such as `afg home loans`, `aims`, `amo group`, `athena`, `aussie`, `bluestone`, `clickloans`, `emoney`, `express reverse mortgage`, `firstmac`, `fox symes`, `freedom lend`, `freedom loans`, `funding`, `heartland reverse mortgages`, `homeloans`, `homestar`, `homestart`, `household capital`, `illawarra home loans`, `keystart`, `la trobe financial`, `liberty financial`, `loans`, `mortgage house`, `mortgage offset`, `mortgageport`, `mortgage repayment`, `onetwo`, `online home loans`, `pacific mortgage group`, `pepper money`, `qantas money`, `reduce home loans`, `resi`, `resimac`, `sucasa`, `switzer home loans`, `ticToc`, `unloan`, `vmg`, `well money`.

## Query Parameters

### Mandatory Arguments

* **q (string, required)**: The search string used to look up the entity (merchant) information. Example: `q=garfish%20MANLY%20NS`
* **institution (string, required)**: Identifies the institution from which the transaction was derived. Must be a Basiq-recognisable institution ID. Example: `institution=AU06703`
* **country (string, required)**: Specifies the country for the search. Must be in ISO 3166 Alpha-2 format. Example: `country=AU`

### Optional Arguments

* **mcc (string, optional)**: Merchant classification code as defined by Visa and Mastercard. Example: `mcc=3299`
* **accountType (string, optional)**: The account type from which the transaction was derived. Valid values: transaction, credit-card, savings, mortgage, loan, foreign. Example: `accountType=transaction`
* **amount (string, optional)**: The dollar/cent amount relevant to the transaction. Example: `amount=-12.95`

> 📘 Note:
>
> If `accountType` and `amount` are not provided, the query will be treated as a payment transaction and categorised accordingly.

## Request Example

```
GET /enrich?q=METRO%20PETROLEUM%20FR%20FORE&country=AU&accountType=transaction&amount=-12.95&institution=AU04301
Authorization: Bearer YOUR_ACCESS_TOKEN
```

### Response

The Enrich API will return a 200 HTTP response with a set of results for each dataset subscribed to: category, entity, and location. If no results are found for the search query, an empty result set will be returned. Invalid parameter inputs will result in an error.

### Prerequisites

* Authentication via the Basiq API service is required before calling the Enrich service.
* The service is only accessible to partners who have been enabled.

For more details, refer to the [Enrich API](https://api.basiq.io/reference/enrich).
