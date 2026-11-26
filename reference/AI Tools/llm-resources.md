---
title: LLM Resources
deprecated: false
hidden: false
metadata:
  title: Basiq LLM Resources | AI-Readable API Documentation & llms.txt Guide
  description: >-
    Access Basiq LLM resources designed for AI systems and developers. Use
    llms.txt to discover API documentation, improve integration accuracy, and
    support AI-driven code generation. Learn how it connects with MCP for
    real-time API access.
  keywords:
    - basiq llm resources
    - llms.txt basiq
    - ai readable api documentation
    - basiq api index
    - machine readable api docs
    - ai integration tools
    - llm optimized documentation
    - basiq developer resources
    - open banking api documentation
    - ai api discovery
    - mcp vs llm resources
    - basiq ai developer tools
  robots: index
---
# LLM Resources

Basiq provides machine-readable documentation designed for AI assistants and code generation tools.

These resources help AI systems understand the Basiq API without requiring manual documentation parsing.

## Available Resources

### Documentation Index

[https://api.basiq.io/llms.txt](https://api.basiq.io/llms.txt)

This root index links to one index for each documentation section:

| Index | URL | Contents |
| --- | --- | --- |
| Developer Hub | [https://api.basiq.io/docs/llms.txt](https://api.basiq.io/docs/llms.txt) | Guides for integration, platform capabilities, data, and AI tools |
| API Reference | [https://api.basiq.io/reference/llms.txt](https://api.basiq.io/reference/llms.txt) | API concepts and endpoint documentation, including legacy APIs |
| Changelog | [https://api.basiq.io/changelog/llms.txt](https://api.basiq.io/changelog/llms.txt) | Published product and API release history |

The root index also links to the [changelog feed](https://api.basiq.io/changelog) and lists every published changelog entry under **Changelog entries**.

The Developer Hub and API Reference indexes list every published page in their section, grouped the same way as the documentation navigation. The changelog section index lists only recent entries, so use the root index for the full release history. Where available, links point to the Markdown version of each page (the page URL with a `.md` suffix).

These indexes are designed for AI tools, retrieval systems, and documentation indexing.

## How to use

AI tools can start from the root index and follow the section index that matches their task. For the complete release history, use the changelog entries in the root index. AI tools can use these files to:

* Discover relevant API documentation pages
* Improve integration accuracy
* Reduce hallucinated API calls
* Bootstrap context for code generation

## Relationship to MCP

LLM resources provide static context.

For real-time API interaction, use the MCP server:

[https://api.basiq.io/mcp](https://api.basiq.io/mcp)