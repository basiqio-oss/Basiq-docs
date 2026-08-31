---
title: May'26 - CDR Insights API Updates
author: Ashman Malik
hidden: false
published_at: '2026-05-06T07:45:14.294Z'
type: added
---
export const Card = ({ children, href, icon, iconColor, target, title, badge }) => {
  const Tag = href ? 'a' : 'div';
  return (
    <Tag
      className={`
        rounded-md border border-gray-200 bg-white shadow-sm p-5 dark:bg-inherit dark:border-white/10
        ${href ? 'no-underline! text-inherit! hover:bg-gray-100 dark:hover:bg-white/10' : ''}
      `}
      href={href}
      target={target}
    >
      <div className="flex items-start justify-between mb-2">
        <div className="flex items-center gap-2">
          {icon && (
            <i className={`text-xl fa-duotone fa-solid ${icon} text-${iconColor}`}></i>
          )}
          {title && (
            <p className="text-gray-800 dark:text-white font-semibold m-0">{title}</p>
          )}
        </div>
        {badge && (
          <span
            className={`text-xs text-white px-2 py-0.5 rounded font-semibold shrink-0 ml-2 ${
              badge === 'Breaking' ? 'bg-red-500' : 'bg-green-600'
            }`}
          >
            {badge}
          </span>
        )}
      </div>
      <div className="text-gray-600 dark:text-gray-300 text-sm">{children}</div>
    </Tag>
  );
};

export const Cards = ({ columns = 2, children }) => {
  return (
    <div
      className={`grid gap-5 ${
        columns <= 1 ? 'grid-cols-1' : `grid-cols-${columns}`
      } max-[414px]:grid-cols-1`}
    >
      {children}
    </div>
  );
};

May 2026 introduces expanded Insights capabilities, including a unified multi-user endpoint, static reference data for Insight types, and a breaking fix to the Balance Verification response structure.

<Cards columns={2}>
  <Card
    title="Create Insight"
    href="https://api.basiq.io/reference/createinsight"
    icon="fa-lightbulb"
    iconColor="green-500"
    badge="New"
    target="_blank"
  >
    The new `POST /insights` endpoint generates an Expense‑to‑Income CDR Insight and supports requests for either a single user or multiple users (1–10). Single‑user requests return an individual insight, while multi‑user requests return an aggregated result.

    - **Endpoint:** `POST /insights`
    - **Supported Types:** `EXPENSE_RATIO_VERIFICATION`, `BALANCE_VERIFICATION`, `ACCOUNT_VERIFICATION`, `IDENTITY_VERIFICATION`, `INCOME_VERIFICATION`
    - **Multi-user:** Multi-user requests (1–10 users) are currently supported only for `EXPENSE_RATIO_VERIFICATION`

    *Use Cases: Generate expense ratio, balance, account, identity, or income verifications across multiple users in a single API call.*
  </Card>

  <Card
    title="List Insight Types"
    href="https://api.basiq.io/reference/getinsighttypes"
    icon="fa-list"
    iconColor="blue-500"
    badge="New"
    target="_blank"
  >
    `GET /insights/types` returns all supported CDR Insight types and the Insight-specific input schema each type expects. Records are pre-seeded per environment and serve as static reference data — no runtime creation or validation occurs.

    - **Endpoint:** `GET /insights/types`
    - **Returns:** `type`, `id`, `name`, `description`, `supportMultipleUsers`, `dataSchema` for each Insight type
    - **Note:** `dataSchema` reflects Insight-specific input only — does not include transport-level fields such as `users` or `type`

    *Use Cases: Discover available Insight types and their required input fields before constructing a `POST /insights` request.*
  </Card>

  <Card
    title="Retrieve Insight Type"
    href="https://api.basiq.io/reference/getinsighttype"
    icon="fa-magnifying-glass"
    iconColor="blue-500"
    badge="New"
    target="_blank"
  >
    `GET /insights/types/{typeId}` returns the definition of a single Insight type by ID. Designed for discoverability and input validation — returns the `dataSchema` for the requested type alongside its metadata.

    - **Endpoint:** `GET /insights/types/{typeId}`
    - **Path Parameter:** `typeId` — one of `ACCOUNT_VERIFICATION`, `BALANCE_VERIFICATION`, `IDENTITY_VERIFICATION`, `INCOME_VERIFICATION`, `EXPENSE_RATIO_VERIFICATION`
    - **Error:** `404` returned for unknown `typeId` values

    *Use Cases: Validate the required input shape for a specific Insight type before submitting a request, or surface type details in a partner-facing UI.*
  </Card>

  <Card
    title="Balance Verification Response Fix"
    href="https://api.basiq.io/reference/getbalanceinsights"
    icon="fa-scale-balanced"
    iconColor="red-500"
    badge="Breaking"
    target="_blank"
  >
    The Balance Verification API response field `accountNumber` has been renamed to `balance`. The previous naming was misleading and caused confusion with Account Verification.

    - **Changed Field:** `accountNumber` → `balance` in `BalanceInsightDataItem` and `AccountBalanceData` schemas
    - **Affected Endpoint:** `GET /users/{userId}/insights/{insightId}` where `insightType` is `balance`

    *Use Cases: Consumers reading balance verification results must update their integration to reference the `balance` field instead of `accountNumber`.*
  </Card>
</Cards>

These updates in May expand Insight generation to support multi-user requests, introduce discoverable reference endpoints for Insight types, and resolve a misleading field name in the Balance Verification response.