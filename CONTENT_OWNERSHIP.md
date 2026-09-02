# Marketing content ownership

Each product fact has one marketing page that owns its explanation. Other pages link to that source or use a short example without repeating the full claim.

| Topic | Canonical page | Evidence source |
| --- | --- | --- |
| Product definition, primary value proposition, schema-to-runtime mechanism | Home | Tagged Daptin README, server routes, tests, current guides, running server |
| Data APIs, accounts, permissions, files, actions, integrations, live updates | Product | Local implementation guides, latest-release source, tests, dashboard3 |
| Buyer-oriented map of all capability families and how they fit together | Feature map | Product evidence map below; detailed configuration lives under `docs/` |
| Buyer-oriented explanation, use cases, and boundaries for an individual capability | The corresponding page under `features/` | Latest-release implementation, tests, and its local guide |
| Invisible backend engineering: identity, integrity, transactions, request and resource controls, lifecycle | Engineering | Tagged source, focused tests, authoritative backend and security standards |
| Customer portal, operations, content, authenticated API | Use cases | Product capabilities and linked examples |
| Release version, native artifacts, Docker, Compose, Kubernetes, databases, storage, operations | Deploy | GitHub release API, Docker Hub, daptin deployment files |
| Runnable demos and schema samples | Examples | The linked repositories and their commit history |

Version and artifact claims must be updated on Deploy first. Product capability claims must link to a current guide, source, screenshot, or runnable example.

## Latest-release claim map

Each revision must first resolve GitHub’s current latest release and check claims against that release’s source, artifacts, tests, and notes. Do not hard-code the resolved version into public copy. This is the
evidence map for every capability family surfaced by the five marketing pages;
it is deliberately a map of claims, not an inventory of unverified ideas.

| Capability family | Evidence used for the site |
| --- | --- |
| Schema, column types, relationships, validation, translations, imports | [`docs/data-modeling/`](docs/data-modeling/) plus the latest-release schema implementation and tests |
| JSON:API, aggregation, GraphQL, OpenAPI, metadata, JS model routes | [`docs/apis/`](docs/apis/) and [`docs/graphql/`](docs/graphql/) plus latest-release route tests |
| Users, groups, row/relation/action permissions, JWT, OTP, OAuth/OIDC | [`docs/authentication/`](docs/authentication/), [`docs/permissions/`](docs/permissions/), and [`docs/oauth-provider/`](docs/oauth-provider/) plus latest-release tests |
| Actions, scheduled tasks, state tracking, data exchange | [`docs/actions/`](docs/actions/), [`docs/scheduled-work/`](docs/scheduled-work/), and [`docs/state-tracking/`](docs/state-tracking/); state tracking is never described as an action-triggering workflow engine |
| Asset columns, local/cloud stores, sites, templates | [`docs/files/`](docs/files/), [`docs/cloud-storage/`](docs/cloud-storage/), and [`docs/sites/`](docs/sites/) plus latest-release implementation |
| WebSockets, YJS, feeds, mail, FTP/FTPS, WebDAV-style routes | [`docs/realtime/`](docs/realtime/), [`docs/collaboration/`](docs/collaboration/), [`docs/mail/`](docs/mail/), and [`docs/protocols/`](docs/protocols/) plus latest-release protocol tests |
| OpenAPI integrations and OpenAI-compatible LLM routing | [`docs/integrations/`](docs/integrations/) and [`docs/ai-routing/`](docs/ai-routing/) plus maintained integration-auth and LLM demos |
| Plans, quotas, credits, rate limits, cluster/runtime operations | [`docs/metering/`](docs/metering/) and [`docs/operations/`](docs/operations/) plus the maintained metering demo |
| Invisible data/runtime engineering claims | [`ENGINEERING_BENEFITS_AUDIT.md`](ENGINEERING_BENEFITS_AUDIT.md), then the latest-release implementation and focused tests; the audit is an internal evidence map, not public navigation |
| Native artifacts and container architecture | GitHub release API and Docker manifest for the latest release |
| Compose and Kubernetes status | The tagged `docker-compose-examples/daptin-postgres.yml`, empty top-level `docker-compose.yml`, and tagged `kubernetes/` files |

## Claim verification standard

Marketing copy may make a technical claim only when it is supported by the
release being described. Use the tagged source and its tests for runtime
behavior, the release API and Docker manifest for artifacts, and the linked
demo repository for a demo assertion. Do not promote an inferred behavior to a
product guarantee.

Security and reliability copy describes the mechanism and its scope. It does
not turn a useful defense into an absolute guarantee: parameterized query
values are not described as proof that SQL injection is impossible, database
transactions do not cover external side effects, and retryable delivery is not
called exactly-once delivery.

The following boundaries are intentionally explicit on the site:

- An image asset column is `DataType: text` with an explicit image
  `ColumnType` and `cloud_store` foreign-key configuration; bare
  `ColumnType: image` is not a valid example.
- A `/live` system-topic subscription checks table-level `CanPeek` when the
  client subscribes. A client must reconnect after a membership or permission
  change; do not claim immediate revocation for an established subscription.
- WebSocket events use separate `type`, `topic`, and `event` fields. Client
  examples must check those fields rather than inventing a combined event name.
- The asset endpoint checks permissions before serving a file. Do not promise
  that non-owner asset access has been verified universally; instruct operators
  to test that boundary in their deployment before storing sensitive files.
- Actions run from HTTP, GraphQL, or scheduled tasks. State tracking validates
  and records allowed transitions; it does not supply entry/exit actions or
  automatically run an action on transition.
- A plan quota is the demonstrated request-denial boundary in the metering
  demo. Credit hooks write ledger records after metering and must not be
  described as a generic prepaid hard limit.
- The historical Kubernetes files and minimal Compose example are not presented
  as production-ready templates. Release-scoped pages must not label newer,
  untagged Kubernetes work as a latest-release feature.

## Editorial voice

- Name the product category and the user outcome directly.
- Use headings that summarize the section. Do not use teaser copy, dramatic fragments, or slogan-like contrasts.
- Explain a standard or protocol through its practical value: existing clients work, familiar tools remain useful, and one component can be replaced without rewriting the rest of the application.
- Prefer concrete nouns, verbs, endpoints, and examples over claims such as "powerful," "seamless," or "future-proof."
- State compatibility limits beside the related capability.
- Do not insert line breaks in headings for dramatic effect. Let the layout wrap the text.
