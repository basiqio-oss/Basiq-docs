---
title: Activate Account
deprecated: false
hidden: true
metadata:
  robots: index
---
<Tab title="Data Storage Best Practices">
  <div className="data-storage-container">
    <div className="data-storage-card">
      <h3 className="data-storage-title">Secure Data Storage</h3>

      <p className="data-storage-description">
        Partners should implement a secure data storage system for storing necessary user information. Ensure that sensitive data is encrypted and access is restricted to authorized personnel only.
      </p>
    </div>

    <div className="data-storage-card">
      <h3 className="data-storage-title">API Call Efficiency</h3>

      <p className="data-storage-description">
        API calls should only be made when absolutely necessary to fetch updated information. Minimizing unnecessary calls reduces load on the system and improves performance for all users.
      </p>
    </div>

    <div className="data-storage-card">
      <h3 className="data-storage-title">Storage Limitations</h3>

      <p className="data-storage-description">
        Note that Basiq is not an information storage service. Use Basiq’s data as an intermediate layer for processing, and store finalized data securely within your own system.
      </p>
    </div>
  </div>
</Tab>

<style jsx>
  {`
    .data-storage-container {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 20px;
      padding: 20px;
    }

    .data-storage-card {
      background-color: #f4f8fa;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      transition: transform 0.3s ease;
    }

    .data-storage-card:hover {
      transform: translateY(-5px);
    }

    .data-storage-title {
      font-size: 1.2em;
      color: #333;
      margin-bottom: 12px;
    }

    .data-storage-description {
      font-size: 1em;
      color: #555;
      line-height: 1.6;
    }
  `}
</style>