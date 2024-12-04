---
title: Processing times
excerpt: How long might we wait for a Collect `payrequest` to process?
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
<Image width="30%" src="https://files.readme.io/ce36d8a-Group_5.png" />

There are a few things to take into considering when looking at processing times. 

* Processing of payments will only occur on **Australian business days** (Which will exclude weekends, and any public holidays that are observed in Sydney and Melbourne collectively)
* Any payrequests submitted on a business day **before 7pm** will likely be credited to your bank account by the end of the day, 2 business days after the payrequests were submitted successfully. 

 

### Some examples scenarios

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Example
      </th>

      <th style={{ textAlign: "left" }}>
        Estimated processing time
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Payrequest submitted on Monday at 8am
      </td>

      <td style={{ textAlign: "left" }}>
        Will likely be credited to partner bank account by the end of Wednesday
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Payrequest submitted on Tuesday at 6pm
      </td>

      <td style={{ textAlign: "left" }}>
        Will likely be credited to your bank account by the end of Thursday
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Payrequest submitted on Friday at 3pm
      </td>

      <td style={{ textAlign: "left" }}>
        Will likely be credited to your bank account by the end of Tuesday
      </td>
    </tr>
  </tbody>
</Table>

 

> 📘 All `payrequests` submitted on a business day **before 7pm** will appear as *individual* payments on your payers' bank accounts, however will be rolled into *one single credit* appearing the payee's bank account. This is the account that is supplied to Basiq when payments is enabled.
