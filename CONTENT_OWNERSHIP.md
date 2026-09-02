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

## v0.12.36 claim map

The September 2026 revision was checked against source tag
[`v0.12.36`](https://github.com/daptin/daptin/tree/v0.12.36). This is the
evidence map for every capability family surfaced by the five marketing pages;
it is deliberately a map of claims, not an inventory of unverified ideas.

| Capability family | Evidence used for the site |
| --- | --- |
| Schema, column types, relationships, validation, translations, imports | [Tagged README feature map](https://github.com/daptin/daptin/blob/v0.12.36/README.md) and schema/reference guides in that tag |
| JSON:API, aggregation, GraphQL, OpenAPI, metadata, JS model routes | [Tagged API overview](https://github.com/daptin/daptin/blob/v0.12.36/wiki/API-Overview.md) and README |
| Users, groups, row/relation/action permissions, JWT, OTP, OAuth/OIDC | [Tagged permissions and provider guides](https://github.com/daptin/daptin/tree/v0.12.36/wiki) and server tests |
| Actions, scheduled tasks, state tracking, data exchange | [Tagged README automation boundaries](https://github.com/daptin/daptin/blob/v0.12.36/README.md); state tracking is never described as an action-triggering workflow engine |
| Asset columns, local/cloud stores, sites, templates | [Tagged asset-column and cloud-storage guides](https://github.com/daptin/daptin/tree/v0.12.36/wiki) |
| WebSockets, YJS, feeds, mail, FTP/FTPS, WebDAV-style routes | [Tagged README protocol scope](https://github.com/daptin/daptin/blob/v0.12.36/README.md) and the corresponding protocol guides |
| OpenAPI integrations and OpenAI-compatible LLM routing | [Tagged integration and LLM guides](https://github.com/daptin/daptin/tree/v0.12.36/wiki) plus maintained integration-auth and LLM demos |
| Plans, quotas, credits, rate limits, cluster/runtime operations | [Tagged metering, clustering, and monitoring guides](https://github.com/daptin/daptin/tree/v0.12.36/wiki) plus maintained metering demo |
| Native artifacts and container architecture | GitHub release API and Docker manifest for `v0.12.36` |
| Compose and Kubernetes status | The tagged `docker-compose-examples/daptin-postgres.yml`, empty top-level `docker-compose.yml`, and tagged `kubernetes/` files |

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
- Actions run from HTTP, GraphQL, or scheduled tasks. State tracking validates
  and records allowed transitions; it does not supply entry/exit actions or
  automatically run an action on transition.
- A plan quota is the demonstrated request-denial boundary in the metering
  demo. Credit hooks write ledger records after metering and must not be
  described as a generic prepaid hard limit.
- The historical Kubernetes files and minimal Compose example are not presented
  as production-ready templates. Their exact limitations belong on Deploy.

## Editorial voice

- Name the product category and the user outcome directly.
- Use headings that summarize the section. Do not use teaser copy, dramatic fragments, or slogan-like contrasts.
- Explain a standard or protocol through its practical value: existing clients work, familiar tools remain useful, and one component can be replaced without rewriting the rest of the application.
- Prefer concrete nouns, verbs, endpoints, and examples over claims such as "powerful," "seamless," or "future-proof."
- State compatibility limits beside the related capability.
- Do not insert line breaks in headings for dramatic effect. Let the layout wrap the text.
