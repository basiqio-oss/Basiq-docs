---
title: HTTP errors per endpoint
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
# POST `/token`

<Table>
  <thead>
    <tr>
      <th>
        Status code
      </th>

      <th>
        Response title/detail
      </th>

      <th>
        Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Your account has been disabled. Please contact Basiq support.`
      </td>

      <td>
        Get in touch with the Customer Success to enable your account.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `Internal server error`
      </td>

      <td>
        There has been some internal error, possibly within the AWS architecture. You'll have to try again and seek assistance from Customer Success if it continues.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Authorization header parameter is required`
      </td>

      <td>
        Provide a valid key-value pair 

        `{"Authorization" : " Basic YOUR_API_KEY" }`

         inside request header.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Version 0.9 is no longer supported. Please upgrade to the latest version`
      </td>

      <td>
        Provide a valid 

        `basiq-version`

         (2.0 - 2.1)
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Basiq-version must be specified in HTTP request header`
      </td>

      <td>
        Provide a valid 

        `basiq-version`

         (2.0 - 2.1)
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Unable to authenticate. Please, check your API key`
      </td>

      <td>
        Provide a valid authorization header. This can happen if your API key is deleted, or your application is deleted, or if you use API key from dev environment in production.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Invalid authorization header`
      </td>

      <td>
        Provide a valid key-value pair 

        `{"Authorization" : " Basic YOUR_API_KEY" }`

         inside request header.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Invalid request`
      </td>

      <td>
        Forbidden. There have been too many requests for the token endpoint within a 5 minute period from a specific IP address.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# POST `/users`

<Table>
  <thead>
    <tr>
      <th>
        Status code
      </th>

      <th>
        Response title/detail
      </th>

      <th>
        Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Invalid authorization token.`
      </td>

      <td>
        Provide a key-value pair 

        `{"authorization" : " Bearer YOUR_ACCESS_TOKEN" }`

         inside request header and provide key-value pair  

        `"email" : " your email"`

         or 

        `"mobile" : "your mobile"`

         or both inside request body
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Posted user is not in valid format.`
      </td>

      <td>
        Provide valid key-value pair inside request body
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `One of 'email' or 'mobile' is required.`
      </td>

      <td>
        Provide key-value pair  

        `"email" : " your email"`

         or 

        `"mobile" : "your mobile"`

         or both  inside request body
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Provided email is in bad format.`
      </td>

      <td>
        Provide correct format of email inside request body
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Provided mobile is in bad format.`
      </td>

      <td>
        Provide correct format of mobile inside request body
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Token has expired`
      </td>

      <td>
        Get a new access token on 

        `/token`

         endpoint
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Access to this resource is forbidden`
      </td>

      <td>
        Incorrect/missing scope set for the token you are using, You likely need to supply 

        `scope=SERVER_ACCESS`

        . Make sure when you provide scope you are setting this in the body and not as a request header.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Accept type is not supported`
      </td>

      <td>
        Provide a valid accept header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Business name is required when business number is provided.`
      </td>

      <td>
        Provide business name
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        503
      </td>

      <td>
        `Service is currently unavailable. Please try again later.`
      </td>

      <td>
        Try again later, and if problem persists reach out to Customer Success
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Posted user is not in valid format.`
      </td>

      <td>
        Provide a valid format of posted user
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# GET `/users/{userId}`

