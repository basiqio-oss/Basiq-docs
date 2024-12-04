---
title: Error codes
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
Below you will find details for our various response codes.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Code
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        **invalid-credentials** 
      </td>

      <td style={{ textAlign: "left" }}>
        **Invalid Attribute**\
        Cannot login to target institution using supplied credentials. Please check credentials and try again.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **resource-not-found** 
      </td>

      <td style={{ textAlign: "left" }}>
        **Invalid Attribute**\
        Requested resource is not found. Check details message.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **resource-already-exists** 
      </td>

      <td style={{ textAlign: "left" }}>
        **Invalid Attribute**\
        Resource already exists. Check details message.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **unsupported-content-type** 
      </td>

      <td style={{ textAlign: "left" }}>
        **Invalid Attribute**\
        Requested content type is not supported.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **unsupported-accept** 
      </td>

      <td style={{ textAlign: "left" }}>
        **Invalid Attribute**\
        Accept type is not supported.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **invalid-content** 
      </td>

      <td style={{ textAlign: "left" }}>
        **Invalid Attribute**\
        Invalid request content. Check details message.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **parameter-not-supplied** 
      </td>

      <td style={{ textAlign: "left" }}>
        **Missing Attribute**\
        Required parameter not supplied. Check details and source message.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **parameter-not-valid** 
      </td>

      <td style={{ textAlign: "left" }}>
        **Invalid Attribute**\
        Parameter value is not valid. Check details and source message.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **internal-server-error** 
      </td>

      <td style={{ textAlign: "left" }}>
        **Server Error**\
        Internal server error. Please contact support.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **service-unavailable** 
      </td>

      <td style={{ textAlign: "left" }}>
        **Service Unavailable**\
        Service is currently unavailable. Please try again later.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **too-many-requests** 
      </td>

      <td style={{ textAlign: "left" }}>
        **Service Unavailable**\
        Request rate limit per connection reached. Follow detail message for futher instructions.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **method-not-allowed** 
      </td>

      <td style={{ textAlign: "left" }}>
        **Not Allowed**\
        Requested method is not allowed.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **unauthorized-access** 
      </td>

      <td style={{ textAlign: "left" }}>
        **Unauthorized**\
        Unauthorized access.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **invalid-authorization-token** 
      </td>

      <td style={{ textAlign: "left" }}>
        **Unauthorized**\
        Invalid authorization token. Check details message.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **invalid-authorization-request** 
      </td>

      <td style={{ textAlign: "left" }}>
        **Unauthorized**\
        Invalid authorization request. Check details message.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **no-production-access** 
      </td>

      <td style={{ textAlign: "left" }}>
        **Unauthorized**\
        Partner has permission to access Sandbox data only. For accessing live Institution data, please contact us via Intercom or email.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **account-not-accessible-requires-user-action** 
      </td>

      <td style={{ textAlign: "left" }}>
        **Not Accesible**\
        An action is required from end-user before account details can be returned.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **maintenance-error** 
      </td>

      <td style={{ textAlign: "left" }}>
        **Not Accessible**\
        Requested resource is currently unavailable due to maintenance on Institution's side.
      </td>
    </tr>
  </tbody>
</Table>
