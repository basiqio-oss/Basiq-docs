---
title: test 01
fullscreen: false
hidden: false
---
import React, \{ useState } from 'react';

const App = () => \{
&#x20; const items = \[
&#x20;   \{ id: 1, title: 'Financial Data Services', description: 'Access detailed financial data from a range of institutions.' },
&#x20;   \{ id: 2, title: 'Payment Services', description: 'Facilitate various payment services, including the ability to collect, send, and receive payments.' },
&#x20;   \{ id: 3, title: 'Data Enrichment Services', description: 'Enhance your financial data with enrichment services.' },
&#x20;   \{ id: 4, title: 'Reporting Services', description: 'Generate insightful reports and analytics from financial data.' },
&#x20;   \{ id: 5, title: 'Webhooks & Real-time Notifications', description: 'Stay updated with real-time notifications.' },
&#x20; ];

&#x20; const \[searchQuery, setSearchQuery] = useState('');

&#x20; const filteredItems = items.filter(item =>&#x20;
&#x20;   item.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
&#x20;   item.description.toLowerCase().includes(searchQuery.toLowerCase())
&#x20; );

&#x20; return (
&#x20;   \<div style=\{\{ padding: '20px' }}>
&#x20;     \<input
&#x20;       type="text"
&#x20;       placeholder="Search..."
&#x20;       value=\{searchQuery}
&#x20;       onChange=\{(e) => setSearchQuery(e.target.value)}
&#x20;       style=\{\{ padding: '10px', marginBottom: '10px', width: '100%' }}
&#x20;     />
&#x20;     \<div>
&#x20;       \{filteredItems.length > 0 ? (
&#x20;         filteredItems.map(item => (
&#x20;           \<div key=\{item.id} style=\{\{ padding: '10px', marginBottom: '10px', border: '1px solid #ddd' }}>
&#x20;             \<h3>\{item.title}\</h3>
&#x20;             \<p>\{item.description}\</p>
&#x20;           \</div>
&#x20;         ))
&#x20;       ) : (
&#x20;         \<p>No results found\</p>
&#x20;       )}
&#x20;     \</div>
&#x20;   \</div>
&#x20; );
};

export default App;