<Table>
  <thead>
    <tr>
      <th>
        Status code
      </th>

      <th>
        Response title/detail
      </th>

      <th>
        Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Invalid authorization token.`
      </td>

      <td>
        Provide a key-value pair 

        `{"authorization" : " Bearer YOUR_ACCESS_TOKEN" }`

         inside request header and provide key-value pair  

        `"email" : " your email"`

         or 

        `"mobile" : "your mobile"`

         or both inside request body
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID value is not valid`
      </td>

      <td>
        Check you are providing a valid 

        `userId`

         in the URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested user does not exist.`
      </td>

      <td>
        `userId`

         does not exist... Provide correct 

        `userId`

         in URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Token has expired`
      </td>

      <td>
        Get a new access token on 

        `/token`

         endpoint
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Accept type application/json is not supported on requested endpoint.`
      </td>

      <td>
        Provide a valid accept type
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `You are not authorized to access this resource`
      </td>

      <td>
        Ensure you the token you're using is valid for use with the 

        `userId`

         in the URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `Internal server error. Please contact support.`
      </td>

      <td>
        Contact Customer Success
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# POST `/users/{userId}`

<Table>
  <thead>
    <tr>
      <th>
        Status code
      </th>

      <th>
        Response title/detail
      </th>

      <th>
        Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `One of 'email' or 'mobile' is required.`
      </td>

      <td>
        Provide email OR mobile in request body
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `"Provided mobile is in bad format."`
      </td>

      <td>
        Provide correct format of mobile phone in request body
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Provided email is in bad format.`
      </td>

      <td>
        Provide correct format of email in request body
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Invalid authorization token.`
      </td>

      <td>
        Provide authorization in request header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID value is not valid`
      </td>

      <td>
        Provide a valid 

        `userId`

         in URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Token has expired`
      </td>

      <td>
        Get a new access token from '/token' endpoint
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        Access to this resource is forbidden\`
      </td>

      <td>
        Incorrect/missing scope set for the token you are using, You likely need to supply 

        `scope=SERVER_ACCESS`

        . Make sure when you provide scope you are setting this in the body and not as a request header.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Accept type application/json is not supported on requested endpoint.`
      </td>

      <td>
        Provide a valid accept header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID not supplied`
      </td>

      <td>
        Provide 

        `userId`
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Posted user is not in valid format.`
      </td>

      <td>
        Provide a valid 

        `userId`
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested user does not exist.`
      </td>

      <td>
        This user is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `Internal server error. Please contact support.`
      </td>

      <td>
        Contact Customer Success
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        503
      </td>

      <td>
        `Service is currently unavailable. Please try again later.`
      </td>

      <td>
        Please try again. If problem persists get in touch with Customer Success.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# DELETE `/users/{userId}`

<Table>
  <thead>
    <tr>
      <th>
        Status code
      </th>

      <th>
        Response title/detail
      </th>

      <th>
        Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Missing Authentication Token`
      </td>

      <td>
        Provide authorization token in request header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        \`Requested user does not exist.'
      </td>

      <td>
        This user is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID value is not valid`
      </td>

      <td>
        Provide a valid userId in URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Invalid authorization token.`
      </td>

      <td>
        Provide authorization in request header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Token has expired`
      </td>

      <td>
        Get a new access token on 

        `/token`

         endpoint
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Accept type application/json is not supported on requested endpoint.`
      </td>

      <td>
        Provide a valid accept header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        User ID not supplied\`
      </td>

      <td>
        Provide userID
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `Internal server error. Please contact support.`
      </td>

      <td>
        Please contact Customer Success
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        503
      </td>

      <td>
        `Service is currently unavailable. Please try again later.`
      </td>

      <td>
        Please wait 5 minutes and try again. If problem persists please contact Customer Success
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# POST `/users/{userId}/connections`

<Table>
  <thead>
    <tr>
      <th>
        Status code
      </th>

      <th>
        Response body
      </th>

      <th>
        Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Invalid authorization token.`
      </td>

      <td>
        provide key-value pair \{"authorization" : " Bearer YOUR\_ACCESS\_TOKEN" }  inside request header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Login ID parameter is required.`
      </td>

      <td>
        Provide valid 

        `{"loginId" }`

        inside request body
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Password parameter is required.`
      </td>

      <td>
        Provide valid 

        `{"password" }`

          inside request body
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Institution ID  parameter is required.`
      </td>

      <td>
        Provide valid 

        `{"institutionId"}`

          inside request body
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Posted connection is not in valid format.`
      </td>

      <td>
        Provide valid request body, not empty body
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        415
      </td>

      <td>
        `Content type application/json is not supported on requested endpoint.`
      </td>

      <td>
        Provide content type
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Token has expired`
      </td>

      <td>
        Get a new access token on 

        `/token`

         endpoint
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Requested institution does not exist.`
      </td>

      <td>
        Provide a valid 

        `institutionId`
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Accept type application/json is not supported on requested endpoint.`
      </td>

      <td>
        Provide a valid accept header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Unauthorized access`
      </td>

      <td>
        Ensure you the token you're using is valid for use with the 

        `userId`

         in the URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID value is not valid`
      </td>

      <td>
        Provide a valid userId
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Please contact us to have your API key enabled for Connections.`
      </td>

      <td>
        You currently only have a sandbox account and need to be enabled for live data before you can connect real institutions. Please contact Customer Support to do so.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested resource is not found`
      </td>

      <td>
        This user is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        \`The institution you are trying to connect to is currently disabled. Our developers have been notified and are working to have the issue resolved.
      </td>

      <td>
        We are having issues with this institution and are working on it. You can check the status of it using the status page on your dashboard.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        503
      </td>

      <td>
        `Service is currently unavailable. Please try again later.`
      </td>

      <td>
        Service is unavailable. Please try again in 5 minutes. If the issue persists please contact Customer Success.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `Internal server error. Please contact support.`
      </td>

      <td>
        Please try again in 5 minutes. If the issue persists please contact Customer Success.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Limit reached for sandbox connections.`
      </td>

      <td>
        Sandbox connections are limited and you have reached that limit. Please reach out to CS to increase your limit.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# GET `/users/{userId}/connections`

