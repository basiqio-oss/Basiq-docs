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

```json Error response
{
    "type": "error",
    "title": "Parameter not valid.",
    "code": "parameter-not-valid",
    "detail": "Amount value is not valid.",
    "source": {...}
}
```

The following table provides an overview of the responses and scenarios that are considered as "un-happy paths". Additionally, it provides a detailed description of the underlying reasons behind these scenarios.

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Error
      </th>

      <th style={{ textAlign: "left" }}>
        code
      </th>

      <th style={{ textAlign: "left" }}>
        Title
      </th>

      <th style={{ textAlign: "left" }}>
        Detailed reason
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Supplying incorrect Amount
      </td>

      <td style={{ textAlign: "left" }}>
        parameter-not-valid
      </td>

      <td style={{ textAlign: "left" }}>
        Parameter not valid.
      </td>

      <td style={{ textAlign: "left" }}>
        The amount needs to be 0.01 or higher
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Payer bank branch code is not valid/missing
      </td>

      <td style={{ textAlign: "left" }}>
        parameter-not-valid
      </td>

      <td style={{ textAlign: "left" }}>
        Parameter value is not valid
      </td>

      <td style={{ textAlign: "left" }}>
        The payer account number is invalid/missing.

        The error of this field being missing would only occur if the payer bank branch code is provided and the account number is not
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Payer account number is not valid/missing
      </td>

      <td style={{ textAlign: "left" }}>
        parameter-not-valid
      </td>

      <td style={{ textAlign: "left" }}>
        Parameter value is not valid
      </td>

      <td style={{ textAlign: "left" }}>
        The payee bank branch code is invalid/missing.

        The error of this field being missing would only occur if the payee account number is provided and the bank branch code is not
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Payee account number is not valid/missing
      </td>

      <td style={{ textAlign: "left" }}>
        parameter-not-valid
      </td>

      <td style={{ textAlign: "left" }}>
        Parameter value is not valid
      </td>

      <td style={{ textAlign: "left" }}>
        The payee account number is invalid/missing.

        The error of this field being missing would only occur if the payee bank branch code is provided and the account number is not
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Payout method is not valid
      </td>

      <td style={{ textAlign: "left" }}>
        parameter-not-valid
      </td>

      <td style={{ textAlign: "left" }}>
        Parameter value is not valid
      </td>

      <td style={{ textAlign: "left" }}>
        Payout method is invalid. Valid values are: \{fast, batch, fast/batch}

        Note: method field is optional and can be omitted.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Duplicate request
      </td>

      <td style={{ textAlign: "left" }}>
        resource-already-exists
      </td>

      <td style={{ textAlign: "left" }}>
        Resource already exists.
      </td>

      <td style={{ textAlign: "left" }}>
        The partner application has already submitted a payment with the same requestId
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Duplicate request in same bulk request
      </td>

      <td style={{ textAlign: "left" }}>
        resource-already-exists
      </td>

      <td style={{ textAlign: "left" }}>
        Resource already exists.
      </td>

      <td style={{ textAlign: "left" }}>
        The request submitted has one or more request Ids with the same values
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Bulk limit exceeded
      </td>

      <td style={{ textAlign: "left" }}>
        maximum-count-exceeded.
      </td>

      <td style={{ textAlign: "left" }}>
        Maximum count exceeded.
      </td>

      <td style={{ textAlign: "left" }}>
        The number of requested payments exceeded the system limit (currently set at 100).
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Payments not enabled
      </td>

      <td style={{ textAlign: "left" }}>
        payments-not-enabled
      </td>

      <td style={{ textAlign: "left" }}>
        Payments not enabled.
      </td>

      <td style={{ textAlign: "left" }}>
        The partner application has not be enabled to send payments
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Catch all for all other schema errors
      </td>

      <td style={{ textAlign: "left" }}>
        invalid-content
      </td>

      <td style={{ textAlign: "left" }}>
        Invalid request content
      </td>

      <td style={{ textAlign: "left" }}>
        The partner needs to rectify the error(s) in the request and resend. 

        These could be:

        A missing or incorrect field

        Format is not followed correctly

        …others
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        User not found
      </td>

      <td style={{ textAlign: "left" }}>
        resource-not-found
      </td>

      <td style={{ textAlign: "left" }}>
        Resource not found.
      </td>

      <td style={{ textAlign: "left" }}>
        The user Id supplied cannot be found
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        User name invalid
      </td>

      <td style={{ textAlign: "left" }}>
        invalid-user-name
      </td>

      <td style={{ textAlign: "left" }}>
        Invalid user name.
      </td>

      <td style={{ textAlign: "left" }}>
        The user referenced has an invalid first and/or last name. First name must have at least 2 letters and last name must have at least 2 letters
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        User email invalid
      </td>

      <td style={{ textAlign: "left" }}>
        invalid-user-email
      </td>

      <td style={{ textAlign: "left" }}>
        Invalid user email.
      </td>

      <td style={{ textAlign: "left" }}>
        The user referenced has an invalid /missing email name.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Missing payee account details
      </td>

      <td style={{ textAlign: "left" }}>
        missing-payee-account-details
      </td>

      <td style={{ textAlign: "left" }}>
        Missing Payee account details.
      </td>

      <td style={{ textAlign: "left" }}>
        We cannot determine which payee account to use for the referenced payee
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Missing payer account details
      </td>

      <td style={{ textAlign: "left" }}>
        missing-payer-account-details
      </td>

      <td style={{ textAlign: "left" }}>
        Missing Payer account details.
      </td>

      <td style={{ textAlign: "left" }}>
        We cannot determine which payer account to use for the referenced payee
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        External provider unreachable
      </td>

      <td style={{ textAlign: "left" }}>
        external-provider-unreachable
      </td>

      <td style={{ textAlign: "left" }}>
        External provider unreachable.
      </td>

      <td style={{ textAlign: "left" }}>
        An error occurred communicating with the external payment provider after retries have been exhausted
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Payment transaction limit reached
      </td>

      <td style={{ textAlign: "left" }}>
        transaction-limit-reached
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction limit reached
      </td>

      <td style={{ textAlign: "left" }}>
        The per transaction limit set on the account within the external provider has been hit. Customer can contact us to agree on new limits if need be.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Daily limit reached
      </td>

      <td style={{ textAlign: "left" }}>
        daily-limit-reached
      </td>

      <td style={{ textAlign: "left" }}>
        Daily limit reached
      </td>

      <td style={{ textAlign: "left" }}>
        The daily limit enforced on the partner has been reached. Customer can contact us to agree on new limits if need be.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Check balance resulted in insufficient funds
      </td>

      <td style={{ textAlign: "left" }}>
        check-balance-insufficient-funds
      </td>

      <td style={{ textAlign: "left" }}>
        Check balance insufficient funds.
      </td>

      <td style={{ textAlign: "left" }}>
        The user account you attempting to debit does not have sufficient funds according to the most recent account balance check

        Please contact the user to make sure the account has
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Account unreachable for checking account balance due to technical reasons
      </td>

      <td style={{ textAlign: "left" }}>
        account-unreachable
      </td>

      <td style={{ textAlign: "left" }}>
        Account unreachable
      </td>

      <td style={{ textAlign: "left" }}>
        The account linked cannot be accessed to check the latest balance
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        The account balance is outdated (has not been updated in the last 24 hours)
      </td>

      <td style={{ textAlign: "left" }}>
        account-balance-outdated
      </td>

      <td style={{ textAlign: "left" }}>
        Account balance outdated
      </td>

      <td style={{ textAlign: "left" }}>
        The account balance is outdated (has not been updated in the last 24 hours)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Invalid or missing payee user Id
      </td>

      <td style={{ textAlign: "left" }}>
        parameter-not-valid
      </td>

      <td style={{ textAlign: "left" }}>
        parameter-not-valid
      </td>

      <td style={{ textAlign: "left" }}>
        payeeUserId value is not valid.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Invalid of missing payer user Id
      </td>

      <td style={{ textAlign: "left" }}>
        parameter-not-valid
      </td>

      <td style={{ textAlign: "left" }}>
        parameter-not-valid
      </td>

      <td style={{ textAlign: "left" }}>
        payerUserId value is not valid.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Payer account cannot be the same account as the partner’s
      </td>

      <td style={{ textAlign: "left" }}>
        payer-account-not-allowed
      </td>

      <td style={{ textAlign: "left" }}>
        Payer account details are not allowed
      </td>

      <td style={{ textAlign: "left" }}>
        External error.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Debit failed: Refer to Customer
      </td>

      <td style={{ textAlign: "left" }}>
        refer\_to\_customer
      </td>

      <td style={{ textAlign: "left" }}>
        Refer to customer
      </td>

      <td style={{ textAlign: "left" }}>
        Usually means insufficient funds or that the target account has breached their transaction limits.
      </td>
    </tr>
  </tbody>
</Table>

For more details, read more about payments [here](https://api.basiq.io/docs/payments).
