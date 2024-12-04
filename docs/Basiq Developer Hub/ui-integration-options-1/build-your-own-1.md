---
title: Build your own
excerpt: For a native experience
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
If you would prefer to build something completely native to your application, our `/institutions` endpoint makes creating your own UI simple.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6d68e40-Greener.svg",
        "Greener.svg",
        3345,
        2373,
        "#000000"
      ],
      "sizing": "80"
    }
  ]
}
[/block]
## STEP 1: Fetch institutions
Get an up to date list of all our supported institutions by calling our `/institutions` endpoint
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d1544ef-with_label_1.svg",
        "with label 1.svg",
        1710,
        390,
        "#000000"
      ],
      "sizing": "80"
    }
  ]
}
[/block]
The API will return a list of institutions that can be presented to the user. From this list they can select an institution and start connecting their accounts.
[block:code]
{
  "codes": [
    {
      "code": "var axios = require('axios');\n\nvar config = {\n  method: 'get',\n  url: 'https://au-api.basiq.io/institutions',\n  headers: { \n    'Authorization': 'Bearer $YOUR_ACCESS_TOKEN', \n    'Accept': 'application/json'\n  }\n};\n\naxios(config)\n.then(function (response) {\n  console.log(response.data);\n})\n.catch(function (error) {\n  console.log(error);\n});",
      "language": "javascript",
      "name": "STEP 1: Fetch institutions"
    },
    {
      "code": "curl --location --request GET 'https://au-api.basiq.io/institutions' \\\n--header 'Authorization: Bearer $YOUR_ACCESS_TOKEN' \\\n--header 'Accept: application/json'",
      "language": "curl"
    }
  ],
  "sidebar": true
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "- Filter out institutions with `\"authorization\": \"other\"` as these will not work for web connections\n- Filter out institutions with `\"stage\": \"alpha\"` as these are still in development\n- Filter out institutions with `\"status\": \"major-outage\"` as these connections are likely to fail due to a temporary issue on the bank's side (e.g., a maintenance outage or performance issue)\n- Filter out institutions which do not offer the data points essential to you (e.g., NAB does not return `features.accounts.accountHolder` for `web` connections)",
  "title": "What to filter from the response"
}
[/block]
## STEP 2: Get users login credentials

Users supply their credentials through an input/form.
[block:code]
{
  "codes": [
    {
      "code": "<form onSubmit={handleSubmit}>\n    <label for=\"uname\"><b>Username</b></label>\n    <input type=\"text\" placeholder=\"Enter Username\" name=\"uname\" required>\n    <label for=\"psw\"><b>Password</b></label>\n    <input type=\"password\" placeholder=\"Enter Password\" name=\"psw\" required>\n    <button type=\"submit\">Continue</button>\n</form>",
      "language": "html",
      "name": "STEP 2: Get users login credentials"
    }
  ],
  "sidebar": true
}
[/block]
**Note: **the `/institutions` endpoint returns a few properties that can help create a better user experience, such as the institution specific labels that should be displayed adjacent to the login and password input fields - for e.g some banks refer to login name as “access id”. 
[block:callout]
{
  "type": "warning",
  "title": "Some banks require extra login parameters",
  "body": "Be aware that some banks require additional login parameters. \n\nThe best way to approach this is to look for attributes with the \"Caption\" suffix to know what to render, **eg.** St George also has `securityCodeCaption`  in addition to the standard `loginIdCaption` and `passwordCaption`. \n\nPass these additional login parameters as *optional* arguments when you create any connection."
}
[/block]

[block:callout]
{
  "type": "danger",
  "body": "In no circumstance should you ever store the user’s login credentials. We have worked hard to ensure that we provide a secure API service that protects the user's details - so leave as much of the security obligations to us."
}
[/block]
## STEP 3: Create a connection 