<Table>
  <thead>
    <tr>
      <th>
        Status code
      </th>

      <th>
        Response title/detail
      </th>

      <th>
        Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Access to this resource is forbidden`
      </td>

      <td>
        Incorrect/missing scope set for the token you are using, You likely need to supply 

        `scope=SERVER_ACCESS`

        . Make sure when you provide scope you are setting this in the body and not as a request header.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Accept type application/json is not supported on requested endpoint.`
      </td>

      <td>
        Provide a valid accept header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID not supplied`
      </td>

      <td>
        Provide a userId
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID value is not valid`
      </td>

      <td>
        Provide a valid userID
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested user does not exist.`
      </td>

      <td>
        This user is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        503
      </td>

      <td>
        `Service is currently unavailable. Please try again later.`
      </td>

      <td>
        Try again in 5 minutes. If problem persists contact customer success.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `Internal server error. Please contact support.`
      </td>

      <td>
        Contact the customer success team,
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# POST `/users/{userId}/connections/refresh`

<Table>
  <thead>
    <tr>
      <th>
        Status code
      </th>

      <th>
        Response title/detail
      </th>

      <th>
        Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Invalid authorization token.`
      </td>

      <td>
        Provide key-value pair 

        `{"authorization" : " Bearer YOUR_ACCESS_TOKEN" }`

          inside request header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Accept type application/json is not supported on requested endpoint.`
      </td>

      <td>
        Provide a valid accept header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID not supplied`
      </td>

      <td>
        Provide userId parameter
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Access to this resource is forbidden`
      </td>

      <td>
        Incorrect/missing scope set for the token you are using, You likely need to supply 

        `scope=SERVER_ACCESS`

        . Make sure when you provide scope you are setting this in the body and not as a request header.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID value is not valid`
      </td>

      <td>
        Provide a valid userId
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested user does not exist.`
      </td>

      <td>
        This user is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `Internal server error. Please contact support.`
      </td>

      <td>
        Please contact support.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# GET `/jobs/{jobId}`

<Table>
  <thead>
    <tr>
      <th>
        Status code
      </th>

      <th>
        Response title/detail
      </th>

      <th>
        Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Invalid authorization token.`
      </td>

      <td>
        Provide key-value pair 

        `{"authorization" : " Bearer YOUR_ACCESS_TOKEN" }`

          inside request header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Token has expired`
      </td>

      <td>
        Get a new access token on 

        `/token`

         endpoint
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Job ID value is not valid`
      </td>

      <td>
        Provide a valid jobId
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        Requested resource is not found
      </td>

      <td>
        This job is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Accept type application/json is not supported on requested endpoint.`
      </td>

      <td>
        Provide a valid accept header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        Job ID not supplied
      </td>

      <td>
        Provide a jobId
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested user does not exist.`
      </td>

      <td>
        This user is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `Internal server error. Please contact support.`
      </td>

      <td>
        Please contact Customer Success
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Access to this resource is forbidden`
      </td>

      <td>
        Incorrect/missing scope set for the token you are using, You likely need to supply 

        `scope=SERVER_ACCESS`

        . Make sure when you provide scope you are setting this in the body and not as a request header.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# GET `/users/{userId}/jobs`

<Table>
  <thead>
    <tr>
      <th>
        Status code
      </th>

      <th>
        Response title/detail
      </th>

      <th>
        Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Invalid authorization token.`
      </td>

      <td>
        Provide key-value pair 

        `{"authorization" : " Bearer YOUR_ACCESS_TOKEN" }`

          inside request header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID value is not valid`
      </td>

      <td>
        Provide a valid userID
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Token has expired`
      </td>

      <td>
        Get a new access token on 

        `/token`

         endpoint
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Access to this resource is forbidden`
      </td>

      <td>
        Incorrect/missing scope set for the token you are using, You likely need to supply 

        `scope=SERVER_ACCESS`

        . Make sure when you provide scope you are setting this in the body and not as a request header.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Accept type application/json is not supported on requested endpoint.`
      </td>

      <td>
        Provide a valid accept header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested user does not exist.`
      </td>

      <td>
        This user is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>

      </td>

      <td>
        Cause: Invalid version for endpoint Body: Route not found for this API version.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# POST `/users/{userId}/connections/{connectionId}`

<Table>
  <thead>
    <tr>
      <th>
        Status code
      </th>

      <th>
        Response title/detail
      </th>

      <th>
        Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID value is not valid`
      </td>

      <td>
        Provide a valid userID
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Invalid authorization token.`
      </td>

      <td>
        Provide key-value pair 

        `{"authorization" : " Bearer YOUR_ACCESS_TOKEN" }`

          inside request header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Token has expired`
      </td>

      <td>
        Get a new access token on 

        `/token`

         endpoint
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Invalid request`
      </td>

      <td>
        Provide a valid userId in URL. This error can happen if you don't provide userId in URL (for example 

        `/users//connections/connectionId`

        )
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Connection ID value is not valid`
      </td>

      <td>
        Provide a valid connectionId in URL, it may be formatted incorrectly.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Access to this resource is forbidden`
      </td>

      <td>
        Incorrect/missing scope set for the token you are using, You likely need to supply 

        `scope=SERVER_ACCESS`

        . Make sure when you provide scope you are setting this in the body and not as a request header.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Accept type application/json is not supported on requested endpoint.`
      </td>

      <td>
        Provide a valid accept header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        415
      </td>

      <td>
        `Content type invalid-content-type is not supported on requested endpoint.`
      </td>

      <td>
        Provide a valid content type
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Unauthorized access`
      </td>

      <td>
        Ensure you the token you're using is valid for use with the resources in the URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Posted connection is not in valid format.`
      </td>

      <td>
        Provide valid request body, not empty body
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Password value is not valid`
      </td>

      <td>
        Please provide correctly formatted password
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested resource is not found`
      </td>

      <td>
        This connection is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Connection type is not Web`
      </td>

      <td>
        The connection type is not web so this is not supported.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Requested resource is not found`
      </td>

      <td>
        This resource is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        \`The institution you are trying to connect to is currently disabled. Our developers have been notified and are working to have the issue resolved.
      </td>

      <td>
        We are having issues with this institution and are working on it. You can check the status of it using the status page on your dashboard.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested resource is not found`
      </td>

      <td>
        This resource is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `Internal server error. Please contact support.`
      </td>

      <td>
        Please contact Customer Success
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        503
      </td>

      <td>
        `Service is currently unavailable. Please try again later.`
      </td>

      <td>
        Please try again. If problem persists get in touch with Customer Success.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# DELETE `/users/{userId}/connections/{connectionId}`

