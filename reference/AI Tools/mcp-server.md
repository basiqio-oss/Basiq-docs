---
title: MCP Server
hidden: true
---
# MCP Server

The Basiq MCP server gives your AI assistant direct access to Basiq API documentation, endpoint references, schemas, and live API capabilities. It works with any editor or tool that supports Model Context Protocol (MCP), including Cursor, Claude Desktop, Windsurf, VS Code Copilot, and other MCP-compatible clients.

## What your AI assistant can do once connected

Once connected to the Basiq MCP server, your AI assistant can:

* Search and retrieve Basiq API documentation
* Explore API endpoints, request schemas, and authentication flows
* Generate production-ready integration code
* Assist with debugging API usage and responses
* Understand consent-based financial data workflows
* Work with webhook integrations and event handling
* Follow onboarding and multi-step integration flows
* Access enabled API routes exposed through your Basiq dashboard
* Execute API requests directly against enabled endpoints

## What is MCP?

Model Context Protocol (MCP) is an open standard that allows AI applications to securely connect with external APIs, documentation systems, and developer tools.

The Basiq MCP server turns Basiq into an AI-accessible API platform by giving AI coding assistants structured access to:

* API documentation
* Endpoint definitions
* Authentication details
* Request and response schemas
* Search and retrieval tools
* Real-time API interactions

This enables AI tools to understand and work with the Basiq API more accurately and efficiently.

## Server URL

```txt SERVER
https://api.basiq.io/mcp
```

# Setup

## Cursor

Add to your `.cursor/mcp.json` file:

```json
{
  "mcpServers": {
    "basiq": {
      "url": "https://api.basiq.io/mcp"
    }
  }
}
```

Restart Cursor to apply changes.

## Claude Desktop

Add to your Claude Desktop config file:

### macOS & Windows

```txt macOS
~/Library/Application Support/Claude/claude_desktop_config.json
```
```Text Windows
%APPDATA%\Claude\claude_desktop_config.json
```

Add:

```json
{
  "mcpServers": {
    "basiq": {
      "url": "https://api.basiq.io/mcp"
    }
  }
}
```

Restart Claude Desktop to apply changes.

## Windsurf

Add to:

```txt
~/.codeium/windsurf/mcp_config.json
```

```json
{
  "mcpServers": {
    "basiq": {
      "url": "https://api.basiq.io/mcp"
    }
  }
}
```

Restart Windsurf to apply changes.

## VS Code Copilot

Add to `.vscode/mcp.json` in your workspace.

You can also use the `MCP: Open User Configuration` command for a global setup.

```json
{
  "servers": {
    "basiq": {
      "type": "http",
      "url": "https://api.basiq.io/mcp"
    }
  }
}
```

VS Code uses a `servers` key instead of `mcpServers` and requires `"type": "http"` for remote MCP servers.

Restart VS Code after making changes.

## Other MCP Clients

Any MCP-compatible client can connect using the server URL above.

Consult your client’s documentation for MCP configuration instructions.

# Authentication

If your Basiq APIs require authentication, you can provide authentication headers through your MCP client configuration.

The exact configuration method depends on the MCP client you are using.

Common approaches include:

* Custom request headers
* Environment variables
* Query parameter configuration
* Client-specific authentication settings

Refer to your MCP client documentation for details.

# Testing Your MCP Setup

Once configured:

1. Open your AI editor or MCP-enabled application
2. Start a new AI chat session
3. Ask questions about the Basiq API

Example prompts:

* “How do I create a user in Basiq?”
* “Show me an example of connecting a bank account”
* “Generate a webhook handler for Basiq”
* “Create a transaction sync workflow using Basiq”
* “Explain how consent-based data access works”

If connected successfully, your AI assistant will be able to access Basiq documentation and enabled MCP tools.

# Built-in MCP Tools

The Basiq MCP server includes built-in tools that AI assistants can use to search documentation, inspect endpoints, and interact with APIs.

## list-endpoints

List all available API endpoints exposed through the MCP server.

Useful for:

* Discovering available routes
* Exploring API categories
* Understanding integration surface areas

Example prompts:

* “List all available Basiq endpoints”
* “Show me all identity endpoints”
* “What API routes are available?”

## get-endpoint

Retrieve detailed information for a specific endpoint.

Returns:

* HTTP method
* Endpoint path
* Parameters
* Request schema
* Response schema
* Authentication requirements

