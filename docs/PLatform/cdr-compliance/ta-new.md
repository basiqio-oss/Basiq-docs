---
title: TA NEW
deprecated: false
hidden: true
metadata:
  robots: index
---
import React from "react";

const TrustedAdvisorGuide = () => (
&#x20; \<div>
&#x20;   \<h1>Trusted Advisor Access Model\</h1>
&#x20;   \<p>
&#x20;     The Trusted Advisor access model allows qualified professionals to access consumer data for the purpose of providing financial advice. Please read this guide carefully to understand the requirements and steps for onboarding on the Trusted Advisor model.
&#x20;   \</p>

&#x20;   \<h2>Overview\</h2>
&#x20;   \<p>
&#x20;     The Trusted Advisor access model allows organisations or individuals to access consumer data for providing financial advice. Partners who qualify as Trusted Advisors can be granted access to the Consumer Data Right (CDR) platform under Basiq.
&#x20;   \</p>

&#x20;   \<Accordion title="Organisation TA Access">
&#x20;     \<p>
&#x20;       Organisations that clearly fit the definition of a Trusted Advisor (e.g., mortgage broker firms). The Trusted Advisor details will be visible on the Consent screen before consent is provided, as well as on the Consent Management and Consent Extension screens for users who previously provided consent with an Individual or Organisation TA.
&#x20;     \</p>
&#x20;     \<ul>
&#x20;       \<li>
&#x20;         \<strong>Integration:\</strong> Integration with the API for Organisation level TA access works similarly to a standard integration. The Consent UI will render the organisation being named as a Trusted Advisor, with information obtained from the provided token.
&#x20;       \</li>
&#x20;     \</ul>

&#x20;     \<h3>Token Specification for Organisation TA Access\</h3>
&#x20;     \<p>
&#x20;       The Trusted Advisor (TA) is passed to the consent UI on launch via the Client Token. The following claims should be added to the token based on the JWT Specs:
&#x20;     \</p>
&#x20;     \<table>
&#x20;       \<thead>
&#x20;         \<tr>
&#x20;           \<th>Field\</th>
&#x20;           \<th>Description\</th>
&#x20;         \</tr>
&#x20;       \</thead>
&#x20;       \<tbody>
&#x20;         \<tr>
&#x20;           \<td>\<code>orgName\</code>\</td>
&#x20;           \<td>The name of the Trusted Advisor organisation (e.g., Accountants XYZ Pty Ltd).\</td>
&#x20;         \</tr>
&#x20;         \<tr>
&#x20;           \<td>\<code>orgRefID\</code>\</td>
&#x20;           \<td>The reference ID of the organisation (e.g., 0123456789).\</td>
&#x20;         \</tr>
&#x20;         \<tr>
&#x20;           \<td>\<code>orgRefType\</code>\</td>
&#x20;           \<td>The type of reference ID (can be ABN, ACN, or any identifier).\</td>
&#x20;         \</tr>
&#x20;         \<tr>
&#x20;           \<td>\<code>orgType\</code>\</td>
&#x20;           \<td>The type of the Trusted Advisor organisation (e.g., Accountant, Financial Broker).\</td>
&#x20;         \</tr>
&#x20;         \<tr>
&#x20;           \<td>\<code>abnAcn\</code>\</td>
&#x20;           \<td>ABN or ACN number (optional, must follow ABN/ACN format if included).\</td>
&#x20;         \</tr>
&#x20;       \</tbody>
&#x20;     \</table>
&#x20;   \</Accordion>

&#x20;   \<Accordion title="Individual TA Access">
&#x20;     \<p>
&#x20;       Suited to organisations that fit the definition of a Trusted Advisor, but their business model does not allow organisation-level access (e.g., mortgage aggregator firms). The consent process is identical for both the individual Trusted Advisor access model and the Organization TA access model.
&#x20;     \</p>
&#x20;     \<table>
&#x20;       \<thead>
&#x20;         \<tr>
&#x20;           \<th>Field\</th>
&#x20;           \<th>Description\</th>
&#x20;         \</tr>
&#x20;       \</thead>
&#x20;       \<tbody>
&#x20;         \<tr>
&#x20;           \<td>\<code>orgName\</code>\</td>
&#x20;           \<td>The name of the Trusted Advisor (e.g., John Doe).\</td>
&#x20;         \</tr>
&#x20;         \<tr>
&#x20;           \<td>\<code>orgRefID\</code>\</td>
&#x20;           \<td>The reference ID of the Trusted Advisor (e.g., 0123456789).\</td>
&#x20;         \</tr>
&#x20;         \<tr>
&#x20;           \<td>\<code>orgRefType\</code>\</td>
&#x20;           \<td>The type of reference ID (can be ABN, ACN, or any identifier).\</td>
&#x20;         \</tr>
&#x20;         \<tr>
&#x20;           \<td>\<code>orgType\</code>\</td>
&#x20;           \<td>The type of the Trusted Advisor Individual (e.g., Accountant, Financial Broker).\</td>
&#x20;         \</tr>
&#x20;         \<tr>
&#x20;           \<td>\<code>abnAcn\</code>\</td>
&#x20;           \<td>ABN or ACN number (optional, must follow ABN/ACN format if included).\</td>
&#x20;         \</tr>
&#x20;       \</tbody>
&#x20;     \</table>
&#x20;   \</Accordion>

&#x20;   \<h2>Token Endpoint Extension\</h2>
&#x20;   \<p>
&#x20;     To support the Trusted Advisor model for partners, Basiq has extended the POST /token endpoint for requests with the scope \<code>CLIENT\_ACCESS\</code>. The new organisation fields should be included in the request body as shown below:
&#x20;   \</p>
&#x20;   \<pre>
&#x20;     \<code>
&#x20;       \{
&#x20;         "scope": "CLIENT\_ACCESS",
&#x20;         "userId": "10be99c6-1944-4552-bd6f-08d893875179",
&#x20;         "orgName": "Accountants XYZ Pty Ltd",
&#x20;         "orgRefID": "0123456789",
&#x20;         "orgRefType": "Mortgage Broker",
&#x20;         "orgType": "Financial Broker",
&#x20;         "abnAcn": "51824753556"
&#x20;       }
&#x20;     \</code>
&#x20;   \</pre>
&#x20;   \<p>
&#x20;     \<strong>Note:\</strong> \<code>orgRefType\</code> can accept any string without specific validation. \<code>abnAcn\</code> is optional but must be a valid ABN/ACN if included.
&#x20;   \</p>

&#x20;   \<h2>Consent UI - Trusted Advisor\</h2>
&#x20;   \<ul>
&#x20;     \<li>Updated the appearance of the TA banner and popup.\</li>
&#x20;     \<li>Added a TA disclaimer message above the consent confirmation button.\</li>
&#x20;   \</ul>

&#x20;   \<h3>Demo\</h3>
&#x20;   \<div style=\{\{ position: "relative", paddingBottom: "calc(50.161117078410314% + 41px)", height: 0, width: "100%" }}>
&#x20;     \<iframe
&#x20;       src="https\://demo.arcade.software/5FZJ6bqKc5r5aqotc60W?embed"
&#x20;       title="Trusted Advisor Model Demo"
&#x20;       frameBorder="0"
&#x20;       loading="lazy"
&#x20;       allow="clipboard-write"
&#x20;       style=\{\{ position: "absolute", top: 0, left: 0, width: "100%", height: "100%", colorScheme: "light" }}
&#x20;     \>\</iframe>
&#x20;   \</div>
&#x20; \</div>
);

const Accordion = (\{ title, children }) => \{
&#x20; const \[isOpen, setIsOpen] = React.useState(false);

&#x20; return (
&#x20;   \<div>
&#x20;     \<button onClick=\{() => setIsOpen(!isOpen)} style=\{\{ display: "block", width: "100%", textAlign: "left", margin: "1rem 0" }}>
&#x20;       \{title}
&#x20;     \</button>
&#x20;     \{isOpen && \<div>\{children}\</div>}
&#x20;   \</div>
&#x20; );
};

&#x20;\<TrustedAdvisorGuide />