<Table align={["center",null,null]}>
  <thead>
    <tr>
      <th style={{ textAlign: "center" }}>
        400
      </th>

      <th>
        `User ID value is not valid`
      </th>

      <th>
        Provide a valid userID
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>
        401
      </td>

      <td>
        `Invalid authorization token.`
      </td>

      <td>
        Provide key-value pair 

        `{"authorization" : " Bearer YOUR_ACCESS_TOKEN" }`

          inside request header
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>
        403
      </td>

      <td>
        `Token has expired`
      </td>

      <td>
        Get a new access token on 

        `/token`

         endpoint
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>
        403
      </td>

      <td>
        `Invalid request`
      </td>

      <td>
        Provide a valid userId in URL
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>
        400
      </td>

      <td>
        `Connection ID value is not valid`
      </td>

      <td>
        Provide a valid connectionId in URL
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>
        403
      </td>

      <td>
        `Access to this resource is forbidden`
      </td>

      <td>
        Incorrect/missing scope set for the token you are using, You likely need to supply 

        `scope=SERVER_ACCESS`

        . Make sure when you provide scope you are setting this in the body and not as a request header.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>
        400
      </td>

      <td>
        `Connection ID not supplied`
      </td>

      <td>
        Provide connection ID
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>
        404
      </td>

      <td>
        `Requested resource is not found`
      </td>

      <td>
        This resource is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>
        404
      </td>

      <td>
        `Requested user does not exist.`
      </td>

      <td>
        This user is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>
        500
      </td>

      <td>
        `Internal server error. Please contact support.`
      </td>

      <td>
        Please contact Customer Success
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>
        503
      </td>

      <td>
        `Service is currently unavailable. Please try again later.`
      </td>

      <td>
        Please try again. If problem persists get in touch with Customer Success.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "center" }}>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# GET `/users/{userId}/connections/{connectionId}`

<Table>
  <thead>
    <tr>
      <th>
        Status code
      </th>

      <th>
        Response title/detail
      </th>

      <th>
        Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Invalid authorization token.`
      </td>

      <td>
        Provide key-value pair 

        `{"authorization" : " Bearer YOUR_ACCESS_TOKEN" }`

          inside request header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID value is not valid`
      </td>

      <td>
        Provide a valid userID
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Connection ID value is not valid`
      </td>

      <td>
        Provide a valid connectionId in URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested resource is not found`
      </td>

      <td>
        This resource is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Token has expired`
      </td>

      <td>
        Get a new access token on 

        `/token`

         endpoint
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Access to this resource is forbidden`
      </td>

      <td>
        Incorrect/missing scope set for the token you are using, You likely need to supply 

        `scope=SERVER_ACCESS`

        . Make sure when you provide scope you are setting this in the body and not as a request header.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Accept type application/json is not supported on requested endpoint.`
      </td>

      <td>
        Provide a valid accept header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Unauthorized access`
      </td>

      <td>
        Ensure you the token you're using is valid for use with the resources in the URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Connection ID not supplied`
      </td>

      <td>
        Provide connection ID
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `Internal server error. Please contact support.`
      </td>

      <td>
        Please contact Customer Success
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        503
      </td>

      <td>
        `Service is currently unavailable. Please try again later.`
      </td>

      <td>
        Please try again. If problem persists get in touch with Customer Success.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# POST `/users/{userId}/connections/{connectionId}/refresh`

