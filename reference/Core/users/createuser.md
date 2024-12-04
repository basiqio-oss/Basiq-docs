---
title: Create a user
excerpt: Creates a new Basiq user object
api:
  file: core.json
  operationId: createUser
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
A user must be created before connecting to any financial institutions, as this is where data will be aggregated. 

##### We do not check for existing users with the same details

We rely on the ID of the user for uniqueness, so will not do a check for existing users with the same mobile or email. If this is a concern then it should be handled in the partner application. You must only provide a mobile OR an email to create the user.

> 📘 For BASIQ Dashboard Only
> 
> You can create users via Basiq dashboard, and you must provide both fields email address and mobile number when creating a user through the Dashboard.

[block:html]
{
  "html": "<script src=\"https://code.jquery.com/jquery-3.5.0.js\"></script>\n<script>\n  setTimeout(() => {    \n    const toolTip =  \"<p class='toolTip'>&#8505;&#65039; &nbsp; Populate your request using the input fields provided</p>\";\n    $(toolTip).insertAfter($('.rm-PlaygroundRequest'));\n\t}, 100)\n</script>"
}
[/block]