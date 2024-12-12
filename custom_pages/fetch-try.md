---
title: Fetch Try
fullscreen: false
hidden: true
---
import { useState, useEffect } from 'react';

// Function to fetch RSS feed
const fetchRSS = async () => {
  const response = await fetch('https://api.basiq.io/changelog.rss');
  const data = await response.text();
  const parser = new DOMParser();
  const xmlDoc = parser.parseFromString(data, 'application/xml');
  const items = xmlDoc.querySelectorAll('item');
  return items.length ? items[0] : null;
};

export const NotificationDemo = () => {
  const [isNotificationVisible, setIsNotificationVisible] = useState(false);
  const [latestFeedItem, setLatestFeedItem] = useState(null);
  const [lastFeedItemTitle, setLastFeedItemTitle] = useState(null);

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

  useEffect(() => {
    const checkForNewFeed = async () => {
      const latestItem = await fetchRSS();

      if (latestItem) {
        const title = latestItem.querySelector('title').textContent;

        // Compare with previous feed item to check if it's new
        if (title !== lastFeedItemTitle) {
          setLatestFeedItem(latestItem);
          setIsNotificationVisible(true);
          setLastFeedItemTitle(title);
        }
      }
    };

    // Check for new feed every 30 seconds
    const intervalId = setInterval(checkForNewFeed, 30000);
    
    // Initial check
    checkForNewFeed();

    // Cleanup the interval on component unmount
    return () => clearInterval(intervalId);
  }, [lastFeedItemTitle]);

  const closeNotification = () => setIsNotificationVisible(false);

  return (
    <div>
      {isNotificationVisible && latestFeedItem && (
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
            New Update: {latestFeedItem.querySelector('title').textContent}
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
