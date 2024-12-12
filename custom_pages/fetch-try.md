---
title: Animated
fullscreen: false
hidden: true
---
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
          transition: 'background-color 0.3s, transform 0.2s',
        }}
        onMouseEnter={(e) => e.target.style.backgroundColor = '#0056b3'}
        onMouseLeave={(e) => e.target.style.backgroundColor = '#007BFF'}
        onMouseDown={(e) => e.target.style.transform = 'scale(0.98)'}
        onMouseUp={(e) => e.target.style.transform = 'scale(1)'}
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
            animation: 'fadeIn 0.5s ease-out',
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
              animation: 'slideIn 0.4s ease-out, scaleUp 0.4s ease-out',
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

            <h2 style={{ marginBottom: '20px' }}>Modal with Iframe</h2>
            <p style={{ fontSize: '14px', marginBottom: '20px' }}>
              This is a modal with an embedded iframe. You can close it by clicking outside or using the cross button.
            </p>

            {/* Iframe Embedding */}
            <div
              style={{
                position: 'relative',
                paddingBottom: 'calc(54.55861070911722% + 41px)',
                height: '0',
                width: '100%',
                borderRadius: '8px',
                overflow: 'hidden',
              }}
            >
              <iframe
                src="https://demo.arcade.software/zTaAEuzoNYTom6qJRvat?embed"
                title="Basiq Dashboard | Activate your Account"
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
                  colorScheme: 'light',
                  borderRadius: '8px',
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
          @keyframes scaleUp {
            from { transform: scale(0.9); }
            to { transform: scale(1); }
          }
        `}
      </style>
    </div>
  );
};