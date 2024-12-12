---
title: Push Notification on the Bottom
fullscreen: false
hidden: true
---
<Accordion title="My Accordion Title" icon="fa-info-circle">
  Lorem ipsum dolor sit amet, **consectetur adipiscing elit.** Ut enim
  ad minim veniam, quis nostrud exercitation ullamco. Excepteur sint
  occaecat cupidatat non proident!
</Accordion>

<br />

import { useState, useEffect } from 'react';

<div style={{ margin: '20px 0' }}>
  <NotificationDemo />
</div>

export const NotificationDemo = () => {
  const [isNotificationVisible, setIsNotificationVisible] = useState(true);

  // Show notification automatically when the page loads
  useEffect(() => {
    const handleEscape = (event) => {
      if (event.key === 'Escape') {
        setIsNotificationVisible(false); // Hide notification on Escape key
      }
    };
    window.addEventListener('keydown', handleEscape);

    // Cleanup event listener on component unmount
    return () => window.removeEventListener('keydown', handleEscape);
  }, []);

  const closeNotification = () => setIsNotificationVisible(false);

  return (
    <div>
      {isNotificationVisible && (
        <div
          style={{
            position: 'fixed',
            bottom: '20px', // Position from the bottom
            right: '20px',  // Position from the right
            backgroundColor: '#007BFF',
            color: '#fff',
            padding: '15px 30px',
            borderRadius: '8px',
            boxShadow: '0 8px 16px rgba(0, 0, 0, 0.2)',
            zIndex: '1000',
            display: 'flex',
            alignItems: 'center',
            animation: 'fadeIn 0.3s',
            justifyContent: 'space-between',
            minWidth: '250px',
          }}
          onClick={closeNotification}
        >
          <p style={{ margin: '0' }}>
            You have a new notification! Click anywhere to close.
          </p>

          {/* Close Button */}
          <button
            onClick={closeNotification}
            style={{
              backgroundColor: 'transparent',
              border: 'none',
              fontSize: '18px',
              color: '#fff',
              cursor: 'pointer',
              fontWeight: 'bold',
              transition: 'color 0.3s',
            }}
            onMouseEnter={(e) => e.target.style.color = '#dc3545'}
            onMouseLeave={(e) => e.target.style.color = '#fff'}
          >
            &times;
          </button>
        </div>
      )}

      <style>
        {`
          @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
          }
        `}
      </style>
    </div>
  );
};