<Table>
  <thead>
    <tr>
      <th>
        Status code
      </th>

      <th>
        Response title/detail
      </th>

      <th>
        Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Invalid authorization token.`
      </td>

      <td>
        Provide key-value pair 

        `{"authorization" : " Bearer YOUR_ACCESS_TOKEN" }`

          inside request header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Token has expired`
      </td>

      <td>
        Get a new access token on 

        `/token`

         endpoint
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID value is not valid`
      </td>

      <td>
        Provide a valid userID
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested user does not exist.`
      </td>

      <td>
        This user is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Connection ID not supplied`
      </td>

      <td>
        Provide a connectionId in URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Connection ID value is not valid`
      </td>

      <td>
        Provide a valid connectionId in URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Accept type application/json is not supported on requested endpoint.`
      </td>

      <td>
        Provide a valid accept header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Access to this resource is forbidden`
      </td>

      <td>
        Incorrect/missing scope set for the token you are using, You likely need to supply 

        `scope=SERVER_ACCESS`

        . Make sure when you provide scope you are setting this in the body and not as a request header.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested resource is not found`
      </td>

      <td>
        This resource is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Connection type is not Web`
      </td>

      <td>
        Connection type is not valid therefore not compatible.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Cannot login to target institution using supplied credentials. Please check credentials and try again.`
      </td>

      <td>
        The credentials are invalid. This could be because a user has changed their password. You may need to prompt user to resupply new credentials.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Please contact us to have your API key enabled for Connections.`
      </td>

      <td>
        You currently only have a sandbox account and need to be enabled for live data before you can connect real institutions. Please contact Customer Support to do so.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `Internal server error. Please contact support.`
      </td>

      <td>
        Please contact Customer Success
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        503
      </td>

      <td>
        `Service is currently unavailable. Please try again later.`
      </td>

      <td>
        Please try again. If problem persists get in touch with Customer Success.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# GET `/users/{userId}/accounts`

<Table>
  <thead>
    <tr>
      <th>
        Status code
      </th>

      <th>
        Response title/detail
      </th>

      <th>
        Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Token has expired`
      </td>

      <td>
        Get a new access token on 

        `/token`

         endpoint
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Invalid authorization token.`
      </td>

      <td>
        Provide key-value pair 

        `{"authorization" : " Bearer YOUR_ACCESS_TOKEN" }`

          inside request header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID value is not valid`
      </td>

      <td>
        Provide a valid userID
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested user does not exist.`
      </td>

      <td>
        This user is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Access to this resource is forbidden`
      </td>

      <td>
        Incorrect/missing scope set for the token you are using, You likely need to supply 

        `scope=SERVER_ACCESS`

        . Make sure when you provide scope you are setting this in the body and not as a request header.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Accept type application/json is not supported on requested endpoint.`
      </td>

      <td>
        Provide a valid accept header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested resource is not found`
      </td>

      <td>
        This resource is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Requested connection does not exist.`
      </td>

      <td>
        This can occur if the connection type is not "web"
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `Internal server error. Please contact support.`
      </td>

      <td>
        Please contact Customer Success
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# GET `/users/{userId}/accounts/{accountId}`

<Table>
  <thead>
    <tr>
      <th>
        Status code
      </th>

      <th>
        Response title/detail
      </th>

      <th>
        Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Token has expired`
      </td>

      <td>
        Get a new access token on 

        `/token`

         endpoint
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Invalid authorization token.`
      </td>

      <td>
        Provide key-value pair 

        `{"authorization" : " Bearer YOUR_ACCESS_TOKEN" }`

          inside request header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Account ID value is not valid`
      </td>

      <td>
        Provide a valid accountId in URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested resource is not found`
      </td>

      <td>
        This resource is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID value is not valid`
      </td>

      <td>
        Provide a valid userID in URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Access to this resource is forbidden`
      </td>

      <td>
        Incorrect/missing scope set for the token you are using, You likely need to supply 

        `scope=SERVER_ACCESS`

        . Make sure when you provide scope you are setting this in the body and not as a request header.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Accept type application/json is not supported on requested endpoint.`
      </td>

      <td>
        Provide a valid accept header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Account ID not supplied`
      </td>

      <td>
        Provide valid accountId
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID value is not valid`
      </td>

      <td>
        Provide a valid userID
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested user does not exist.`
      </td>

      <td>
        This user is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `Internal server error. Please contact support.`
      </td>

      <td>
        Please contact Customer Success
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# GET `/users/{userId}/transactions`

<Table>
  <thead>
    <tr>
      <th>
        Status code
      </th>

      <th>
        Response title/detail
      </th>

      <th>
        Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Token has expired`
      </td>

      <td>
        Get a new access token on 

        `/token`

         endpoint
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Invalid authorization token.`
      </td>

      <td>
        Provide key-value pair 

        `{"authorization" : " Bearer YOUR_ACCESS_TOKEN" }`

          inside request header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID value is not valid`
      </td>

      <td>
        Provide a valid userID in URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID value is not valid`
      </td>

      <td>
        Provide a valid userID
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested user does not exist.`
      </td>

      <td>
        This user is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Access to this resource is forbidden`
      </td>

      <td>
        Incorrect/missing scope set for the token you are using, You likely need to supply 

        `scope=SERVER_ACCESS`

        . Make sure when you provide scope you are setting this in the body and not as a request header.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Accept type application/json is not supported on requested endpoint.`
      </td>

      <td>
        Provide a valid accept header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Next value is not valid`
      </td>

      <td>
        Provide a valid value for parameter next in URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Limit value is not valid`
      </td>

      <td>
        Provide a valid value for parameter limit in URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Maximum limit allowed is 500`
      </td>

      <td>
        Provide a value for parameter limit that is not greater than 500
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `PostDate is not valid`
      </td>

      <td>
        Provide a valid value for parameter PostDate
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `Internal server error. Please contact support.`
      </td>

      <td>
        Please contact Customer Success
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# GET `/users/{userId}/transactions/{transactionId}`

