---
title: Institutions
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
The institution object represents a financial institution (such as a bank, credit union etc). You can use this object to obtain a list of supported institutions or to get general information about each institution.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Attributes
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        **type**
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Value is "institution".
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **id**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        A string that uniquely identifies the institution.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **name**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        The full name of the institution.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **shortName**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Short name of institution.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **institutionType**\
        *enum, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        An enum identifying the institution type. Possible values include:

        * Bank
        * Bank (Foreign)
        * Test Bank
        * Credit Union
        * Financial Services
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **country**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Country in which this institution operates. English short name used by [ISO 3166/MA](https://www.iso.org/iso-3166-country-codes.html).
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **serviceName**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Name of the supported service (as defined by the institution).
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **serviceType**\
        *enum, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        An enum identifying the service type. Possible values include:

        * Personal Banking
        * Business Banking
        * Card Access
        * Test
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **loginIdCaption**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Caption used by institution to request login id.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **secondaryLoginIdCaption**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Caption used by institution to request secondary login id.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **passwordCaption**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Caption used by institution to request password.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **securityCodeCaption**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Caption used by institution to request security code.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **colors**\
        *object, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Object that contains institution colors (e.g. primary).
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **tier**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Institution's tier - a representation of it's business and market share in the relevant country/region. Values range from 1 to 4. Tier 1 are Institutions with the highest impact on the market. For example, CBA is a Tier 1 Bank, Suncorp is a Tier 2 Bank, etc.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **logo**\
        *object, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Object that contains main colors, and URLs of square and full institution logo image, returned in SVG format.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **links**\
        *object, read-only*
      </td>

      <td style={{ textAlign: "left" }}>
        A links object containing the following members:

        * `self` link to the requested institution
      </td>
    </tr>
  </tbody>
</Table>

```json Example Institution Object
{
    "type": "institution",
    "id": "AU00000",
    "name": "Hooli Bank",
    "shortName": "Hooli",
    "institutionType": "Test Bank",
    "country": "Australia",
    "serviceName": "Personal Online Banking",
    "serviceType": "Test",
    "loginIdCaption": "Login",
    "passwordCaption": "Password",
    "tier": "4",
    "logo": {
        "type": "image",
        "colors": {
            "primary": "#000000"
        },
        "links": {
            "square": "https://s3-ap-southeast-2.amazonaws.com/basiq-institutions/AU00000.svg",
            "full": "https://s3-ap-southeast-2.amazonaws.com/basiq-institutions/AU00000-full.svg"
        }
    },
    "links": {
        "self": "https://au-api.basiq.io/institutions/AU00000"
    }
}
```
