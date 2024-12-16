---
title: test
fullscreen: false
hidden: false
---
import React, \{ useEffect, useState } from "react";

const InstitutionList = () => \{
&#x20; const \[institutions, setInstitutions] = useState(\[]);
&#x20; const \[loading, setLoading] = useState(true);

&#x20; useEffect(() => \{
&#x20;   const fetchInstitutions = async () => \{
&#x20;     try \{
&#x20;       const response = await fetch(
&#x20;         "https\://au-api.basiq.io/public/connectors?filter=connector.method.eq('open-banking')"
&#x20;       );
&#x20;       const data = await response.json();

&#x20;       // Extract only the \`institution\` objects
&#x20;       const institutionsData = data.data.map((connector) => connector.institution);
&#x20;       setInstitutions(institutionsData);
&#x20;     } catch (error) \{
&#x20;       console.error("Error fetching data:", error);
&#x20;     } finally \{
&#x20;       setLoading(false);
&#x20;     }
&#x20;   };

&#x20;   fetchInstitutions();
&#x20; }, \[]);

&#x20; if (loading) \{
&#x20;   return \<div>Loading institutions...\</div>;
&#x20; }

&#x20; return (
&#x20;   \<div style=\{\{ padding: "16px", fontFamily: "Arial, sans-serif" }}>
&#x20;     \<h1>Institutions\</h1>
&#x20;     \{institutions.length === 0 ? (
&#x20;       \<p>No institutions found.\</p>
&#x20;     ) : (
&#x20;       \<div>
&#x20;         \{institutions.map((institution, index) => (
&#x20;           \<div
&#x20;             key=\{index}
&#x20;             style=\{\{
&#x20;               border: "1px solid #ddd",
&#x20;               borderRadius: "8px",
&#x20;               padding: "16px",
&#x20;               marginBottom: "16px",
&#x20;             }}
&#x20;           \>
&#x20;             \<h2>\{institution.name} (\{institution.shortName})\</h2>
&#x20;             \<p>\<strong>Type:\</strong> \{institution.type}\</p>
&#x20;             \<p>\<strong>Country:\</strong> \{institution.country}\</p>
&#x20;             \<p>\<strong>Tier:\</strong> \{institution.tier}\</p>
&#x20;             \<p>
&#x20;               \<strong>FAQ:\</strong>\{" "}
&#x20;               \<a href=\{institution.cdrFAQ} target="\_blank" rel="noopener noreferrer">
&#x20;                 \{institution.cdrFAQ}
&#x20;               \</a>
&#x20;             \</p>
&#x20;             \<p>
&#x20;               \<strong>CDR Policy:\</strong>\{" "}
&#x20;               \<a href=\{institution.cdrPolicy} target="\_blank" rel="noopener noreferrer">
&#x20;                 \{institution.cdrPolicy}
&#x20;               \</a>
&#x20;             \</p>
&#x20;             \<p>\<strong>Email:\</strong> \{institution.cdrEmail}\</p>
&#x20;             \<p>\<strong>ABN:\</strong> \{institution.abn}\</p>
&#x20;             \<p>\<strong>ACN:\</strong> \{institution.acn}\</p>
&#x20;             \{institution.logo && institution.logo.links && (
&#x20;               \<img
&#x20;                 src=\{institution.logo.links.square}
&#x20;                 alt=\{\`$\{institution.shortName} Logo\`}
&#x20;                 style=\{\{ width: "64px", height: "64px" }}
&#x20;               />
&#x20;             )}
&#x20;           \</div>
&#x20;         ))}
&#x20;       \</div>
&#x20;     )}
&#x20;   \</div>
&#x20; );
};

export default InstitutionList;