<p align="left">
 <img width="100px" src="https://github.com/basiqio/api-ref/assets/102712545/4fae7b18-07c3-406e-aa6c-16cd569e36b8" align="center" alt="API Docs" />
</p>

---

# Features

- **Connect**
- **Platform**
- **Enrich**
- **CDR Insights**
- **Identity**
- **Reporting**
- **Webhooks**

### Changelog
Please check the [changelog](https://api.basiq.io/changelog) for more details on API changes.

---

### How to Contribute
Report an issue: [Issues](https://github.com/basiqio-oss/Basiq-docs/issues/new)

---

### API Documentation

Access comprehensive API documentation for each section:

- **Connect**: [connect.json](./reference/connect.json)
- **Platform**: [platform.json](./reference/platform.json)
- **Enrich**: [enrich.json](./reference/enrich.json)
- **CDR Insights**: [insights.json](./reference/insights.json)
- **Identity**: [identity.json](./reference/identity.json)
- **Reporting**: [reports.json](./reference/reports.json)
- **Webhooks**: [webhooks.json](./reference/webhooks.json)

### AI Tools & Extensions

- **LLMs & AI Integrations**: See [llms.txt](https://api.basiq.io/llms.txt) for information on supported large language models and AI-powered features.
- **MCP (Model Context Protocol)**: Documentation and usage examples for MCP are available in the repo and developer hub.

#### Maintaining the LLM indexes

The Git-managed indexes are `llms.txt` and `docs/llms.txt`,
`reference/llms.txt`, and `changelog/llms.txt`. They cover the public ReadMe
sitemap, including legacy APIs and historical changelog entries. Changelog
content is maintained in ReadMe rather than this repository.

After publishing, add or remove links in the appropriate index to match the
live sitemap. Use the published page title and its `.md` URL; if that endpoint
is broken but the page is accessible, use the canonical HTML URL and recheck
it later. Keep the existing section grouping and avoid duplicate links. The
changelog landing page is excluded because it is not an individual entry.

```sh
python3 scripts/validate_llms.py
python3 scripts/validate_llms.py --check-live
python3 -m unittest discover -s tests -p 'test_validate_llms.py'
```

The first command compares the indexes with the live sitemap; the second also
checks page responses and reports Markdown failures for HTML fallbacks. CI
checks coverage on pull requests, relevant pushes, and weekly; it checks live
responses weekly and when manually dispatched. Since coverage is compared with
the **published** sitemap, publish new or removed pages first, then update the
indexes in a follow-up change. An unavailable sitemap or inaccessible indexed
page fails the check; investigate and retry transient network failures.

To serve these files, connect this repository to ReadMe, then in **AI > AI
Discoverability > Content Discoverability** enable **LLMs.txt** and **Custom
LLMs.txt**. After syncing, verify all four public index URLs. Disabling Custom
LLMs.txt restores ReadMe's generated indexes. See ReadMe's
[AI Discoverability](https://docs.readme.com/main/docs/ai-discoverability)
and [LLMs.txt](https://docs.readme.com/main/docs/llmstxt) documentation.

---

### Documentation Hub

Visit the [Basiq Developer Hub](https://api.basiq.io/reference) for detailed guides, tutorials, and FAQs.

---