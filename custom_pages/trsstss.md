---
title: trsstss
fullscreen: false
hidden: false
---
import React from 'react';

export const AddRSSToSlackButton = () => (
  <div>
    <h2>Subscribe to Our Changelog on Slack</h2>
    <p>Stay up-to-date with the latest changes by subscribing to our RSS feed directly in Slack:</p>
    <a 
      href="https://slack.com/apps/A0F827V8R-rss" 
      target="_blank" 
      rel="noopener noreferrer"
      style={{
        textDecoration: 'none',
        display: 'inline-block',
        backgroundColor: '#0073e6',
        color: 'white',
        padding: '10px 20px',
        border: 'none',
        borderRadius: '5px',
        cursor: 'pointer',
      }}
    >
      Add RSS Feed to Slack
    </a>
  </div>
);

export default AddRSSToSlackButton;