<Table>
  <thead>
    <tr>
      <th>
        Status code
      </th>

      <th>
        Response title/detail
      </th>

      <th>
        Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Token has expired`
      </td>

      <td>
        Get a new access token on 

        `/token`

         endpoint
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Invalid authorization token.`
      </td>

      <td>
        Provide key-value pair 

        `{"authorization" : " Bearer YOUR_ACCESS_TOKEN" }`

          inside request header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID not supplied`
      </td>

      <td>
        Provide userId in URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID value is not valid`
      </td>

      <td>
        Provide a valid userID in the URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested user does not exist.`
      </td>

      <td>
        This user is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Transaction ID value is not valid`
      </td>

      <td>
        Provide valid transactionId in URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested resource is not found`
      </td>

      <td>
        This resource is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Accept type application/json is not supported on requested endpoint.`
      </td>

      <td>
        Provide a valid accept header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Access to this resource is forbidden`
      </td>

      <td>
        Incorrect/missing scope set for the token you are using, You likely need to supply 

        `scope=SERVER_ACCESS`

        . Make sure when you provide scope you are setting this in the body and not as a request header.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Transaction ID not supplied`
      </td>

      <td>
        Provide transaction ID in URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        503
      </td>

      <td>
        `Service is currently unavailable. Please try again later.`
      </td>

      <td>
        Please try again. If problem persists get in touch with Customer Success.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `Internal server error. Please contact support.`
      </td>

      <td>
        Please contact Customer Success
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# POST `/users/{userId}/affordability`

<Table>
  <thead>
    <tr>
      <th>
        Status code
      </th>

      <th>
        Response title/detail
      </th>

      <th>
        Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Invalid authorization token.`
      </td>

      <td>
        Provide key-value pair 

        `{"authorization" : " Bearer YOUR_ACCESS_TOKEN" }`

          inside request header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Token has expired`
      </td>

      <td>
        Get a new access token on 

        `/token`

         endpoint
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID value is not valid`
      </td>

      <td>
        Provide a valid userID
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested resource is not found`
      </td>

      <td>
        These accounts are unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Accept type application/json is not supported on requested endpoint.`
      </td>

      <td>
        Provide a valid accept header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Access to this resource is forbidden`
      </td>

      <td>
        Incorrect/missing scope set for the token you are using, You likely need to supply 

        `scope=SERVER_ACCESS`

        . Make sure when you provide scope you are setting this in the body and not as a request header.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Unauthorized access`
      </td>

      <td>
        Ensure you the token you're using is valid for use with the resources in the URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        Dates not in valid format. Date has to be in yyyy-mm-dd format
      </td>

      <td>
        Provide a valid dates format in yyyy-mm-dd format
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `fromDate not in valid format. Date has to be in yyyy-mm-dd format`
      </td>

      <td>
        Provide a valid dates format in yyyy-mm-dd format
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `toDate not in valid format. Date has to be in yyyy-mm-dd format`
      </td>

      <td>
        Provide a valid toDate format in yyyy-mm-dd format
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `toDate must be be after or equal to fromDate`
      </td>

      <td>
        Ensure you are sendign a
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested user does not exist.`
      </td>

      <td>
        This user is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `Internal server error. Please contact support.`
      </td>

      <td>
        Please contact Customer Success
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User's accounts contains mixed currencies`
      </td>

      <td>
        User's accounts contains mixed currencies which is causing issues with aggregation. Remove these accounts
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# GET `/users/{userId}/affordability/{snapshotId}`

<Table>
  <thead>
    <tr>
      <th>
        Status code
      </th>

      <th>
        Response title/detail
      </th>

      <th>
        Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Invalid authorization token.`
      </td>

      <td>
        Provide key-value pair 

        `{"authorization" : " Bearer YOUR_ACCESS_TOKEN" }`

          inside request header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Token has expired`
      </td>

      <td>
        Get a new access token on 

        `/token`

         endpoint
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID value is not valid`
      </td>

      <td>
        Provide a valid userID
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Snapshot ID value is not valid`
      </td>

      <td>
        Provide a valid snapshotId in URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Accept type is not supported`
      </td>

      <td>
        Provide a valid accept type
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Access to this resource is forbidden`
      </td>

      <td>
        Incorrect/missing scope set for the token you are using, You likely need to supply 

        `scope=SERVER_ACCESS`

        . Make sure when you provide scope you are setting this in the body and not as a request header.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Unauthorized access`
      </td>

      <td>
        Ensure you the token you're using is valid for use with the resources in the URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Snapshot ID value is not supplied`
      </td>

      <td>
        Missing snapshotId, please provide.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested user does not exist.`
      </td>

      <td>
        This user is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `Internal server error. Please contact support.`
      </td>

      <td>
        Please contact Customer Success
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Please contact us to have your API key enabled for Income Summary.`
      </td>

      <td>
        You are not enabled for this feature. Please contact Customer Success to have this enabled.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        503
      </td>

      <td>
        `Service is currently unavailable. Please try again later.`
      </td>

      <td>
        Please try again. If problem persists get in touch with Customer Success.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# POST `users/{userId}/income`

