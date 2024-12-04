---
title: Consent Scopes
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
Here we provide a breakdown on the configurable scopes for your very own customisable consent policy. You can see the **name and description**, the **API endpoints** where it returns the data, as well as what **specific data points** are fetched with each one. 

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Consent Scope
      </th>

      <th style={{ textAlign: "left" }}>
        Entity
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>

      <th style={{ textAlign: "left" }}>
        Attributes
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Name and occupation
      </td>

      <td style={{ textAlign: "left" }}>
        Basiq API  

        * `/connections`CDR Scope  
        * `common:customer.basic:read`
      </td>

      <td style={{ textAlign: "left" }}>
        The scope allows access to personally identifiable information about the customer. Includes name and occupation of the individual.
      </td>

      <td style={{ textAlign: "left" }}>
        * Name
        * Occupation
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Name, occupation, contact details
      </td>

      <td style={{ textAlign: "left" }}>
        Basiq API  

        * `/connections`CDR Scope  
        * `common:customer.detail:read`
      </td>

      <td style={{ textAlign: "left" }}>
        The scope allows access to more detailed information about the customer. Includes the data available with the Basic Customer Data scope plus contact details. Includes basic data plus phone, email and address information.
      </td>

      <td style={{ textAlign: "left" }}>
        * Name
        * Occupation
        * Phone
        * Email address
        * Mail address
        * Residential address
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Organisation profile
      </td>

      <td style={{ textAlign: "left" }}>
        Basiq API  

        * `/identities`CDR Scope  
        * `common:customer.basic:read`
      </td>

      <td style={{ textAlign: "left" }}>
        The scope allows access to identifiable information about the customer. Includes business numbers and industry code for organisations
      </td>

      <td style={{ textAlign: "left" }}>
        * Agent name and role
        * Organisation name
        * Organisation numbers (ABN or ACN)
        * Charity status
        * Establishment date
        * Industry
        * Organisation type
        * Country of registration
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Organisation profile and contact details
      </td>

      <td style={{ textAlign: "left" }}>
        Basiq API\
        `/identities`  

        CDR Scope  

        * `common:customer.detail:read`
      </td>

      <td style={{ textAlign: "left" }}>
        The scope allows access to more detailed information about the customer. Includes the data available with the Basic Customer Data scope plus contact details. Includes basic data plus phone, email and address information.
      </td>

      <td style={{ textAlign: "left" }}>
        * Agent name and role
        * Organisation name
        * Organisation numbers (ABN or ACN)
        * Charity status
        * Establishment date
        * Industry
        * Organisation type
        * Country of registration
        * Organisation address
        * Mail address
        * Phone number
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Account name, type and balance 
      </td>

      <td style={{ textAlign: "left" }}>
        Basiq API  

        * `/accounts`CDR Scope  
        * `bank:accounts.basic:read`
      </td>

      <td style={{ textAlign: "left" }}>
        This scope allows access to basic information of the customer's accounts.  

        Includes simple account information including balance. This scope does not include account numbers, product information or transaction data.  

        **Account number in this scope is masked**   

        **Account name, type and balance are required.**\
        ![](https://files.readme.io/dca0227-permissions.png)
      </td>

      <td style={{ textAlign: "left" }}>
        * Name of account
        * Account number
        * Type of account
        * Account balance
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Account numbers and features  

        *requires Account name, type and balance scope*
      </td>

      <td style={{ textAlign: "left" }}>
        Basiq API  

        * `/accounts`CDR Scope  
        * `bank:accounts.detail:read`
      </td>

      <td style={{ textAlign: "left" }}>
        This scope allows access to detailed information of the customer's accounts. Includes basic account information plus account identifiers and product information. Does not include transaction data.
      </td>

      <td style={{ textAlign: "left" }}>
        * Account number
        * Interest rates
        * Fees
        * Discounts
        * Account terms
        * Account mail address
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Transaction details
      </td>

      <td style={{ textAlign: "left" }}>
        Basiq API  

        * `/transactions`CDR Scope  
        * `bank:transactions:read`
      </td>

      <td style={{ textAlign: "left" }}>
        This scope allows access to transaction data for accounts. Includes all account transaction data.
      </td>

      <td style={{ textAlign: "left" }}>
        * Incoming and outgoing transactions
        * Amounts
        * Dates
        * Descriptions of transactions
        * Who you have sent money to and received money from
      </td>
    </tr>
  </tbody>
</Table>
