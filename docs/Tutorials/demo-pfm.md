---
title: Personal Finance Management (PFM)
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
# BASIQ PFM Demo Application

Welcome to Basiq's Personal Finance Management (PFM) demo application! :rocket:

<Image align="center" alt={1080} border={false} caption="PFM demo application" title="8b7aa57-PFM_DevHubStarterKit_1080x800.png" src="https://files.readme.io/2d6c6616e5901cb14148b6e6f09f456b82d2eaaa7cbb121fcabeaaa9e11d94e7-Screenshot_2025-07-03_at_10.15.22_am.png" />

Our PFM demo application was designed to help accelerate your time to market by providing a personal finance management (PFM) application that incorporates best practices, follows our API integration, user flow guidelines, and can be easily tailored to align with your brand guidelines and product offerings.

# Starter Kits and Demo Apps that work together

Our PFM demo application is intended to work in conjunction with our [account verification starter kit](https://api.basiq.io/docs/starter-kit-account-verification), providing you with a fully CDR compliant, seamless and more secure integration to capture user consent.

Unlike our account verification starter kit which is a fully functioning application, our PFM demo application does have some static elements, which require further development in order for them to function how you would like them to.

# Features and Benefits of the PFM Demo Application

Integrating with the Basiq API means that account aggregation and analysis becomes a seamless process that provides more secure data from the bank. Additionally, our PFM Demo application offers the following benefits:

* Streamlined customer onboarding and a faster, more effective account aggregation process.
* Ability to instantly retrieve and analyse account information from multiple financial institutions, including bank balances, transaction histories, and spending patterns.
* Customisable dashboard that displays key financial metrics and allows users to track their spending and savings goals.
* Easily configurable to fit your brand guidelines by updating the tailwind.config.js file with your brand colors and typeface.
* Customisable logos and product-specific copy to align with your application's value proposition and messaging.

# Gold Standard

Our PFM Demo application is built on a modern tech stack using React, Next.js, and Tailwind, and adheres to Basiq's best practices around areas such as:

* Token management
* Job handling, including both happy and unhappy paths
* Strong pre-consent flow (when using our account verification starter kit) with a clearly defined value proposition to build trust with users
* And more...

Our PFM demo application is hosted on [pfm-demo.basiq.io](https://pfm-demo.basiq.io), and provides a real-life example of how the application looks and feels. Please note that this demo app is for testing purposes and connects to test bank and sandbox accounts.

You can use our sandbox credentials to login and test the app. We recommend using Hooli Bank for testing and the Wentworth Smith ID logins, as it provides the best dummy data to explore the application with.

You will need to follow the following steps to gain access and be able to click around:

* Click on the "Get Started" button and enter your email address, press "continue", to get started.
* Search for Hooli bank and use the Wentworth-Smith credentials found [here](https://api.basiq.io/reference/testing).
* Once your account is linked, you will be able to view your account balance, transaction history, and categorise your expenses. You can also view your income and savings to get a complete picture of your financial health.

**NOTE:** It is important to note that the demo application uses dummy data, so you can try out all of the features without actually linking your real bank account. However, if you want to use the app with your actual bank account, you will need to sign up for a Basiq account and go through a verification process.

# Get started today!

To get started with our PFM Demo Kit, all you need is an API key to spin up a PFM demo application. Check our guide [here](https://api.basiq.io/docs/getting-started) for details on how to get started. Also, accelerate your time to market through our blog post [here](https://www.basiq.io/blog/accelerate-your-time-to-market-with-basiqs-pfm-demo-app/).

# Source Code Access

The PFM demo application is available on [GitHub](https://github.com/flyingdonkey-it/PFM-starterkit). This repository contains all the necessary code and instructions for setting up and customising the PFM Starter Kit to fit your needs.

To get started, simply clone the repository and follow the instructions in the README file. The README file provides detailed instructions on how to customize the PFM demo application by updating the configuration files, branding, and logos.

Additionally, the GitHub repository provides access to the latest version of the PFM demo application, allowing you to stay up-to-date with the latest features and enhancements.

<br />

> 👍 Quick Links
>
> * [Live Application](https://pfm-demo.basiq.io/) to test out
> * [Public Git Repo](https://github.com/basiqio-oss/Basiq-pfm) for your use
> * [Test Credentials](https://api.basiq.io/reference/testing) for our Sandbox users

<div
  style={{
    marginTop: '2rem',
    marginBottom: '2rem',
    display: 'flex',
    flexWrap: 'wrap',
    alignItems: 'center',
    justifyContent: 'center',
    gap: '1.5rem',
    padding: '1.5rem',
    background: 'linear-gradient(to bottom right, #f9fafb, #f3f4f6)',
    border: '1px solid #e5e7eb',
    borderRadius: '0.75rem',
    boxShadow: '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
    textAlign: 'center',
    fontFamily: 'system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif',
  }}
>
  <div
    style={{
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
    }}
  >
    <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#4b5563" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ marginRight: '1rem', flexShrink: 0 }}>
      <path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z" />

      <path d="M8 12h.01" />

      <path d="M12 12h.01" />

      <path d="M16 12h.01" />
    </svg>

    <p
      style={{
        fontSize: '1.125rem',
        fontWeight: 600,
        color: '#1f2937',
        margin: 0,
      }}
    >
      Got a question or need assistance?
    </p>
  </div>

  <button onClick={() => Intercom('showNewMessage', 'issues on FAQs:')} style={{
                                                      padding: '0.75rem 2rem',
                                                      fontSize: '1rem',
                                                      fontWeight: 600,
                                                      borderRadius: '9999px',
                                                      boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
                                                      transition: 'all 0.3s ease-in-out',
                                                      backgroundColor: '#1f2937',
                                                      color: '#ffffff',
                                                      border: 'none',
                                                      cursor: 'pointer',
                                                      outline: 'none',
                                                      flexShrink: 0,
                                                    }} onMouseEnter={(e) => {
                                                      e.currentTarget.style.backgroundColor = '#374151';
                                                      e.currentTarget.style.transform = 'scale(1.05)';
                                                    }} onMouseLeave={(e) => {
                                                      e.currentTarget.style.backgroundColor = '#1f2937';
                                                      e.currentTarget.style.transform = 'scale(1)';
                                                    }} onFocus={(e) => {
                                                      e.currentTarget.style.outline = '2px solid #6b7280';
                                                      e.currentTarget.style.outlineOffset = '2px';
                                                      e.currentTarget.style.backgroundColor = '#374151';
                                                      e.currentTarget.style.transform = 'scale(1.05)';
                                                    }} onBlur={(e) => {
                                                      e.currentTarget.style.outline = 'none';
                                                      e.currentTarget.style.outlineOffset = '0px';
                                                      e.currentTarget.style.backgroundColor = '#1f2937';
                                                      e.currentTarget.style.transform = 'scale(1)';
                                                    }}>Chat with Support</button>
</div>