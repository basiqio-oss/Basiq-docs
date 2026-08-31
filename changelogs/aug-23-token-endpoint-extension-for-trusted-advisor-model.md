---
title: Aug '23 - Token Endpoint Extension for Trusted Advisor Model
author: Ashman Malik
hidden: false
published_at: '2023-08-01T05:26:00.768Z'
type: added
---
# Token Endpoint Extension :mega:

Basiq has extended the POST `/token` endpoint for requests with the scope `CLIENT_ACCESS`. The new organisation fields should be included in the request body as follows:

```json body
{
    "scope": "CLIENT_ACCESS", 
    "userId": "10be99c6-1944-4552-bd6f-08d893875179",
    "orgName": "Accountants XYZ Pty Ltd",
    "orgRefID": "0123456789",
    "orgRefType": "ABN",
    "orgType": "Financial Broker"
}
```

The supported values for the orgRefType field are `ABN`, `AFSL`, and `ACN`.

The supported values for the orgType field are `Accountant`, `Financial Broker`, `Financial Advisor`, `Legal Professional`, `Tax Agent`, and `Financial Counselling Agency`.

You can use the provided token to initiate the consent UI and continue connecting to your institution securely. The token includes the necessary information, such as the Trusted Advisor details and other relevant data, to ensure a smooth and compliant consent process.

By utilizing this token, you can seamlessly integrate the Trusted Advisor access model into your application, allowing qualified professionals to access consumer data for providing financial advice. You can read more about Trusted Advisor Model [here](https://api.basiq.io/docs/trusted-advisor). 

If you have any questions or need assistance during the onboarding process or while using the Trusted Advisor model, please feel free to reach out to our dedicated support team. We are here to help and ensure a successful experience for you and your users.