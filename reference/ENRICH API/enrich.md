---
title: Enrich
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
The Enrich resource enables you to retrieve details by passing in a search `query` containing a bank transaction description. 

The service enriches transaction data with multiple attributes, returning a transaction classification and three metadata components.  The transaction classification will first determine if the transaction is of type payment, transfer, cash-withdrawal, bank-fee etc. The engine then derives merchant information, purchase location and prescribes an industry standard categorisation for each payment transaction.

You can subscribe to one or all of the following three core datasets returned depending on your use case.  

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Data
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `Merchant`
      </td>

      <td style={{ textAlign: "left" }}>
        Details relating to the store or merchant such as business name, website and contact details
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `Location`
      </td>

      <td style={{ textAlign: "left" }}>
        Details relating to the location of the entity such as address and geocode location
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `Category`
      </td>

      <td style={{ textAlign: "left" }}>
        Industry standard categorisation with a 4 level hierarchy for banking transactions.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `Links`
      </td>

      <td style={{ textAlign: "left" }}>
        Provides direct link to `self` - original query\
        Provides links master and thumb merchant logos
      </td>
    </tr>
  </tbody>
</Table>

The query will typically be the full textual description of a transaction record, however the partner calling the API may also optionally pass in more details to make the search more relevant (such as an MCC code). 

**Pre-requisties**

• Prior to calling the enrich service, you will need to be authenticated via the Basiq API service.\
• The service will only be accessible to partners that have been enabled.

**Request**

You can call the `enrich` endpoint by passing in the following query parameters:

