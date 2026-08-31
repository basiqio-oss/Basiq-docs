---
title: Feb '24 - API & Dashboard Improvements
author: Ashman Malik
hidden: false
published_at: '2024-02-20T00:52:53.323Z'
type: improved
---
## API Updates :sunrise:

We are thrilled to announce the latest enhancements to our Accounts Endpoint (EP), which bring a host of new features and capabilities to enrich your experience. These updates are designed to provide you with deeper insights and greater flexibility in accessing account-related data.

# New Features :snowflake:

## amortisedLimit

* Introducing the amortisedLimit field, allowing you to access the available limit amortised according to the payment schedule. Even if absent, it's now assumed to be zero.

## bundleName

* You can now benefit from the optional bundleName field, providing insight into whether an account is part of a bundle offering additional customer benefits.

## creditLimit

* We've added support for creditLimit, indicating eligibility for various account types such as credit cards, loans, and mortgages. 

## meta

* Enhancing the meta field to offer comprehensive fee details including name, feeType, amount, balanceRate, transactionRate, accruedRate, accrualFrequency, currency, additionalValue, additionalInfo, additionalInfoUri, discounts, and eligibility. This includes descriptions and conditions for fees, their types, amounts, frequencies, and discount details. 

## lendingRates

* Now providing detailed information on lending rates with lendingRates, including type, rate, comparisonRate, calculationFrequency, applicationFrequency, interestPaymentDue, repaymentType, loanPurpose, tiers with conditions, and additional rate details.

## termDeposit

* Included detailed information about term deposits, covering lodgementDate, maturityDate, maturityAmount, maturityCurrency, and maturityInstructions. 

## loan

* Expanded loan data to include various parameters such as startDate, endDate, repaymentType, loanAmount, loanCurrency, nextInstalmentDate, minInstalmentAmount, minInstalmentCurrency, maxRedraw, maxRedrawCurrency, minRedraw, minRedrawCurrency, offsetAccountEnabled, offsetAccountIds, and repaymentFrequency. 

## creditCard

* Detailed information about credit cards is now available, including minPaymentAmount, paymentDueAmount, paymentCurrency, and paymentDueDate. 

> 📘 Documentation
>
> Our documentation has been updated to reflect these exciting new additions to the [Accounts Endpoint](https://api.basiq.io/reference/getaccounts).

## Dashboard Updates :wrench:

We're thrilled to share the latest enhancements to our Basiq Dashboard:

## Fresh Look and Feel

* We've given the dashboard a makeover to match the sleek design of our updated [basiq.io](https://basiq.io/) website. Expect redesigned fonts, colors, and components that are easy on the eyes!

## Improved Customise UI Layout

* We've revamped the customisation options for the Customise UI layout, making it even easier for you to tailor your [dashboard experience](https://dashboard.basiq.io/customise-ui) to your preferences.

## Consent Management

* Partners are no longer able to set custom text for consent scopes/permissions; it now defaults to CDR required wording read more [here](https://api.basiq.io/docs/dash-configuration#navigating-changes-in-permissions). 

## Enhanced Consent Functionality

* Need to reauthorise consent? No problem! We've added a handy "Reauthorise consent" option to the Request consent link parameters, giving you more control over your data permissions.

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(54.55861070911722% + 41px); height: 0; width: 100%;">
  <iframe src="https://demo.arcade.software/pPFVDHv3rKitgI7gEtx5?embed" title="Basiq - Reauthorise consent" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe>
</div>
`}</HTMLBlock>

Check out our [documentation](https://api.basiq.io/docs/dash-configuration) for more on customising your Customise UI. Dive in and explore these exciting updates, and don't hesitate to reach out if you have any questions or feedback!