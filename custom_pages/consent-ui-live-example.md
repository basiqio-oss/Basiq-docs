---
title: Connectors FAQ down
fullscreen: false
hidden: true
---
import React, { useEffect, useState } from "react";

export const InstitutionList = () => {
  const [institutions, setInstitutions] = useState([]);
  const [searchQuery, setSearchQuery] = useState("");
  const [loading, setLoading] = useState(true);
  const [currentPage, setCurrentPage] = useState(1);
  const [isDarkTheme, setIsDarkTheme] = useState(
    document.documentElement.getAttribute("data-color-mode") === "dark"
  );
  const [notifications, setNotifications] = useState([]); // Stores error notifications
  const itemsPerPage = 10;

  useEffect(() => {
    // Fetch institutions
    fetch(
      `https://au-api.basiq.io/public/connectors?filter=connector.method.eq('open-banking'),connector.stage.ne(%27alpha%27),connector.authorization.type.in(%27other%27,%27user%27,%27user-mfa%27,%27user-mfa-intermittent%27,%27token%27)`
    )
      .then((response) => response.json())
      .then((data) => {
        const institutionData = data.data.map((connector) => connector.institution);
        setInstitutions(institutionData);

        // Check all links after data is loaded
        checkAllLinks(institutionData);
      })
      .catch((error) => console.error("Error fetching data:", error))
      .finally(() => setLoading(false));
  }, []);

  useEffect(() => {
    const observer = new MutationObserver(() => {
      const darkTheme = document.documentElement.getAttribute("data-color-mode") === "dark";
      setIsDarkTheme(darkTheme);
    });

    observer.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ["data-color-mode"],
    });

    return () => observer.disconnect();
  }, []);

  const checkAllLinks = (institutions) => {
    institutions.forEach((institution) => {
      if (institution.cdrFAQ) {
        checkLink(institution.cdrFAQ, "FAQ", institution.shortName);
      }
      if (institution.cdrPolicy) {
        checkLink(institution.cdrPolicy, "CDR Policy", institution.shortName);
      }
    });
  };

  const checkLink = (url, type, institutionName) => {
    // Log each link for debugging purposes
    console.log(`Checking link: ${url}`);

    fetch(url, { method: "HEAD" })
      .then((response) => {
        if (response.status === 404) {
          // If the status is 404, trigger a notification
          setNotifications((prevNotifications) => [
            ...prevNotifications,
            {
              institution: institutionName,
              type: type,
              link: url,
            },
          ]);
        }
      })
      .catch(() => {
        // In case of any error (e.g., network error), add a notification
        setNotifications((prevNotifications) => [
          ...prevNotifications,
          {
            institution: institutionName,
            type: type,
            link: url,
          },
        ]);
      });
  };

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
              setCurrentPage(1);
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
            &#x1F50D;
          </span>
        </div>
      </div>

      <table
        border="1"
        cellPadding="8"
        cellSpacing="0"
        style={{
          width: "100%",
          textAlign: "left",
          backgroundColor: isDarkTheme ? "#1e1e1e" : "#ffffff",
          color: isDarkTheme ? "#f5f5f5" : "#000000",
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
                backgroundColor: isDarkTheme && index % 2 === 0 ? "#2b2b2b" : isDarkTheme ? "#1e1e1e" : "#ffffff",
                color: isDarkTheme ? "#f5f5f5" : "#000000",
              }}
            >
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

      <div style={{ marginTop: "16px", display: "flex", justifyContent: "center", gap: "16px" }}>
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

      {/* Display individual toast notifications */}
      {notifications.map((notification, idx) => (
        <div
          key={idx}
          style={{
            position: "fixed",
            bottom: `${16 + idx * 60}px`,
            right: "16px",
            backgroundColor: "red",
            color: "white",
            padding: "12px 16px",
            borderRadius: "4px",
            zIndex: 1000,
            maxWidth: "300px",
          }}
        >
          <p>
            <strong>{notification.institution}</strong> - {notification.type}:{" "}
            <a
              href={notification.link}
              target="_blank"
              rel="noopener noreferrer"
              style={{ color: "white", textDecoration: "underline" }}
            >
              {notification.link}
            </a>
          </p>
        </div>
      ))}
    </div>
  );
};

//export default InstitutionList;

<br />

<InstitutionList />