---
title: Grafana Graphs
fullscreen: false
hidden: false
---
<Cards columns={4}>
  <Card title="First Card" href="https://readme.com" icon="fa-home" target="_blank">
    Neque porro quisquam est qui dolorem ipsum quia
  </Card>

  <Card title="Second Card" icon="fa-user">
    *Lorem ipsum dolor sit amet, consectetur adipiscing elit*
  </Card>

  <Card title="Third Card" icon="fa-star">
    > Ut enim ad minim veniam, quis nostrud ullamco
  </Card>

  <Card title="Fourth Card" icon="fa-question">
    **Excepteur sint occaecat cupidatat non proident**
  </Card>
</Cards>

<br />

import React from 'react';

export const PageWithIframe = () => {
  return (
    <div style={{ margin: '20px 0' }}>
      <h2 style={{ textAlign: 'center', marginBottom: '20px' }}>Raintank Dashboard Snapshot</h2>
      
      <p style={{ textAlign: 'center', fontSize: '14px', marginBottom: '20px' }}>
        Below is an embedded Raintank Dashboard snapshot.
      </p>

      {/* Iframe Embedding */}
      <div
        style={{
          position: 'relative',
          width: '100%',
          maxWidth: '1200px',  // Optional: Max width for responsiveness
          height: '600px',  // Set a fixed height for the iframe
          margin: '0 auto',  // Center the iframe horizontally
          borderRadius: '8px',
          overflow: 'hidden',
        }}
      >
        <iframe
          src="https://snapshots.raintank.io/dashboard/snapshot/TWq2oCPxUcZfrldh6dnVHJQoZJWh5lX2"
          title="Raintank Dashboard Snapshot"
          frameBorder="0"
          loading="lazy"
          webkitAllowFullScreen
          mozAllowFullScreen
          allowFullScreen
          allow="clipboard-write"
          style={{
            position: 'absolute',
            top: '0',
            left: '0',
            width: '100%',
            height: '100%',
            borderRadius: '8px',
          }}
        ></iframe>
      </div>
    </div>
  );
};