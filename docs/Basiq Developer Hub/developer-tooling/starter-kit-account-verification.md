---
title: Starter Kits
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
<Image width="80%" src="https://files.readme.io/2ba685f-Untitled_design_9.gif" />

Basiq's starter kits were created to **accelerate time to production**. We’ve done the full API integration and user flow, closely following all our best practices, so partners can focus on their innovation. Focusing on both user- and developer- experience, the app is easily tailored to create a native user experience that aligns with any application's product and brand guidelines, and can be used standalone, incorporated into your own application, or simply as reference code for **what "great" looks like**. 

# Account Verification

Integrating with the Basiq API means account verification can become seamless, and more secure, as the data is coming direct from the bank. It also allows partners to: 

* Reduce application abandonment through streamlined customer onboarding and a faster, more effective account verification process.
* Instantly verify ID and accounts for deposits and withdrawals
* Create authentic eye catching user experiences by surfacing and displaying things like bank balances within your solution
* Cut out time-consuming, cumbersome merchant processes with real-time access to financial data. 

The **Account Verification** Starter Kit is a template project that partners can use to generate their own project  get to market - fast. **All you need is your API key to spin up a fully functional account verification app.** Check it out [here](https://github.com/basiqio/account-verification-API-v3.0). 

### Style and brand configuration

 

<Image width="smart" src="https://files.readme.io/f9a1157-Group_2682.png" />

 

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Config
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Brand colours and typeface
      </td>

      <td style={{ textAlign: "left" }}>
        Our starter kits are configurable to fit all brand guidelines, mainly by updating the `tailwind.config.js` with your brands colours and typeface. *Importing fonts can be done via`styles.css`*
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Logos
      </td>

      <td style={{ textAlign: "left" }}>
        You'll also want to replace the following logos with your own, maintaining the naming convention: 

        * `public/product-logo-full.svg`
        * `public/product-logo-square.svg`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Copy
      </td>

      <td style={{ textAlign: "left" }}>
        All product specific copy is noted as `PRODUCT_COPY` - in order to highlight exactly what should be updated based on your applications intentions and value proposition.
      </td>
    </tr>
  </tbody>
</Table>

### Gold standard

Our starter kits maintain all of the [Basiq best practices](https://api.basiq.io/docs/basiq-best-practices-1) around areas such as: 

* Token management
* Job handling - both happy and unhappy paths
* Strong pre consent flow - Clearly defined **value proposition** and a focus on **building trust**
* *& more..*

As well as being built on a **modern tech stack** using React, Next.js and Tailwind. 

### Check out our sample apps!

Real life examples of how the starter kits look *and* feel. Check them out [here](https://account-verification-git-v3-bridget-basiq.vercel.app/). 

> 📘 Sample apps will only work for test banks and sandbox accounts
>
> **We have disabled connecting to live banks for our sample apps.** You can login to our test banks using all of the sandbox credentials (for both happy and unhappy path scenarios) found [here](ref:connect). *We recommend using Hooli bank for testing*
