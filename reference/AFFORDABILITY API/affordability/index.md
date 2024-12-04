---
title: Affordability
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
The affordability object includes a summary of financial position, assets, liabilities, with links to an income object and an expenses object, for an individual user for account and transaction data stored against that user

> 📘 PDF response also available
>
> The affordability API returns a JSON response by default however you can specify to return a PDF report version of the affordability summary

> 👍 Sandbox testing the Affordability endpoint
>
> You will need to create a user and create or refresh all connections before creating an affordability resource.  Use the *Wentworth-Smith* test credentials to create a connection for our test institution AU00000 before calling the Affordability endpoint. See our [testing](https://api.basiq.io/reference/testing) section for more information.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Attributes
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `type`
      </td>

      <td style={{ textAlign: "left" }}>
        Value of this resource is "affordability"
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `id`
      </td>

      <td style={{ textAlign: "left" }}>
        The identifier of the affordability resource to be retrieved.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `fromMonth`
      </td>

      <td style={{ textAlign: "left" }}>
        Start month for the period for which the Affordability summary is generated. The period of time relates to the account and transaction data used as input into the report.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `toMonth`
      </td>

      <td style={{ textAlign: "left" }}>
        End month (usually the current month)  for the period for which the Affordability summary is generated.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `coverageDays`
      </td>

      <td style={{ textAlign: "left" }}>
        Number of days included in the report period.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `generatedDate`
      </td>

      <td style={{ textAlign: "left" }}>
        Date the report was generated. e.g. "2018-09-12T00:59:28"
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Summary
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `assets`
      </td>

      <td style={{ textAlign: "left" }}>
        Total of cash based assets
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `liabilities`
      </td>

      <td style={{ textAlign: "left" }}>
        Total of account based liabilities split into credit and loan liabilities
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `netPosition`
      </td>

      <td style={{ textAlign: "left" }}>
        Total assets minus total liabilities
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `creditLimit`
      </td>

      <td style={{ textAlign: "left" }}>
        Total credit limit across all credit cards and overdrafts
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `regularIncome`
      </td>

      <td style={{ textAlign: "left" }}>
        Provides an average of monthly - `avgMonthly` regular income calculated over the previous 3 month period `previous3Months`.

        For example:\
        "regularIncome": \{\
                    "previous3Months": \{\
                        "avgMonthly": "5000.00"\
                    }\
                }
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `expenses`
      </td>

      <td style={{ textAlign: "left" }}>
        Provides an average of monthly expenses calculated for the whole period of data retrieved (e.g. 13 months)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `savings`
      </td>

      <td style={{ textAlign: "left" }}>
        Average of monthly savings calculated for the whole period of data retrieved (e.g. 13 months)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Assets
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `type`
      </td>

      <td style={{ textAlign: "left" }}>
        Value of this resource is "account"
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `currency`
      </td>

      <td style={{ textAlign: "left" }}>
        The currency in which the account is recorded.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `balance`
      </td>

      <td style={{ textAlign: "left" }}>
        The balance at the time of the query.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `availableFunds`
      </td>

      <td style={{ textAlign: "left" }}>
        The available funds at the time of the query.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `account`
      </td>

      <td style={{ textAlign: "left" }}>
        Identifies the **type** and **product** of the account:
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `type` (values as defined in `class` object `Account Type` in [Accounts](ref:accounts)

        * `product` (as defined by the institution)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `institution`
      </td>

      <td style={{ textAlign: "left" }}>
        The name of the financial institution with whom the account is held.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `previous6months`
      </td>

      <td style={{ textAlign: "left" }}>
        Includes minimum and maximum balances recorded in the account of the queried period.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `minBalance`

        * `maxBalance`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Credit Liabilities
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `currency`
      </td>

      <td style={{ textAlign: "left" }}>
        The currency in which the account is recorded.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `balance`
      </td>

      <td style={{ textAlign: "left" }}>
        The balance at the time of the query.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `availableFunds`
      </td>

      <td style={{ textAlign: "left" }}>
        The available funds at the time of the query.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `account`
      </td>

      <td style={{ textAlign: "left" }}>
        Identifies the **type** and **product** of the account:
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `type` (values as defined in `class` object `Account Type` in [Accounts](ref:accounts)

        * `product` (as defined by the institution)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `institution`
      </td>

      <td style={{ textAlign: "left" }}>
        The name of the financial institution with whom the account is held.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `previousMonth`
      </td>

      <td style={{ textAlign: "left" }}>
        A summary of the credit facility activity of the previous month, consisting of:
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `totalCredits`

        * `totalDebits`

        * `minBalance`

        * `maxBalance`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `previous6months`
      </td>

      <td style={{ textAlign: "left" }}>
        Acknowledges any cash advances made in the previous 6 months:
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `cashAdvances` - value of cash advances in period
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `creditLimit`
      </td>

      <td style={{ textAlign: "left" }}>
        Total credit limit available for the specified credit facility.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Loan Liabilities
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `currency`
      </td>

      <td style={{ textAlign: "left" }}>
        The currency in which the account is recorded.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `balance`
      </td>

      <td style={{ textAlign: "left" }}>
        The balance at the time of the query.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `availableFunds`
      </td>

      <td style={{ textAlign: "left" }}>
        The available funds at the time of the query.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `account`
      </td>

      <td style={{ textAlign: "left" }}>
        Identifies the **type** and **product** of the account:
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `type` (values as defined in `class` object `Account Type` in [Accounts](ref:accounts)

        * `product` (as defined by the institution)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `institution`
      </td>

      <td style={{ textAlign: "left" }}>
        The name of the financial institution with whom the account is held.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `previousMonth`
      </td>

      <td style={{ textAlign: "left" }}>
        A summary of the credit facility activity of the previous month, consisting of:
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `totalCredits`

        * `totalDebits`

        * `totalInterestCharged`

        * `totalRepayments`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `changeHistory`
      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `direction`  - debit or credit

        * `amount` - amount loan-interest or loan-repayment

        * `date`  - date  e.g. "2019-03-15T17:00:00"

        * `source` - cleaned transaction description
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `previous6months`
      </td>

      <td style={{ textAlign: "left" }}>
        Acknowledges if the account is in repayment arrears:
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `arrears` - has the loan been in arrears in the past 6 months -  returned as a **string** value (*true* or *false* or *null*)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

> 📘 External Relationships *new*
>
> New Affordability feature to surface external relationships (e.g. Latitude Loans) that are held externally to the bank accounts that have not been disclosed or linked by the user e.g. surfacing buy now pay later services. These are now represented now as external payments rather than living expenses. Identified external relationships are grouped under this new attribute `external`.  The first version of this feature is for a selection of the [32 most common merchants](https://api.basiq.io/reference#2021-03) for small pay-day loans, buy now pay later services and collections agencies.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        External
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `source`
      </td>

      <td style={{ textAlign: "left" }}>
        Source of external payment (cleaned transaction description).
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `payments`
      </td>

      <td style={{ textAlign: "left" }}>
        Aggregated attributes relating to payments for this source (identified as an external)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `first`  - date of first payment e.g. "2019-03-15"

        * `last` - date of last payment e.g. "2020-03-15"

        * `noOccurrences`  - number of occurrences for same source (in this group)

        * `amountAvg` - average amount of payment e.g. "-50.50"

        * `amountAvgMonthly` - average monthly payment amount e.g. "-20.00"

        * `total` - amount of total payments identified for source in the affordability snapshot e.g. "-146.50"
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `changeHistory`
      </td>

      <td style={{ textAlign: "left" }}>
        Each transaction (repeated for each source ordered by most recent):
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `amount` - amount of payment

        * `date`  - date  e.g. "2019-03-15"

        * `source` - full transaction description
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Links
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `links`
      </td>

      <td style={{ textAlign: "left" }}>
        A links object containing the following members:
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `self` - link to the affordability resource

        * `income` - [income](https://api.basiq.io/reference/income)

        * `expenses` - [expenses](https://api.basiq.io/reference/expenses)

        * `accounts` - an array of [accounts](https://api.basiq.io/reference/accounts)\
          links
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

> 🚧 You will need to create a user and create or refresh all connections before creating the affordability resource.

**Returns**

Returns a created affordability resource, if the operation succeeded. Returns an [error](https://api.basiq.io/docs/errors-1) if the post failed (e.g. not supplying required properties).

```json Example Affordability object
{
  "type": "affordability",
  "id": "s55bf3",
  "fromMonth": "2019-03",
  "toMonth": "2020-03",
  "coverageDays": 392,
  "generatedDate": "2020-03-26T06:56:44",
  "summary": {
    "assets": "59983.11",
    "liabilities": "-323946.20",
    "netPosition": "-263963.09",
    "creditLimit": "20000.00",
    "expenses": "-12046.00",
    "savings": "93.00",
    "regularIncome": {
      "previous3Months": {
        "avgMonthly": "18098.00"
      }
    }
  },
  "assets": [
    {
      "currency": "AUD",
      "balance": "35298.67",
      "availableFunds": "35298.67",
      "institution": "Hooli",
      "type": "account",
      "account": {
        "product": "Hooli Saver",
        "type": "savings"
      },
      "previous6Months": {
        "minBalance": "32427.79",
        "maxBalance": "34798.67"
      }
    },
    {
      "currency": "AUD",
      "balance": "24684.44",
      "availableFunds": "24684.44",
      "institution": "Hooli",
      "type": "account",
      "account": {
        "product": "Hooli Transaction",
        "type": "transaction"
      },
      "previous6Months": {
        "minBalance": "10032.81",
        "maxBalance": "38309.44"
      }
    }
  ],
  "liabilities": {
    "loan": [
      {
        "currency": "AUD",
        "balance": "-312233.00",
        "availableFunds": "87767.00",
        "institution": "Hooli",
        "account": {
          "type": "mortgage",
          "product": "Hooli Home Loan"
        },
        "previousMonth": {
          "totalCredits": "5768.00",
          "totalDebits": "-4303.50",
          "totalInterestCharged": "-4303.50",
          "totalRepayments": "5768.00"
        },
        "changeHistory": [
          {
            "direction": "debit",
            "amount": "-4220.75",
            "date": "2019-03-19",
            "source": "Mortgage Interest Payment 746833"
          },
          {
            "direction": "credit",
            "amount": "5768.00",
            "date": "2019-03-31",
            "source": "Transfer Platnm Homeloan 346454"
          },
          {
            "direction": "debit",
            "amount": "-4228.50",
            "date": "2019-04-19",
            "source": "Mortgage Interest Payment 746833"
          }
        ],
        "previous6Months": {
          "arrears": false
        }
      }
    ],
    "credit": [
      {
        "currency": "AUD",
        "balance": "-11713.20",
        "availableFunds": "8286.80",
        "institution": "Hooli",
        "creditLimit": "20000.00",
        "account": {
          "type": "credit-card",
          "product": "Hooli Visa"
        },
        "previousMonth": {
          "totalCredits": "0.00",
          "totalDebits": "-8287.10",
          "minBalance": "-3174.16",
          "maxBalance": "-12329.16"
        },
        "previous6Months": {
          "cashAdvances": "-2053.50"
        }
      }
    ]
  },
  "external": [
    {
      "source": "afterpay",
      "payments": {
        "first": "2019-11-15",
        "last": "2019-11-15",
        "noOccurrences": 2,
        "amountAvg": "-146.50",
        "amountAvgMonthly": "-12.00",
        "total": "-146.50"
      },
      "changeHistory": [
        {
          "amount": "-146.50",
          "date": "2019-11-15",
          "source": "AFTERPAY MELBOURNE VI AUS Card xx3854 Value Date: 10/11/2019"
        },
        {
          ...
        }
      ]
    }
  ],
  "links": {
    "self": "https://au-api.basiq.io/users/25c8d1ed77/affordability/s55bf3",
    "income": "https://au-api.basiq.io/users/25c8d1ed77/income/s55bf4",
    "expenses": "https://au-api.basiq.io/users/25c8d1ed77/expenses/s55bf5",
    "accounts": [
      "https://au-api.basiq.io/users/25c8d1ed77/accounts/20024b08",
      "https://au-api.basiq.io/users/25c8d1ed77/accounts/64880430",
      "https://au-api.basiq.io/users/25c8d1ed77/accounts/55bf3089",
      "https://au-api.basiq.io/users/25c8d1ed77/accounts/6jk43056"
    ]
  }
}
```
