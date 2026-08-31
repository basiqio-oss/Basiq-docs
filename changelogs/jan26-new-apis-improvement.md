---
title: Jan'26 - New API's & Improvement
author: Ashman Malik
hidden: false
published_at: '2026-01-27T03:06:56.955Z'
type: added
---
import React from 'react';

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

Starting off 2026 with powerful new features! This month, we have released the Payees API and Expense Ratio Insights to give you more control over payee management and financial analysis.

<Cards columns={2}>
  <Card
    title="Payees API"
    href="https://api.basiq.io/reference/payees"
    icon="fa-users"
    iconColor="green-500"
    badge="New"
    target="_blank"
  >
    Manage and retrieve payee information with support for multiple payee types including domestic, biller, international, and digital wallet payments. List all payees with advanced filtering and pagination.

    - **`GET /users/{userId}/payees`:** List all payees with pagination and filtering support
    - **`GET /users/{userId}/payees/{payeeId}`:** Get detailed payee information by payee ID
    - **Query Parameters:** `limit` (1–500), filter by `type`, `connectionId`, or created date

    *Use Cases: Retrieve all domestic payees, filter payees by connection, or get detailed information for a specific payee including bank details.*
  </Card>

  <Card
    title="Expense Ratio Insights"
    href="https://api.basiq.io/reference/getexpenseratioinsights"
    icon="fa-chart-pie"
    iconColor="green-500"
    badge="New"
    target="_blank"
  >
    Analyse spending patterns and expense distribution across categories. Get insights into how much users are spending on different expense categories relative to their income.

    - **Body Params:** Period and category filters for expense analysis
    - **`expense` object:** Configuration for expense ratio calculation and filtering
    - **Response:** Returns expense breakdown by category with ratio percentages

    *Use Cases: Analyze expense ratios for budgeting applications, identify spending trends, or provide personalized financial recommendations based on expense categories.*
  </Card>
</Cards>

Welcome to 2026! We're excited to empower your applications with better payee management and financial insights.