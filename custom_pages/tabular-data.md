---
title: Tabular Data
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

  const darkModeStyles = {
    backgroundColor: "var(--background-color)",
    color: "var(--text-color)",
  };

  const inputStyles = {
    ...darkModeStyles,
    padding: "8px 8px 8px 32px",
    width: "100%",
    border: "1px solid var(--border-color)",
    borderRadius: "4px",
    fontSize: "16px",
  };

  const tableStyles = {
    width: "100%",
    textAlign: "left",
    border: "1px solid var(--border-color)",
  };

  const buttonStyles = (disabled) => ({
    padding: "8px 16px",
    border: "none",
    borderRadius: "4px",
    backgroundColor: disabled ? "var(--disabled-bg)" : "var(--button-bg)",
    color: "var(--button-text)",
    cursor: disabled ? "not-allowed" : "pointer",
    fontSize: "16px",
  });

  return (
    <div style={darkModeStyles}>
      <h1>Institutions</h1>
      
      {/* Display total institutions count */}
      <div style={{ marginBottom: "16px", fontSize: "16px" }}>
        <strong>Total Institutions: {institutions.length}</strong>
      </div>

      <div style={{ marginBottom: "16px", display: "flex", justifyContent: "flex-end" }}>
        <div style={{ position: "relative", maxWidth: "400px", width: "100%" }}>
          <input
            type="text"
            placeholder="Search by institution name"
            value={searchQuery}
            onChange={(e) => {
              setSearchQuery(e.target.value);
              setCurrentPage(1); // Reset to the first page on new search
            }}
            style={inputStyles}
          />
          <span
            style={{
              position: "absolute",
              left: "8px",
              top: "50%",
              transform: "translateY(-50%)",
              fontSize: "18px",
              color: "var(--icon-color)",
            }}
          >
            &#x1F50D; {/* Unicode character for search icon */}
          </span>
        </div>
      </div>

      <table border="1" cellPadding="8" cellSpacing="0" style={tableStyles}>
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
              <td>{institution.cdrEmail || "N/A"}</td>
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
          style={buttonStyles(currentPage === 1)}
        >
          &laquo; Previous
        </button>
        <span style={{ fontSize: "16px", fontWeight: "bold" }}>
          Page {currentPage} of {totalPages}
        </span>
        <button
          onClick={() => handlePageChange("next")}
          disabled={currentPage === totalPages}
          style={buttonStyles(currentPage === totalPages)}
        >
          Next &raquo;
        </button>
      </div>
    </div>
  );
};

<br />

<InstitutionList />