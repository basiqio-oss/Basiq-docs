---
title: Pagination Data
fullscreen: false
hidden: true
---
import React, { useEffect, useState } from "react";

export const InstitutionList = () => {
  const [institutions, setInstitutions] = useState([]);
  const [searchQuery, setSearchQuery] = useState("");
  const [loading, setLoading] = useState(true);
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 10; // Number of items per page

  useEffect(() => {
    // Fetch all institutions
    fetch(
      `https://au-api.basiq.io/public/connectors?filter=connector.method.eq('open-banking')`
    )
      .then((response) => response.json())
      .then((data) => {
        const institutionData = data.data.map((connector) => connector.institution);
        setInstitutions(institutionData); // set all institutions
      })
      .catch((error) => console.error("Error fetching data:", error))
      .finally(() => setLoading(false));
  }, []); // only fetch once on component mount

  const filteredInstitutions = institutions.filter((institution) =>
    institution.shortName.toLowerCase().includes(searchQuery.toLowerCase())
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
    return <div>Loading institutions...</div>;
  }

  return (
    <div>
      <h1>Institutions</h1>
      <div style={{ marginBottom: "16px" }}>
        <input
          type="text"
          placeholder="Search by institution name"
          value={searchQuery}
          onChange={(e) => {
            setSearchQuery(e.target.value);
            setCurrentPage(1); // Reset to the first page on new search
          }}
          style={{
            padding: "8px",
            width: "100%",
            maxWidth: "400px",
            border: "1px solid #ccc",
            borderRadius: "4px",
          }}
        />
      </div>
      <table border="1" cellPadding="8" cellSpacing="0" style={{ width: "100%", textAlign: "left" }}>
        <thead>
          <tr>
            <th>Logo</th>
            <th>Short Name</th>
            <th>FAQ</th>
            <th>CDR Policy</th>
            <th>Email</th>
            <th>CDR Provider Number</th>
          </tr>
        </thead>
        <tbody>
          {paginatedInstitutions.map((institution, index) => (
            <tr key={index}>
              <td>
                {institution.logo && institution.logo.links ? (
                  <img
                    src={institution.logo.links.square}
                    alt={`${institution.shortName} Logo`}
                    style={{ width: "64px", height: "64px" }}
                  />
                ) : (
                  "N/A"
                )}
              </td>
              <td>{institution.shortName}</td>
              <td>
                <a href={institution.cdrFAQ} target="_blank" rel="noopener noreferrer">
                  FAQ
                </a>
              </td>
              <td>
                <a href={institution.cdrPolicy} target="_blank" rel="noopener noreferrer">
                  CDR Policy
                </a>
              </td>
              <td>
                {institution.shortName === "Bankwest Bank" ? (
                  <>
                    Call 13 2339<br />
                    Overseas? Call +61 2 9009 0593
                  </>
                ) : institution.shortName === "CBA - CommBiz" ? (
                  <>
                    Call 132 221<br />
                    Overseas? Call +61 2 9999 3283
                  </>
                ) : institution.shortName === "Unloan" ? (
                  <>
                    Visit Unloan Support<br />
                    Call 1800 865 262
                  </>
                ) : institution.shortName === "CBA" ? (
                  <>
                    Call 13 2221<br />
                    Overseas? Call +61 2 9999 3283
                  </>
                ) : institution.cdrEmail ? (
                  institution.cdrEmail
                ) : (
                  "N/A"
                )}
              </td>
              <td>{institution.cdrProviderNumber}</td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* Pagination Controls */}
      <div style={{ marginTop: "16px", display: "flex", justifyContent: "center", alignItems: "center", gap: "16px" }}>
        <button
          onClick={() => handlePageChange("prev")}
          disabled={currentPage === 1}
          style={{
            padding: "8px 16px",
            border: "none",
            borderRadius: "4px",
            backgroundColor: currentPage === 1 ? "#d3d3d3" : "#007bff",
            color: "white",
            cursor: currentPage === 1 ? "not-allowed" : "pointer",
            fontSize: "16px",
          }}
        >
          &laquo; Previous
        </button>
        <span style={{ fontSize: "16px", fontWeight: "bold" }}>
          Page {currentPage} of {totalPages}
        </span>
        <button
          onClick={() => handlePageChange("next")}
          disabled={currentPage === totalPages}
          style={{
            padding: "8px 16px",
            border: "none",
            borderRadius: "4px",
            backgroundColor: currentPage === totalPages ? "#d3d3d3" : "#007bff",
            color: "white",
            cursor: currentPage === totalPages ? "not-allowed" : "pointer",
            fontSize: "16px",
          }}
        >
          Next &raquo;
        </button>
      </div>
    </div>
  );
};

<InstitutionList />

<p> </p>