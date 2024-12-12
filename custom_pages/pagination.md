---
title: Pagination
fullscreen: false
hidden: true
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

import React from 'react';

export const EmbeddedList = () => {
  // Sample data to display in the list
  const data = [
    'Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6', 
    'Item 7', 'Item 8', 'Item 9', 'Item 10', 'Item 11', 'Item 12', 
    'Item 13', 'Item 14', 'Item 15', 'Item 16', 'Item 17', 'Item 18'
  ];

  return (
    <div style={{ margin: '20px 0' }}>
      {/* List Display */}
      <ul style={{ padding: '0', listStyle: 'none' }}>
        {data.map((item, index) => (
          <li key={index} style={{ padding: '8px 0', borderBottom: '1px solid #ddd' }}>
            <h4>{item}</h4>
            {/* Embedded Iframe */}
            <div style={{ marginTop: '10px' }}>
              <iframe
                src="https://grafana.basiq-internal.com/d-solo/c7e04373-10ed-4e78-ab27-5c06328e84b7/basiq-product-usage?orgId=1&from=now-5y&to=now&panelId=2"
                width="450"
                height="200"
                frameBorder="0"
                title={`Grafana Panel - ${item}`}
              />
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

Page now resolved.