---
title: OpenBanking Connectors
fullscreen: false
hidden: false
---
import React, \{ useEffect, useState } from "react";

const InstitutionList = () => \{
&#x20; const \[institutions, setInstitutions] = useState(\[]);
&#x20; const \[searchQuery, setSearchQuery] = useState("");
&#x20; const \[loading, setLoading] = useState(true);
&#x20; const \[currentPage, setCurrentPage] = useState(1);
&#x20; const itemsPerPage = 10; // Number of items per page

&#x20; useEffect(() => \{
&#x20;   // Fetch all institutions
&#x20;   fetch(
&#x20;     \`https\://au-api.basiq.io/public/connectors?filter=connector.method.eq('open-banking')\`
&#x20;   )
&#x20;     .then((response) => response.json())
&#x20;     .then((data) => \{
&#x20;       const institutionData = data.data.map((connector) => connector.institution);
&#x20;       setInstitutions(institutionData); // set all institutions
&#x20;     })
&#x20;     .catch((error) => console.error("Error fetching data:", error))
&#x20;     .finally(() => setLoading(false));
&#x20; }, \[]); // only fetch once on component mount

&#x20; const filteredInstitutions = institutions.filter((institution) =>
&#x20;   institution.shortName.toLowerCase().includes(searchQuery.toLowerCase())
&#x20; );

&#x20; const totalPages = Math.ceil(filteredInstitutions.length / itemsPerPage);

&#x20; const handlePageChange = (direction) => \{
&#x20;   if (direction === "next" && currentPage \< totalPages) \{
&#x20;     setCurrentPage((prevPage) => prevPage + 1);
&#x20;   } else if (direction === "prev" && currentPage > 1) \{
&#x20;     setCurrentPage((prevPage) => prevPage - 1);
&#x20;   }
&#x20; };

&#x20; const paginatedInstitutions = filteredInstitutions.slice(
&#x20;   (currentPage - 1) \* itemsPerPage,
&#x20;   currentPage \* itemsPerPage
&#x20; );

&#x20; if (loading) \{
&#x20;   return \<div>Loading institutions...\</div>;
&#x20; }

&#x20; return (
&#x20;   \<div>
&#x20;     \<style>\{\`
&#x20;       html\[data-color-mode="dark"] \{
&#x20;         \--table-bg: #1e1e1e;
&#x20;         \--table-text: #f5f5f5;
&#x20;         \--table-header-bg: #333333;
&#x20;         \--table-header-text: #ffffff;
&#x20;         \--table-border: #555555;
&#x20;         \--link-color: #1e90ff;
&#x20;         \--row-alt-bg: #2b2b2b;
&#x20;       }

&#x20;       html\[data-color-mode="light"] \{
&#x20;         \--table-bg: #ffffff;
&#x20;         \--table-text: #000000;
&#x20;         \--table-header-bg: #f2f2f2;
&#x20;         \--table-header-text: #000000;
&#x20;         \--table-border: #cccccc;
&#x20;         \--link-color: #007bff;
&#x20;         \--row-alt-bg: #f9f9f9;
&#x20;       }

&#x20;       table \{
&#x20;         width: 100%;
&#x20;         text-align: left;
&#x20;         background-color: var(--table-bg);
&#x20;         color: var(--table-text);
&#x20;         border-collapse: collapse;
&#x20;       }

&#x20;       th \{
&#x20;         background-color: var(--table-header-bg);
&#x20;         color: var(--table-header-text);
&#x20;         border-bottom: 1px solid var(--table-border);
&#x20;         padding: 8px;
&#x20;         font-weight: bold;
&#x20;       }

&#x20;       td \{
&#x20;         padding: 8px;
&#x20;         border-bottom: 1px solid var(--table-border);
&#x20;       }

&#x20;       tr:nth-child(even) \{
&#x20;         background-color: var(--row-alt-bg);
&#x20;       }

&#x20;       a \{
&#x20;         color: var(--link-color);
&#x20;         text-decoration: none;
&#x20;       }

&#x20;       a:hover \{
&#x20;         text-decoration: underline;
&#x20;       }
&#x20;     \`}\</style>
&#x20;     \<h1>Institutions\</h1>

&#x20;     \{/\* Display total institutions count \*/}
&#x20;     \<div style=\{\{ marginBottom: "16px", fontSize: "16px" }}>
&#x20;       \<strong>Total Institutions: \{institutions.length}\</strong>
&#x20;     \</div>

&#x20;     \<div style=\{\{ marginBottom: "16px", display: "flex", justifyContent: "flex-end" }}>
&#x20;       \<div style=\{\{ position: "relative", maxWidth: "400px", width: "100%" }}>
&#x20;         \<input
&#x20;           type="text"
&#x20;           placeholder="Search by institution name"
&#x20;           value=\{searchQuery}
&#x20;           onChange=\{(e) => \{
&#x20;             setSearchQuery(e.target.value);
&#x20;             setCurrentPage(1); // Reset to the first page on new search
&#x20;           }}
&#x20;           style=\{\{
&#x20;             padding: "8px 8px 8px 32px", // Add padding for the icon
&#x20;             width: "100%",
&#x20;             border: "1px solid #ccc",
&#x20;             borderRadius: "4px",
&#x20;             fontSize: "16px",
&#x20;           }}
&#x20;         />
&#x20;         \<span
&#x20;           style=\{\{
&#x20;             position: "absolute",
&#x20;             left: "8px",
&#x20;             top: "50%",
&#x20;             transform: "translateY(-50%)",
&#x20;             fontSize: "18px",
&#x20;             color: "#ccc",
&#x20;           }}
&#x20;         \>
&#x20;           \&#x1F50D; \{/\* Unicode character for search icon \*/}
&#x20;         \</span>
&#x20;       \</div>
&#x20;     \</div>

&#x20;     \<table border="1" cellPadding="8" cellSpacing="0">
&#x20;       \<thead>
&#x20;         \<tr>
&#x20;           \<th>Logo\</th>
&#x20;           \<th>Short Name\</th>
&#x20;           \<th>FAQ\</th>
&#x20;           \<th>CDR Policy\</th>
&#x20;           \<th>Email\</th>
&#x20;           \<th>CDR Provider Number\</th>
&#x20;         \</tr>
&#x20;       \</thead>
&#x20;       \<tbody>
&#x20;         \{paginatedInstitutions.map((institution, index) => (
&#x20;           \<tr key=\{index}>
&#x20;             \<td>
&#x20;               \{institution.logo && institution.logo.links ? (
&#x20;                 \<img
&#x20;                   src=\{institution.logo.links.square}
&#x20;                   alt=\{\`$\{institution.shortName} Logo\`}
&#x20;                   style=\{\{ width: "64px", height: "64px" }}
&#x20;                 />
&#x20;               ) : (
&#x20;                 "N/A"
&#x20;               )}
&#x20;             \</td>
&#x20;             \<td>\{institution.shortName}\</td>
&#x20;             \<td>
&#x20;               \<a href=\{institution.cdrFAQ} target="\_blank" rel="noopener noreferrer">
&#x20;                 FAQ
&#x20;               \</a>
&#x20;             \</td>
&#x20;             \<td>
&#x20;               \<a href=\{institution.cdrPolicy} target="\_blank" rel="noopener noreferrer">
&#x20;                 CDR Policy
&#x20;               \</a>
&#x20;             \</td>
&#x20;             \<td>\{institution.cdrEmail || "N/A"}\</td>
&#x20;             \<td>\{institution.cdrProviderNumber}\</td>
&#x20;           \</tr>
&#x20;         ))}
&#x20;       \</tbody>
&#x20;     \</table>

&#x20;     \{/\* Pagination Controls \*/}
&#x20;     \<div style=\{\{ marginTop: "16px", display: "flex", justifyContent: "center", alignItems: "center", gap: "16px" }}>
&#x20;       \<button
&#x20;         onClick=\{() => handlePageChange("prev")}
&#x20;         disabled=\{currentPage === 1}
&#x20;         style=\{\{
&#x20;           padding: "8px 16px",
&#x20;           border: "none",
&#x20;           borderRadius: "4px",
&#x20;           backgroundColor: currentPage === 1 ? "#d3d3d3" : "#007bff",
&#x20;           color: "white",
&#x20;           cursor: currentPage === 1 ? "not-allowed" : "pointer",
&#x20;           fontSize: "16px",
&#x20;         }}
&#x20;       \>
&#x20;         \&laquo; Previous
&#x20;       \</button>
&#x20;       \<span style=\{\{ fontSize: "16px", fontWeight: "bold" }}>
&#x20;         Page \{currentPage} of \{totalPages}
&#x20;       \</span>
&#x20;       \<button
&#x20;         onClick=\{() => handlePageChange("next")}
&#x20;         disabled=\{currentPage === totalPages}
&#x20;         style=\{\{
&#x20;           padding: "8px 16px",
&#x20;           border: "none",
&#x20;           borderRadius: "4px",
&#x20;           backgroundColor: currentPage === totalPages ? "#d3d3d3" : "#007bff",
&#x20;           color: "white",
&#x20;           cursor: currentPage === totalPages ? "not-allowed" : "pointer",
&#x20;           fontSize: "16px",
&#x20;         }}
&#x20;       \>
&#x20;         Next \&raquo;
&#x20;       \</button>
&#x20;     \</div>
&#x20;   \</div>
&#x20; );
};

\<InstitutionList />


<p> </p>