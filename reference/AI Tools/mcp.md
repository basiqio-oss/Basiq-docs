---
title: MCP Server
hidden: true
---
# MCP Server

The Basiq Model Context Protocol (MCP) server enables AI coding tools and agents to interact directly with the Basiq API and documentation.

It turns Basiq into an AI-accessible API platform, allowing assistants to search documentation, understand endpoints, and generate working integrations.

## What is MCP?

Model Context Protocol (MCP) is an open standard that allows AI applications to securely access external data sources and tools. The Basiq API MCP server provides AI agents with:

* **Direct API access** to Basiq API functionality
* **Documentation search** capabilities
* **Real-time data** from your Basiq API account
* **Code generation** assistance for Basiq API integrations

## What the Basiq MCP server provides

When connected, AI tools can:

* Search and retrieve Basiq API documentation
* Explore endpoints, schemas, and authentication flows
* Generate production-ready integration code
* Assist with debugging API usage
* Follow multi-step onboarding workflows
* Understand webhook and consent-based data flows

## MCP Server URL

[https://api.basiq.io/mcp](https://api.basiq.io/mcp)

## Basiq API MCP Server Setup

Basiq API hosts a remote MCP server at `https://api.basiq.io/mcp`. Configure your AI development tools to connect to this server. If your APIs require authentication, you can pass in headers via query parameters or however headers are configured in your MCP client.

<Tabs>
  <Tab title="Cursor">
    **Add to`~/.cursor/mcp.json`:**

    ```json
    {
      "mcpServers": {
        "basiq": {
          "url": "https://api.basiq.io/mcp"
        }
      }
    }
    ```
  </Tab>

  <Tab title="Windsurf">
    **Add to`~/.codeium/windsurf/mcp_config.json`:**

    ```json
    {
      "mcpServers": {
        "basiq": {
          "url": "https://api.basiq.io/mcp"
        }
      }
    }
    ```
  </Tab>

  <Tab title="Claude Desktop">
    **Add to`claude_desktop_config.json`:**

    ```json
    {
      "mcpServers": {
        "basiq": {
          "url": "https://api.basiq.io/mcp"
        }
      }
    }
    ```
  </Tab>
</Tabs>

## Testing Your MCP Setup

Once configured, you can test your MCP server connection:

1. **Open your AI editor** (Cursor, Windsurf, etc.)
2. **Start a new chat** with the AI assistant
3. **Ask about Basiq API** - try questions like:
   * "How do I [common use case]?"
   * "Show me an example of [API functionality]"
   * "Create a [integration type] using Basiq API"

The AI should now have access to your Basiq API account data and documentation through the MCP server.

## Relationship to LLM Resources

MCP is a live integration layer.

For lightweight documentation access without a live connection, use:

[https://api.basiq.io/llms.txt](https://api.basiq.io/llms.txt)