---
title: Create an auth_link
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
An Auth Link object can be generated to securely capture data from a User. Using the URL allows data to be captured via the hosted Basiq Connect Consent workflow for a given User.

Create a new auth\_link object by making a POST request to the auth\_link endpoint. The new auth\_link will effectively delete previous auth-links for that User/applicant, rendering the previous URL(s) invalid. The 'mobile' attribute is optional. If it is specified this number will take preference over the User object mobile number for 2FA SMS verification. 

**Returns**

Returns a created auth\_link resource, if the operation succeeded. Returns an [error](https://api.basiq.io/docs/errors-1) if the post failed (e.g. not supplying required properties).

```json Definition
POST /users/{user.id}/auth_link
```

```json Example Request
POST /users/ea3a81/auth_link HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json

{
  "mobile": "+123456789"
}
```

```json Example Response
HTTP/1.1 201 Created
Content-Type: application/json

{
    "type": "auth_link",
    "userId": "ec4ea48d-c6a4-4c2d-bc68-8bac810e2e21",
    "expiresAt": "2019-11-21T04:08:50Z",
    "mobile": "+61410888666",
    "links": {
        "self": "https://au-api.basiq.io/users/ec4ea48d/auth_link",
        "public": "https://connect.basiq.io/63448be4"
    }
}
```
