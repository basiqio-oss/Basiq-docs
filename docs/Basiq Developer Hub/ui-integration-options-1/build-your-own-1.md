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

<Image width="80%" src="https://files.readme.io/6d68e40-Greener.svg" />

## STEP 1: Fetch institutions

Get an up to date list of all our supported institutions by calling our `/institutions` endpoint

<Image width="80%" src="https://files.readme.io/d1544ef-with_label_1.svg" />

The API will return a list of institutions that can be presented to the user. From this list they can select an institution and start connecting their accounts.

```javascript STEP 1: Fetch institutions
var axios = require('axios');

var config = {
  method: 'get',
  url: 'https://au-api.basiq.io/institutions',
  headers: { 
    'Authorization': 'Bearer $YOUR_ACCESS_TOKEN', 
    'Accept': 'application/json'
  }
};

axios(config)
.then(function (response) {
  console.log(response.data);
})
.catch(function (error) {
  console.log(error);
});
```
```curl
curl --location --request GET 'https://au-api.basiq.io/institutions' \
--header 'Authorization: Bearer $YOUR_ACCESS_TOKEN' \
--header 'Accept: application/json'
```

> 📘 What to filter from the response
>
> * Filter out institutions with `"authorization": "other"` as these will not work for web connections
> * Filter out institutions with `"stage": "alpha"` as these are still in development
> * Filter out institutions with `"status": "major-outage"` as these connections are likely to fail due to a temporary issue on the bank's side (e.g., a maintenance outage or performance issue)
> * Filter out institutions which do not offer the data points essential to you (e.g., NAB does not return `features.accounts.accountHolder` for `web` connections)

## STEP 2: Get users login credentials

Users supply their credentials through an input/form.

```html STEP 2: Get users login credentials
<form onSubmit={handleSubmit}>
    <label for="uname"><b>Username</b></label>
    <input type="text" placeholder="Enter Username" name="uname" required>
    <label for="psw"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="psw" required>
    <button type="submit">Continue</button>
</form>
```

**Note:** the `/institutions` endpoint returns a few properties that can help create a better user experience, such as the institution specific labels that should be displayed adjacent to the login and password input fields - for e.g some banks refer to login name as “access id”. 

> 🚧 Some banks require extra login parameters
>
> Be aware that some banks require additional login parameters. 
>
> The best way to approach this is to look for attributes with the "Caption" suffix to know what to render, **eg.** St George also has `securityCodeCaption`  in addition to the standard `loginIdCaption` and `passwordCaption`. 
>
> Pass these additional login parameters as *optional* arguments when you create any connection.

> ❗️ In no circumstance should you ever store the user’s login credentials. We have worked hard to ensure that we provide a secure API service that protects the user's details - so leave as much of the security obligations to us.

## STEP 3: Create a connection

Your app will now create a connection by posting the credentials and `institution.id` to the `/connections` endpoint.

```javascript STEP 3: Create a connection
var axios = require('axios');
var data = JSON.stringify({
  "loginId": "gavinBelson",
  "password": "hooli2016",
  "institution": {
    "id": "AU00000"
  }
});

var config = {
  method: 'post',
  url: 'https://au-api.basiq.io/users/{user.id}/connections',
  headers: { 
    'Authorization': 'Bearer $YOUR_ACCESS_TOKEN', 
    'Accept': 'application/json', 
    'Content-Type': 'application/json'
  },
  data : data
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```
```curl
curl --location --request POST 'https://au-api.basiq.io/users/{user.id}/connections' \
--header 'Authorization: Bearer $YOUR_ACCESS_TOKEN' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
  "loginId": "gavinBelson",
  "password": "hooli2016",
  "institution":{
    "id":"AU00000"
  }
}'
```

This process may take anywhere from 3 - 15 seconds (depending on the institution being connected to and the network latency). The request response will contain a link to the connection, and a jobId. You can then to use that `jobId` to poll the `/jobs` endpoint, checking on the status of each job step until the job has either

* successfully completed the relevant step/s;
* failed at any of the steps.

> 🚧 Handling jobs
>
> Handling these jobs correctly is crucial to creating a seamless experience for your users. See our [guide to handling jobs](https://api.basiq.io/docs/handling-jobs) on how to best do this.

> ❗️ Access tokens
>
> The `/users/{user.id}/connections` requires a `CLIENT_ACCESS` scoped token. This is because you should **never** pass a users credentials back to your server, and instead call the endpoint directly from your UI. 
>
> See [here](https://api.basiq.io/docs/authentication-1) for more information on authentication and access tokens.

```javascript Checking a job status
var axios = require('axios');

var config = {
  method: 'get',
  url: 'https://au-api.basiq.io/jobs/{jobId}',
  headers: { 
    'Authorization': 'Bearer $YOUR_ACCESS_TOKEN', 
    'Accept': 'application/json'
  }
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```
```curl
curl --location --request GET 'https://au-api.basiq.io/jobs/{jobId}' \
--header 'Authorization: Bearer $YOUR_ACCESS_TOKEN' \
--header 'Accept: application/json'
```

You should keep your user engaged until the first step, verify-credentials, is complete, as dragging them back if the credentials didn't work is poor UX. 

As soon as the verify-credentials step is complete, you should release the user to continue onboarding as Basiq fetches their accounts and transactions (job steps 2 and 3) in the background. 

> 📘 Tips and tricks
>
> * Check the `institution.stats` in the `/institutions` endpoint for an indication of how long each bank typically takes to complete each job step.
>
> * For the best user experience, have your user connect their banks as early in the onboarding journey as possible. This allows more time for Basiq to fetch their information by the time onboarding is complete.
>
> * Filter out any sandbox institutions when in production: *AU00000, AU00001, AU00002, AU00003*
>
> * See more best practices [here](https://api.basiq.io/docs/basiq-best-practices-1).
