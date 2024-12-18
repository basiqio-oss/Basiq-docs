---
title: Create Permission Sets
excerpt: >-
  Permission Sets in the Basiq Dashboard are essential tools for ensuring
  security and operational efficiency. These sets allow you to control access to
  various features and data within the platform, making sure team members have
  access aligned with their roles.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
### Step 1: Accessing Permission Sets

To begin, log in to the Basiq Dashboard and navigate to the 'Settings' tab. Here, you will find the 'Permission Sets' option, which is your gateway to managing access controls.

### Step 2: Creating a New Permission Set

Click on 'New Permission Set' to start creating a new set. Assign a descriptive name that clearly identifies the set's purpose. This name is crucial for easy management and recognition of the set's role.

### Step 3: Assigning Permissions

In this step, you select the specific API endpoints that the permission set will have access to. These endpoints typically include Get, Post, and Delete requests. For example, by selecting 'Delete user', the permission set is endowed with the capability to remove users from the system. This method of assigning permissions ensures that each set can be finely tuned to the exact needs of its role, providing a tailored and secure user experience.

### Step 4: Saving and Activating Permission Sets

Once you have configured your permission sets, save your changes to activate them. These sets become effective immediately, enforcing the defined access controls without delay.

<HTMLBlock>{`
<div style="position: relative; padding-bottom: calc(54.55861070911722% + 41px); height: 0; width: 100%;"><iframe src="https://demo.arcade.software/MEJ9MaJ3rrO40syZmn4Z?embed" title="Basiq - Permissions Sets" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;"></iframe></div>
`}</HTMLBlock>

## Best Practices

* **Adhere to Least Privilege**: Ensure that each role or API key is granted only the permissions necessary for its function.
* **Conduct Regular Audits**: Regularly review your permission sets to ensure they align with evolving roles and responsibilities.
* **Use Clear Naming Conventions**: Choose descriptive names for your permission sets to facilitate easy identification and management.
* **Role Specificity**: Design permission sets that are specific to the roles in your organization. Avoid one-size-fits-all approaches, as they can lead to over-privileging or under-privileging.
* **Segregate Duties**: Where possible, distribute permissions among roles to prevent any single role from having excessive access, reducing risks of misuse.
* **Update with Organizational Changes**: Modify permission sets in tandem with any changes in organizational structure or roles to maintain appropriate access levels.

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
        e.target.style.backgroundColor = '#1565c0'; // Darker blue on hover
      }}
      onMouseLeave={(e) => {
        e.target.style.transform = 'scale(1)';
        e.target.style.backgroundColor = '#1e88e5'; // Original blue
      }}
    >
      Support team
    </button>
  </div>
</div>