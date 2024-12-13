---
title: Application Setup
excerpt: >-
  Setting up your application within the Basiq Dashboard is an essential first
  step to effectively interact with the Basiq platform. Each application you
  create serves as a unique operational space, where API integrations are
  managed, settings are configured, and user permissions are controlled.
  Importantly, each application also acts as a boundary for the data it handles,
  ensuring data integrity and security.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
### Step 1: Accessing the Dashboard

Start by accessing the Basiq Dashboard at [dashboard.basiq.io](https://dashboard.basiq.io). If you are a new user, you'll need to register first by providing your details. For existing users, simply log in with your credentials. This is your control center for interacting with all of Basiq's services.

### Step 2: Creating a New Application

Once logged in, your next action is to create a new application. This can be done by locating and clicking on the “Create New Application” button in the Dashboard. When naming your application, choose a name that reflects its purpose or the environment it's aligned with. For example, an application intended for a production environment could be named “Home Loans - Production”. You will then choose between two types: the Default Application, suitable for Sandbox or Production environments, and the Business Application, which supports collecting data from businesses under the CDR Business Consumer Consent.

<HTMLBlock>{`
<!--ARCADE EMBED START--><div style="position: relative; padding-bottom: calc(50.215053763440864% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/ER6rQXg5PzsABkg7QOha?embed&embed_mobile=tab&embed_desktop=inline" title="Basiq - Create a New Regular Application" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; color-scheme: light;" ></iframe></div><!--ARCADE EMBED END-->
`}</HTMLBlock>

### Step 3: Configuring Application Settings

After creating your application, you need to configure its settings. This involves specifying whether the application aligns with a specific development environment, like Development, Staging, or Production. If the application is intended for a specific business function or department, name it accordingly, such as “Credit Cards - UAT”. This naming convention aids in better organisation and management of your applications.

## Best Practices and Strategies

When setting up applications in the Basiq Dashboard, it's vital to adopt strategies that align with your organisational structure and operational needs. Here are some best practices and additional points to consider:

* **Reflect Development Environments**: Create separate applications for different stages of your development lifecycle - Development, Staging, and Production. This approach helps in isolating data and functionalities based on the application's current stage and usage.

* **Align with Business Functions**: For organisations with multiple departments or varied use cases, consider creating applications specific to each function. This segregation ensures that the data and functionalities of each department do not overlap, maintaining data integrity and focus.

<div
  style={{
    border: "2px solid #4e9ccf", // Classic blue border
    borderRadius: "8px",
    backgroundColor: "#e3f2fd", // Light blue background (cascade effect)
    padding: "16px",
    margin: "16px 0",
    fontFamily: "Arial, sans-serif",
    color: "#333", // Dark text for readability
  }}
>
  <strong style={{ color: "#1e88e5" }}>📢 Attention!</strong> If you have any issues, please reach out to our amazing support team.

  <div style={{ display: 'flex', alignItems: 'center' }}>
    <button
      onClick={() => Intercom('showNewMessage', 'issues on FAQs:')}
      style={{
        padding: '12px 30px',
        backgroundColor: '#1e88e5', // Classic blue button color
        color: '#ffffff',
        border: 'none',
        borderRadius: '50px',
        fontSize: '16px',
        fontWeight: '600',
        textTransform: 'uppercase',
        cursor: 'pointer',
        boxShadow: '0 4px 10px rgba(30, 136, 229, 0.2)', // Soft blue shadow
        transition: 'background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease',
        outline: 'none',
        display: 'flex',
        justifyContent: 'center',
        height: '45px',
        position: 'relative',
        overflow: 'hidden',
        marginLeft: '10px', // Add space between text and button
        minWidth: '150px', // Ensure the button has enough width for the text
      }}
      onMouseEnter={(e) => {
        e.target.style.transform = 'scale(1.1)';
        e.target.style.boxShadow = '0 6px 15px'; // Darker shadow on hover
        e.target.style.backgroundColor = '#1565c0'; // Darker blue on hover
      }}
      onMouseLeave={(e) => {
        e.target.style.transform = 'scale(1)';
        e.target.style.boxShadow = '0 4px 10px';
        e.target.style.backgroundColor = '#1e88e5'; // Original blue
      }}
    >
      Support team
    </button>
  </div>
</div>