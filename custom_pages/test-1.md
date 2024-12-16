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
            {institution.name} ({institution.shortName}) - {institution.country}
          </li>
        ))}
      </ul>
    </div>
  );
};

// If using this file directly in MDX, you can use the `InstitutionList` component as follows:


<InstitutionList />
