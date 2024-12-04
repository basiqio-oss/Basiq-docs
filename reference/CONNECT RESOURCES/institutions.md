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
[block:parameters]
{
  "data": {
    "h-0": "Attributes",
    "0-0": "**type**\n*string, readonly*",
    "0-1": "Value is \"institution\".",
    "1-0": "**id**\n*string, readonly*",
    "1-1": "A string that uniquely identifies the institution.",
    "2-0": "**name**\n*string, readonly*",
    "2-1": "The full name of the institution.",
    "3-0": "**shortName**\n*string, readonly*",
    "3-1": "Short name of institution.",
    "4-0": "**institutionType**\n*enum, readonly*",
    "4-1": "An enum identifying the institution type. Possible values include:\n- Bank\n- Bank (Foreign)\n- Test Bank\n- Credit Union\n- Financial Services",
    "5-0": "**country**\n*string, readonly*",
    "5-1": "Country in which this institution operates. English short name used by [ISO 3166/MA](https://www.iso.org/iso-3166-country-codes.html).",
    "6-0": "**serviceName**\n*string, readonly*",
    "6-1": "Name of the supported service (as defined by the institution).",
    "7-0": "**serviceType**\n*enum, readonly*",
    "7-1": "An enum identifying the service type. Possible values include:\n- Personal Banking\n- Business Banking\n- Card Access\n- Test",
    "8-0": "**loginIdCaption**\n*string, readonly*",
    "8-1": "Caption used by institution to request login id.",
    "9-0": "**passwordCaption**\n*string, readonly*",
    "9-1": "Caption used by institution to request password.",
    "10-0": "**securityCodeCaption**\n*string, readonly*",
    "10-1": "Caption used by institution to request security code.",
    "11-0": "**logo**\n*object, readonly*",
    "11-1": "Object that contains main colors, and URLs of square and full institution logo image, returned in SVG format.",
    "12-0": "**links**\n*object, read-only*",
    "12-1": "A links object containing the following members:\n- `self` link to the requested institution"
  },
  "cols": 2,
  "rows": 13
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"type\": \"institution\",\n  \"id\": \"AU00000\",\n  \"name\": \"Hooli Bank\",\n  \"shortName\": \"Hooli\",\n  \"institutionType\": \"Test Bank\",\n  \"country\": \"Australia\",\n  \"serviceName\": \"Personal Online Banking\",\n  \"serviceType\": \"Test\",\n  \"loginIdCaption\": \"Login\",\n  \"passwordCaption\": \"Password\",\n  \"logo\": {\n    \"type\": \"image\",\n    \"links\": {\n      \"self\": \"https://s3-ap-southeast-2.amazonaws.com/basiq-institutions/AU00000.png\"\n    }\n  },\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/institutions/AU00000\"\n  }\n}",
      "language": "json",
      "name": "Example Institution Object"
    }
  ],
  "sidebar": true
}
[/block]