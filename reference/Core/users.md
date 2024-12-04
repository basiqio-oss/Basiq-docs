---
title: Users
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
## Creating a User

To [create a new user](https://api.basiq.io/reference/createuser), make a POST request to the following endpoint:

```curl Create a User
POST https://au-api.basiq.io/users
```

Ensure the request includes the necessary headers:

```curl
accept: application/json
content-type: application/json
```

The request body should contain the user details in JSON format. The minimum required fields are either "email" or "mobile". Optionally, you can include additional details such as first name, last name, and business information. Example request:

```curl
{
  "email": "gavin@hooli.com",
  "mobile": "+61410888999",
  "firstName": "Gavin",
  "lastName": "Belson",
  "businessName": "Manly Accounting PTY LTD",
  "businessIdNo": "16 7645 892",
  "businessIdNoType": "ABN",
  "businessAddress": {
    "addressLine1": "21 Sydney Rd",
    "suburb": "Manly",
    "state": "NSW",
    "postcode": "2095",
    "countryCode": "AUS"
  },
  "verificationStatus": true,
  "verificationDate": "12/01/2024"
}

```

Please note that the Basiq API does not check for existing users with the same email or mobile number. It relies on the user ID for uniqueness.

## Retrieving a User

To [retrieve the details of an existing user](https://api.basiq.io/reference/getuser), make a GET request to the following endpoint:

```curl
GET https://au-api.basiq.io/users/{userId}
```

Replace {userId} with the unique identifier of the user returned upon creation.

## Updating a User

To [update a user's details](https://api.basiq.io/reference/updateuser), make a POST request to the following endpoint:

```curl
POST https://au-api.basiq.io/users/{userId}
```

Replace {userId} with the unique identifier of the user. Provide the parameters you wish to update in the request body. Any parameters not provided will remain unchanged.

## Deleting a User

To [permanently delete a user](https://api.basiq.io/reference/deleteuser) and all associated data, make a DELETE request to the following endpoint:

```curl
DELETE https://au-api.basiq.io/users/{userId}
```

Replace {userId} with the unique identifier of the user.

> 🚧 Deleting a user cannot be undone and will permanently remove all associated data.