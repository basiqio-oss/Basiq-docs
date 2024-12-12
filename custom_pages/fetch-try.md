---
title: Fetch Try
fullscreen: false
hidden: true
---
\<Accordion title="My Accordion Title" icon="fa-info-circle">
&#x20; Lorem ipsum dolor sit amet, \*\*consectetur adipiscing elit.\*\* Ut enim
&#x20; ad minim veniam, quis nostrud exercitation ullamco. Excepteur sint
&#x20; occaecat cupidatat non proident!
\</Accordion>

import \{ useState, useEffect } from 'react';

const fetchRSS = async () => \{
&#x20; const response = await fetch('https\://api.basiq.io/changelog.rss');
&#x20; const data = await response.text();
&#x20; const parser = new DOMParser();
&#x20; const xmlDoc = parser.parseFromString(data, 'application/xml');
&#x20; const items = xmlDoc.querySelectorAll('item');
&#x20; return items.length ? items\[0] : null;
};

export const NotificationDemo = () => \{
&#x20; const \[isNotificationVisible, setIsNotificationVisible] = useState(false);
&#x20; const \[latestFeedItem, setLatestFeedItem] = useState(null);
&#x20; const \[lastFeedItemTitle, setLastFeedItemTitle] = useState(null);

&#x20; // Show notification automatically when the page loads
&#x20; useEffect(() => \{
&#x20;   const handleEscape = (event) => \{
&#x20;     if (event.key === 'Escape') \{
&#x20;       setIsNotificationVisible(false); // Hide notification on Escape key
&#x20;     }
&#x20;   };
&#x20;   window\.addEventListener('keydown', handleEscape);

&#x20;   // Cleanup event listener on component unmount
&#x20;   return () => window\.removeEventListener('keydown', handleEscape);
&#x20; }, \[]);

&#x20; useEffect(() => \{
&#x20;   const checkForNewFeed = async () => \{
&#x20;     const latestItem = await fetchRSS();

&#x20;     if (latestItem) \{
&#x20;       const title = latestItem.querySelector('title').textContent;

&#x20;       // Compare with previous feed item to check if it's new
&#x20;       if (title !== lastFeedItemTitle) \{
&#x20;         setLatestFeedItem(latestItem);
&#x20;         setIsNotificationVisible(true);
&#x20;         setLastFeedItemTitle(title);
&#x20;       }
&#x20;     }
&#x20;   };

&#x20;   // Check for new feed every 30 seconds
&#x20;   const intervalId = setInterval(checkForNewFeed, 30000);
&#x20;  &#x20;
&#x20;   // Initial check
&#x20;   checkForNewFeed();

&#x20;   // Cleanup the interval on component unmount
&#x20;   return () => clearInterval(intervalId);
&#x20; }, \[lastFeedItemTitle]);

&#x20; const closeNotification = () => setIsNotificationVisible(false);

&#x20; return (
&#x20;   \<div>
&#x20;     \{isNotificationVisible && latestFeedItem && (
&#x20;       \<div
&#x20;         style=\{\{
&#x20;           position: 'fixed',
&#x20;           bottom: '20px', // Position from the bottom
&#x20;           right: '20px',  // Position from the right
&#x20;           backgroundColor: '#007BFF',
&#x20;           color: '#fff',
&#x20;           padding: '15px 30px',
&#x20;           borderRadius: '8px',
&#x20;           boxShadow: '0 8px 16px rgba(0, 0, 0, 0.2)',
&#x20;           zIndex: '1000',
&#x20;           display: 'flex',
&#x20;           alignItems: 'center',
&#x20;           animation: 'fadeIn 0.3s',
&#x20;           justifyContent: 'space-between',
&#x20;           minWidth: '250px',
&#x20;         }}
&#x20;         onClick=\{closeNotification}
&#x20;       \>
&#x20;         \<p style=\{\{ margin: '0' }}>
&#x20;           New Update: \{latestFeedItem.querySelector('title').textContent}
&#x20;         \</p>

&#x20;         \{/\* Close Button \*/}
&#x20;         \<button
&#x20;           onClick=\{closeNotification}
&#x20;           style=\{\{
&#x20;             backgroundColor: 'transparent',
&#x20;             border: 'none',
&#x20;             fontSize: '18px',
&#x20;             color: '#fff',
&#x20;             cursor: 'pointer',
&#x20;             fontWeight: 'bold',
&#x20;             transition: 'color 0.3s',
&#x20;           }}
&#x20;           onMouseEnter=\{(e) => e.target.style.color = '#dc3545'}
&#x20;           onMouseLeave=\{(e) => e.target.style.color = '#fff'}
&#x20;         \>
&#x20;           \&times;
&#x20;         \</button>
&#x20;       \</div>
&#x20;     )}

&#x20;     \<style>
&#x20;       \{\`
&#x20;         @keyframes fadeIn \{
&#x20;           from \{ opacity: 0; }
&#x20;           to \{ opacity: 1; }
&#x20;         }
&#x20;       \`}
&#x20;     \</style>
&#x20;   \</div>
&#x20; );
};