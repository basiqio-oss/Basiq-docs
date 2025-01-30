---
title: Connecting Business accounts via CDR
deprecated: false
hidden: true
metadata:
  robots: index
---
Presently with the CDR program, the sharing of business bank accounts established under a business entity (not an individual) requires additional steps to be taken. These business entities include structures such as Sole traders, Partnerships, Companies and Trusts.

These additional steps are required as data sharing for businesses is ‘opt-in’ under the CDR regime. For sole traders and single directors it is usually a straightforward process because only one consent is required, but for businesses with multiple directors, the consent process can be a little more complicated.

Businesses wanting to to share their banking data via CDR require the following to take place:

* The business entity that owns the business bank account must be enabled for online banking.
* The controlling party of that business entity (e.g. director(s)) must give authority to other individuals to be able to share accounts owned by the business entity via their online banking access (if this is done correctly they will see an additional page in the CDR data sharing flow implemented by banks that asks them to pick the profile for data sharing and they can either select their personal profile or the business profiles they have authority for).

Each bank manages these additional steps in a different way. In some cases, it’s a simple case of providing authority via the bank’s app, while for others, it requires the business owner submitting a form to their bank. This is an industry issue which we’re working to resolve in collaboration with the relevant Government departments.

In the event that frontline bank staff do not know about CDR, apart from escalating the issue with the bank, you can also find the bank under the [Data Holders list](https://www.cdr.gov.au/find-a-provider?providerType=Data%2520Holder) and reach out via a specific email address for the respective CDR support team.

## Testing CDR Data Sharing

Businesses can now test their accounts via [myCDR](https://mycdrdata.cds.cuscal.com.au/) to explore their CDR data in the Business Connecting Consumer (BCC) flow. [myCDR](https://mycdrdata.cds.cuscal.com.au/) is a testing tool that allows you to review your data. Once you’ve gone through this process, connect with our sales team to start sharing your data. Visit [myCDR](https://mycdrdata.cds.cuscal.com.au/) Data to begin.

> 📘 Note:
>
> Be aware that some brands, account types, or specific data fields may be exempt from the CDR requirements. For detailed information on these exemptions, refer to the [ACCC Consumer Data Right Exemptions Register.](https://www.accc.gov.au/public-registers/consumer-data-right-exemptions-register)

Below is a list of resources for each bank to help when attempting to connect to Business accounts via the CDR.

import React, { useEffect, useState } from "react";

export const InstitutionList = () => {
  const [institutions, setInstitutions] = useState([]);
  const [searchQuery, setSearchQuery] = useState("");
  const [loading, setLoading] = useState(true);
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 10;
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(
      `https://au-api.basiq.io/public/connectors?filter=connector.method.eq('open-banking'),connector.stage.ne(%27alpha%27),connector.authorization.type.in(%27other%27,%27user%27,%27user-mfa%27,%27user-mfa-intermittent%27,%27token%27)`
    )
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        const institutionData = data.data.map((connector) => connector.institution);
        setInstitutions(institutionData);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
        setError("Failed to load institutions. Please try again later.");
      })
      .finally(() => setLoading(false));
  }, []);

  const filteredInstitutions = institutions.filter((institution) =>
    institution.shortName?.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const totalPages = Math.ceil(filteredInstitutions.length / itemsPerPage);

  const handlePageChange = (direction) => {
    if (direction === "next" && currentPage < totalPages) {
      setCurrentPage((prevPage) => prevPage + 1);
    } else if (direction === "prev" && currentPage > 1) {
      setCurrentPage((prevPage) => prevPage - 1);
    }
  };

  const paginatedInstitutions = filteredInstitutions.slice(
    (currentPage - 1) * itemsPerPage,
    currentPage * itemsPerPage
  );

  if (loading) {
    return <div className="dark-mode">Loading institutions...</div>;
  }

  if (error) {
    return <div className="dark-mode">{error}</div>;
  }

  return (
    <div className="dark-mode">
      <style>
        {`
          .dark-mode {
            background-color: #121212;
            color: white;
            padding: 16px;
            min-height: 100vh;
          }

          .dark-table {
            width: 100%;
            text-align: left;
            border-collapse: collapse;
            background-color: transparent;
          }

          .dark-table th {
            background-color: #333;
            font-weight: bold;
            border-bottom: 1px solid #444;
            padding: 8px;
            color: white;
          }

          .dark-table td {
            padding: 8px;
          }

          .dark-row-even {
            background-color: #1e1e1e;
          }

          .dark-row-odd {
            background-color: #2c2c2c;
          }

          .dark-search-container {
            margin-bottom: 16px;
            display: flex;
            justify-content: flex-end;
          }

          .dark-search-input {
            padding: 8px 8px 8px 32px;
            width: 100%;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
            background-color: #1e1e1e;
            color: white;
          }

          .dark-pagination {
            margin-top: 16px;
            display: flex;
            justify-content: center;
            gap: 16px;
          }

          .dark-button {
            padding: 8px 16px;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
            color: white;
          }

          .dark-button-enabled {
            background-color: #4db8ff;
          }

          .dark-button-disabled {
            background-color: #444;
            cursor: not-allowed;
          }
        `}
      </style>

      <h1>Institutions</h1>

      <div style={{ marginBottom: "16px", fontSize: "16px" }}>
        <strong>Total Institutions: {institutions.length}</strong>
      </div>

      <div className="dark-search-container">
        <input
          type="text"
          placeholder="Search by institution name"
          value={searchQuery}
          onChange={(e) => {
            setSearchQuery(e.target.value);
            setCurrentPage(1);
          }}
          className="dark-search-input"
        />
      </div>

      <table className="dark-table">
        <thead>
          <tr>
            {["Logo", "Short Name", "FAQ", "CDR Policy", "Email", "CDR Provider Number"].map((header) => (
              <th key={header}>{header}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {paginatedInstitutions.map((institution, index) => (
            <tr key={index} className={index % 2 === 0 ? "dark-row-even" : "dark-row-odd"}>
              <td>
                {institution.logo?.links?.square ? (
                  <img
                    src={institution.logo.links.square}
                    alt={`${institution.shortName} Logo`}
                    style={{ width: "64px", height: "64px" }}
                  />
                ) : (
                  "N/A"
                )}
              </td>
              <td>{institution.shortName || "N/A"}</td>
              <td>
                <a href={institution.cdrFAQ} target="_blank" rel="noopener noreferrer" style={{ color: "#4db8ff" }}>
                  FAQ
                </a>
              </td>
              <td>
                <a href={institution.cdrPolicy} target="_blank" rel="noopener noreferrer" style={{ color: "#4db8ff" }}>
                  CDR Policy
                </a>
              </td>
              <td>{institution.cdrEmail || "N/A"}</td>
              <td>{institution.cdrProviderNumber || "N/A"}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <div className="dark-pagination">
        <button
          onClick={() => handlePageChange("prev")}
          disabled={currentPage === 1}
          className={`dark-button ${currentPage === 1 ? "dark-button-disabled" : "dark-button-enabled"}`}
        >
          &laquo; Previous
        </button>
        <span style={{ fontSize: "16px", fontWeight: "bold" }}>
          Page {currentPage} of {totalPages}
        </span>
        <button
          onClick={() => handlePageChange("next")}
          disabled={currentPage === totalPages}
          className={`dark-button ${currentPage === totalPages ? "dark-button-disabled" : "dark-button-enabled"}`}
        >
          Next &raquo;
        </button>
      </div>
    </div>
  );
};

<InstitutionList />;