---
title: Payments Errors
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The Payment API employs standard HTTP response codes to convey the outcome of an API request, whether it was successful or encountered an error. In case of an error, the API will provide a comprehensive response that includes detailed information such as the reason for the error,  the error code, the title of the error, and the error message itself. This ensures that developers and users can easily identify and understand the nature of the error and take appropriate actions to resolve it.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"type\": \"error\",\n    \"title\": \"Parameter not valid.\",\n    \"code\": \"parameter-not-valid\",\n    \"detail\": \"Amount value is not valid.\",\n    \"source\": {...}\n}",
      "language": "json",
      "name": "Error response"
    }
  ]
}
[/block]
The following table provides an overview of the responses and scenarios that are considered as "un-happy paths". Additionally, it provides a detailed description of the underlying reasons behind these scenarios.
[block:parameters]
{
  "data": {
    "h-0": "Error",
    "h-1": "code",
    "h-2": "Title",
    "h-3": "Detailed reason",
    "h-4": "",
    "0-0": "Supplying incorrect Amount",
    "0-1": "parameter-not-valid",
    "0-2": "Parameter not valid.",
    "0-3": "The amount needs to be 0.01 or higher",
    "1-0": "Payer bank branch code is not valid/missing",
    "1-1": "parameter-not-valid",
    "1-2": "Parameter value is not valid",
    "1-3": "The payer account number is invalid/missing.\n\nThe error of this field being missing would only occur if the payer bank branch code is provided and the account number is not",
    "2-0": "Payer account number is not valid/missing",
    "2-1": "parameter-not-valid",
    "2-2": "Parameter value is not valid",
    "2-3": "The payee bank branch code is invalid/missing.\n\nThe error of this field being missing would only occur if the payee account number is provided and the bank branch code is not",
    "3-0": "Payee account number is not valid/missing",
    "3-1": "parameter-not-valid",
    "3-2": "Parameter value is not valid",
    "3-3": "The payee account number is invalid/missing.\n\nThe error of this field being missing would only occur if the payee bank branch code is provided and the account number is not",
    "4-0": "Payout method is not valid",
    "4-1": "parameter-not-valid",
    "4-2": "Parameter value is not valid",
    "4-3": "Payout method is invalid. Valid values are: {fast, batch, fast/batch}\n\nNote: method field is optional and can be omitted.",
    "5-0": "Duplicate request",
    "5-1": "resource-already-exists",
    "5-2": "Resource already exists.",
    "5-3": "The partner application has already submitted a payment with the same requestId",
    "6-0": "Duplicate request in same bulk request",
    "6-1": "resource-already-exists",
    "6-2": "Resource already exists.",
    "6-3": "The request submitted has one or more request Ids with the same values",
    "7-0": "Bulk limit exceeded",
    "7-1": "maximum-count-exceeded.",
    "7-2": "Maximum count exceeded.",
    "7-3": "The number of requested payments exceeded the system limit (currently set at 100).",
    "8-0": "Payments not enabled",
    "8-1": "payments-not-enabled",
    "8-2": "Payments not enabled.",
    "8-3": "The partner application has not be enabled to send payments",
    "9-0": "Catch all for all other schema errors",
    "9-1": "invalid-content",
    "9-2": "Invalid request content",
    "9-3": "The partner needs to rectify the error(s) in the request and resend. \n\nThese could be:\n\nA missing or incorrect field\n\nFormat is not followed correctly\n\n…others",
    "10-0": "User not found",
    "10-1": "resource-not-found",
    "10-2": "Resource not found.",
    "10-3": "The user Id supplied cannot be found",
    "11-0": "User name invalid",
    "11-1": "invalid-user-name",
    "11-2": "Invalid user name.",
    "11-3": "The user referenced has an invalid first and/or last name. First name must have at least 2 letters and last name must have at least 2 letters",
    "12-0": "User email invalid",
    "12-1": "invalid-user-email",
    "12-2": "Invalid user email.",
    "12-3": "The user referenced has an invalid /missing email name.",
    "13-0": "Missing payee account details",
    "13-1": "missing-payee-account-details",
    "13-2": "Missing Payee account details.",
    "13-3": "We cannot determine which payee account to use for the referenced payee",
    "14-0": "Missing payer account details",
    "14-1": "missing-payer-account-details",
    "14-2": "Missing Payer account details.",
    "14-3": "We cannot determine which payer account to use for the referenced payee",
    "15-0": "External provider unreachable",
    "15-1": "external-provider-unreachable",
    "15-2": "External provider unreachable.",
    "15-3": "An error occurred communicating with the external payment provider after retries have been exhausted",
    "16-0": "Payment transaction limit reached",
    "16-1": "transaction-limit-reached",
    "16-2": "Transaction limit reached",
    "16-3": "The per transaction limit set on the account within the external provider has been hit. Customer can contact us to agree on new limits if need be.",
    "17-0": "Daily limit reached",
    "17-1": "daily-limit-reached",
    "17-2": "Daily limit reached",
    "17-3": "The daily limit enforced on the partner has been reached. Customer can contact us to agree on new limits if need be.",
    "18-0": "Check balance resulted in insufficient funds",
    "18-1": "check-balance-insufficient-funds",
    "18-2": "Check balance insufficient funds.",
    "18-3": "The user account you attempting to debit does not have sufficient funds according to the most recent account balance check\n\nPlease contact the user to make sure the account has",
    "19-0": "Account unreachable for checking account balance due to technical reasons",
    "19-1": "account-unreachable",
    "19-2": "Account unreachable",
    "19-3": "The account linked cannot be accessed to check the latest balance",
    "20-0": "The account balance is outdated (has not been updated in the last 24 hours)",
    "20-1": "account-balance-outdated",
    "20-2": "Account balance outdated",
    "20-3": "The account balance is outdated (has not been updated in the last 24 hours)",
    "21-0": "Invalid or missing payee user Id",
    "21-1": "parameter-not-valid",
    "21-2": "parameter-not-valid",
    "22-0": "Invalid of missing payer user Id",
    "22-1": "parameter-not-valid",
    "22-2": "parameter-not-valid",
    "22-3": "payerUserId value is not valid.",
    "21-3": "payeeUserId value is not valid.",
    "23-0": "Payer account cannot be the same account as the partner’s",
    "23-1": "payer-account-not-allowed",
    "23-2": "Payer account details are not allowed",
    "23-3": "External error.",
    "24-0": "Debit failed: Refer to Customer",
    "24-1": "refer_to_customer",
    "24-2": "Refer to customer",
    "24-3": "Usually means insufficient funds or that the target account has breached their transaction limits."
  },
  "cols": 4,
  "rows": 25
}
[/block]
For more details, read more about payments [here](https://api.basiq.io/docs/payments).