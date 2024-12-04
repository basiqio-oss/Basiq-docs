---
title: Handling jobs
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
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b253686-Invalid-credentials-1.png",
        "Invalid-credentials-1.png",
        2070,
        1155,
        "#62a5c0"
      ],
      "sizing": "80"
    }
  ]
}
[/block]
# Keeping track of jobs

Providing your users with a simple, intuitive and informed experience is key to good UX.

To help keep you and your users informed we provide job status and error messages which your Support teams can use to troubleshoot issues and pass directly onto the user (i.e. in cases of invalid credentials).

To do this, you can use the `/job` endpoint, checking on the status of each step to see if there have been any failures. 

## What to do when a job fails

The best case scenario, is that all job steps will have completed successfully. In practice, live banks present a number of scenarios that prevent Basiq from fetching a user's accounts and transactions from their internet banking. In the event that a step has failed, the result object will contain an embedded error object, and the information within that will determine how you clear the issue and fetch their data successfully.

# Possible job failure scenarios
[block:parameters]
{
  "data": {
    "h-0": "Scenario",
    "h-1": "Where it occurs",
    "h-2": "What it means",
    "h-3": "Recommended action",
    "2-0": "`account-not-accessible-requires-user-action`",
    "2-1": "Can occur on any job step, depending on where Basiq encounters the error when navigating the user's internet banking",
    "2-2": "The bank is presenting a popup to the user in their internet banking. Whenever possible Basiq will navigate through these, but for example if the bank presents new T&Cs to the user and offers only options to \"Agree\" or \"Decline\", then Basiq will fail the job with this error",
    "2-3": "Ask your user to login to their internet banking, navigate to accounts and transactions, and address any CTA's/popups requiring action from the bank\n\nYou/your application can then [refresh the connection](#refresh-a-connection). If the popup has cleared, the job should complete as normal",
    "6-0": "`service-unavailable`\n*At all other times*",
    "6-1": "Can occur on any job step, depending  on where Basiq encounters the error condition on the bank's internet banking portal.",
    "6-2": "The bank is unable to service Basiq's request This is typically due to a maintenance outage or performance issue on the bank's website, but can occasionally happen if the bank has made significant changes to their internet banking",
    "6-3": "You can let the user know there is a problem fetching data from their bank, and that you will let them know when their data is ready.\n\nCheck the status for this bank in the `/connectors` \n[endpoint](https://api.basiq.io/reference/getconnectors-1) if it is major-outage then the problem is widespread and you should alert your user, and wait until the status has lifted\n\nIf the institution status is anything other than major-outage then wait 10 minutes and try again.\n\nIf, after a couple of retries, the error has not cleared, then report the `connection-id` to Basiq's support team, to investigate.",
    "0-0": "`Invalid credentials`\n\nOn *\"Refresh connection\"*",
    "0-1": "Can occur on `verify-credentials` step when you make a request to *refresh* a users connection.",
    "0-2": "This could happen for the same reasons as \"Create connection\", but could also be that your user has changed their internet banking password.",
    "0-3": "When your user returns to your application, prompt them to resubmit their credentials, and update these using the `Update Connection` request.",
    "4-0": "`service-unavailable` \n*On updating a connection*",
    "4-1": "Can occur when making a `UPDATE` request to the connections endpoint,",
    "4-2": "Due to failure in either the financial institution or the Basiq connector.",
    "4-3": "Basiq's connection retry mechanism will kick in, meaning the job will be placed in a queue to be retried every 2 hours until either it is successful, or expires (after 7 days). \n\nYou can let the user know there is a problem fetching data from their bank, and that you will let them know when their data is ready.\n\nIn the meantime you can use the `/jobs` endpoint to monitor the status of this job (**note** polling should be done at much longer intervals than the standard job polling as retries are attempted every 2 hours)."
  },
  "cols": 4,
  "rows": 7
}
[/block]

[block:callout]
{
  "type": "info",
  "title": "Sandbox users for testing job failure scenarios",
  "body": "We have created test users especially for replicating these failure scenarios in your user flow. These three users will always fail on the same job steps. You can find them [here](ref:testing)."
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "If you attempt to refresh a connection while a job is either queued or still in progress, the API will return a 200 status with the original job instead of a newly created job.",
  "title": "Avoiding duplicate jobs"
}
[/block]