# Platform, open source, ecosystem, and evaluation page plan

Plan date: 2026-09-02

## Shared editorial strategy

The four routes answer different questions in one evaluation journey. They use the existing visual system, short factual headings, dense tables, linked evidence, explicit boundaries, and a next-step path. Claims are grounded in the latest Daptin release available during research (`v0.12.36`), the local release source, current public repository metadata, the project's policy files, and the GNU LGPL-3.0 text. Public copy avoids pinning a version so it does not become stale.

Every page must:

- identify its decision job in the first viewport;
- link claims to implementation guides, source, releases, or runnable proof;
- distinguish released behavior from operator responsibility;
- avoid absolutes about security, compatibility, scalability, or licensing;
- provide several meaningful internal destinations, not one terminal CTA;
- remain legible as a long-form reference on narrow screens.

## `/platform/` — how the runtime works

Audience: engineers and architects deciding whether the platform model fits their system.

Content sequence:

1. Define Daptin as a running application server rather than generated source.
2. Trace schema → world metadata/resource graph → shared middleware → runtime surfaces.
3. Explain identity, request bounds, authorization, transactions, and delivery in request order.
4. Map the system tables that configure actions, schedules, state, storage, sites, integrations, model providers, and plans.
5. Separate application APIs, file delivery, realtime/collaboration, and protocol services.
6. State the deployment and external-side-effect boundary explicitly.

Primary evidence: tagged README; schema/resource, permission, action, server, endpoint, and deployment source; local implementation guides.

## `/open-source/` — what ownership means

Audience: technical and organizational evaluators considering source access, self-hosting, compliance, or a maintained fork.

Content sequence:

1. Explain practical control: inspect, reproduce, operate, and migrate.
2. Give a careful LGPL-3.0 orientation with a prominent not-legal-advice boundary.
3. Map useful project evidence: releases, history, CI, issues, security policy, and docs.
4. Describe a reproducible contribution path with denial-path testing.
5. Give an ownership checklist for releases, backups, hardening, observation, and forks.

Primary evidence: repository LICENSE, CONTRIBUTING, code of conduct, security policy, releases, issue tracker, GNU LGPL-3.0 and licensing FAQ.

## `/ecosystem/` — what connects and how

Audience: application developers and operators choosing a client or integration boundary.

Content sequence:

1. Compare direct JSON:API, GraphQL, JavaScript, and Go client paths.
2. Position the CLI, dashboard, and discovery routes as operational tools.
3. Map HTTP, GraphQL, WebSocket, Yjs, mail, file transfer, feeds, and WebDAV-style protocol scopes with verification boundaries.
4. Explain OpenAPI integrations, per-user OAuth, model providers, and rclone-backed storage.
5. Directory the active tools and focused demos; mark older schema samples as references.
6. End with a least-coupling selection rule.

Primary evidence: tagged README and endpoints; Daptin organization repository metadata; current protocol, integration, AI-routing, and storage guides.

## `/why-daptin/` — should we adopt it

Audience: product and engineering teams making a platform decision.

Content sequence:

1. Define the strongest fit: relational products needing several connected backend responsibilities.
2. Pair each area of built-in leverage with work the adopter still owns.
3. Name weak-fit cases directly.
4. Compare architecture categories without unsupported competitor claims.
5. Review maturity, security, data-lifecycle, and operational-load risks.
6. Provide a six-step vertical-slice proof that includes denial, restore, upgrade, and exit tests.
7. State an adoption rule based on demonstrated leverage rather than feature count.

Primary evidence: the Platform, Engineering, Deploy, Features, Docs, Examples, Open source, and Ecosystem evidence maps.
