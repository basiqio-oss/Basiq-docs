---
title: Pagination
fullscreen: false
hidden: false
---
<Columns layout="auto">
  <Column>
    Neque porro quisquam est qui dolorem ipsum quia
  </Column>

  <Column>
    *Lorem ipsum dolor sit amet, consectetur adipiscing elit*
  </Column>

  <Column>
    > Ut enim ad minim veniam, quis nostrud ullamco
  </Column>
</Columns>

<br />

import React, { useState } from 'react';

export const PaginatedList = () => {
  // Sample data to display in the list
  const data = [
    'Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6', 
    'Item 7', 'Item 8', 'Item 9', 'Item 10', 'Item 11', 'Item 12', 
    'Item 13', 'Item 14', 'Item 15', 'Item 16', 'Item 17', 'Item 18'
  ];

  // Pagination settings
  const itemsPerPage = 5; // Number of items to display per page
  const [currentPage, setCurrentPage] = useState(1); // Current page state

  // Calculate total pages
  const totalPages = Math.ceil(data.length / itemsPerPage);

  // Get items for the current page
  const indexOfLastItem = currentPage * itemsPerPage;
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;
  const currentItems = data.slice(indexOfFirstItem, indexOfLastItem);

  // Handlers for page navigation
  const handleNextPage = () => {
    if (currentPage < totalPages) {
      setCurrentPage(currentPage + 1);
    }
  };

  const handlePrevPage = () => {
    if (currentPage > 1) {
      setCurrentPage(currentPage - 1);
    }
  };

  const handlePageChange = (pageNumber) => {
    setCurrentPage(pageNumber);
  };

  return (
    <div style={{ margin: '20px 0' }}>
      {/* List Display */}
      <ul style={{ padding: '0', listStyle: 'none' }}>
        {currentItems.map((item, index) => (
          <li key={index} style={{ padding: '8px 0', borderBottom: '1px solid #ddd' }}>
            {item}
          </li>
        ))}
      </ul>

      {/* Pagination Controls */}
      <div style={{ display: 'flex', justifyContent: 'center', marginTop: '20px' }}>
        <button
          onClick={handlePrevPage}
          disabled={currentPage === 1}
          style={{
            padding: '8px 16px',
            margin: '0 5px',
            cursor: currentPage === 1 ? 'not-allowed' : 'pointer',
            backgroundColor: '#007BFF',
            color: '#fff',
            border: 'none',
            borderRadius: '4px',
          }}
        >
          Prev
        </button>

        {/* Page number buttons */}
        {[...Array(totalPages).keys()].map((num) => (
          <button
            key={num}
            onClick={() => handlePageChange(num + 1)}
            style={{
              padding: '8px 16px',
              margin: '0 5px',
              cursor: 'pointer',
              backgroundColor: currentPage === num + 1 ? '#007BFF' : '#fff',
              color: currentPage === num + 1 ? '#fff' : '#007BFF',
              border: '1px solid #007BFF',
              borderRadius: '4px',
            }}
          >
            {num + 1}
          </button>
        ))}

        <button
          onClick={handleNextPage}
          disabled={currentPage === totalPages}
          style={{
            padding: '8px 16px',
            margin: '0 5px',
            cursor: currentPage === totalPages ? 'not-allowed' : 'pointer',
            backgroundColor: '#007BFF',
            color: '#fff',
            border: 'none',
            borderRadius: '4px',
          }}
        >
          Next
        </button>
      </div>
    </div>
  );
};

Page now resolved.