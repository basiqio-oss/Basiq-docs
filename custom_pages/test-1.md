---
title: test
fullscreen: false
hidden: false
---
import React, { useEffect, useState } from "react";

export const InstitutionList = () => {
  const [institutions, setInstitutions] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("https://au-api.basiq.io/public/connectors?filter=connector.method.eq('open-banking')")
      .then((response) => response.json())
      .then((data) => {
        // Extract only the 'institution' object from the fetched data
        const institutionData = data.data.map((connector) => connector.institution);
        setInstitutions(institutionData);
      })
      .catch((error) => console.error("Error fetching data:", error))
      .finally(() => setLoading(false));
  }, []);

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
    </div>
  );
};

// If using this file directly in MDX, you can use the `InstitutionList` component as follows:

<InstitutionList />