---
title: Toast Notifications
fullscreen: false
hidden: true
---
import React, \{ useState, useEffect } from 'react';

const getStatusColor = (status) => \{
&#x20; switch (status) \{
&#x20;   case 'partial-outage':
&#x20;     return '#ffa726'; // Orange
&#x20;   case 'under-maintenance':
&#x20;     return '#6c757d'; // Gray
&#x20;   case 'major-outage':
&#x20;     return '#dc3545'; // Red
&#x20;   case 'degraded-performance':
&#x20;     return '#ffc107'; // Yellow
&#x20;   default:
&#x20;     return '#28a745'; // Green for "operational" status, or fallback
&#x20; }
};

export const StatusNotifications = () => \{
&#x20; const \[notifications, setNotifications] = useState(\[]);
&#x20;&#x20;
&#x20; useEffect(() => \{
&#x20;   // Fetching the data periodically every 30 seconds
&#x20;   const fetchData = async () => \{
&#x20;     try \{
&#x20;       const response = await fetch('https\://au-api.basiq.io/public/connectors?filter=connector.method.eq(%27open-banking%27)');
&#x20;       const data = await response.json();
&#x20;      &#x20;
&#x20;       const filteredNotifications = data.data.filter(institution =>
&#x20;         \['partial-outage', 'under-maintenance', 'major-outage', 'degraded-performance'].includes(institution.status)
&#x20;       );
&#x20;      &#x20;
&#x20;       // Create notifications
&#x20;       const newNotifications = filteredNotifications.map((institution, index) => (\{
&#x20;         id: institution.id,
&#x20;         name: institution.institution.shortName,
&#x20;         status: institution.status,
&#x20;         color: getStatusColor(institution.status),
&#x20;       }));
&#x20;      &#x20;
&#x20;       // Update the notifications state
&#x20;       setNotifications((prevNotifications) => \{
&#x20;         // Limit to 10 notifications, showing only new ones
&#x20;         const newStack = \[...newNotifications, ...prevNotifications].slice(0, 10);
&#x20;         return newStack;
&#x20;       });
&#x20;     } catch (error) \{
&#x20;       console.error('Error fetching data:', error);
&#x20;     }
&#x20;   };

&#x20;   // Fetch the data every 30 seconds
&#x20;   const interval = setInterval(fetchData, 30000);

&#x20;   // Initial fetch
&#x20;   fetchData();

&#x20;   return () => clearInterval(interval);
&#x20; }, \[]);

&#x20; const removeNotification = (id) => \{
&#x20;   setNotifications((prevNotifications) =>
&#x20;     prevNotifications.filter((notification) => notification.id !== id)
&#x20;   );
&#x20; };

&#x20; return (
&#x20;   \<div>
&#x20;     \{notifications.map((notification) => (
&#x20;       \<div
&#x20;         key=\{notification.id}
&#x20;         style=\{\{
&#x20;           backgroundColor: notification.color,
&#x20;           color: '#fff',
&#x20;           padding: '10px 20px',
&#x20;           borderRadius: '5px',
&#x20;           marginBottom: '10px',
&#x20;           position: 'relative',
&#x20;         }}
&#x20;       \>
&#x20;         \<p style=\{\{ margin: '0' }}>
&#x20;           \{notification.name} is currently experiencing \{notification.status.replace('-', ' ')}.
&#x20;         \</p>
&#x20;         \<button
&#x20;           onClick=\{() => removeNotification(notification.id)}
&#x20;           style=\{\{
&#x20;             position: 'absolute',
&#x20;             top: '10px',
&#x20;             right: '10px',
&#x20;             background: 'transparent',
&#x20;             border: 'none',
&#x20;             color: '#fff',
&#x20;             fontSize: '18px',
&#x20;             cursor: 'pointer',
&#x20;           }}
&#x20;         \>
&#x20;           \&times;
&#x20;         \</button>
&#x20;       \</div>
&#x20;     ))}
&#x20;   \</div>
&#x20; );
};


// If using this file directly in MDX, you can use the `InstitutionList` component as follows:

<br />

<InstitutionList />