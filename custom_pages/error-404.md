---
title: Page Not Found
fullscreen: false
hidden: false
---
export const meta = {
  title: "404 - Page Not Found",
};

<div
  style={{
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  justifyContent: 'center',
  minHeight: '100vh',
  textAlign: 'center',
  backgroundColor: '#f9fafb',
  padding: '2rem'
}}
>
  <h1 style={{ fontSize: '8rem', color: '#f56565', margin: 0 }}>404</h1>

  <h2 style={{ fontSize: '2rem', color: '#2d3748', margin: '1rem 0' }}>
    Page Not Found
  </h2>

  <p style={{ fontSize: '1.25rem', color: '#4a5568', maxWidth: '400px', margin: '0 auto' }}>
    Oops! The page you are looking for doesn’t exist or has been moved.
  </p>

  <a
    href="/"
    style={{
      marginTop: '2rem',
      padding: '0.75rem 1.5rem',
      backgroundColor: '#3182ce',
      color: '#fff',
      borderRadius: '0.375rem',
      textDecoration: 'none',
      fontWeight: 'bold'
    }}
  >
    Go Back Home
  </a>
</div>