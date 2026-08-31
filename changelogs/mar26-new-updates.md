---
title: Mar'26 - New Updates
author: amalik@cuscal.com.au
hidden: false
published_at: '2026-03-26T00:37:18.151Z'
type: improved
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
              badge === 'Breaking'
                ? 'bg-red-500'
                : badge === 'New'
                ? 'bg-green-600'
                : 'bg-blue-500'
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

March 2026 brings extended capabilities for financial data access, webhook monitoring, and granular permissions configuration.

<Cards columns={3}>
  <Card
    title="Auth Links Validity Extended"
    href="https://api.basiq.io/reference/authlinks"
    icon="fa-link"
    iconColor="blue-500"
    badge="Update"
    target="_blank"
  >
    Auth Links now remain valid for 30 days, allowing users to link and share data from multiple accounts across financial institutions within this period. Links expire automatically after 30 days or once users complete the disclosure flow.

    - **Auth Link Expiry:** 30 days or upon disclosure flow completion
    - **Supported Actions:** Link multiple accounts, share data with multiple institutions

    *Use Cases: Enable longer self-service financial data capture, reduce repeated consent requests, and allow multi-account linking in a single window.*
  </Card>

  <Card
    title="Webhook Stats Endpoint"
    href="https://api.basiq.io/reference/getwebhookstats"
    icon="fa-bell"
    iconColor="green-500"
    badge="New"
    target="_blank"
  >
    The new `GET /notifications/webhooks/{webhookId}/stats` endpoint provides real-time monitoring of webhook delivery. Track performance and troubleshoot delivery issues directly through the API.

    - **Endpoint:** `GET /notifications/webhooks/{webhookId}/stats`
    - **Response:** Returns delivery status, success/failure counts, and timestamps

    *Use Cases: Monitor webhook success rates, identify failures, and ensure timely notifications for financial events.*
  </Card>

  <Card
    title="Expanded Permission Sets"
    href="https://api.basiq.io/docs/create-permission-sets"
    icon="fa-shield"
    iconColor="blue-500"
    badge="Update"
    target="_blank"
  >
    Permission sets now support additional endpoints across Events, Merchants, Reports, Users, Enrich, and Webhooks categories, allowing partners to enable or disable access via the Dashboard to prevent unexpected `403` errors.

    - **Events & Jobs:** `GET /events/{eventId}`, `POST /jobs/{jobId}/mfa`
    - **Merchants:** `GET /merchants`, `GET /merchants/{merchantId}`
    - **Reports:** `GET /reports/types/{reportTypeId}`, `DELETE /reports/{reportId}`, `GET /reports/{reportId}/transactions`
    - **Users:** `POST /users/{userId}/connections/{connectionId}/purge`, `GET /users/{userId}/identities`, `POST /users/{userId}/insights/expense-ratio`
    - **Enrich:** `GET/POST /enrich/jobs`, `GET /enrich/jobs/{id}`
    - **Webhooks:** `GET /notifications/webhooks/{webhookId}/stats`

    *Use Cases: Control access to sensitive endpoints, manage user-level permissions, and reduce API errors due to insufficient permissions.*
  </Card>
</Cards>

These updates in March enhance user access, monitoring, and control across Basiq's APIs, giving partners more flexibility and insight into their integrations.