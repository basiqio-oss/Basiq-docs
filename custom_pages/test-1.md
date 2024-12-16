---
title: test
fullscreen: false
hidden: false
---
import React, { useEffect, useState } from "react";

const InstitutionList = () => {
  const [institutions, setInstitutions] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchInstitutions = async () => {
      try {
        const response = await fetch(
          "https://au-api.basiq.io/public/connectors?filter=connector.method.eq('open-banking')"
        );
        const data = await response.json();

        // Extract only the `institution` objects
        const institutionsData = data.data.map((connector) => connector.institution);
        setInstitutions(institutionsData);
      } catch (error) {
        console.error("Error fetching data:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchInstitutions();
  }, []);

  if (loading) {
    return <div>Loading institutions...</div>;
  }

  return (
    <div style={{ padding: "16px", fontFamily: "Arial, sans-serif" }}>
      <h1>Institutions</h1>
      {institutions.length === 0 ? (
        <p>No institutions found.</p>
      ) : (
        <div>
          {institutions.map((institution, index) => (
            <div
              key={index}
              style={{
                border: "1px solid #ddd",
                borderRadius: "8px",
                padding: "16px",
                marginBottom: "16px",
              }}
            >
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
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

// MDX Component Export
export default InstitutionList;
