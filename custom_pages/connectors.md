---
title: Connectors
fullscreen: false
hidden: false
---
import React, { useEffect, useState } from "react";

export const InstitutionList = () => {
  const [institutions, setInstitutions] = useState([]);
  const [searchQuery, setSearchQuery] = useState("");
  const [loading, setLoading] = useState(true);
  const [currentPage, setCurrentPage] = useState(1);
  const [isDarkTheme, setIsDarkTheme] = useState(false);
  const itemsPerPage = 10;

  // Set theme only on client
  useEffect(() => {
    if (typeof document !== "undefined") {
      setIsDarkTheme(document.documentElement.getAttribute("data-color-mode") === "dark");
    }
  }, []);

  useEffect(() => {
    // Fetch data
    fetch(
      `https://au-api.basiq.io/public/connectors?filter=connector.method.eq('open-banking'),connector.stage.ne(%27alpha%27),connector.authorization.type.in(%27other%27,%27user%27,%27user-mfa%27,%27user-mfa-intermittent%27,%27token%27)`
    )
      .then((res) => res.json())
      .then((data) => {
        const institutionData = data.data.map(({ institution }) => institution);
        setInstitutions(institutionData);
      })
      .catch((err) => console.error("Error fetching data:", err))
      .finally(() => setLoading(false));
  }, []);

  useEffect(() => {
    if (typeof document === "undefined") return;

    const observer = new MutationObserver(() => {
      setIsDarkTheme(document.documentElement.getAttribute("data-color-mode") === "dark");
    });

    observer.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ["data-color-mode"],
    });

    return () => observer.disconnect();
  }, []);

  const filteredInstitutions = institutions.filter(({ shortName }) =>
    shortName.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const totalPages = Math.max(1, Math.ceil(filteredInstitutions.length / itemsPerPage));

  // Pagination fix: clamp currentPage within valid range on filteredInstitutions change
  useEffect(() => {
    if (currentPage > totalPages) {
      setCurrentPage(totalPages);
    }
  }, [currentPage, totalPages]);

  const paginatedInstitutions = filteredInstitutions.slice(
    (currentPage - 1) * itemsPerPage,
    currentPage * itemsPerPage
  );

  const handlePageChange = (direction) => {
    if (direction === "next" && currentPage < totalPages) {
      setCurrentPage((prev) => prev + 1);
    } else if (direction === "prev" && currentPage > 1) {
      setCurrentPage((prev) => prev - 1);
    }
  };

  if (loading) return <div>Loading institutions...</div>;

  return (
    <div style={{ maxWidth: 960, margin: "auto", padding: 20, fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif" }}>
      <h1>Institutions</h1>

      <div>
        <strong>Total Institutions: {institutions.length}</strong>
      </div>

      <div style={{ display: "flex", justifyContent: "flex-end", marginBottom: 16 }}>
        <div style={{ position: "relative" }}>
          <input
            type="text"
            placeholder="Search by institution name"
            value={searchQuery}
            onChange={(e) => {
              setSearchQuery(e.target.value);
              setCurrentPage(1);
            }}
            style={{
              padding: "8px 12px 8px 36px",
              width: 300,
              borderRadius: 6,
              border: "1px solid #ccc",
              fontSize: 16,
              position: "relative",
            }}
          />
          <span
            style={{
              position: "absolute",
              left: 12,
              top: "50%",
              transform: "translateY(-50%)",
              fontSize: 18,
              color: "#aaa",
              pointerEvents: "none",
            }}
          >
            &#x1F50D;
          </span>
        </div>
      </div>

      <table
        style={{
          width: "100%",
          borderCollapse: "collapse",
          boxShadow: "0 0 10px rgba(0,0,0,0.1)",
          backgroundColor: isDarkTheme ? "#2c2c2c" : "#fff",
          color: isDarkTheme ? "#eee" : "#000",
        }}
      >
        <thead>
          <tr>
            {["Logo", "Short Name", "FAQ", "CDR Policy", "Email", "CDR Provider Number"].map((header) => (
              <th
                key={header}
                style={{
                  backgroundColor: isDarkTheme ? "#0056b3" : "#007bff",
                  color: "white",
                  fontWeight: "600",
                  padding: "12px 15px",
                  textAlign: "left",
                }}
              >
                {header}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {paginatedInstitutions.map((inst, idx) => (
            <tr
              key={idx}
              style={{
                backgroundColor: idx % 2 === 0 ? (isDarkTheme ? "#383838" : "#f5f5f5") : "transparent",
              }}
            >
              <td style={{ padding: "12px 15px", borderBottom: "1px solid #ddd", verticalAlign: "middle" }}>
                {inst.logo?.links?.square ? (
                  <img src={inst.logo.links.square} alt={`${inst.shortName} Logo`} width={48} height={48} />
                ) : (
                  "N/A"
                )}
              </td>
              <td style={{ padding: "12px 15px", borderBottom: "1px solid #ddd", verticalAlign: "middle" }}>{inst.shortName}</td>
              <td style={{ padding: "12px 15px", borderBottom: "1px solid #ddd", verticalAlign: "middle" }}>
                {inst.cdrFAQ ? (
                  <a
                    href={inst.cdrFAQ}
                    target="_blank"
                    rel="noopener noreferrer"
                    style={{ color: isDarkTheme ? "#66aaff" : "#007bff", textDecoration: "none" }}
                  >
                    FAQ
                  </a>
                ) : (
                  "N/A"
                )}
              </td>
              <td style={{ padding: "12px 15px", borderBottom: "1px solid #ddd", verticalAlign: "middle" }}>
                {inst.cdrPolicy ? (
                  <a
                    href={inst.cdrPolicy}
                    target="_blank"
                    rel="noopener noreferrer"
                    style={{ color: isDarkTheme ? "#66aaff" : "#007bff", textDecoration: "none" }}
                  >
                    CDR Policy
                  </a>
                ) : (
                  "N/A"
                )}
              </td>
              <td style={{ padding: "12px 15px", borderBottom: "1px solid #ddd", verticalAlign: "middle" }}>{inst.cdrEmail || "N/A"}</td>
              <td style={{ padding: "12px 15px", borderBottom: "1px solid #ddd", verticalAlign: "middle" }}>{inst.cdrProviderNumber || "N/A"}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <div style={{ marginTop: 20, display: "flex", justifyContent: "center", alignItems: "center", gap: 12 }}>
        <button
          style={{
            padding: "8px 14px",
            border: "none",
            borderRadius: 5,
            backgroundColor: currentPage === 1 ? "#ccc" : "#007bff",
            color: "white",
            cursor: currentPage === 1 ? "not-allowed" : "pointer",
            fontSize: 16,
          }}
          onClick={() => handlePageChange("prev")}
          disabled={currentPage === 1}
        >
          &laquo; Previous
        </button>
        <span>
          Page {currentPage} of {totalPages}
        </span>
        <button
          style={{
            padding: "8px 14px",
            border: "none",
            borderRadius: 5,
            backgroundColor: currentPage === totalPages ? "#ccc" : "#007bff",
            color: "white",
            cursor: currentPage === totalPages ? "not-allowed" : "pointer",
            fontSize: 16,
          }}
          onClick={() => handlePageChange("next")}
          disabled={currentPage === totalPages}
        >
          Next &raquo;
        </button>
      </div>
    </div>
  );
};