> 📘
>
> You will need to ensure that the search query is **url encoded** before calling the resource and must contain at least 3 characters.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Mandatory Arguments
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        **q**
        *string, required*
      </td>

      <td style={{ textAlign: "left" }}>
        This is the search string that is used to lookup the entity (merchant) information. 

        `**q=garfish%20MANLY%20NS**&country=AU&institution=AU06703`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **institution**\
        *string, required*
      </td>

      <td style={{ textAlign: "left" }}>
        Identifies the institution from where the transaction was derived.\
        This must be a Basiq recognisable institution ID.

        `enrich?METRO%20PETROLEUM%20FR%20FORE&country=AU&accountType=transaction&amount=-12.95&**institution=AU04301**`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **country**\
        *string, required*
      </td>

      <td style={{ textAlign: "left" }}>
        Specifies the country the search should be narrowed down to.\
        Passing in a country value will limit the search to the specified country.\
        The country must be in [ISO 3166 Alpha-2 format] ([https://www.iso.org/obp/ui/#search](https://www.iso.org/obp/ui/#search)) 

        `q=garfish%20MANLY%20NS&**country=AU**&institution=AU06703`
      </td>
    </tr>
  </tbody>
</Table>

Note: accountType and amount are mandatory arguments for transaction classification. If these arguments are not provided, the query will be treated as a payment transaction and categorised accordingly.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Optional Arguments
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        **mcc**
        *string, optional*
      </td>

      <td style={{ textAlign: "left" }}>
        Merchant classification code as defined by Visa and Mastercard

        `q=garfish%20MANLY%20NS&country=AU&institution=AU06703&**mcc=3299**`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **accountType**\
        *string, optional*
      </td>

      <td style={{ textAlign: "left" }}>
        The Account type from which the transaction was derived.

        `METRO%20PETROLEUM%20FR%20FORE&country=AU&**accountType=transaction**&institution=AU04301**`

        Valid values:

        * transaction
        * credit-card
        * savings
        * mortgage
        * loan
        * foreign
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **amount**\
        *string, optional*
      </td>

      <td style={{ textAlign: "left" }}>
        The dollar/cent amount relevant to the transaction.

        `q=garfish%20MANLY%20NS&country=AU&institution=AU06703&**amount=-12.95**`
      </td>
    </tr>
  </tbody>
</Table>

```json Definition
GET /enrich
```

```json Example Request
GET enrich?q=METRO%20PETROLEUM%20FR%20FORE&country=AU&accountType=transaction&amount=-12.95&institution=AU04301
HTTP/1.1
Content-Type: application/json
Authorization: Bearer YOUR_ACCESS_TOKEN
```

**Response**

The `enrich` endpoint will always return a 200 response to the user, along with a set of results for each of the datasets subscribed to: category, entity and location. If no results are found for the search query then an empty result set is returned. If parameter inputs are invalid an error is returned.

You can subscribe one or all of the following three datasets depending on your use case.  The datasets are described below.

```json Example Response: result found
HTTP/1.1 200 OK
Content-Type: application/json

{
    "type": "enrich",
    "direction": "debit",
    "class": "payment",
    "data": {
        "merchant": {
            "id": "15e83d60-7332-4cec-96ab-06cfc4e3d710",
            "businessName": "Metro Petroleum",
            "website": "http://www.metropetroleum.com.au/",
            "phoneNumber": {
                "local": "(03) 9471 0283",
                "international": "+61 3 9471 0283"
            }
        },
        "location": {
            "routeNo": "145",
            "route": "Spring St",
            "postalCode": "3073",
            "suburb": "Reservoir",
            "state": "VIC",
            "country": "Australia",
            "formattedAddress": "139/145 Spring St, Reservoir VIC 3073",
            "geometry": {
                "lat": "-37.7263016",
                "lng": "145.0009305"
            }
        },
        "category": {
            "anzsic": {
                "division": {
                    "code": "G",
                    "title": "Retail Trade"
                },
                "subdivision": {
                    "code": "40",
                    "title": "Fuel Retailing"
                },
                "group": {
                    "code": "400",
                    "title": "Fuel Retailing"
                },
                "class": {
                    "code": "4000",
                    "title": "Fuel Retailing"
                }
            }
        }
    },
    "links": {
        "self": "https://au-api.basiq.io/enrich?country=AU&institution=AU04301&q=METRO+PETROLEUM+FR+FORE",
        "logo-master": "https://enrich-enrichmerchantslogobucket-6or17iuhdvs9.s3-ap-southeast-2.amazonaws.com/metro_petroleum-master.png",
        "logo-thumb": "https://enrich-enrichmerchantslogobucket-6or17iuhdvs9.s3-ap-southeast-2.amazonaws.com/metro_petroleum-thumb.png"
    }
}
```

```json Example Response: no result found
HTTP/1.1 200 OK
Content-Type: application/json

{
    "type": "enrich",
    "direction": "debit",
    "class": "payment",
    "data": {
        "merchant": null,
        "location": null,
        "category": null
    },
    "links": {
        "self": "https://au-api.basiq.io/enrich?accountType=transaction&amount=-12.95&country=AU&institution=AU06703&q=sfdsdfsd",
        "logo-master": null,
        "logo-thumb": null
    }
}
```

```json
HTTP/1.1 400 Bad Request
Content-Type: application/json
{
    "type": "list",
    "correlationId": "923788f1-72de-11e9-9a9f-a7c155f44712",
    "data": [
        {
            "type": "error",
            "code": "parameter-not-valid",
            "title": "Parameter value is not valid",
            "detail": "accountType is not valid Basiq account type value",
            "source": {
                "parameter": "accountType"
            }
        }
    ]
}
```

**Attributes**

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Enrich
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `type`
      </td>

      <td style={{ textAlign: "left" }}>
        Value is "enrich"
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `direction`
      </td>

      <td style={{ textAlign: "left" }}>
        Debit or Credit transaction
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `class`
      </td>

      <td style={{ textAlign: "left" }}>
        Describes the type of transaction: payment, transfer, cash-withdrawal, bank-fee, interest, refund etc.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Merchant
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `id`
      </td>

      <td style={{ textAlign: "left" }}>
        The merchant id.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `businessName`
      </td>

      <td style={{ textAlign: "left" }}>
        The merchant business name.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `ABN`
      </td>

      <td style={{ textAlign: "left" }}>
        The merchant business ABN.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `website`
      </td>

      <td style={{ textAlign: "left" }}>
        The merchant website.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `phoneNumber`
      </td>

      <td style={{ textAlign: "left" }}>
        Provides the `local` and `international` telephone numbers of the merchant.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Location
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `routeNo`
      </td>

      <td style={{ textAlign: "left" }}>
        The street number of the merchant location.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `route`
      </td>

      <td style={{ textAlign: "left" }}>
        The street name of the merchant location.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `postalCode`
      </td>

      <td style={{ textAlign: "left" }}>
        The post code of the merchant location.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `suburb`
      </td>

      <td style={{ textAlign: "left" }}>
        The suburb of the merchant location.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `state`
      </td>

      <td style={{ textAlign: "left" }}>
        The state of the merchant location.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `country`
      </td>

      <td style={{ textAlign: "left" }}>
        The country of the merchant location.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `formattedAddress`
      </td>

      <td style={{ textAlign: "left" }}>
        The full address for the merchant location
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `geometry`
      </td>

      <td style={{ textAlign: "left" }}>
        Contains the `lat` and `lng` coordinates of the merchant location.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Category
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `class`
      </td>

      <td style={{ textAlign: "left" }}>
        Details the `code` and `title` of the merchant ANZSIC class.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `group`
      </td>

      <td style={{ textAlign: "left" }}>
        Details the `code` and `title` of the merchant ANZSIC group.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `subdivision`
      </td>

      <td style={{ textAlign: "left" }}>
        Details the `code` and `title` of the merchant ANZSIC subdivision.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `division`
      </td>

      <td style={{ textAlign: "left" }}>
        Details the `code` and `title` of the merchant ANZSIC division.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Links
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `self`
      </td>

      <td style={{ textAlign: "left" }}>
        Provides a reference link to the original query.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `logo-master`
      </td>

      <td style={{ textAlign: "left" }}>
        Provides link to master logo. Logos are provided in a variety of formats: .svg, .png, .jpg, jpeg, gif. Where null no merchant logo is available.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `logo-thumb`
      </td>

      <td style={{ textAlign: "left" }}>
        Provides link to thumb logo (where no thumb available master logo is returned for both).  Logos are provided in a variety of formats: .svg, .png, .jpg, jpeg, gif. Where null no merchant logo is available.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>