<Table>
  <thead>
    <tr>
      <th>
        Status code
      </th>

      <th>
        Response title/detail
      </th>

      <th>
        Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Invalid authorization token.`
      </td>

      <td>
        Provide key-value pair 

        `{"authorization" : " Bearer YOUR_ACCESS_TOKEN" }`

          inside request header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Token has expired`
      </td>

      <td>
        Get a new access token on 

        `/token`

         endpoint
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID value is not valid`
      </td>

      <td>
        Provide a valid userID
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Accept type application/json is not supported on requested endpoint.`
      </td>

      <td>
        Provide a valid accept header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Access to this resource is forbidden`
      </td>

      <td>
        Incorrect/missing scope set for the token you are using, You likely need to supply 

        `scope=SERVER_ACCESS`

        . Make sure when you provide scope you are setting this in the body and not as a request header.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Unauthorized access`
      </td>

      <td>
        Ensure you the token you're using is valid for use with the resources in the URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        Dates not in valid format. Date has to be in yyyy-mm-dd format
      </td>

      <td>
        Provide a valid dates format in yyyy-mm-dd format
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `fromDate not in valid format. Date has to be in yyyy-mm-dd format`
      </td>

      <td>
        Provide a valid dates format in yyyy-mm-dd format
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `toDate not in valid format. Date has to be in yyyy-mm-dd format`
      </td>

      <td>
        Provide a valid toDate format in yyyy-mm-dd format
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested user does not exist.`
      </td>

      <td>
        This user is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested resource is not found`
      </td>

      <td>
        This resource is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Please contact us to have your API key enabled for Income Summary.`
      </td>

      <td>
        You are not enabled for this feature. Please contact Customer Success to have this enabled.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User's accounts contains mixed currencies`
      </td>

      <td>
        User's accounts contains mixed currencies which is causing issues with aggregation. Remove these accounts
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `Internal server error. Please contact support.`
      </td>

      <td>
        Please contact Customer Success
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# GET `/users/{userId}/income/{snapshotId}`

<Table>
  <thead>
    <tr>
      <th>
        Status code
      </th>

      <th>
        Response title/detail
      </th>

      <th>
        Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Invalid authorization token.`
      </td>

      <td>
        Provide key-value pair 

        `{"authorization" : " Bearer YOUR_ACCESS_TOKEN" }`

          inside request header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Token has expired`
      </td>

      <td>
        Get a new access token on 

        `/token`

         endpoint
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID value is not valid`
      </td>

      <td>
        Provide a valid userID
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Snapshot ID value is not valid`
      </td>

      <td>
        Provide a valid snapshotId in URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Accept type application/json is not supported on requested endpoint.`
      </td>

      <td>
        provide a valid accept type
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Access to this resource is forbidden`
      </td>

      <td>
        Incorrect/missing scope set for the token you are using, You likely need to supply 

        `scope=SERVER_ACCESS`

        . Make sure when you provide scope you are setting this in the body and not as a request header.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Unauthorized access`
      </td>

      <td>
        Ensure you the token you're using is valid for use with the resources in the URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Snapshot ID value is not supplied`
      </td>

      <td>
        Missing snapshotId, please provide in URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested user does not exist.`
      </td>

      <td>
        This user is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested resource is not found`
      </td>

      <td>
        This resource is unable to be found as the user does not have any accounts.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Please contact us to have your API key enabled for Income Summary.`
      </td>

      <td>
        You are not enabled for this feature. Please contact Customer Success to have this enabled.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `Internal server error. Please contact support.`
      </td>

      <td>
        Please contact Customer Success
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# POST `/users/{userId}/expenses`

<Table>
  <thead>
    <tr>
      <th>
        Status code
      </th>

      <th>
        Response title/detail
      </th>

      <th>
        Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Invalid authorization token.`
      </td>

      <td>
        Provide key-value pair 

        `{"authorization" : " Bearer YOUR_ACCESS_TOKEN" }`

          inside request header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Token has expired`
      </td>

      <td>
        Get a new access token on 

        `/token`

         endpoint
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID value is not valid`
      </td>

      <td>
        Provide a valid userID
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Accept type is not supported`
      </td>

      <td>
        Provide a valid accept type
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Access to this resource is forbidden`
      </td>

      <td>
        Incorrect/missing scope set for the token you are using, You likely need to supply 

        `scope=SERVER_ACCESS`

        . Make sure when you provide scope you are setting this in the body and not as a request header.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Unauthorized access`
      </td>

      <td>
        Ensure you the token you're using is valid for use with the resources in the URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        Dates not in valid format. Date has to be in yyyy-mm-dd format
      </td>

      <td>
        Provide a valid dates format in yyyy-mm-dd format
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `fromDate not in valid format. Date has to be in yyyy-mm-dd format`
      </td>

      <td>
        Provide a valid dates format in yyyy-mm-dd format
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `toDate not in valid format. Date has to be in yyyy-mm-dd format`
      </td>

      <td>
        Provide a valid toDate format in yyyy-mm-dd format
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested resource is not found`
      </td>

      <td>
        This resource is unable to be found as the user does not have any accounts.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Please contact us to have your API key enabled for Income Summary.`
      </td>

      <td>
        You are not enabled for this feature. Please contact Customer Success to have this enabled.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User's accounts contains mixed currencies`
      </td>

      <td>
        User's accounts contains mixed currencies which is causing issues with aggregation. Remove these accounts
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `Internal server error. Please contact support.`
      </td>

      <td>
        Please contact Customer Success
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# GET `users/{userId}/expenses/{snapshotId}`