Example prompts:

* “Get details for the users endpoint”
* “Show me the schema for transaction retrieval”
* “Explain the connect endpoint”

## execute-request

Execute requests directly against enabled Basiq API endpoints.

Useful for:

* Testing integrations
* Validating requests
* Inspecting live responses
* Debugging workflows

Example prompts:

* “Execute a request to retrieve transactions”
* “Test the accounts endpoint”
* “Call the identity verification endpoint”

## search-endpoints

Search endpoints using keywords, categories, or functionality.

Example prompts:

* “Search endpoints related to webhooks”
* “Find transaction-related endpoints”
* “Search for authentication APIs”

## list-specs

List available API specifications exposed through the MCP server.

Useful for:

* Discovering API definitions
* Understanding available schemas
* Reviewing supported services

Example prompts:

* “List available API specs”
* “Show all specification files”
* “What API specs are exposed?”

## fetch

Retrieve documentation pages or specification content directly.

Useful for:

* Getting full documentation content
* Reviewing schemas
* Accessing integration details

Example prompts:

* “Fetch the webhook documentation”
* “Retrieve the identity API docs”
* “Get the reporting API specification”

## search

Full-text search across Basiq documentation and API references.

Searches:

* Documentation pages
* Endpoint descriptions
* Schema definitions
* Integration guides

Example prompts:

* “Search for webhook verification”
* “Find transaction sync documentation”
* “Search for consent management”

# Custom MCP Tools

Basiq also supports custom MCP tools that can be defined and exposed to AI assistants.

Custom tools allow you to:

* Create organization-specific workflows
* Expose internal business logic
* Automate repetitive actions
* Extend AI functionality beyond standard API access

These tools can be managed directly from the Basiq dashboard.

# Enabled MCP Routes

The Basiq dashboard allows you to control which API routes are exposed through MCP.

By default, all routes are enabled.

Available route groups include:

* `affordability.json`
* `analytics.json`
* `connect.json`
* `enrich.json`
* `identity.json`
* `insights.json`
* `payees.json`
* `platform.json`
* `reporting.json`
* `webhooks.json`

This allows you to limit AI access to only the APIs relevant to your environment or use case.

# Relationship to LLM Resources

The MCP server provides a live integration layer for AI tools.

For lightweight documentation access without MCP connectivity, Basiq also provides LLM-friendly resources.

## llms.txt

```txt
https://api.basiq.io/llms.txt
```

Provides a lightweight index of documentation content optimized for AI systems.

# Usage Tips

## Start with search

Ask your AI assistant to search documentation before requesting implementation details.

Example:

```txt
Search Basiq docs for webhook handling
```

## Explore endpoints first

Use endpoint listing tools to understand available APIs before building integrations.

Example:

```txt
List all connect API endpoints
```

## Fetch detailed schemas

Retrieve full endpoint details when implementing requests or validating responses.

Example:

```txt
Get endpoint details for transaction retrieval
```

## Use execute-request for testing

Validate requests and inspect real responses directly through MCP.

Example:

```txt
Execute a request against the accounts endpoint
```

## Combine with custom tools

Custom MCP tools can extend Basiq integrations with organization-specific workflows and automation.

# Troubleshooting

## Connection Issues

If your MCP client cannot connect:

* Verify the server URL is exactly:

```txt
https://api.basiq.io/mcp
```

* Restart your AI editor after configuration changes
* Ensure outbound HTTPS connections are allowed
* Confirm your MCP configuration file syntax is valid

## Authentication Problems

If authenticated requests fail:

* Verify API credentials are configured correctly
* Ensure authentication headers are being passed properly
* Confirm your MCP client supports authenticated remote MCP servers

## No Results or Missing Endpoints

If searches or endpoint listings return incomplete results:

* Try broader search terms
* Verify the route group is enabled in the dashboard
* Confirm your environment has access to the requested APIs

## MCP Tool Access

Some MCP features may require upgraded Ask AI plans or additional dashboard configuration.

Available enhancements may include:

* Increased usage limits
* Additional MCP tools
* Custom AI behavior
* Advanced AI integrations
* Ask AI API access

# Security

The Basiq MCP server supports secure AI access to documentation and enabled APIs.

Access can be controlled through:

* MCP route enablement
* Authentication configuration
* API permission scopes
* Dashboard-level controls

Only enabled routes and authorized API functionality are exposed through the MCP server.
