---
title: Toast Notifications
fullscreen: false
hidden: true
---
import React, { useState, useEffect } from 'react';

export const InstitutionList = () => {
  const [institutions, setInstitutions] = useState([]);
  const [statusNotifications, setStatusNotifications] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [currentPage, setCurrentPage] = useState(1);
  const [institutionsPerPage] = useState(10);

  useEffect(() => {
    const fetchInstitutions = async () => {
      try {
        const response = await fetch(
          'https://au-api.basiq.io/public/connectors?filter=connector.method.eq(%27open-banking%27)'
        );
        const data = await response.json();

        if (Array.isArray(data.data)) {
          const institutionList = data.data.map((connector) => connector.institution);
          setInstitutions(institutionList);

          // Process status notifications for each institution
          const statusList = data.data.map((connector) => {
            const { status, institution } = connector;
            return { status, institution };
          });

          setStatusNotifications(statusList);
        } else {
          console.error('Unexpected API response structure:', data);
        }
      } catch (error) {
        console.error('Error fetching institutions:', error);
      }
    };

    // Initial fetch
    fetchInstitutions();

    // Set interval to fetch data every 30 seconds
    const interval = setInterval(() => {
      fetchInstitutions();
    }, 30000);

    return () => clearInterval(interval); // Cleanup interval on unmount
  }, []);

const getStatusColor = (status) => {
  switch (status) {
    case 'partial-outage':
      return '#ffa726'; // Orange
    case 'under-maintenance':
      return '#6c757d'; // Gray
    case 'major-outage':
      return '#dc3545'; // Red
    case 'degraded-performance':
      return '#ffc107'; // Yellow
    default:
      return '#28a745'; // Green for "operational" status, or fallback
  }
};

  const closeToast = (index) => {
    setStatusNotifications((prevState) => prevState.filter((_, i) => i !== index));
  };

  // Pagination logic
  const filteredInstitutions = institutions.filter((institution) =>
    institution.shortName.toLowerCase().includes(searchQuery.toLowerCase())
  );
  const totalPages = Math.ceil(filteredInstitutions.length / institutionsPerPage);
  const paginatedInstitutions = filteredInstitutions.slice(
    (currentPage - 1) * institutionsPerPage,
    currentPage * institutionsPerPage
  );

  return (
    <div>
      {/* Toast Notifications for statuses */}
      {statusNotifications.map((notification, index) => (
        <div
          key={index}
          style={{
            position: 'fixed',
            bottom: `${20 + index * 70}px`, // Stack multiple notifications
            right: '20px',
            backgroundColor: getStatusColor(notification.status),
            color: '#fff',
            padding: '15px 20px',
            borderRadius: '8px',
            boxShadow: '0 4px 8px rgba(0, 0, 0, 0.2)',
            zIndex: '1000',
            opacity: '1',
            animation: 'fadeOut 5s ease-in-out',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            width: '300px',
          }}
        >
          <div>
            <strong>{notification.institution.shortName}</strong> - {notification.status.replace('-', ' ')}
          </div>
          <button
            onClick={() => closeToast(index)}
            style={{
              background: 'none',
              border: 'none',
              color: '#fff',
              fontSize: '20px',
              cursor: 'pointer',
            }}
          >
            &times;
          </button>
        </div>
      ))}

      {/* Search bar */}
      <div style={{ marginBottom: '16px', display: 'flex', justifyContent: 'flex-end' }}>
        <div style={{ position: 'relative', maxWidth: '400px', width: '100%' }}>
          <input
            type="text"
            placeholder="Search by institution name"
            value={searchQuery}
            onChange={(e) => {
              setSearchQuery(e.target.value);
              setCurrentPage(1); // Reset to first page on new search
            }}
            style={{
              padding: '8px 8px 8px 32px',
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
            &#x1F50D;
          </span>
        </div>
      </div>

      {/* Institutions Table */}
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
            <tr key={index}>
              <td>
                {institution.logo?.links?.square ? (
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
          onClick={() => setCurrentPage((prev) => Math.max(prev - 1, 1))}
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
          onClick={() => setCurrentPage((prev) => Math.min(prev + 1, totalPages))}
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

      {/* CSS for Fade Out Animation */}
      <style>
        {`
          @keyframes fadeOut {
            0% { opacity: 1; }
            90% { opacity: 0.1; }
            100% { opacity: 0; }
          }
        `}
      </style>
    </div>
  );
};

// If using this file directly in MDX, you can use the `InstitutionList` component as follows:

<br />

<InstitutionList />