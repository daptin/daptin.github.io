# Marketing content ownership

Each product fact has one marketing page that owns its explanation. Other pages link to that source or use a short example without repeating the full claim.

| Topic | Canonical page | Evidence source |
| --- | --- | --- |
| Product definition, schema-to-runtime mechanism, protocol surface, reliability controls | Home | Tagged Daptin README, server routes, tests, current guides, running server |
| Data APIs, accounts, permissions, files, actions, integrations, live updates | Product | Current Wiki guides, server source, dashboard3 |
| Customer portal, operations, content, authenticated API | Use cases | Product capabilities and linked examples |
| Release version, native artifacts, Docker, Compose, Kubernetes, databases, storage, operations | Deploy | GitHub release API, Docker Hub, daptin deployment files |
| Runnable demos and schema samples | Examples | The linked repositories and their commit history |

Version and artifact claims must be updated on Deploy first. Product capability claims must link to a current guide, source, screenshot, or runnable example.

## Claim verification standard

Marketing copy may make a technical claim only when it is supported by the
release being described. Use the tagged source and its tests for runtime
behavior, the release API and Docker manifest for artifacts, and the linked
demo repository for a demo assertion. Do not promote an inferred behavior to a
product guarantee.

The following boundaries are intentionally explicit on the site:

- An image asset column is `DataType: text` with an explicit image
  `ColumnType` and `cloud_store` foreign-key configuration; bare
  `ColumnType: image` is not a valid example.
- A `/live` system-topic subscription checks table-level `CanPeek` when the
  client subscribes. A client must reconnect after a membership or permission
  change; do not claim immediate revocation for an established subscription.
- WebSocket events use separate `type`, `topic`, and `event` fields. Client
  examples must check those fields rather than inventing a combined event name.

## Editorial voice

- Name the product category and the user outcome directly.
- Use headings that summarize the section. Do not use teaser copy, dramatic fragments, or slogan-like contrasts.
- Explain a standard or protocol through its practical value: existing clients work, familiar tools remain useful, and one component can be replaced without rewriting the rest of the application.
- Prefer concrete nouns, verbs, endpoints, and examples over claims such as "powerful," "seamless," or "future-proof."
- State compatibility limits beside the related capability.
- Do not insert line breaks in headings for dramatic effect. Let the layout wrap the text.
