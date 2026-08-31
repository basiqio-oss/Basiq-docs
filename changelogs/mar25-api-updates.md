---
title: Mar'25 - API and ConsentUI Updates
author: Ashman Malik
hidden: false
published_at: '2025-03-20T01:13:37.152Z'
type: added
---
We’ve rolled out some exciting updates:

### **Income and Expense Report subtypes**

* You can now use the Reports API to generate an Income or Expense `reportSubType`
* This will create a report with only Income or only Expense related Metrics and Groups
* Depending on the amount of transactions, a report may be generated up to 40% faster 🏎️
* You can also choose to include specific Metrics and Groups by specifying their IDs in the request payload

### **Enhancements to the Consent Extend and Reauthorise flow**

* To better align with CDR CX guidelines, we have updated the user experience when a User is Extending or Reauthorising their Consent
* Now -- prior to Extending or redirecting the User to their bank, Basiq will display the ongoing Consent details
* This ensures the Users are fully aware of the terms before making any changes

## <hr />Stay Updated :loudspeaker:

<HTMLBlock>{`
<a href="https://api.basiq.io/changelog.rss" target="_blank">   <img src="https://img.shields.io/badge/RSS-Subscribe-orange?style=for-the-badge" alt="RSS Subscribe"> </a>
`}</HTMLBlock>

If you have any questions or need further assistance, don't hesitate to reach out to our support team. <hr />