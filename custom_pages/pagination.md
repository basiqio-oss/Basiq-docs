---
title: Pagination
fullscreen: false
hidden: true
---
\<Columns layout="auto">
&#x20; \<Column>
&#x20;   Neque porro quisquam est qui dolorem ipsum quia
&#x20; \</Column>

&#x20; \<Column>
&#x20;   \*Lorem ipsum dolor sit amet, consectetur adipiscing elit\*
&#x20; \</Column>

&#x20; \<Column>
&#x20;   \> Ut enim ad minim veniam, quis nostrud ullamco
&#x20; \</Column>
\</Columns>

import React from 'react';

const EmbeddedList = () => \{
&#x20; return (
&#x20;   \<div style=\{\{ margin: '20px 0' }}>
&#x20;     \<ul style=\{\{ padding: '0', listStyle: 'none' }}>
&#x20;       \<li style=\{\{ padding: '10px 0', borderBottom: '1px solid #ddd' }}>
&#x20;         \<h4>Item 1\</h4>
&#x20;         \<iframe
&#x20;           src="https\://grafana.basiq-internal.com/d-solo/c7e04373-10ed-4e78-ab27-5c06328e84b7/basiq-product-usage?orgId=1\&from=now-5y\&to=now\&panelId=2"
&#x20;           width="450"
&#x20;           height="200"
&#x20;           frameBorder="0"
&#x20;           title="Grafana Panel - Item 1"
&#x20;         />
&#x20;       \</li>
&#x20;       \<li style=\{\{ padding: '10px 0', borderBottom: '1px solid #ddd' }}>
&#x20;         \<h4>Item 2\</h4>
&#x20;         \<iframe
&#x20;           src="https\://grafana.basiq-internal.com/d-solo/c7e04373-10ed-4e78-ab27-5c06328e84b7/basiq-product-usage?orgId=1\&from=now-5y\&to=now\&panelId=2"
&#x20;           width="450"
&#x20;           height="200"
&#x20;           frameBorder="0"
&#x20;           title="Grafana Panel - Item 2"
&#x20;         />
&#x20;       \</li>
&#x20;       \{/\* Add more items as needed \*/}
&#x20;     \</ul>
&#x20;   \</div>
&#x20; );
};

export default EmbeddedList;