<Table>
  <thead>
    <tr>
      <th>
        Status code
      </th>

      <th>
        Response title/detail
      </th>

      <th>
        Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Invalid authorization token.`
      </td>

      <td>
        Provide key-value pair 

        `{"authorization" : " Bearer YOUR_ACCESS_TOKEN" }`

          inside request header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Token has expired`
      </td>

      <td>
        Get a new access token on 

        `/token`

         endpoint
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID value is not valid`
      </td>

      <td>
        Provide a valid userID
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Snapshot ID value is not valid`
      </td>

      <td>
        Provide a valid snapshotId in URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Accept type application/json is not supported on requested endpoint.`
      </td>

      <td>
        Provide a valid accept header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Access to this resource is forbidden`
      </td>

      <td>
        Incorrect/missing scope set for the token you are using, You likely need to supply 

        `scope=SERVER_ACCESS`

        . Make sure when you provide scope you are setting this in the body and not as a request header.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Unauthorized access`
      </td>

      <td>
        Ensure you the token you're using is valid for use with the resources in the URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Snapshot ID value is not supplied`
      </td>

      <td>
        Missing snapshotId, please provide in URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `Internal server error. Please contact support.`
      </td>

      <td>
        Please contact Customer Success
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested user does not exist.`
      </td>

      <td>
        This user is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Invalid expenses snapshot ID provided`
      </td>

      <td>
        Invalid snapshotId, please check the value you are providing
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `User doesn't have any accounts`
      </td>

      <td>
        User does not have any accounts connected
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Please contact us to have your API key enabled for Income Summary.`
      </td>

      <td>
        You are not enabled for this feature. Please contact Customer Success to have this enabled.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

# POST `users/{userId}/statements`

<Table>
  <thead>
    <tr>
      <th>
        Status code
      </th>

      <th>
        Response title/detail
      </th>

      <th>
        Action
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Invalid authorization token.`
      </td>

      <td>
        Provide key-value pair 

        `{"authorization" : " Bearer YOUR_ACCESS_TOKEN" }`

          inside request header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Token has expired`
      </td>

      <td>
        Get a new access token on 

        `/token`

         endpoint
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User ID value is not valid`
      </td>

      <td>
        Provide a valid userID
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Statement is not valid`
      </td>

      <td>
        Check you are providing either a valid statement file or an institutionId.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        413
      </td>

      <td>
        `Request Too Long`
      </td>

      <td>
        The statement you have provided is too large, try with something smaller.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Institution AU00000 is not supported on this endpoint`
      </td>

      <td>
        Choose correct/compatible institution for statement upload
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `Accept type application/json is not supported on requested endpoint.`
      </td>

      <td>
        Provide a valid accept header
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Access to this resource is forbidden`
      </td>

      <td>
        Incorrect/missing scope set for the token you are using, You likely need to supply 

        `scope=SERVER_ACCESS`

        . Make sure when you provide scope you are setting this in the body and not as a request header.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        401
      </td>

      <td>
        `Unauthorized access`
      </td>

      <td>
        Ensure you the token you're using is valid for use with the resources in the URL
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        404
      </td>

      <td>
        `Requested user does not exist.`
      </td>

      <td>
        This user is unable to be found. It may have been deleted or you may be using the incorrect API as resources are restricted to their designated applications.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        403
      </td>

      <td>
        `Please contact us to have your API key enabled for Income Summary.`
      </td>

      <td>
        You are not enabled for this feature. Please contact Customer Success to have this enabled.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        400
      </td>

      <td>
        `User's accounts contains mixed currencies`
      </td>

      <td>
        User's accounts contains mixed currencies which is causing issues with aggregation. Remove these accounts
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        500
      </td>

      <td>
        `Internal server error. Please contact support.`
      </td>

      <td>
        Please contact Customer Success
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        503
      </td>

      <td>
        `Service is currently unavailable. Please try again later.`
      </td>

      <td>
        Please try again. If problem persists get in touch with Customer Success.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>

      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>
