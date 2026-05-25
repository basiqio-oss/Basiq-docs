---
title: Agent Integration Overview
deprecated: false
hidden: false
icon: fad fa-hand-wave
metadata:
  robots: index
---
# AI Tools

Basiq provides AI-native access to its API and documentation through MCP and LLM-compatible resources.

These tools are designed to help AI assistants understand, integrate, and generate code for the Basiq API without manual documentation lookup.

## Available AI Interfaces

### MCP Server

The Basiq MCP server provides real-time access to Basiq API documentation and functionality.

It enables AI tools to:

- Search and retrieve API documentation
- Understand endpoint schemas and authentication flows
- Generate integration code
- Assist with debugging and implementation

Server URL: [https://api.basiq.io/mcp](https://api.basiq.io/mcp)

### LLM Resources

Basiq provides a lightweight, machine-readable index of its documentation for AI tools.

- [https://api.basiq.io/llms.txt](https://api.basiq.io/llms.txt)

This file is used by AI systems to quickly discover relevant API documentation pages.

## Recommended AI Setup

For best results with AI coding tools:

1. Connect the MCP server
2. Use `llms.txt`for lightweight documentation discovery
3. Refer to API Reference for detailed schemas and examples

## What this enables

With AI tools connected, you can:

- Generate full Basiq integrations from prompts
- Understand authentication and consent flows
- Build webhook handlers automatically
- Debug API issues using live documentation

<br />
