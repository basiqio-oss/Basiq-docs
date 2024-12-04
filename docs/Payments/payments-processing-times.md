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
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ce36d8a-Group_5.png",
        "Group 5.png",
        1201,
        1201,
        "#cdd6d9"
      ],
      "sizing": "30"
    }
  ]
}
[/block]
There are a few things to take into considering when looking at processing times. 

- Processing of payments will only occur on **Australian business days** (Which will exclude weekends, and any public holidays that are observed in Sydney and Melbourne collectively)
- Any payrequests submitted on a business day **before 7pm** will likely be credited to your bank account by the end of the day, 2 business days after the payrequests were submitted successfully. 

&nbsp;
### Some examples scenarios
[block:parameters]
{
  "data": {
    "h-0": "Example",
    "h-1": "Estimated processing time",
    "0-0": "Payrequest submitted on Monday at 8am",
    "0-1": "Will likely be credited to partner bank account by the end of Wednesday",
    "1-0": "Payrequest submitted on Tuesday at 6pm",
    "1-1": "Will likely be credited to your bank account by the end of Thursday",
    "2-0": "Payrequest submitted on Friday at 3pm",
    "2-1": "Will likely be credited to your bank account by the end of Tuesday"
  },
  "cols": 2,
  "rows": 3
}
[/block]
&nbsp;
[block:callout]
{
  "type": "info",
  "body": "All `payrequests` submitted on a business day **before 7pm** will appear as *individual* payments on your payers' bank accounts, however will be rolled into *one single credit* appearing the payee's bank account. This is the account that is supplied to Basiq when payments is enabled."
}
[/block]