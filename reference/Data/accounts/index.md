---
title: Accounts
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
The account object represents an account held with a financial institution (e.g. a savings account). You can use this object to retrieve specific account details such as the account number, balance and available funds.

```json accounts
{
  "type": "list",
  "data": [
    {
      "type": "account",
      "id": "s55bf3",
      "depositRate": "string",
      "lendingRate": "string",
      "bsb": "string",
      "unmaskedAccNum": "string",
      "creationDate": "string",
      "accountHolder": "GAVIN BELSON",
      "maskedNumber": "string",
      "accountOwnership": "ONE_PARTY",
      "isOwned": true,
      "amortisedLimit": "string",
      "bundleName": "string",
      "accountNo": "600000157441965",
      "availableFunds": "420.28",
      "balance": "356.50",
      "creditLimit": "400000.00",
      "class": {
        "type": "mortgage",
        "product": "Hooli Home Loan"
      },
      "connection": "8fce3b",
      "currency": "AUD",
      "institution": "AU00000",
      "lastUpdated": "2019-09-28T13:39:33Z",
      "name": "Master Savings",
      "status": "available",
      "meta": {
        "fees": [
          {
            "name": "Dishonour fee",
            "feeType": "EVENT",
            "amount": "10.00",
            "balanceRate": "string",
            "transactionRate": "string",
            "accruedRate": "string",
            "accrualFrequency": "P1M",
            "currency": "string",
            "additionalValue": "string",
            "additionalInfo": "string",
            "additionalInfoUri": "string",
            "discounts": {
              "description": "string",
              "discountType": "string",
              "amount": "string",
              "balanceRate": "string",
              "transactionRate": "string",
              "accruedRate": "string",
              "feeRate": "string",
              "additionalValue": "string",
              "additionalInfo": "string",
              "additionalInfoUri": "string",
              "eligibility": {
                "discountEligibilityType": "BUSINESS",
                "additionalValue": "string",
                "additionalInfo": "string",
                "additionalInfoUri": "string"
              }
            }
          }
        ],
        "depositRates": [
          {
            "depositRateType": "VARIABLE",
            "rate": "0.0385",
            "calculationFrequency": "string",
            "applicationFrequency": "P1M",
            "tiers": {
              "name": "string",
              "unitOfMeasure": "DAY",
              "minimumValue": 0,
              "maximumValue": 0,
              "rateApplicationMethod": "PER_TIER",
              "applicabilityConditions": {
                "additionalInfo": "string",
                "additionalInfoUri": "string"
              },
              "additionalInfo": "string",
              "additionalInfoUri": "string"
            },
            "additionalValue": "string",
            "additionalInfo": "string",
            "additionalInfoUri": "string"
          }
        ],
        "lendingRates": [
          {
            "lendingRateType": "PURCHASE",
            "rate": "0.2024",
            "comparisonRate": "string",
            "calculationFrequency": "string",
            "applicationFrequency": "string",
            "interestPaymentDue": "IN_ADVANCE",
            "repaymentType": "INTEREST_ONLY",
            "loanPurpose": "INVESTMENT",
            "tiers": {
              "name": "string",
              "unitOfMeasure": "DAY",
              "minimumValue": 0,
              "maximumValue": 0,
              "rateApplicationMethod": "PER_TIER",
              "applicabilityConditions": {
                "additionalInfo": "string",
                "additionalInfoUri": "string"
              },
              "additionalInfo": "string",
              "additionalInfoUri": "string"
            },
            "additionalValue": "string",
            "additionalInfo": "string",
            "additionalInfoUri": "string"
          }
        ],
        "termDeposit": [
          {
            "lodgementDate": "string",
            "maturityDate": "string",
            "maturityAmount": "string",
            "maturityCurrency": "string",
            "maturityInstructions": "PAID_OUT_AT_MATURITY"
          }
        ],
        "loan": {
          "startDate": "2019-10-01",
          "endDate": "2045-10-01",
          "repaymentType": "PRINCIPAL_AND_INTEREST",
          "loanAmount": "string",
          "loanCurrency": "string",
          "nextInstalmentDate": "string",
          "minInstalmentAmount": "string",
          "minInstalmentCurrency": "string",
          "maxRedraw": "string",
          "maxRedrawCurrency": "string",
          "minRedraw": "string",
          "minRedrawCurrency": "string",
          "offsetAccountEnabled": true,
          "offsetAccountIds": [
            "string"
          ],
          "repaymentFrequency": "string"
        },
        "creditCard": {
          "minPaymentAmount": "117.00",
          "paymentDueAmount": "5847.00",
          "paymentCurrency": "AUD",
          "paymentDueDate": "2023-12-12"
        },
        "addresses": [
          {
            "addressType": "paf",
            "simple": {
              "mailingName": "string",
              "addressLine1": "string",
              "addressLine2": "string",
              "addressLine3": "string",
              "postcode": "string",
              "city": "string",
              "state": "string",
              "country": "string",
              "paf": {
                "dpid": "string",
                "thoroughfareNumber1": 0,
                "thoroughfareNumber1Suffix": "string",
                "thoroughfareNumber2": 0,
                "thoroughfareNumber2Suffix": "string",
                "flatUnitType": "string",
                "flatUnitNumber": "string",
                "floorLevelType": "string",
                "floorLevelNumber": "string",
                "lotNumber": "string",
                "buildingName1": "string",
                "buildingName2": "string",
                "streetName": "string",
                "streetType": "string",
                "streetSuffix": "string",
                "postalDeliveryType": "string",
                "postalDeliveryNumber": 0,
                "postalDeliveryNumberPrefix": "string",
                "postalDeliveryNumberSuffix": "string",
                "localityName": "string",
                "postcode": "string",
                "state": "string"
              }
            }
          }
        ]
      },
      "transactionIntervals": [
        {
          "from": "2018-07-01",
          "to": "2018-12-30"
        }
      ]
    }
  ],
  "links": {
    "self": "https://au-api.basiq.io/users/cd6fbd92/accounts/319ae910",
    "transactions": "https://au-api.basiq.io/users/ea3a81/transactions?filter=account.id.eq('s55bf3')",
    "connection": "https://au-api.basiq.io/users/cd6fbd92/connections/321312asa",
    "institution": "https://au-api.basiq.io/institutions/AU00000",
    "statements": []
  }
}
```

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Attributes
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        id
      </td>

      <td style={{ textAlign: "left" }}>
        Uniquely identifies the account.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        accountHolder
      </td>

      <td style={{ textAlign: "left" }}>
        The name of the account holder as returned by the institution. No formatting is applied. Returns a string or null when not available.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        accountOwnership
      </td>

      <td style={{ textAlign: "left" }}>
        Value indicating the number of customers that have ownership of the account, according to the data holder's definition of account ownership. Does not indicate that all account owners are eligible consumers.  

        The enum options for accountOwnership are:  

        UNKNOWN\
        ONE\_PARTY\
        TWO\_PARTY\
        MANY\_PARTY\
        OTHER
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        accountNo
      </td>

      <td style={{ textAlign: "left" }}>
        Full account number. This represents the unified form of the BSB and Account Number where applicable.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        availableFunds
      </td>

      <td style={{ textAlign: "left" }}>
        Funds that are available to an account holder for withdrawal or other use. This may include funds from an overdraft facility or line of credit. As well as funds classified as the available balance, such as from cleared and existing deposits.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        balance
      </td>

      <td style={{ textAlign: "left" }}>
        Amount of funds in the account right now - excluding any pending transactions. For a credit card, this would be zero or the minus amount spent.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        creditLimit
      </td>

      <td style={{ textAlign: "left" }}>
        Eligible account types are credit-card, loan, and mortgage.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        class.type
      </td>

      <td style={{ textAlign: "left" }}>
        Account type.  

        * `transaction`: A transaction account is a type of bank account that allows frequent deposits, withdrawals, and transactions. It is primarily used for day-to-day banking activities, such as paying bills, making purchases, and transferring funds. Transaction accounts often do not earn interest and may have lower or no minimum balance requirements.
        * `savings`: A savings account is a bank account designed for accumulating savings. It typically offers interest on the account balance, allowing the account holder to earn a return on their savings over time. Savings accounts may have restrictions on the number of withdrawals or transactions allowed per month and may require a minimum balance to be maintained.
        * `credit-card`: A credit card account represents a line of credit extended by a financial institution to the account holder. It allows the cardholder to make purchases and access funds up to a predetermined credit limit. The cardholder is required to make regular repayments on the outstanding balance, and interest is charged on the unpaid amount if not paid in full by the due date.
        * `mortgage`: A mortgage account represents a loan provided by a financial institution to finance the purchase of a property. The mortgage account is used to track the outstanding balance, interest rate, and repayment terms associated with the mortgage loan. The borrower makes regular repayments to gradually pay off the loan over an agreed-upon term.
        * `loan`: A loan account represents a financial arrangement where a financial institution provides funds to an individual or entity, which must be repaid over time with interest. Loan accounts can include personal loans, car loans, student loans, or other types of installment loans. The account tracks the loan balance, interest rate, and repayment schedule.
        * `investment`: An investment account represents an account used for investment purposes, such as buying and selling securities (stocks, bonds, etc.) or participating in investment funds. Investment accounts provide the ability to hold and manage investments, track portfolio performance, and execute investment transactions.
        * `term-deposit`: A term deposit account, also known as a certificate of deposit (CD), is a fixed-term investment account with a specified duration. The funds are deposited for a predetermined period, and the account holder earns interest on the deposit. Term deposit accounts typically have higher interest rates than regular savings accounts but have limited flexibility for early withdrawals.
        * `insurance`: An insurance account represents an account associated with an insurance policy. It tracks the premium payments, policy coverage details, and other relevant information related to the insurance contract. Insurance accounts can be used for various types of insurance, such as life insurance, health insurance, auto insurance, or property insurance.
        * `foreign`: A foreign account represents a bank account held in a foreign currency. It allows the account holder to hold and transact in a currency other than their domestic currency. Foreign accounts are commonly used for international business transactions, travel, or to manage funds in different currencies.
        * `unknown`: An unknown account represents a bank account with an unknown or unspecified type. It may indicate that the specific type of the account could not be determined or is not within the predefined account types."
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        class.product
      </td>

      <td style={{ textAlign: "left" }}>
        Product name.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        connection
      </td>

      <td style={{ textAlign: "left" }}>
        The ID of the connection resource that was used to retrieve the account.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        currency
      </td>

      <td style={{ textAlign: "left" }}>
        The currency the funds are stored in, using [ISO 4217](https://www.iban.com/currency-codes.html) standard.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        institution
      </td>

      <td style={{ textAlign: "left" }}>
        The ID of the institution resource the account originated from.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        lastUpdated
      </td>

      <td style={{ textAlign: "left" }}>
        Timestamp of the last update in UTC, RFC 3339 format (e.g., "2017-09-28T13:39:33Z").
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        name
      </td>

      <td style={{ textAlign: "left" }}>
        Account name as defined by the institution or user.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        status
      </td>

      <td style={{ textAlign: "left" }}>
        Account status.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        transactionIntervals
      </td>

      <td style={{ textAlign: "left" }}>
        An array of date intervals indicating the coverage of the transaction data relating to the account. Will return a single element for accounts sourced from a single bank connection. Will return multiple elements in cases where there have been multiple PDF/CSV uploads for an account.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        transactionIntervals.from
      </td>

      <td style={{ textAlign: "left" }}>
        Date of the first transaction on this account.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        transactionIntervals.to
      </td>

      <td style={{ textAlign: "left" }}>
        Date of the last transaction on this account.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        meta.fees
      </td>

      <td style={{ textAlign: "left" }}>
        Array of fees associated with the account.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        fees.name
      </td>

      <td style={{ textAlign: "left" }}>
        Name of the fee.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        fees.feeType
      </td>

      <td style={{ textAlign: "left" }}>
        The type of fee. Possible values:  

        * `DEPOSIT`: A fee associated with making a deposit into the bank account.
        * `EVENT`: A fee associated with a specific event related to the bank account, such as account closure or account activation.
        * `EXIT`: A fee charged when closing the bank account.
        * `PAYMENT`: A fee charged for a payment made from the bank account, such as a payment to a third party or a bill payment.
        * `PERIODIC`: A recurring fee charged periodically for maintaining the bank account.
        * `PURCHASE`: A fee associated with a purchase made using the bank account, such as a transaction fee for each purchase made with a debit card.
        * `TRANSACTION`: A fee charged for each transaction made from the bank account, such as a fee for each withdrawal or transfer made.
        * `UPFRONT`: A fee charged upfront, typically at the time of account opening or initiation.
        * `VARIABLE`: A fee that can vary depending on certain factors, such as the transaction amount or account balance.
        * `WITHDRAWAL`: A fee charged for each withdrawal made from the bank account, such as a fee for each ATM withdrawal or cash withdrawal."
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        fees.amount
      </td>

      <td style={{ textAlign: "left" }}>
        The amount charged for the fee.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        fees.accrualFrequency
      </td>

      <td style={{ textAlign: "left" }}>
        The indicative frequency with which the fee is calculated on the account.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        meta.depositRates
      </td>

      <td style={{ textAlign: "left" }}>
        Array of deposit rates associated with the account.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        depositRates.depositRateType
      </td>

      <td style={{ textAlign: "left" }}>
        The type of rate (base, bonus, etc.) for deposit rates. Possible values:  

        * `BONUS`: A bonus rate offered on a bank account, typically provided as an incentive for opening the account or meeting certain conditions.
        * `BUNDLE_BONUS`: A bundle bonus rate offered on a bank account, which is a bonus rate provided when multiple products or services are bundled together, such as having a linked savings account or using other bank services.
        * `FIXED`: A fixed deposit rate that remains constant over a specific period, providing stability and predictable interest earnings on the bank account.
        * `FLOATING`: A floating deposit rate that can fluctuate based on market conditions or other factors, offering potential changes in interest earnings on the bank account.
        * `INTRODUCTORY`:  An introductory deposit rate offered for a limited period when opening a new bank account, usually higher than the standard rate to attract new customers.
        * `MARKET_LINKED`: A market-linked deposit rate that is tied to a specific financial market index or benchmark, with interest earnings adjusted based on the performance of the market index.
        * `VARIABLE`: A variable deposit rate that can change over time, typically influenced by factors such as the prevailing market conditions or the bank's discretion.        "
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        depositRates.rate
      </td>

      <td style={{ textAlign: "left" }}>
        The rate to be applied for the deposit rate type.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        depositRates.applicationFrequency
      </td>

      <td style={{ textAlign: "left" }}>
        The period after which the calculated amount(s) are 'applied' (i.e., debited or credited) to the account for deposit rates.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        meta.lendingRates
      </td>

      <td style={{ textAlign: "left" }}>
        Array of lending rates associated with the account.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        lendingRates.lendingRateType
      </td>

      <td style={{ textAlign: "left" }}>
        The type of rate (fixed, variable, etc.) for lending rates. Possible values:  

        * `BUNDLE_DISCOUNT_FIXED`: A fixed lending rate with a bundle discount applied. This type of rate is associated with a bundle or package offered by the bank, where the borrower receives a discounted interest rate on the loan as part of the package benefits.
        * `BUNDLE_DISCOUNT_VARIABLE`: A variable lending rate with a bundle discount applied. Similar to the fixed bundle discount rate, this type of rate is associated with a bundle or package offered by the bank, where the borrower receives a discounted interest rate on the loan that can vary over time based on market conditions or other factors.
        * `CASH_ADVANCE`: A lending rate associated with cash advances made using a credit card or a similar facility. Cash advances typically have different interest rates compared to regular purchases or transactions, and this rate represents the interest applied to the amount borrowed as a cash advance.
        * `DISCOUNT`: A discounted lending rate offered on a loan, usually as an incentive or promotional rate. This type of rate allows borrowers to benefit from a reduced interest rate for a specific period or under certain conditions, providing potential interest savings during the discounted period.
        * `FIXED`: A fixed lending rate that remains constant over a specific period, offering borrowers stability and predictable interest payments throughout the loan term.
        * `FLOATING`: A floating lending rate that can change over time, typically influenced by market conditions or other factors. The interest rate fluctuates along with a reference rate or index, such as a benchmark rate or a market-determined rate. Borrowers with floating rate loans may experience changes in their interest payments in response to fluctuations in the reference rate.
        * `INTRODUCTORY`: An introductory lending rate provided for a limited period at the beginning of a loan. This rate is usually lower than the standard or ongoing rate and is offered as an incentive to attract borrowers. Borrowers can benefit from a reduced interest expense during the introductory period before the rate reverts to the regular rate.
        * `MARKET_LINKED`: A lending rate linked to a specific financial market index or benchmark. The interest rate on the loan is adjusted periodically based on the performance of the market index. This type of rate reflects changes in market conditions and provides borrowers with interest rate variations that align with the movement of the underlying market index.
        * `PENALTY`: A penalty lending rate applied when a borrower fails to meet certain obligations or breaches the terms of the loan agreement. Penalties may be imposed for late payments, defaults, or other specified events. The penalty rate is generally higher than the standard rate and serves as a disincentive for non-compliance with the loan terms.
        * `PURCHASE`: A lending rate associated with purchases made using a credit card or a similar facility. This rate represents the interest charged on the outstanding balance for purchases made on the credit card, typically different from cash advance rates or other types of transactions.
        * `VARIABLE`: A variable lending rate that can change over time based on various factors, such as market conditions, economic indicators, or changes in the bank's lending policy. Borrowers with variable rate loans may experience fluctuations in their interest payments, as the rate adjusts periodically according to predetermined criteria or market conditions.
        * `IN_ADVANCE`: A lending rate calculated based on an upfront interest payment made in advance. In this type of rate, the interest expense is paid at the beginning of the loan. "
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        lendingRates.rate
      </td>

      <td style={{ textAlign: "left" }}>
        The rate to be applied for the lending rate type.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        lendingRates.applicationFrequency
      </td>

      <td style={{ textAlign: "left" }}>
        The period after which the calculated amount(s) are applied (i.e., debited or credited) to the account for lending rates.Formatted according to [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations) (excludes recurrence syntax)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        meta.loan
      </td>

      <td style={{ textAlign: "left" }}>
        loan metadata associated with the account.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        loan.startDate
      </td>

      <td style={{ textAlign: "left" }}>
        Start date for the loan.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        loan.endDate
      </td>

      <td style={{ textAlign: "left" }}>
        Date that the loan is due to be repaid in full.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        loan.repaymentType
      </td>

      <td style={{ textAlign: "left" }}>
        Options in place for repayments. If absent, defaults to `PRINCIPAL_AND_INTEREST`. Possible values:  

        * `INTEREST_ONLY`: A repayment type where the borrower is only required to pay the interest amount on the loan during a specified period, typically for an initial period. With interest-only repayments, the borrower does not make principal repayments, resulting in lower monthly payments. However, at the end of the interest-only period, the borrower will be required to start making principal and interest repayments.

        * `PRINCIPAL_AND_INTEREST`: The most common repayment type where the borrower makes regular repayments that include both principal and interest amounts. With each repayment, a portion goes towards reducing the loan principal, while the remaining amount covers the accrued interest. Over time, the principal reduces, and the interest portion decreases accordingly. This repayment type ensures gradual loan repayment until the loan is fully paid off."
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        loan.minInstalmentAmount
      </td>

      <td style={{ textAlign: "left" }}>
        Minimum amount of the next installment.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        meta.creditCard
      </td>

      <td style={{ textAlign: "left" }}>
        Array of credit card metadata associated with the account.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        creditCard.minPaymentAmount
      </td>

      <td style={{ textAlign: "left" }}>
        The minimum payment amount due for the next card payment.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        creditCard.paymentDueAmount
      </td>

      <td style={{ textAlign: "left" }}>
        The amount due for the next card payment.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        creditCard.paymentCurrency
      </td>

      <td style={{ textAlign: "left" }}>
        If absent, assumes `AUD`.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        creditCard.paymentDueDate
      </td>

      <td style={{ textAlign: "left" }}>
        Date that the next payment for the card is due.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        links.self
      </td>

      <td style={{ textAlign: "left" }}>
        URL of the requested account.
      </td>
    </tr>
  </tbody>
</Table>
