---
title: Institutions EP to Connectors EP
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
# Introduction

This guide is designed to assist you in migrating from the [Institutions Endpoint](https://api.basiq.io/v2.0/reference/institutions) (EP) to the [Connectors Endpoint](https://api.basiq.io/reference/getconnectors) (EP) in our API. We've introduced the Connectors EP to provide enhanced features and greater compatibility (supporting both versions 2.x and 3.x of our API). This guide will take you through the key differences and the necessary steps to transition smoothly to Connectors EP.

## Understanding the Schema Differences

First, let's understand the key differences in the schema of both endpoints:

### Institutions EP Schema (version 2.x):

Primarily focused on financial institutions like banks and credit unions.\
Attributes include `type`, `id`, `name`, `type`, `country`, `authorization`, and several others.

### Connectors EP Schema (versions 2.x and 3.x):

More comprehensive and detailed, offering extended functionality.\
Includes attributes like `authorization`, `id`, `institution`, `links`, `method`, `scopes`, `stage`, `stats`, `status`, and `type`.

## Updated Usage of the institution Field

The `institution` field in the `/accounts`, `/transactions`, and `/connections` EPs will maintain its label but will undergo a significant change in terms of functionality. From the deprecation date, the links within the institution field will begin pointing to the specific method in the Connectors EP, enhancing the integration and data consistency.

### Example

#### Old Structure:

```curl json
"links": {
    "self": "https://au-api.basiq.io/institutions/AU00601"
}
```

#### New Structure:

```curl json
"links": {
    "self": "https://au-api.basiq.io/connectors/AU00601"
}
```

# Step-by-Step Migration Process

### Mapping Institution Attributes to Connector Attributes:

* **type, id, name, country:** These attributes remain largely the same. Ensure they are mapped directly.
* **authorization:** This has become more detailed in Connectors EP. You'll need to align your current authorization mechanism with the new format.
* **logo, links, stats:** These attributes have similar functionalities but with extended capabilities in Connectors EP. Pay special attention to their new structures.
* For `/accounts`, `/transactions`, and `/connections` EPs: Update the institution field links to point to the Connectors EP. Ensure that these links accurately reflect the corresponding method in the Connectors EP.

### Updating Authorization Mechanisms:

* If you are using `user`, `user-token`, `user-mfa`, or `user-mfa-intermittent` in `Institutions` EP, review the new authorization object structure in Connectors EP. Adjust your code to accommodate the changes.

### Handling New and Modified Fields:

* Fields like `method`, `scopes`, `stage`, and `status` are new in Connectors EP. Understand their purpose and integrate them into your system as needed.
* Pay attention to `stats` and `institution` objects, as they have undergone significant changes.

### Adapting to Enhanced Security Features:

* Connectors EP may have enhanced security features (like MFA challenges). Ensure your application can handle these.

### Testing Your Implementation:

* Thoroughly test your updated application against the Connectors EP.
* Verify that all data is correctly mapped and all functionalities are working as expected.

### Migration of Existing Data:

* Migrate your existing data to align with the Connectors EP schema.
* This may involve transforming data formats and values.

### Final Validation and Go-Live:

After successful testing, validate the entire process with a subset of real users if possible.\
Once validated, you can fully transition to using Connectors EP.

### Breaking Changes and Special Attention

* **Breaking Change in Authorization:** The new `authorization` structure in Connectors EP is a significant change. Ensure your system's authentication and authorization mechanisms are compatible with this new structure.
* **Attention to New Fields:** Fields like `method` and `scopes` are new in Connectors EP. Understand their implications for your application and integrate them accordingly.

# Conclusion

Migrating to Connectors EP will bring enhanced features and better compatibility with future versions of our API. Follow this guide carefully to ensure a smooth transition. For any assistance or clarification, please reach out to our support team.
