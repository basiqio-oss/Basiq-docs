---
title: Tabular Data
fullscreen: false
hidden: true
---
import React, { useEffect, useState } from "react";

export const InstitutionList = () => {
  const [institutions, setInstitutions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [page, setPage] = useState(1); // current page
  const [totalCount, setTotalCount] = useState(0); // total count of institutions
  const [perPage] = useState(10); // items per page

  useEffect(() => {
    // Fetch institutions with pagination
    fetch(
      `https://au-api.basiq.io/public/connectors?filter=connector.method.eq('open-banking')&page=${page}&limit=${perPage}`
    )
      .then((response) => response.json())
      .then((data) => {
        const institutionData = data.data.map((connector) => connector.institution);
        setInstitutions((prevInstitutions) => [...prevInstitutions, ...institutionData]); // append new data to the list
        setTotalCount(data.totalCount); // set total count of institutions
      })
      .catch((error) => console.error("Error fetching data:", error))
      .finally(() => setLoading(false));
  }, [page, perPage]); // re-fetch when the page changes

  const handleLoadMore = () => {
    setPage((prevPage) => prevPage + 1); // increment the page to load more data
  };

  if (loading && institutions.length === 0) {
    return <div>Loading institutions...</div>;
  }

  return (
    <div>
      <h1>Institutions</h1>
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
          {institutions.map((institution, index) => (
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

      {/* Load More button */}
      {institutions.length < totalCount && !loading && (
        <div style={{ marginTop: "16px" }}>
          <button onClick={handleLoadMore}>Load More</button>
        </div>
      )}

      {/* Loading state */}
      {loading && institutions.length > 0 && <div>Loading more institutions...</div>}
    </div>
  );
};

<br />

<InstitutionList />