---
title: test 01
fullscreen: false
hidden: false
---
import React, { useState } from 'react';

const App = () => {
  const items = [
    { id: 1, title: 'Financial Data Services', description: 'Access detailed financial data from a range of institutions.' },
    { id: 2, title: 'Payment Services', description: 'Facilitate various payment services, including the ability to collect, send, and receive payments.' },
    { id: 3, title: 'Data Enrichment Services', description: 'Enhance your financial data with enrichment services.' },
    { id: 4, title: 'Reporting Services', description: 'Generate insightful reports and analytics from financial data.' },
    { id: 5, title: 'Webhooks & Real-time Notifications', description: 'Stay updated with real-time notifications.' },
  ];

  const [searchQuery, setSearchQuery] = useState('');

  const filteredItems = items.filter(item => 
    item.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
    item.description.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <div style={{ padding: '20px' }}>
      <input
        type="text"
        placeholder="Search..."
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
        style={{ padding: '10px', marginBottom: '10px', width: '100%' }}
      />
      <div>
        {filteredItems.length > 0 ? (
          filteredItems.map(item => (
            <div key={item.id} style={{ padding: '10px', marginBottom: '10px', border: '1px solid #ddd' }}>
              <h3>{item.title}</h3>
              <p>{item.description}</p>
            </div>
          ))
        ) : (
          <p>No results found</p>
        )}
      </div>
    </div>
  );
};

export default App;
