---
title: Open Banking
excerpt: An overview
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
## CDR 

Australia has commenced a new program called **Consumer Data Right (CDR)** that provides a framework for the sharing of data held with specific institutions. The CDR program is an industry wide initiative which will be rolled out to Banking, Utilities, Telecommunication and other industries over time. The first industry that CDR is being rolled out-to is the Banking sector, with an initiative called Open Banking. Open Banking provides a series of API services that **Accredited Data Recipients (ADR)** i.e. Fintechs can consumer from **Data Holders (DH)** i.e. banks.

&nbsp;
&nbsp;
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bbddefc-Group_2590_1.svg",
        "Group 2590 (1).svg",
        510,
        143,
        "#d0ffee"
      ],
      "sizing": "smart"
    }
  ]
}
[/block]
&nbsp;
The CDR framework ultimately is a set of rules and regulations that outline the controls and requirements around consent management and the handling of data. CDR at present only deals with the reading of data, and has no support for write access i.e. the ability for actions to be executed with these institutions.  

###### For more information regarding the latest CDR rules see [here](https://www.legislation.gov.au/Series/F2020L00094).

## Open Banking 

To consume the APIs made available through Open Banking, the Australian Government has introduced an accreditation process that all ADRs (consumers of APIs) are required to go through. This process ensures that each company has appropriate security controls in place, and methods by which to protect customer privacy. Once a company has been granted accreditation, they are issued with a set of certificates that enables them to be identified when consuming data from a Data Holder. Each Data Holder is required to verify that the ADR consuming the data is accredited. This is done by consuming API services from the ACCC Register.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ef31054-Frame_6.svg",
        "Frame 6.svg",
        800,
        300,
        "#130f26"
      ]
    }
  ]
}
[/block]
Please note the existence of 3 entities that are part of the CDR process: 

1. **Accredited Data Recipient (ADR)** - An accredited company that requires consented access to customers financial data.

2. **ACCC Register** - The government body (and set-of services) that holds a register of all accredited parties. 

3. **Data Holder (DH)** - The institution e.g. Bank that provides access to a customers financial data.

## Enabling your application for Open Banking

*Being enabled for Open Banking is optional and is not required in order to use API v3.0, however partners must be using v3.0 in order to be enabled for Open Banking.*

Enablement for Open Banking will be done at an application level. Partners wishing to enable themselves for Open Banking will need to reach out to the customer success who will assist them in registering the following CDR details:
[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Description",
    "h-2": "description",
    "0-0": "type",
    "0-1": "Accreditation type",
    "1-0": "entityName",
    "2-0": "licenceNumber",
    "1-1": "The Partner Legal entity name for CDR",
    "2-1": "The Accreditation Number the Partner will be using to access CDR data"
  },
  "cols": 2,
  "rows": 3
}
[/block]
## Supported models 

Due to the strictly regulated nature of the CDR, Basiq is responsible for ensuring any of our partners consuming CDR data via the platform are doing so under an approved CDR access model. Initially Basiq will be offering three models for partners to subscribe to: 

1. **ADR:** For Accredited Data Recipients
2. **Sponsor/Affiliate:** For partners who Basiq has sponsored.
3. **Principal/Representative:** For partners who Basiq have accepted as Representatives.

Read more about the sponsorship models [here](https://api.basiq.io/docs/supported-access-models).