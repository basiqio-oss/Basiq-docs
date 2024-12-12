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

import { useState, useEffect } from 'react';

<div style={{ margin: '20px 0' }}>
  <ModalDemo />
</div>

export const ModalDemo = () => {
  const [isOpen, setIsOpen] = useState(false);

  // Open the modal automatically when the page loads
  useEffect(() => {
    setIsOpen(true);  // Modal opens on page load

    const handleEscape = (event) => {
      if (event.key === 'Escape') {
        setIsOpen(false);
      }
    };
    window.addEventListener('keydown', handleEscape);

    // Cleanup event listener on component unmount
    return () => window.removeEventListener('keydown', handleEscape);
  }, []); // Empty dependency array ensures this runs only once on mount

  const toggleModal = () => setIsOpen(!isOpen);

  return (
    <div>
      <button
        onClick={toggleModal}
        style={{
          padding: '12px 20px',
          fontSize: '16px',
          backgroundColor: '#007BFF',
          color: '#fff',
          border: 'none',
          borderRadius: '8px',
          cursor: 'pointer',
          marginTop: '20px',
          transition: 'background-color 0.3s',
        }}
        onMouseEnter={(e) => e.target.style.backgroundColor = '#0056b3'}
        onMouseLeave={(e) => e.target.style.backgroundColor = '#007BFF'}
      >
        Open Modal
      </button>

      {isOpen && (
        <div
          style={{
            position: 'fixed',
            top: '0',
            left: '0',
            width: '100vw',
            height: '100vh',
            backgroundColor: 'rgba(0, 0, 0, 0.7)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            animation: 'fadeIn 0.3s',
            zIndex: '1000',
          }}
          onClick={toggleModal}
        >
          <div
            style={{
              backgroundColor: '#fff',
              padding: '30px',
              borderRadius: '12px',
              boxShadow: '0 8px 16px rgba(0, 0, 0, 0.2)',
              minWidth: '600px',
              minHeight: '400px',
              textAlign: 'center',
              animation: 'slideIn 0.4s',
              overflow: 'hidden',
              position: 'relative', // Positioning context for the close button
            }}
            onClick={(e) => e.stopPropagation()}
          >
            {/* Cross Button in the Top Right Corner */}
            <button
              onClick={toggleModal}
              style={{
                position: 'absolute',
                top: '10px',
                right: '10px',
                backgroundColor: 'transparent',
                border: 'none',
                fontSize: '24px',
                color: '#333',
                cursor: 'pointer',
                fontWeight: 'bold',
                transition: 'color 0.3s',
              }}
              onMouseEnter={(e) => e.target.style.color = '#dc3545'}
              onMouseLeave={(e) => e.target.style.color = '#333'}
            >
              &times;
            </button>

            <h2 style={{ marginBottom: '20px' }}>Raintank Dashboard Snapshot</h2>
            <p style={{ fontSize: '14px', marginBottom: '20px' }}>
              This is a modal with an embedded Raintank Dashboard snapshot. You can close it by clicking outside or using the cross button.
            </p>

            {/* Iframe Embedding */}
            <div
              style={{
                position: 'relative',
                paddingBottom: 'calc(54.55861070911722% + 41px)', // Aspect ratio (height / width)
                height: '0',
                width: '100%',
                borderRadius: '8px',
                overflow: 'hidden', // Prevent scrolling within the container
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
                scrolling="no"  // Disable scrolling inside the iframe
                style={{
                  position: 'absolute',
                  top: '0',
                  left: '0',
                  width: '100%',
                  height: '100%',
                  colorScheme: 'light',
                  borderRadius: '8px',
                  overflow: 'hidden', // Prevent internal scrollbars
                }}
              ></iframe>
            </div>
          </div>
        </div>
      )}

      <style>
        {`
          @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
          }
          @keyframes slideIn {
            from { transform: translateY(-50px); }
            to { transform: translateY(0); }
          }
        `}
      </style>
    </div>
  );
};