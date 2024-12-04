---
title: Enrich API
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
The Enrich API returns merchant metadata regarding name, location and category.

This service can be tested using bank transaction data that you provide.  You can use real bank transaction data and the Enrich API will return enriched records for those transactions. Note that the same endpoint is utilised for both testing and production users, however a limit of 100 queries is set for testing users. 

> 🚧 Contact us (via the "help" icon at the bottom of the page) to have your Enrich access enabled.

> 📘 You will need to ensure that the search query is **url encoded** before calling the resource and must contain at least 3 characters.
>
> Example queries:\
> q=garfish%20MANLY%20NS\&country=AU\&institution=AU06703\&accountType=transaction\&amount=-12.95\
> q=garfish%20MANLY%20NS\&institution= AU13601

<Table align={["left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Example Queries
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        1. `GARFISH MANLY NS`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        2. `12 VOLT DIRECT PTY L LONSDALE AU`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        3. `HARVEY NORMAN AV/IT BALGOWLAH AU`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        4. `CALTEX ALDINGA BEACH ALDINGA BEACHAU`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        5. `KMART 1055 WARRIEWOOD AU`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        6. `KAKADU LODGE & CARAV JABIRU AU`
      </td>
    </tr>
  </tbody>
</Table>

```json
GET enrich?q=garfish%20MANLY%20NS&country=AU&institution=AU06703&accountType=transaction&amount=-12.95 HTTP/1.1
Content-Type: application/json
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Returns merchant, category, location
HTTP/1.1 200 OK
Content-Type: application/json

{
    "type": "enrich",
    "direction": "debit",
    "class": "payment",
    "data": {
        "merchant": {
            "businessName": "Garfish Manly",
            "website": "http://garfish.com.au/garfish-manly/",
            "phoneNumber": {
                "local": "(02) 9977 0707",
                "international": "+61 2 9977 0707"
            }
        },
        "location": {
            "routeNo": "39",
            "route": "E Esplanade",
            "postalCode": "2095",
            "suburb": "Manly",
            "state": "NSW",
            "country": "Australia",
            "formattedAddress": "1/39 E Esplanade, Manly NSW 2095",
            "geometry": {
                "lat": "-33.79988520000001",
                "lng": "151.2858021"
            }
        },
        "category": {
            "anzsic": {
                "division": {
                    "code": "H",
                    "title": "Accommodation and  Food Services"
                },
                "subdivision": {
                    "code": "45",
                    "title": "Food and Beverage Services"
                },
                "group": {
                    "code": "451",
                    "title": "Cafes, Restaurants and Takeaway Food Services"
                },
                "class": {
                    "code": "4511",
                    "title": "Cafes and Restaurants"
                }
            }
        }
    },
    "links": {
        "self": "https://au-api.basiq.io/enrich?country=AU&institution=AU06703&q=garfish+MANLY+NS"
    }
}
```
