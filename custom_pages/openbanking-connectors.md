---
title: OpenBanking Connectors
fullscreen: false
hidden: false
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
        setInstitutions(institutionData); // Set all institutions
      })
      .catch((error) => console.error("Error fetching data:", error))
      .finally(() => setLoading(false));
  }, []); // Only fetch once on component mount

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

  const isDarkTheme = document.documentElement.getAttribute("data-color-mode") === "dark";

  if (loading) {
    return <div>Loading institutions...</div>;
  }

  return (
    <div>
      <h1>Institutions</h1>

      {/* Display total institutions count */}
      <div style={{ marginBottom: "16px", fontSize: "16px" }}>
        <strong>Total Institutions: {institutions.length}</strong>
      </div>

      {/* Search Bar */}
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
            style={{
              padding: "8px 8px 8px 32px",
              width: "100%",
              border: "1px solid #ccc",
              borderRadius: "4px",
              fontSize: "16px",
            }}
          />
          <span
            style={{
              position: "absolute",
              left: "8px",
              top: "50%",
              transform: "translateY(-50%)",
              fontSize: "18px",
              color: "#ccc",
            }}
          >
            &#x1F50D; {/* Unicode character for search icon */}
          </span>
        </div>
      </div>

      {/* Institutions Table */}
      <table
        border="1"
        cellPadding="8"
        cellSpacing="0"
        style={{
          width: "100%",
          textAlign: "left",
          backgroundColor: "#ffffff", // Always white table background
          color: isDarkTheme ? "#f5f5f5" : "#000000", // Dynamic text color based on theme
          borderCollapse: "collapse",
        }}
      >
        <thead>
          <tr>
            {["Logo", "Short Name", "FAQ", "CDR Policy", "Email", "CDR Provider Number"].map((header) => (
              <th
                key={header}
                style={{
                  backgroundColor: isDarkTheme ? "#333333" : "#f2f2f2",
                  color: isDarkTheme ? "#ffffff" : "#000000",
                  fontWeight: "bold",
                  borderBottom: isDarkTheme ? "1px solid #555555" : "1px solid #cccccc",
                  padding: "8px",
                }}
              >
                {header}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {paginatedInstitutions.map((institution, index) => (
            <tr
              key={index}
              style={{
                backgroundColor: index % 2 === 0 ? "#f9f9f9" : "#ffffff", // Alternating row colors
                color: isDarkTheme ? "#f5f5f5" : "#000000", // Dynamic text color
              }}
            >
              <td
                style={{
                  backgroundColor: "#ffffff", // Always white background for the logo column
                }}
              >
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
                <a
                  href={institution.cdrFAQ}
                  target="_blank"
                  rel="noopener noreferrer"
                  style={{
                    color: isDarkTheme ? "#1e90ff" : "#007bff",
                    textDecoration: "none",
                  }}
                >
                  FAQ
                </a>
              </td>
              <td>
                <a
                  href={institution.cdrPolicy}
                  target="_blank"
                  rel="noopener noreferrer"
                  style={{
                    color: isDarkTheme ? "#1e90ff" : "#007bff",
                    textDecoration: "none",
                  }}
                >
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

<p />