---
title: Toast Notifications
fullscreen: false
hidden: true
---
import React, { useState, useEffect } from 'react';

export const InstitutionList = () => {
  const [institutions, setInstitutions] = useState([]);
  const [outageInstitutions, setOutageInstitutions] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [currentPage, setCurrentPage] = useState(1);
  const [institutionsPerPage] = useState(10);

  useEffect(() => {
    // Fetch institutions and their outage status
    const fetchInstitutions = async () => {
      try {
        const response = await fetch('https://au-api.basiq.io/public/connectors?filter=connector.method.eq(%27open-banking%27)'); // Replace with actual API URL
        const data = await response.json();
        setInstitutions(data.institutions);

        // Filter institutions that are in outage
        const outages = data.institutions.filter(
          (institution) => institution.isOutage
        );
        setOutageInstitutions(outages);
      } catch (error) {
        console.error('Error fetching institutions:', error);
      }
    };

    fetchInstitutions();
  }, []);

  const handlePageChange = (direction) => {
    if (direction === 'prev' && currentPage > 1) {
      setCurrentPage((prevPage) => prevPage - 1);
    } else if (direction === 'next' && currentPage < totalPages) {
      setCurrentPage((prevPage) => prevPage + 1);
    }
  };

  // Search functionality
  const filteredInstitutions = institutions.filter((institution) =>
    institution.shortName.toLowerCase().includes(searchQuery.toLowerCase())
  );

  // Pagination logic
  const totalPages = Math.ceil(filteredInstitutions.length / institutionsPerPage);
  const paginatedInstitutions = filteredInstitutions.slice(
    (currentPage - 1) * institutionsPerPage,
    currentPage * institutionsPerPage
  );

  return (
    <div>
      {/* Display total institutions count */}
      <div style={{ marginBottom: '16px', fontSize: '16px' }}>
        <strong>Total Institutions: {institutions.length}</strong>
      </div>

      {/* Display institutions in outage */}
      {outageInstitutions.length > 0 && (
        <div style={{ marginBottom: '16px', fontSize: '16px', color: 'red' }}>
          <strong>Outages Detected: {outageInstitutions.length}</strong>
          <ul>
            {outageInstitutions.map((institution, index) => (
              <li key={index}>
                {institution.shortName} - {institution.reason || 'Outage reason not specified'}
              </li>
            ))}
          </ul>
        </div>
      )}

      <div style={{ marginBottom: '16px', display: 'flex', justifyContent: 'flex-end' }}>
        <div style={{ position: 'relative', maxWidth: '400px', width: '100%' }}>
          <input
            type="text"
            placeholder="Search by institution name"
            value={searchQuery}
            onChange={(e) => {
              setSearchQuery(e.target.value);
              setCurrentPage(1); // Reset to the first page on new search
            }}
            style={{
              padding: '8px 8px 8px 32px', // Add padding for the icon
              width: '100%',
              border: '1px solid #ccc',
              borderRadius: '4px',
              fontSize: '16px',
            }}
          />
          <span
            style={{
              position: 'absolute',
              left: '8px',
              top: '50%',
              transform: 'translateY(-50%)',
              fontSize: '18px',
              color: '#ccc',
            }}
          >
            &#x1F50D; {/* Unicode character for search icon */}
          </span>
        </div>
      </div>

      <table border="1" cellPadding="8" cellSpacing="0" style={{ width: '100%', textAlign: 'left' }}>
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
          {paginatedInstitutions.map((institution, index) => (
            <tr
              key={index}
              style={{
                backgroundColor: institution.isOutage ? '#ffd6d6' : 'transparent',
              }}
            >
              <td>
                {institution.logo && institution.logo.links ? (
                  <img
                    src={institution.logo.links.square}
                    alt={`${institution.shortName} Logo`}
                    style={{ width: '64px', height: '64px' }}
                  />
                ) : (
                  'N/A'
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
              <td>{institution.cdrEmail || 'N/A'}</td>
              <td>{institution.cdrProviderNumber}</td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* Pagination Controls */}
      <div
        style={{
          marginTop: '16px',
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          gap: '16px',
        }}
      >
        <button
          onClick={() => handlePageChange('prev')}
          disabled={currentPage === 1}
          style={{
            padding: '8px 16px',
            border: 'none',
            borderRadius: '4px',
            backgroundColor: currentPage === 1 ? '#d3d3d3' : '#007bff',
            color: 'white',
            cursor: currentPage === 1 ? 'not-allowed' : 'pointer',
            fontSize: '16px',
          }}
        >
          &laquo; Previous
        </button>
        <span style={{ fontSize: '16px', fontWeight: 'bold' }}>
          Page {currentPage} of {totalPages}
        </span>
        <button
          onClick={() => handlePageChange('next')}
          disabled={currentPage === totalPages}
          style={{
            padding: '8px 16px',
            border: 'none',
            borderRadius: '4px',
            backgroundColor: currentPage === totalPages ? '#d3d3d3' : '#007bff',
            color: 'white',
            cursor: currentPage === totalPages ? 'not-allowed' : 'pointer',
            fontSize: '16px',
          }}
        >
          Next &raquo;
        </button>
      </div>
    </div>
  );
};

// If using this file directly in MDX, you can use the `InstitutionList` component as follows:

<br />

<InstitutionList />