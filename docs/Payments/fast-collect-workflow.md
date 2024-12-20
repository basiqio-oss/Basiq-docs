---
title: Fast Collect Payments
excerpt: '![Beta](https://img.shields.io/badge/Status-Beta-yellow)'
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
<Image align="center" width="20%" src="https://files.readme.io/a170a64-Group_4_2.png" />

   

> 🚧 Disclaimer
>
> Please be advised that the PayTo (Collect Fast) feature, as part of our ongoing efforts to enhance our service offerings, is not available yet. We are working diligently to ensure that this new feature meets our high standards for reliability and user experience.

 

#### To *Collect* is to pull funds from a user (also know as the payer).

**Example:** Piper Pay, a PFM app, charges a monthly $2.99 subscription fee for their customers to continue using their service. On the 1st of every month, they will collect this fee from their customers using the Basiq API. 

Fast Collect is done using NPP PayTo, which is a form of real time debits done by businesses to collect funds from their users. In order to use this service an agreement needs to be established and approved between the business and the payer user.

## Prerequisites for using Fast Collect

In order to start collecting funds from your users in real time you will need to perform the following steps:

* The application must be enabled for payments by Basiq, with the appropriate environment setup. You can enable the application for payments in Sandbox or request production access through the Basiq dashboard.
* The paying user must be set up as active in the partner application, and therefore have a `userId` to associate the payment with. Read more about creating a user [here](ref:createuser)
* The paying user must have a valid user name and email address. This includes having a first name with a minimum of 2 characters and a last name with a minimum of 2 characters and the email address exists and be a valid email address.
* In order to do a fast collect against a user an agreement needs to be accepted by the paying user. 

## Establishing an agreement

In order to perform a Fast Collect (PayTo) payrequest against a user you will need to have an agreement established with the user. There are a few things to keep in mind for this setting this up:

1. The paying user needs to be with a bank that accepts PayTo agreements and payments. For a list of these banks please refer to [Fast Collect (PayTo) Enabled Banks](doc:fast-collect-payto-enabled-banks)
2. The paying user needs to receive the PayTo agreement request and accept it. This is performed through the bank's applications and channels (App and/or web)

### Steps for establishing and agreement

1. Make sure the user is created in your application and ready to go as per the pre-requisites above.
2. Send an instruction to create an agreement by calling the [Create agreement](ref:createagreement). If the agreement instruction is successful, you will receive a job object with a `job Id`. This will also be the agreement instruction Id that you can query by calling [Get payment agreement instruction](ref:getpaymentagreementinstruction)\
   The agreement could be rejected by our payment processor and/or payer bank for a number of reasons.\
   A common failure of agreement instructions relates to reachability such as:
   1. The payer bank cannot process fast payments
   2. The payer account cannot process fast payments
   3. The payee bank cannot process fast payments (in case you specified a payee on the agreement)
   4. The payee account cannot process fast payments (in case you specified a payee on the agreement)
3. In case the agreement instruction does reach the payer user. Once they action it through their bank's channels, the response is sent to Basiq and forwarded to you via a webhook with the event `payment-agreement.active`. Additionally you can query the agreement instruction using the previously returned job id by passing that value to [Get payment agreement instruction](ref:getpaymentagreementinstruction)
4. If the agreement is accepted you can query the agreement itself by querying [Get payment agreement](ref:getpaymentagreement) and passing the same Id

## Performing a Fast Collect payrequest

1. You can start collecting payments from a user with an active agreement by [submiting payment requests](ref:submitpayrequests), including in the request:

* `requestId`: A unique ID generated by the partner application
* `method`: Specifying the value `fast` to indicate a Fast Collect (PayTo)
* `agreementId`: Indicating the agreement Id to be used and verified against
* `amount`: The amount of the payment you are collecting
* `description`: The description to be included on the payment
* `reference`: This is an optional field for Fast Collect payrequests to include a reference such as an invoice number that flows end to end to the payer user and the payee
* `payee`: This is an optional object to indicate where the funds should go to. This can only be specified if the `payee` object is not defined in the agreement. It includes the following fields:
  * `payeeType`: Indicating whether is a `person`or `organisation`
  * `payeePayId`: Indicating the PayID to pay to
  * `payeePayIdType`: Indicating the type of PayID to pay to (`email`, `phone-number`, `business-number`, `organisation-id`)
  * `bankBranchCode`: The 6 digit bank and branch code of the payee
  * `accountNumber`: The account number of the payee
  * `ultimatePayeeName`: The name of the ultimate recipient of the funds. In most cases this would be the same as the Payee name

Note: You can either specify PayID fields (`payeePayId` and `payeePayIdType`) or bank account number fields (`bankBranchCode` and `accountNumber`) but not both