Your app will now create a connection by posting the credentials and `institution.id` to the `/connections` endpoint.
[block:code]
{
  "codes": [
    {
      "code": "var axios = require('axios');\nvar data = JSON.stringify({\n  \"loginId\": \"gavinBelson\",\n  \"password\": \"hooli2016\",\n  \"institution\": {\n    \"id\": \"AU00000\"\n  }\n});\n\nvar config = {\n  method: 'post',\n  url: 'https://au-api.basiq.io/users/{user.id}/connections',\n  headers: { \n    'Authorization': 'Bearer $YOUR_ACCESS_TOKEN', \n    'Accept': 'application/json', \n    'Content-Type': 'application/json'\n  },\n  data : data\n};\n\naxios(config)\n.then(function (response) {\n  console.log(JSON.stringify(response.data));\n})\n.catch(function (error) {\n  console.log(error);\n});",
      "language": "javascript",
      "name": "STEP 3: Create a connection"
    },
    {
      "code": "curl --location --request POST 'https://au-api.basiq.io/users/{user.id}/connections' \\\n--header 'Authorization: Bearer $YOUR_ACCESS_TOKEN' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--data-raw '{\n  \"loginId\": \"gavinBelson\",\n  \"password\": \"hooli2016\",\n  \"institution\":{\n    \"id\":\"AU00000\"\n  }\n}'",
      "language": "curl"
    }
  ],
  "sidebar": true
}
[/block]
This process may take anywhere from 3 - 15 seconds (depending on the institution being connected to and the network latency). The request response will contain a link to the connection, and a jobId. You can then to use that `jobId` to poll the `/jobs` endpoint, checking on the status of each job step until the job has either
- successfully completed the relevant step/s;
- failed at any of the steps.
[block:callout]
{
  "type": "warning",
  "title": "Handling jobs",
  "body": "Handling these jobs correctly is crucial to creating a seamless experience for your users. See our [guide to handling jobs](https://api.basiq.io/docs/handling-jobs) on how to best do this."
}
[/block]

[block:callout]
{
  "type": "danger",
  "title": "Access tokens",
  "body": "The `/users/{user.id}/connections` requires a `CLIENT_ACCESS` scoped token. This is because you should **never** pass a users credentials back to your server, and instead call the endpoint directly from your UI. \n\nSee [here](https://api.basiq.io/docs/authentication-1) for more information on authentication and access tokens."
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "var axios = require('axios');\n\nvar config = {\n  method: 'get',\n  url: 'https://au-api.basiq.io/jobs/{jobId}',\n  headers: { \n    'Authorization': 'Bearer $YOUR_ACCESS_TOKEN', \n    'Accept': 'application/json'\n  }\n};\n\naxios(config)\n.then(function (response) {\n  console.log(JSON.stringify(response.data));\n})\n.catch(function (error) {\n  console.log(error);\n});",
      "language": "javascript",
      "name": "Checking a job status"
    },
    {
      "code": "curl --location --request GET 'https://au-api.basiq.io/jobs/{jobId}' \\\n--header 'Authorization: Bearer $YOUR_ACCESS_TOKEN' \\\n--header 'Accept: application/json'",
      "language": "curl"
    }
  ],
  "sidebar": true
}
[/block]
You should keep your user engaged until the first step, verify-credentials, is complete, as dragging them back if the credentials didn't work is poor UX. 

As soon as the verify-credentials step is complete, you should release the user to continue onboarding as Basiq fetches their accounts and transactions (job steps 2 and 3) in the background. 
[block:callout]
{
  "type": "info",
  "title": "Tips and tricks",
  "body": "- Check the `institution.stats` in the `/institutions` endpoint for an indication of how long each bank typically takes to complete each job step.\n\n- For the best user experience, have your user connect their banks as early in the onboarding journey as possible. This allows more time for Basiq to fetch their information by the time onboarding is complete.\n\n- Filter out any sandbox institutions when in production: *AU00000, AU00001, AU00002, AU00003*\n\n- See more best practices [here](https://api.basiq.io/docs/basiq-best-practices-1)."
}
[/block]