---
title: Developer Hub
excerpt: >-
  Basiq simplifies finance with an Open Finance API platform that empowers
  businesses to create innovative financial solutions and connect consumers with
  their financial data.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
  pages:
    - type: endpoint
      slug: authentication
      title: Authentication
---
## Whether You're Hands-On or Just Curious

Whether you're hands on and integrating, or just want to get acquainted with the API, you can find everything you need in the [Basiq Developer Hub](https://api.basiq.io/docs). We cover everything from quick start guides, to best practices, and how it all works in the wild.

<Image align="center" src="https://files.readme.io/3de91547c866fd675def58f52424eea0fde5758c722f07dc8e113ac76cbce6e7-6e1e27d-Basiq_platform_1.png" />

## API Reference

The full OpenAPI specification for [api.basiq.io/reference](https://api.basiq.io/reference) is available on [GitHub](https://github.com/basiqio/api-ref). We regularly update the repository to reflect the latest changes. You can download the spec and explore features like:

* Core
* Data
* Identity
* Reporting (Insights)
* Webhooks
* Enrich
* Affordability

## SDK Integration

Our platform uses an SDK to streamline integration, powered by OpenAPI specifications. With the API Reference and SDK generation tools, developers can seamlessly incorporate our APIs into their projects, whether using TypeScript or JavaScript.

## Installation

To generate the SDK for your project:

```shell
$ npx api install <path to an OpenAPI definition>
```

This command initiates the `api` installer, guiding you through project-specific prompts to customize the SDK.

## Supported URI Formats:

* API Registry UUID\
  Example: `@basiq/v3.0#4rlk1xm0uio155`
* URLs\
  Example: `https://raw.githubusercontent.com/basiqio/api-ref/main/core.yml`
* Local file paths are also supported.

API Registry UUID can be found from [here](https://api.basiq.io/reference/posttoken).

<HTMLBlock>{`
<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/QCru8oqvZEskgpjoMNO8?embed&embed_mobile=tab&embed_desktop=inline" title="API Registry" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->
`}</HTMLBlock>

## Code Generation

The code generation installation process that `api` offers comes in the form of an api CLI.

## How It Works

The `api` CLI:

* Downloads your OpenAPI definition and caches it in a `.api/` directory.
* Generate a full api library appropriate for the language you want. 
  > Note that only TypeScript and JavaScript (targeting CommonJS or ECMAScript) are available right now. 
* Install necessary packages required for the generated library to run.
* Install an `@api/your-api` package in your local `package.json`
  * This allows you to use the library with `require('@api/your-api')` or `import '@api/your-api'`.

<HTMLBlock>{`
<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(62.5% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/235B4CBjRZP76VD9eUi6?embed&embed_mobile=tab&embed_desktop=inline" title="Generate BASIQ SDK" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->
`}</HTMLBlock>

To use the SDK, you can integrate it into your project as follows, we are using Javascript as an example:

```javascript
const sdk = require('@api/apiversion3');

sdk.auth('Basic <YOUR-API-KEY>');
sdk.postToken({scope: 'SERVER_ACCESS'}, {
  'BASIQ-version': '3.0'
})
  .then(({ data }) => console.log(data))
  .catch(err => console.error(err));
```

<HTMLBlock>{`
<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(62.5% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/Z5TOPedR9rrRsxF6JUYw?embed&embed_mobile=tab&embed_desktop=inline" title="Run Code " frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->
`}</HTMLBlock>

<hr/>

## Usage

When making API requests using the SDK, you only need to supply either one or two objects, as the SDK automatically handles the placement of parameters and request body payloads according to the API definition.

### Parameters and Request Body

* `body`: This object contains all the data required for a request body payload, such as for POST or PUT requests. It can be either an array or an object, depending on the API operation you're using.
* `metadata`: This object includes all parameters related to path, query, header, or cookie. The SDK manages the placement of these parameters based on the API definition, so you don't need to specify their types explicitly.

### Examples

As we have imported `CORE` OAS from the [github](https://github.com/basiqio/api-ref). We will receive the below functions. 

>  You can repeat this process for the other sections.

```
CORE/
├── authentication/
│   └── post/
├── users/
│   ├── create/
│   ├── retrieve/
│   ├── update/
│   └── delete/
├── consents/
│   ├── retrieve/
│   └── delete/
├── auth_links/
│   ├── create/
│   ├── retrieve/
│   └── delete/
├── events/
│   ├── list_all/
│   ├── retrieve/
│   ├── list_types/
│   └── retrieve_type/
└── jobs/
    ├── get_user_jobs/
    ├── retrieve_job/
    └── create_mfa_response/
```

Let's go through each of them and how to invoke these function calls.

#### Auth Request:

* `auth(...values: string\[])`
  * Handles authentication for the API using different methods such as HTTP Basic, Bearer tokens, or API Keys.
  * Example:\
    Bearer Token: `sdk.auth('myBearerToken')`\
    API Key: `sdk.auth('basic myApiKey')`

```Text Auth
sdk.auth('Basic <YOUR-API-KEY>');
```

#### Post Token (Generate an Auth Token)

* `postToken(body: Object, metadata?: Object)`:
  * Sends a POST request to the /token endpoint.
  * Example: `sdk.postToken(body, metadata)`

#### Create User

For a POST request, provide the request body payload like this:

* `createUser(body: Object)`:
  * Creates a new user with the provided data.
  * Throws: Errors like 400, 401, 403, 404, 500 on various failure scenarios.

```Text POST
sdk.createUser({ name: 'Buster' }).then(...)
```

In this case, `name` corresponds to the request body payload for `createUser`, and the SDK will issue a POST request to `/users` to create a new user named "Buster".

#### Get User

* `getUser(metadata?: Object)`:
  * Retrieves user details by their unique ID.
  * Throws: Errors like 400, 401, 403, 404, 500.

For a GET request, you would supply parameters as follows:

```Text GET
sdk.getUser({ id: 1234 }).then(...)
```

Here, `id` matches the `path` parameter for `getUser`, and the SDK will issue a GET request to `/users/1234`.

#### Update User

* `updateUser(body: Object, metadata?: Object)`:
  * Updates an existing user by setting the provided parameters.
  * Throws: Errors like 400, 401, 403, 404, 500.

#### Delete User

* `deleteUser(metadata: Object)`:
  * Deletes a user permanently along with all their associated data.
  * Throws: Errors like 400, 401, 403, 404, 500, 503.

#### Get Consents

* `getConsents(metadata?: Object)`:
  * Retrieves a list of consents for a user.
  * Throws: Errors like 400, 401, 403, 404, 500.

#### Delete Consents

* `deleteConsent(metadata: Object)`:
  * Deletes a user consent permanently.
  * Throws: Errors like 400, 401, 403, 404, 500, 503.

#### Post Auth Link

* postAuthLink(body: Object, metadata?: Object):
  * Creates an authentication link for a user to authorize a connection.
  * Throws: Errors similar to other endpoints.

#### Get Auth Link

* getAuthLink(metadata?: Object):
  * Retrieves the most recent authentication link for a user.
  * Throws: Errors like 400, 401, 403, 404, 410, 500, 503.

#### Delete Auth Link

* deleteAuthLink(metadata: Object):
  * Deletes the user's authentication link.
  * Throws: Errors like 400, 401, 404, 500, 503.

#### Get all Events

* getEvents(metadata?: Object):
  * Retrieves a list of all events.
  * Throws: Errors like 400, 401, 403, 404, 500, 503.

#### Get an Event

* getTypeById(metadata: Object):
  * Retrieves a specific event type by its ID.
  * Throws: Errors like 400, 401, 403, 404, 429, 500, 503.

#### List Event Types

* listEventTypes():
  * Returns a list of event types.
  * Throws: Errors like 401, 403, 429, 500, 503.

#### Get User Jobs

* `getUserJobs`: 
  * Retrieves the details of all existing and previous jobs associated with a user (only jobs that are less than 7 days old).
  * Throws: Errors like 400, 401, 403, 404, 500, 503.

#### Retrieve a Job

* `getJobs`: 
  * Retrieves the details of an existing job using the unique job identifier returned upon job creation.
  * Throws: Errors like 400, 401, 403, 404, 500, 503.

#### Create MFA Response

* `postJobMfa`: 
  * Creates an MFA (Multi-Factor Authentication) response for a job. Ensure you generate an authentication token with scope CLIENT\_ACCESS and basiq-version = 3.0 to create this resource.
  * Throws: Errors like 400, 401, 403, 404, 500, 503.

### Code Example:

```javascript
const sdk = require('@api/apiversion3');
let access; // 'let' instead of 'var' for block scope

// Authenticate and get access token
sdk.auth('Basic <YOUR-API-KEY');

sdk.postToken({ scope: 'SERVER_ACCESS' }, {
  'BASIQ-version': '3.0'
})
  .then(({ data }) => {
    access = data.access_token;
    console.log('Access token:', access);

    // Authenticate using the access token
    sdk.auth(access);

    // Create a new user
    return sdk.createUser({
      email: 'gavin@hooli.com',
      mobile: '+61410888666',
      firstName: 'Gavin',
      middleName: '',
      lastName: 'Belson'
    });
  })
  .then(({ data }) => {
    console.log('User created:', data);
  })
  .catch(err => console.error('Error:', err));

```

You can clone one of our boilerplate from [here](https://github.com/basiq-ash/Basiq-API-Boilerplate). Also, you can play around with our API reference and see how it all works in the wild [here](https://api.basiq.io/reference/posttoken). 

<Image align="center" src="https://files.readme.io/8ef10e333d598feac5eb4849dde07b862fd73d6d3124f84c9dc4df599b3352b4-274ea20-connect_retina.png" />

Below is the walk through of how to use BASIQ APIs

## API Ref Walkthrough

<HTMLBlock>{`
<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(50.161117078410314% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/xyfpHOLf7mINMxk4v1Do?embed&embed_mobile=tab&embed_desktop=inline" title="API Ref Walkthrough" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->
`}</HTMLBlock>

If you have any questions? feel free to reach out to our support team.
