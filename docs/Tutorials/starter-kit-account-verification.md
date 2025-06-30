---
title: Account Verification (IAV)
excerpt: Instant Account Verification Starter Kit
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
<Image align="center" width="auto" src="https://files.readme.io/2dcf482-DevHub_StarterKit_1080x800.png" />

Basiq's starter kits were created to **accelerate time to production**. We’ve done the full API integration and user flow, closely following all our best practices, so partners can focus on their innovation. Focusing on both user- and developer- experience, the app is easily tailored to create a native user experience that aligns with any application's product and brand guidelines, and can be used standalone, incorporated into your own application, or simply as reference code for **what "great" looks like**.

## Account Verification

<Embed url="https://www.google.com/sorry/index?continue=https://www.youtube.com/watch%3Fv%3DAsQl_IlcWRM&q=EhAmAB8YEA2fEflVPTOI6fAvGMaC-bYGIjDM7LW9R21AKP2Zl8ylaNLjACDxDuUdqKqGUnytEUZUcun24KBp8vE1LSs3rYXmWJcyAXJaAUM" href="https://www.google.com/sorry/index?continue=https://www.youtube.com/watch%3Fv%3DAsQl_IlcWRM&q=EhAmAB8YEA2fEflVPTOI6fAvGMaC-bYGIjDM7LW9R21AKP2Zl8ylaNLjACDxDuUdqKqGUnytEUZUcun24KBp8vE1LSs3rYXmWJcyAXJaAUM" typeOfEmbed="default" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252FAsQl_IlcWRM%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DAsQl_IlcWRM%26key%3D02466f963b9b4bb8845a05b53d3235d7%26type%3Dtext%252Fhtml%26schema%3Dgoogle%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />

Integrating with the Basiq API means account verification can become seamless, and more secure, as the data is coming direct from the bank. It also allows partners to:

* Reduce application abandonment through streamlined customer onboarding and a faster, more effective account verification process.
* Instantly verify ID and accounts for deposits and withdrawals
* Create authentic eye catching user experiences by surfacing and displaying things like bank balances within your solution
* Cut out time-consuming, cumbersome merchant processes with real-time access to financial data.

The **Account Verification** Starter Kit is a template project that partners can use to generate their own project  get to market - fast. **All you need is your API key to spin up a fully functional account verification app.** Check it out [here](https://github.com/basiqio/account-verification-API-v3.0).

# Style and brand configuration

<Image align="center" width="smart" src="https://files.readme.io/f9a1157-Group_2682.png" />

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Config
      </th>

      <th>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Brand colours and typeface
      </td>

      <td>
        Our starter kits are configurable to fit all brand guidelines, mainly by updating the `tailwind.config.js` with your brands colours and typeface. *Importing fonts can be done via`styles.css`*
      </td>
    </tr>

    <tr>
      <td>
        Logos
      </td>

      <td>
        You'll also want to replace the following logos with your own, maintaining the naming convention:

        * `public/product-logo-full.svg`
        * `public/product-logo-square.svg`
      </td>
    </tr>

    <tr>
      <td>
        Copy
      </td>

      <td>
        All product specific copy is noted as `PRODUCT_COPY` - in order to highlight exactly what should be updated based on your applications intentions and value proposition.
      </td>
    </tr>
  </tbody>
</Table>

# Gold standard

Our starter kits maintain all of the [Basiq best practices](https://api.basiq.io/docs/best-practices) around areas such as:

* Token management
* Job handling - both happy and unhappy paths
* Strong pre consent flow - Clearly defined **value proposition** and a focus on **building trust**
* *& more..*

As well as being built on a **modern tech stack** using React, Next.js and Tailwind.

### Check out our sample apps!

Real life examples of how the starter kits look *and* feel. Check them out [here](https://av-demo.basiq.io/).

> 📘 Sample apps will only work for test banks and sandbox accounts
>
> **We have disabled connecting to live banks for our sample apps.** You can login to our test banks using all of the sandbox credentials (for both happy and unhappy path scenarios) found [here](https://api.basiq.io/reference/testing#unhappy-path-test-users). *We recommend using Hooli bank for testing*

# Spinning up the starterKit **under 5 mins**

When developers start a new project, they often begin by using a starter kit or demo app as a foundation for their work. This starting point provides a pre-existing code base, which can be tailored to fit their specific needs. To use this code base, the developer needs to make a copy of it, either by downloading it from a repository or cloning it from a version control system.

Here's a demo of how to spin up the starterKit in under 5 mins.

<Embed url="https://www.google.com/sorry/index?continue=https://www.youtube.com/watch%3Fv%3DBljMvHvYckM&q=EhAmAB8YEA2fIdxl3yyUagcGGMaC-bYGIjCEd0hhz-T6WLYWyXaQYuxUO7CHVdZIdO5BYNJXvg-whKdr9t-TUBkIMwpgWJj-MdEyAXJaAUM" href="https://www.google.com/sorry/index?continue=https://www.youtube.com/watch%3Fv%3DBljMvHvYckM&q=EhAmAB8YEA2fIdxl3yyUagcGGMaC-bYGIjCEd0hhz-T6WLYWyXaQYuxUO7CHVdZIdO5BYNJXvg-whKdr9t-TUBkIMwpgWJj-MdEyAXJaAUM" typeOfEmbed="default" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252FBljMvHvYckM%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DBljMvHvYckM%26key%3D02466f963b9b4bb8845a05b53d3235d7%26type%3Dtext%252Fhtml%26schema%3Dgoogle%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />

> 👍 Quick Links
>
> * [Live Application](https://av-demo.basiq.io/) to test out
> * [Public Git Repo](https://github.com/basiqio/account-verification-API-v3.0) for your use
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