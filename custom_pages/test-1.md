---
title: test
fullscreen: false
hidden: false
---
import React, { useEffect, useState } from "react";

export const InstitutionList = () => {
  const [institutions, setInstitutions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [page, setPage] = useState(1); // current page
  const [totalPages, setTotalPages] = useState(1); // total pages
  const [perPage] = useState(10); // items per page

  useEffect(() => {
    // Fetch institutions with pagination
    fetch(`https://au-api.basiq.io/public/connectors?filter=connector.method.eq('open-banking')&page=${page}&limit=${perPage}`)
      .then((response) => response.json())
      .then((data) => {
        const institutionData = data.data.map((connector) => connector.institution);
        setInstitutions(institutionData);
        setTotalPages(Math.ceil(data.totalCount / perPage)); // calculate total pages
      })
      .catch((error) => console.error("Error fetching data:", error))
      .finally(() => setLoading(false));
  }, [page, perPage]); // re-fetch when the page changes

  if (loading) {
    return <div>Loading institutions...</div>;
  }

  return (
    <div>
      <h1>Institutions</h1>
      <ul>
        {institutions.map((institution, index) => (
          <li key={index}>
            <h2>{institution.name} ({institution.shortName})</h2>
            <p><strong>Type:</strong> {institution.type}</p>
            <p><strong>Country:</strong> {institution.country}</p>
            <p><strong>Tier:</strong> {institution.tier}</p>
            <p>
              <strong>FAQ:</strong>{" "}
              <a href={institution.cdrFAQ} target="_blank" rel="noopener noreferrer">
                {institution.cdrFAQ}
              </a>
            </p>
            <p>
              <strong>CDR Policy:</strong>{" "}
              <a href={institution.cdrPolicy} target="_blank" rel="noopener noreferrer">
                {institution.cdrPolicy}
              </a>
            </p>
            <p><strong>Email:</strong> {institution.cdrEmail}</p>
            <p><strong>ABN:</strong> {institution.abn}</p>
            <p><strong>ACN:</strong> {institution.acn}</p>
            {institution.logo && institution.logo.links && (
              <img
                src={institution.logo.links.square}
                alt={`${institution.shortName} Logo`}
                style={{ width: "64px", height: "64px" }}
              />
            )}
          </li>
        ))}
      </ul>

      {/* Pagination controls */}
      <div>
        <button
          onClick={() => setPage((prevPage) => Math.max(prevPage - 1, 1))}
          disabled={page === 1}
        >
          Previous
        </button>
        <span>
          Page {page} of {totalPages}
        </span>
        <button
          onClick={() => setPage((prevPage) => Math.min(prevPage + 1, totalPages))}
          disabled={page === totalPages}
        >
          Next
        </button>
      </div>
    </div>
  );
};

// If using this file directly in MDX, you can use the `InstitutionList` component as follows:

<br />

<InstitutionList />