```json Example request without payee
POST /payments/payrequests HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Basic $YOUR_ACCESS_TOKEN

{
    "payrequests": [
        {
            "requestId": "01824ad0-73f1-0138-3700-0a58a9feac09",
            "agreementId": "21824ad0-73f1-0138-3700-0a58a9feac09",
            "amount": 123.20,
						"refernce": "INV-123",
            "description": "Investment"
        }
    ]
}
```
```json Example request with payee (PayID)
POST /payments/payrequests HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Basic $YOUR_ACCESS_TOKEN

{
    "payrequests": [
        {
            "requestId": "01824ad0-73f1-0138-3700-0a58a9feac09",
            "agreementId": "21824ad0-73f1-0138-3700-0a58a9feac09",
            "amount": 123.20,
						"refernce": "INV-123",
            "description": "Investment",
          	"payee":
          		{
                "payeeType": "person",
                "payeePayID": "gavin@gmail.com",
                "payeePayIDType": "email",
                "ultimatePayeeName": "Gavin Belson"
              }
        }
    ]
}
```
```json Example request with payee (Account)
POST /payments/payrequests HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Basic $YOUR_ACCESS_TOKEN

{
    "payrequests": [
        {
            "requestId": "01824ad0-73f1-0138-3700-0a58a9feac09",
            "agreementId": "21824ad0-73f1-0138-3700-0a58a9feac09",
            "amount": 123.20,
						"refernce": "INV-123",
            "description": "Investment",
          	"payee":
          		{
                "payeeType": "person",
                "bankBranchCode": "072333",
                "accountNumber": "123456789",
                "ultimatePayeeName": "Gavin Belson"
              }
        }
    ]
}
```

2. The response will contain the **job resource** responsible for processing this payment request. **It will not return the payment itself**. You can use this job to track the progress of the payment request and know when it has successfully completed. 

```json Example response
HTTP/1.1 202 Accepted
Content-Type: application/json

{
  "type": "job",
  "id": "b1824ad0-73f1-0138-3700-0a58a9feac09",
  "requestId": "01824ad0-73f1-0138-3700-0a58a9feac09",
  "links": {
    "self": "https://au-api.basiq.io/jobs/b1824ad0-73f1-0138-3700-0a58a9feac09"
  }
}
```

5. Use the `job.Id` you receive to track the payment requests progress via the job endpoint [Jobs](ref:jobs) . You can continue to poll this endpoint regularly to stay updated of the success/failure of your request. 

```json Get job by Id example
{
  "type": "job",
  "id": "33454ad0-73f1-0138-3700-0a58a9feac09",
  "created": "2016-06-08T09:10:32.000Z",
  "updated": "2016-06-08T09:14:28.000Z",
  "steps": [
    {
      "title": "validate-payment",
      "status": "success",
      "result": {
        "type": "link",
        "url": "/payments/payrequests/33454ad0-73f1-0138-3700-0a58a9feac09"
      }
    },
    {
      "title": "external-processing",
      "status": "success",
      "result": {
        "type": "link",
        "url": "/payments/payrequests/33454ad0-73f1-0138-3700-0a58a9feac09"
      }
    },
    {
      "title": "payment-completed",
      "status": "success",
      "result": {
        "type": "link",
        "url": "/payments/payrequests/33454ad0-73f1-0138-3700-0a58a9feac09"
      }
    }
  ],
  "links": {
    "self": "/jobs/33454ad0-73f1-0138-3700-0a58a9feac09",
    "source": "/payments/payrequests/33454ad0-73f1-0138-3700-0a58a9feac09"
  }
}
```

Note: The `jobId` returned can also be used to retrieve the `payrequest` directly via the API

5. You can use Use the returned `job.Id` you receive to enquire about the payment requests progress by calling [Retrieve a payment request](ref:getpayrequest)

```json Get payrequest by Id example
{
  "type": "payrequest",
  "id": "d3334ad0-73f1-0138-3700-0a58a9feac33",
  "requestId": "b1824ad0-73f1-0138-3700-0a58a9feac0b",
  "created": "2022-03-21T20:28:22.378Z",
  "updated": "2022-03-21T20:28:22.378Z",
  "method": "fast",
  "status": "successful",
  "agreementId": "f2024ad0-73f1-0138-3700-0a58a9feac0f",
  "payer": {
    "payerUserId": "21824ad0-73f1-0138-3700-0a58a9feac09",
    "payerBankBranchCode": "730002",
    "payerAccountNumber": "123456789",
    "payerAccountId": "31824ad0-73f1-0138-3700-0a58a9feac09"
  },
  "payee": {
    "payeeBankBranchCode": "012345",
    "payeeAccountNumber": "321456987",
    "ultimatePayeeName": "Gavin"
  },
  "reference": "INV-011",
  "description": "Investment",
  "amount": 173.45,
  "currency": "AUD",
  "links": {
    "self": "/payments/payrequests/d3334ad0-73f1-0138-3700-0a58a9feac33",
    "job": "/jobs/d3334ad0-73f1-0138-3700-0a58a9feac33"
  }
```
