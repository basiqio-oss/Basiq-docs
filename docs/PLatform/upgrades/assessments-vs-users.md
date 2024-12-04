---
title: Assessments vs Users
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
With the new dashboard comes the concept of users, rather than assessments. A user and an assessment are ultimately one and the same - a bucket in which we can aggregate financial data - however there are some subtle differences between the two, including new features and data points you can now access via a user. 

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>

      </th>

      <th style={{ textAlign: "left" }}>
        Assessment
      </th>

      <th style={{ textAlign: "left" }}>
        User
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        ### What is it?
      </td>

      <td style={{ textAlign: "left" }}>
        An assessment in the Classic Dashboard is a way to capture all the financial details for a specific person a group of people, like a bucket of information.

        When creating an assessment an Assessment ID is generated to be able to identify that assessment uniquely. 

        You can also add in a First Name and Last Name for the assessment to make it easier to identify for a human.
      </td>

      <td style={{ textAlign: "left" }}>
        As user in the New Dashboard is a way to capture all the financial details for a specific person or a group of people, like a bucket of information.

        When creating the user a user ID is generated to be able to identify that user uniquely. 

        It is required to input an Email and a Mobile Number for this user in the dashboard to make it easier to identify for a human.  We do not do a verification of check these emails from Basiq’s side. You can also include First Name, Middle Name and Last Name for this user object.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        ### Fields included
      </td>

      <td style={{ textAlign: "left" }}>
        * ID
        * First Name
        * Last Name
        * Owner
        * Date/Time Created
      </td>

      <td style={{ textAlign: "left" }}>
        * ID
        * First Name
        * Middle Name
        * Last Name
        * Date/Time Created
        * Email Address
        * Mobile Number

        *There is no concept of record owner with the new dashboard. Alternatively we encourage partners to use application management or permission sets in order to restrict access.*
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        ### *Editable* fields
      </td>

      <td style={{ textAlign: "left" }}>
        * First Name
        * Last Name
        * Owner
      </td>

      <td style={{ textAlign: "left" }}>
        * First Name
        * Middle Name
        * Last Name
        * Email Address
        * Mobile Number
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        ### Connections
      </td>

      <td style={{ textAlign: "left" }}>
        * End user can create a connection via the Basiq magic link
        * End user can provide PDF statements for partners to upload
      </td>

      <td style={{ textAlign: "left" }}>
        * End user can create a connection via the Basiq magic link
        * End user can provide PDF statements for partners to upload

        Partners can view connection details such as:

        * The date the connection to the bank was made
        * The date the connection was updated via Basiq
        * The job success/failure details when creating/refreshing connection (great for troubleshooting!)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        ### Accounts
      </td>

      <td style={{ textAlign: "left" }}>
        * Shortened Number
        * Account Holder Name
        * Account Name
        * Account Type
        * Institution Name
        * Account Balance
        * Available Funds
        * Last updated
        * Transaction Status
      </td>

      <td style={{ textAlign: "left" }}>
        * Full Account Number
        * Account Holder Name
        * Account Name
        * Account Type
        * Institution Name
        * Institution Logo
        * Account Balance
        * Available Funds
        * Currency Type
        * Last updated
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        ### Transactions
      </td>

      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * Posted Date
        * Description
        * Class
        * Amount
        * Direction (Credit or Debit)
      </td>
    </tr>
  </tbody>
</Table>
