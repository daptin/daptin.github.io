# Daptin site quality and communication remediation plan

Plan date: 2026-09-02
Source audit: [`UX_UI_DESIGN_INCONSISTENCY_AUDIT.md`](UX_UI_DESIGN_INCONSISTENCY_AUDIT.md)
Scope: information architecture, missing links, navigation, content quality, page templates, responsive behavior, accessibility, metadata, and regression prevention across all 59 HTML files.

## Outcome

The repaired site must help a visitor move through one continuous journey:

1. understand what Daptin is and whether it fits;
2. see how capabilities connect;
3. choose a relevant use case or feature;
4. follow exact implementation instructions;
5. verify the result and recover from failure;
6. deploy and operate it safely.

The work is successful only when those journeys are possible from links in the page body. A complete footer and a passing broken-link check do not compensate for missing contextual links.

## Product communication model

Each page type gets one job. Content should be moved or linked instead of repeated when it belongs elsewhere.

| Page type | Question it answers | Required content | Must not become |
|---|---|---|---|
| Home | What is Daptin, who is it for, and what should I do next? | Category, outcome, proof, audience/task routes, primary quickstart CTA | A feature catalogue or reference manual |
| Product | How does the complete system fit together? | Architecture, shared model, major subsystem relationships, evidence | A sequence of unrelated feature pitches |
| Use case | How would Daptin support my kind of application? | Scenario, model, actors/access, capability map, frontend boundary, proof, next step | Unlinked prose or a generic example CTA |
| Feature | Why and when should I use this capability? | Outcome, system relationship, use cases, boundaries, visual proof, guide/demo links | A shallow implementation guide |
| Guide | How do I complete and verify one task? | Prerequisites, exact steps, examples, expected results, errors, rollback, related tasks | Marketing cards or vague imperatives |
| Reference | What values and behavior are supported? | Complete fields/options/defaults/types/limits/version/source | A narrative overview |
| Operations runbook | How do I deploy, observe, recover, and change this safely? | Topology, checks, commands, failure response, backup/restore, rollback | A four-item checklist without procedures |
| Example | Can I run and inspect a real flow? | Prerequisites, repository, commands, expected output, refusal/failure proof, related pages | An external link with no local context |

## Non-negotiable content rules

Every published claim and instruction must be:

- **Specific:** name the setting, endpoint, screen, command, record, or file.
- **Located:** say where the user performs the action.
- **Bounded:** state prerequisites, supported scope, and important limitations beside the claim.
- **Verifiable:** show the expected response, state, log, or visible result.
- **Connected:** link prerequisites, underlying concepts, next steps, and runnable proof in context.
- **Release-backed:** follow `CONTENT_OWNERSHIP.md`; validate behavior against the latest release before publishing technical instructions.
- **Owned:** show tested version, last reviewed date, and an edit/source route on every guide.

Avoid using word count as a writing target. The audit’s word counts identify pages that cannot presently complete their stated task; completion evidence is the target.

## Delivery strategy

Use seven workstreams delivered in dependency order. Do not rewrite all pages before the shared navigation and content patterns exist.

| Order | Workstream | Purpose | Audit issues closed |
|---:|---|---|---|
| 0 | Baseline and page data | Make current behavior measurable and remove hand-copied global data | QA-01, QA-02, META-02, part of NAV-01/02/05 |
| 1 | Navigation and link architecture | Make place, prerequisites, relationships, and next steps visible | IA-01–05, NAV-01–05, A11Y-01–03 |
| 2 | Core task documentation | Unblock evaluation, configuration, deployment, and operations | DOC-01–04, DOC-07–08 |
| 3 | Feature communication | Explain how capabilities form one system and provide proof | DOC-05–06, UI-02–03, UI-07 |
| 4 | Use cases and examples | Connect scenarios to models, guides, and runnable evidence | IA-05, UI-01, UI-07 |
| 5 | Visual/accessibility system | Normalize components and responsive behavior | UI-01–06, NAV-03/05, A11Y-01–03 |
| 6 | Metadata and regression gates | Correct identity and keep the repair from drifting | META-01–03, QA-01–02 |

Workstream 0 is the foundation. Workstreams 2–4 may proceed in parallel after the first navigation/content components from Workstream 1 are stable. Workstream 5 should refine those components rather than inventing a second system. Workstream 6 runs throughout and becomes the release gate.

## Workstream 0 — Baseline and reusable page data

### 0.1 Capture the baseline

Create a machine-readable inventory for every HTML page containing:

- route and page type;
- title, H1, description, canonical, `og:url`, breadcrumb leaf;
- current primary-nav section;
- main-content word count and heading outline;
- unique in-body internal destinations, excluding footer/global nav;
- incoming contextual links from other main-content regions;
- required related pages, examples, and prerequisites;
- tested release, review date, and content owner for docs.

Store the declared relationships in one data file, for example `site-pages.json`. A simple static generator or build script may render repeated fragments, but generated HTML must remain publishable by GitHub Pages. Do not introduce a large framework solely for includes.

### 0.2 Stop hand-copying global chrome

Create single-source renderers/data for:

- `<head>` metadata;
- global header and primary navigation;
- visible and structured breadcrumbs;
- docs navigation;
- page footer;
- related-content blocks;
- docs freshness/applicability block.

Add a deterministic build/check command. CI must fail when generated global fragments differ from committed HTML.

### 0.3 Add baseline reports before enforcing thresholds

Extend or replace `scripts/audit-site.sh` so it examines all 59 HTML files. Initially report, then gate after remediation:

- missing and broken links/fragments;
- absent required links from the declared relationship graph;
- pages with no incoming contextual links;
- canonical/`og:url`/breadcrumb mismatch;
- missing favicon/theme/social metadata;
- missing or multiple H1s;
- missing current navigation state;
- footer headings inside the page’s content outline;
- template-required sections;
- duplicate long copy;
- stale review/version fields.

#### Workstream 0 acceptance

- One command reproduces all HTML or verifies it is current.
- All 59 pages appear in the page inventory.
- Global navigation, footer, metadata, breadcrumbs, and relationship data each have one source of truth.
- Audit output distinguishes broken links from required-but-missing links.

## Workstream 1 — Navigation and missing-link architecture

### 1.1 Adopt a smaller primary navigation

Use four durable user choices:

- **Product** — product overview and feature map;
- **Solutions** — use cases and examples;
- **Developers** — engineering, deploy, and supporting resources;
- **Docs** — documentation home and guides;
- keep **Run Daptin** as the visually primary action.

If dropdowns are not implemented accessibly, retain direct landing pages instead of hover-only menus. Every route must set `aria-current="page"` on its owning primary item.

### 1.2 Replace mobile overflow with a real menu

Implement a button with an accessible name, `aria-expanded`, and `aria-controls`. The disclosed panel must include every primary destination and Run Daptin. Requirements:

- works without hover;
- predictable Escape, Tab, Shift+Tab, and focus behavior;
- no invisible horizontal scroller;
- no loss of CTA at widths below 900px;
- usable at 320px and 200% zoom;
- progressively enhanced: core destinations remain available if JavaScript fails.

### 1.3 Add visible breadcrumbs

Render breadcrumbs above the H1 on Product/Feature/Docs/Use-case/Deploy/Example detail contexts. The visible trail and JSON-LD must come from the same page data.

Examples:

- `Home / Features / Sites and publishing`
- `Home / Docs / Files and publishing / Publish sites`
- `Home / Docs / Operations / Server configuration`

### 1.4 Create the docs information architecture

Group docs into task-oriented sections:

1. **Start:** Getting started, Data modeling, APIs.
2. **Identity and access:** Authentication, Permissions, Two-factor authentication, OAuth/OIDC provider.
3. **Files and publishing:** Files, Cloud storage, Sites, Protocols, WebDAV-style access.
4. **Application behavior:** Actions, Scheduled work, State tracking, Email actions.
5. **Connections:** Integrations, AI routing, Realtime, Collaboration, Mail, Metering.
6. **Operate:** Server configuration, Database setup, Production deployment, TLS, Monitoring, Clustering, Operations.
7. **Focused interfaces:** GraphQL and any future protocol references.

Every docs page must include:

- visible breadcrumb;
- section sidebar/disclosure with current page;
- local TOC when the page has three or more H2 sections;
- prerequisites near the start;
- related tasks near the relevant instruction;
- previous/next controls based on a deliberate path, not alphabetic order.

Merge `/docs/feature-guides/` into `/docs/` or turn it into genuinely ordered learning paths. Preferred option: redirect it to `/docs/#guides` and keep one documentation home.

### 1.5 Implement declared relationship types

Every contextual link must have a reason. Support these relationship labels:

- **Prerequisite** — required first;
- **Concept** — explains why or the model underneath;
- **Implementation** — exact guide/reference;
- **Works with** — connected capability;
- **Security** — authentication/permission/secrets boundary;
- **Operate** — production concerns;
- **Proof** — runnable example or evidence;
- **Next** — recommended continuation.

Do not auto-render every relationship everywhere. Show 3–6 links selected for the current task and put links inline at the sentence where the dependency matters.

### 1.6 Required relationship graph

| Page/capability | Prerequisite and concept links | Implementation/operations links | Proof/next links |
|---|---|---|---|
| Data modeling | Permissions, files, state tracking | Data-modeling guide, APIs guide | schema example, build an API |
| APIs | Data model, authentication, permissions | APIs, GraphQL, realtime, metering | first CRUD flow, API example |
| Authentication | Data model, permissions/groups | Authentication, 2FA, OAuth provider | auth example, secure a resource |
| Permissions | Authentication, data model | Permissions, files, actions, realtime | multi-tenant example |
| Files | Data model, permissions | Files, cloud storage, protocols, sites | asset example, publish a site |
| Sites | Files, cloud storage, permissions | Sites, TLS, protocols/FTP, scheduling | site flow, deploy frontend |
| Actions | Data model, permissions | Actions, schedules, state, integrations, mail | runnable action |
| Scheduled work | Actions, acting user/permissions | Scheduling, monitoring | observable scheduled run |
| State tracking | Data model, permissions | State tracking, actions | state-machine example |
| Integrations | Authentication/OAuth, permissions | Integrations, actions, AI routing | provider-auth demo |
| Realtime | Data model, permissions | Realtime, clustering, collaboration | live client example |
| Collaboration | Authentication, permissions | Collaboration, realtime, persistence | Yjs client example |
| Mail | Accounts, storage, permissions | Mail, email actions, TLS/DNS, monitoring | send/receive example |
| Protocols | Files, sites, permissions | Protocols, WebDAV, TLS | per-protocol verification |
| Metering | Identity, APIs | Metering, operations, AI routing | quota-denial demo |
| Operations | Deployment architecture | Config, database, TLS, monitoring, clustering, backup/restore | production checklist |

#### Workstream 1 acceptance

- All applicable pages expose a visible hierarchy and current location.
- Every page answers: prerequisite, system connection, implementation, and verification through contextual links.
- The 19 feature pages no longer depend on one repeated guide CTA as their only route onward.
- Each use-case section has its own feature, guide, and proof links.
- Keyboard and mobile users can reach all global and docs navigation destinations.

## Workstream 2 — Core task documentation

Complete this work in four batches. No page graduates from draft because it reaches a word count; it graduates only after a clean-room task test succeeds.

### Standard guide contract

Every procedural guide must contain:

1. outcome and supported scope;
2. tested Daptin version and last-reviewed date;
3. prerequisites and security assumptions;
4. exact UI/API/CLI location;
5. copyable configuration or commands;
6. field/default/allowed-value reference where applicable;
7. expected result after every major step;
8. verification, including a negative/failure check;
9. common errors and diagnosis;
10. rollback, disable, or cleanup instructions;
11. contextual prerequisite/related/next links;
12. source/edit link.

Operations runbooks additionally require topology, persistence scope, backup/restore, upgrade/rollback, alert/failure response, and rehearsal guidance.

### Batch 2A — Evaluation and basic configuration

#### Getting started

Build one primary 10-minute path:

`install/run → confirm health → define a small model → inspect generated API → create/read a record → show dashboard/result → stop and clean up`

Then branch to native binary, Docker, databases, permissions, and production. Include expected terminal output and HTTP responses.

#### Server configuration

Replace the current four-card summary with:

- configuration sources and precedence;
- exact flag/environment/config-table names supported by the audited release;
- bind address, public URL, ports, secrets, request limits and timeouts;
- database driver, connection strings, pool settings/defaults;
- storage/site, mail, protocol, AI/integration, cluster, and cache toggles;
- which changes require restart/reconfigure;
- security warnings and secret-handling rules;
- startup/health/statistics verification;
- links to every focused guide at the relevant setting group.

The sentence “Select the driver and connection details, then bound the connection pool” must be removed or expanded into exact steps, values, criteria, and verification.

#### Database setup

Provide tested SQLite, PostgreSQL, and MySQL paths with connection strings, TLS expectations, persistence/backup, migration behavior, pool sizing criteria, connection verification, and common errors.

### Batch 2B — Production operations

- **Production deployment:** supported artifact/topology, persistence, secrets, proxy/TLS, probes, graceful changes, backup/restore, upgrades/rollback.
- **TLS certificates:** Daptin vs reverse proxy decision, exact configuration, ACME/DNS/ports, SNI, renewal and expiry monitoring, test commands.
- **Monitoring:** liveness/readiness/statistics semantics by released version, logs, pool signals, collection examples, suggested alerts, failure interpretation.
- **Clustering:** topology, Olric configuration/discovery, shared vs local state, failure policy, node loss, rolling operations, verification.
- **Operations:** become the runbook hub that connects configuration, deployment, database, TLS, monitoring, clustering, backup, and upgrade tasks without duplicating shallow summaries.

### Batch 2C — Focused thin guides

Rewrite GraphQL, Two-factor authentication, Email actions, and WebDAV-style access using the standard guide contract. Each must contain at least one complete success path and one expected refusal/error path.

### Batch 2D — Deepen existing guides

Bring the remaining guides to the same contract:

- Data modeling, APIs, Authentication, Permissions, OAuth provider;
- Files, Cloud storage, Sites;
- Actions, Scheduled work, State tracking;
- Integrations, AI routing, Realtime, Collaboration;
- Mail, Protocols, Metering.

Prioritize missing executable examples, negative verification, troubleshooting, and cross-links rather than adding generic explanatory paragraphs.

### Content verification workflow

For each guide:

1. resolve the latest release according to `CONTENT_OWNERSHIP.md`;
2. verify names, defaults, routes, semantics, and examples against release source/tests;
3. run the documented happy path in a clean environment where feasible;
4. run the documented negative/failure check;
5. have a second reviewer follow only the page, recording guesses or external searches;
6. fix every undocumented dependency;
7. publish the tested version and review date.

#### Workstream 2 acceptance

- A new user completes Getting started without consulting another source.
- Server configuration is a real reference and task guide, not a category summary.
- Each P0 operations page passes a clean-room task review.
- All guides satisfy the standard contract or are explicitly labeled conceptual/reference with the appropriate contract.

## Workstream 3 — Feature communication and system understanding

### 3.1 Replace the universal card formula with proof appropriate to each capability

| Feature | Primary explanatory artifact |
|---|---|
| Data modeling | entity/relationship example annotated with generated behavior |
| APIs | interface decision table plus request/response examples |
| Authentication | account lifecycle flow |
| Permissions | role × operation × record matrix |
| OAuth provider | authorization-code + PKCE sequence |
| Files | record → field → store → authorized delivery diagram |
| Cloud storage | provider choice and credential/store/field model |
| Sites | end-to-end publishing and application connection diagram |
| Actions | input → conditions → outcomes → transaction boundary |
| Scheduled work | action/schedule/acting-user/execution timeline |
| State tracking | valid/invalid transition graph |
| Integrations | browser/Daptin/provider identity and credential flow |
| AI routing | client/Daptin/provider/usage flow and capability table |
| Realtime | subscription/auth/event/reconnect/cluster flow |
| Collaboration | standalone vs record-backed comparison |
| Mail | receive/store/read and action/outbox/send flows |
| Protocols | protocol-by-task decision table |
| Metering | plan/member/usage/quota/decision entity flow |
| Operations | deployment topology and signal responsibility map |

Use HTML/CSS/SVG-native diagrams when they remain accessible and maintainable; provide text equivalents and do not embed essential labels only in raster images.

### 3.2 Make Sites the model cross-capability page

Rebuild `/features/sites/` first to establish the pattern:

`application data model → permission-aware APIs/actions → frontend build/templates → files in cloud_store → site record and host/path routing → cache → TLS/basic auth/FTP → monitoring and scheduled sync`

The page must state:

- which parts are static and which remain dynamic;
- where templates/builds happen and what Daptin does or does not execute;
- how a frontend reaches data/actions;
- where permissions apply and where public/static delivery changes the boundary;
- configuration order;
- direct links from each node to its feature and guide;
- one worked scenario and proof link.

Use this page to validate the reusable system-diagram and related-content patterns before applying them elsewhere.

### 3.3 Give feature pages distinct evidence

Each feature page needs:

- one concrete outcome in the hero;
- one system relationship visual;
- one worked example or product screenshot;
- one explicit limitation/boundary beside the related claim;
- contextual links covering concept, implementation, security/operations, and proof;
- no duplicate top/bottom CTA unless each placement serves a different decision moment.

#### Workstream 3 acceptance

- A user can explain how each feature connects to Daptin’s data and permission model after reading its page.
- Feature pages are distinguishable by their explanatory artifact, not only their headings.
- Sites answers the data model, permission model, template/build, configuration-order, and operations questions raised in the audit.

## Workstream 4 — Use cases and runnable proof

### 4.1 Fix the hero component immediately

Wrap the `/use-cases/` CTA in the shared `.actions` container, or make the hero-copy layout use a consistent parent `gap`. Ensure `.hero-facts` never controls spacing to whatever follows it. Remove the page-specific accidental spacing dependency.

### 4.2 Turn every use case into a navigable solution map

Each of the four use cases must include:

- a small entity/relationship model;
- actors and access rules;
- Daptin responsibilities;
- frontend responsibilities;
- a “Build this” ordered path;
- links to every named feature at first mention;
- direct links to relevant implementation guides;
- a runnable example or clearly labeled closest available proof;
- deployment/operations next step.

Required routes:

| Use case | Core feature links | Guide links | Proof |
|---|---|---|---|
| Customer portal/private workspace | modeling, authentication, permissions, files, actions, realtime | model, auth, permissions, files | workspace/ownership flow or closest reproducible schema |
| Internal operations/approvals | modeling, APIs, actions, schedules, state tracking, operations | model, actions, schedules, state | approval/action flow |
| Content/documents/assets | modeling, files, cloud storage, sites, permissions, protocols | model, files, storage, sites | content/site flow |
| Authenticated API/provider gateway | authentication, permissions, OAuth provider, integrations, AI routing, metering | auth, permissions, OAuth, integrations, AI, metering | OAuth, provider-auth, LLM, and quota demos |

If a runnable proof does not exist, label the gap and create an example task; do not imply that the generic Examples index proves the scenario.

### 4.3 Standardize example cards and pages

Every example entry must show:

- what it proves;
- tested Daptin release/commit;
- prerequisites and approximate steps—not unsupported performance/time claims;
- commands/repository link;
- expected success and refusal/failure result;
- related use case, feature, and guide links;
- maintenance status.

#### Workstream 4 acceptance

- No use-case section contains an unlinked mention of a page that exists.
- Each scenario has a direct implementation route and honest proof status.
- Facts-to-actions spacing is identical across use-case and feature heroes at all target breakpoints.

## Workstream 5 — Visual and accessibility system

### 5.1 Establish component contracts

Define semantic markup and spacing rules for:

- page hero, facts, and actions;
- breadcrumb;
- inline/content links;
- step lists;
- configuration/reference tables;
- code and expected output;
- note, warning, security, and version callouts;
- relationship diagrams;
- related-content/next-step groups;
- docs sidebar and TOC;
- global header/mobile menu;
- compact footer.

Use container `gap` for sibling rhythm instead of page-specific margins. Remove selectors that only compensate for one template, such as `.feature-detail .page-hero .actions`, after the shared contract is applied.

### 5.2 Repair typography and link affordance

- Make normal content at least `1rem` with a readable line length.
- Make supporting text and controls at least `0.875rem` unless a tested exception is necessary.
- Increase navigation, footer, tag, and code sizes from the current `0.65–0.78rem` range.
- Underline prose links by default; do not rely on hover or color alone.
- Provide consistent hover, active, visited, and `:focus-visible` states.
- Remove button translation on keyboard focus; use a stable outline/background treatment.

### 5.3 Replace the footer directory

Use a smaller footer containing:

- Product: Overview, Features, Use cases;
- Learn: Docs, Getting started, Examples;
- Operate: Deploy, Operations;
- Project: Source, license/community links that actually exist;
- primary Run Daptin action.

Use lists and one footer landmark heading so the eight current `<h2>` elements do not pollute every page outline. Contextual body links and docs navigation must be in place before removing the oversized directory.

### 5.4 Responsive and accessibility verification

Verify representative templates at:

- 320px, 375px, 768px, 1024px, and wide desktop;
- 200% and 400% zoom/reflow where applicable;
- keyboard only;
- screen reader landmarks, headings, current state, menu, breadcrumb, diagrams, tables, and code;
- reduced motion;
- touch target sizing;
- high contrast/forced colors where practical.

#### Workstream 5 acceptance

- No required navigation or CTA is hidden at any supported width.
- No horizontal page scroll is required at 320px or 200% zoom; intentionally scrollable code/tables are labeled and contained.
- Inline links remain identifiable without hover.
- Main-content heading outlines are not dominated by footer labels.
- Feature, guide, reference, and operations pages are visually distinguishable.

## Workstream 6 — Metadata and permanent quality gates

### 6.1 Correct page identity

Immediately fix:

- `/features/mail/` canonical and breadcrumb leaf to `https://daptin.github.io/features/mail/`;
- `/features/protocols/` canonical and breadcrumb leaf to `https://daptin.github.io/features/protocols/`.

Require every indexable page to have absolute, matching canonical, `og:url`, and breadcrumb-leaf URLs.

### 6.2 Normalize shared metadata

Generate and require:

- title and meta description;
- absolute canonical;
- favicon;
- theme color;
- Open Graph type/title/description/url/image;
- Twitter card/image;
- structured breadcrumbs where applicable.

### 6.3 Make freshness truthful

Generate sitemap `lastmod` from the last meaningful change to each content page, or omit it. Do not stamp every URL with a deployment/audit date. Display docs applicability separately as tested version and review date.

### 6.4 CI release gates

The site cannot ship when any of these fail:

- generated HTML is stale;
- internal link or fragment is broken;
- a declared required relationship is absent from main content;
- a content page has zero incoming contextual links;
- canonical, Open Graph URL, or breadcrumb identity disagrees;
- required metadata is missing;
- primary current-page state is absent or incorrect;
- H1/landmark/heading rules fail;
- template-required guide fields are missing;
- automated accessibility tests report serious/critical violations;
- representative responsive screenshots differ without approval.

Do not gate on a universal minimum number of links or words. Gate on declared relationships and template requirements.

#### Workstream 6 acceptance

- All 59 files pass the same structural audit.
- Required-but-missing links are testable separately from broken links.
- No page has contradictory URL identity or incomplete shared metadata.
- Sitemap and visible applicability signals are derived from truthful sources.

## Implementation backlog

The backlog is ordered so each item leaves the repository in a coherent state.

| ID | Deliverable | Depends on | Size | Completion evidence |
|---|---|---|---:|---|
| FND-01 | `site-pages.json` route/type/navigation/relationship inventory for all 59 pages | — | M | schema validation and 59 unique routes |
| FND-02 | shared renderer/check for head, header, breadcrumbs, footer, related links | FND-01 | L | deterministic build; no duplicated divergent fragments |
| QA-01 | whole-site structural/link/metadata audit | FND-01 | M | fixtures prove broken and missing-link failures are distinct |
| NAV-01 | compact desktop navigation and correct `aria-current` | FND-02 | M | route matrix passes current-state tests |
| NAV-02 | accessible mobile disclosure navigation | NAV-01 | M | keyboard, 320px, zoom, no-JS checks |
| NAV-03 | visible breadcrumbs synchronized with JSON-LD | FND-02 | S | visual/structured path equality on every detail page |
| NAV-04 | docs grouping, sidebar/TOC, previous/next | FND-01, FND-02 | L | all docs routes navigable without footer |
| LINK-01 | declared capability relationship graph | FND-01 | M | relationship validator passes all capability pages |
| LINK-02 | contextual links on all feature/docs pages | LINK-01 | L | no missing declared relation; editorial review |
| DOC-01 | complete Getting started | shared guide components | L | clean-room first-run task succeeds |
| DOC-02 | complete Server configuration reference/task guide | DOC-01 research setup | XL | field/source verification and task review |
| DOC-03 | complete Database setup | DOC-02 | L | three database paths verified or accurately scoped |
| OPS-01 | Production deployment runbook | DOC-02, DOC-03 | XL | deploy/backup/restore/upgrade review |
| OPS-02 | TLS and Monitoring runbooks | OPS-01 | L | certificate and monitoring verification succeeds |
| OPS-03 | Clustering and Operations hub | OPS-01, OPS-02 | XL | topology/failure/rolling-operation review |
| DOC-04 | GraphQL, 2FA, Email actions, WebDAV guide rewrites | guide components | XL | success + failure path per guide |
| DOC-05 | deepen remaining 19 implementation guides | guide components, LINK-01 | XXL | standard guide contract review |
| FEAT-01 | Sites feature/system map pilot | LINK-01 | L | answers all five reported connection questions |
| FEAT-02 | differentiated proof for remaining feature pages | FEAT-01 | XXL | artifact/content contract per feature |
| USE-01 | normalize use-case hero spacing | component contract | S | visual regression at target widths |
| USE-02 | four navigable use-case solution maps | LINK-01 | XL | model + access + guides + proof per case |
| EX-01 | example proof/maintenance cards and missing-example backlog | USE-02 | L | every claim linked to honest proof status |
| UI-01 | typography and link affordance repair | component contract | M | contrast/link/zoom review |
| UI-02 | compact semantic footer | LINK-02, NAV-04 | M | reduced outline and mobile length |
| META-01 | Mail/Protocols canonical hotfix | — | S | canonical/OG/breadcrumb validator |
| META-02 | shared metadata and truthful sitemap dates | FND-02 | M | metadata/sitemap audit passes |
| QA-02 | automated a11y and responsive regression suite | stable components | L | agreed breakpoint/browser matrix in CI |

Size is relative: S is a focused change, M a multi-page/component change, L a substantial feature or guide, XL a research-heavy runbook or page family, and XXL a multi-iteration program. It is not a calendar commitment.

## Recommended release slices

### Release A — Stop actively harmful behavior

- META-01 canonical corrections;
- USE-01 hero spacing;
- current navigation state;
- mobile navigation that retains Run Daptin;
- visible breadcrumbs;
- initial whole-site audit.

This release improves orientation and removes clear defects, but does not claim the documentation problem is solved.

### Release B — Make evaluation and setup viable

- complete Getting started;
- complete Server configuration and Database setup;
- docs shell/navigation;
- contextual links for those journeys;
- shared guide components and applicability metadata.

### Release C — Make production guidance credible

- Production deployment, TLS, Monitoring, Clustering, and Operations runbooks;
- deploy-page links to exact runbooks;
- backup/restore and upgrade/rollback task tests.

### Release D — Explain one connected product

- Sites cross-capability pilot;
- Files, Cloud storage, Permissions, APIs, and Scheduling links/content needed by that flow;
- content/assets use-case solution map and runnable proof.

### Release E — Complete the capability system

- remaining feature artifacts and implementation guides;
- all use-case solution maps;
- example proof cards;
- reduced footer and finalized visual system;
- all regression gates enforced.

## Review and governance

### Required review roles

- **Product/content owner:** page job, audience, hierarchy, terminology, and next action.
- **Daptin engineer:** release-backed accuracy, examples, defaults, limitations, and failure behavior.
- **UX/accessibility reviewer:** navigation, link meaning, responsive behavior, semantics, keyboard and screen-reader operation.
- **Fresh reader:** completes the documented task without unpublished context.

One person may fill more than one role, but the fresh-reader test must be performed by someone who did not write the page.

### Pull-request checklist

- Which audit IDs does this close?
- Which user journey becomes possible or clearer?
- Which links were intentionally added, and what question does each answer?
- Which latest release/source/tests support the technical statements?
- What success and failure paths were run?
- Which viewport, keyboard, and accessibility checks were performed?
- Did metadata, breadcrumbs, sitemap source, and current navigation remain consistent?
- Did the whole-site audit pass?

## Measurement

Capture a baseline before Release A and compare after each slice.

### Task measures

- first successful local run completion rate;
- first model + record completion rate;
- server/database configuration completion rate;
- production checklist comprehension and correct next-step selection;
- time and wrong turns from use case → relevant guide → runnable proof.

### Navigation measures

- percentage of feature/docs pages satisfying all declared relationship types;
- pages with zero incoming contextual links;
- footer clicks used as recovery after reading a feature/guide;
- mobile navigation discovery and completion;
- search exits and backtracks from thin docs.

### Quality measures

- guides passing the standard contract and clean-room review;
- serious/critical accessibility issues;
- broken links versus required-but-missing links, reported separately;
- metadata identity mismatches;
- stale review/version signals;
- unauthorized visual-regression changes.

Do not optimize raw link count, word count, page views, or time on page. A concise page that completes a task and routes the next decision is better than a long page that strands the reader.

## Completion matrix

This matrix prevents broad improvements from leaving individual audit findings unresolved.

| Audit finding | Primary backlog item(s) | Proof required to close |
|---|---|---|
| IA-01 | NAV-04 | docs hierarchy, current state, TOC, prerequisites, previous/next on every guide |
| IA-02 | LINK-01, LINK-02, USE-02 | declared contextual relationships present; editorial journey review |
| IA-03 | LINK-01, LINK-02 | reciprocal feature/guide and cross-capability links |
| IA-04 | NAV-04 | redirect/merge or demonstrably distinct learning-path content |
| IA-05 | USE-02, EX-01 | feature + guide + proof route per use case |
| NAV-01 | NAV-01 | correct visible and semantic current state on all routes |
| NAV-02 | NAV-03 | visible/structured breadcrumb equality |
| NAV-03 | NAV-02 | keyboard/mobile/zoom/no-JS verification |
| NAV-04 | NAV-01 | simplified tested information architecture |
| NAV-05 | UI-02, LINK-02 | compact footer after contextual navigation exists |
| UI-01 | USE-01 | cross-page visual regression at all target widths |
| UI-02 | shared guide/feature components | distinct templates confirmed in page inventory |
| UI-03 | FEAT-01, FEAT-02, guide components | ordered/table/diagram patterns match information type |
| UI-04 | UI-01 | typography review at mobile/desktop/zoom |
| UI-05 | UI-01 | inline links identifiable in default/focus/visited states |
| UI-06 | UI-01 | stable keyboard focus; reduced-motion test |
| UI-07 | FEAT-01, FEAT-02, EX-01 | purposeful evidence artifact per capability |
| DOC-01 | DOC-01–05, OPS-01–03 | all thin guides pass appropriate content contract |
| DOC-02 | DOC-02 | complete verified configuration task/reference |
| DOC-03 | DOC-01 | clean-room onboarding success |
| DOC-04 | OPS-01–03, DOC-03 | operational runbook reviews |
| DOC-05 | FEAT-01 | Sites end-to-end system map and links |
| DOC-06 | FEAT-02 | differentiated artifact per feature |
| DOC-07 | DOC-01–05 | instruction-level specificity review |
| DOC-08 | FND-01, FND-02 | tested version/review/source on every guide |
| META-01 | META-01 | canonical/OG/breadcrumb agreement |
| META-02 | META-02 | shared required metadata on all applicable pages |
| META-03 | META-02 | source-derived or omitted `lastmod` |
| A11Y-01 | NAV-01–04, QA-02 | semantic navigation audit |
| A11Y-02 | NAV-02, QA-02 | all controls available at target widths/zoom |
| A11Y-03 | UI-02, QA-02 | meaningful heading outline on representative/all pages |
| QA-01 | QA-01, QA-02 | automated coverage of all 59 files and rendered templates |
| QA-02 | LINK-01, QA-01 | separate missing-required-link and broken-link tests |

## Site-wide definition of done

The remediation program is complete when all of the following are proven in the current site, not merely planned:

- all 59 pages are generated or validated from shared navigation, metadata, breadcrumb, and relationship data;
- every audit finding in the completion matrix has its required evidence;
- Getting started succeeds for a fresh reader;
- Server configuration and every operations page support exact, verifiable tasks;
- every feature explains its relationship to data, access, runtime, and operations where relevant;
- every use case links to a model, implementation route, and honest runnable proof;
- no content page relies on the footer as its only route to prerequisites or related work;
- desktop, mobile, zoomed, keyboard, reduced-motion, and screen-reader navigation pass the agreed checks;
- metadata identity is consistent and sitemap freshness is truthful;
- whole-site structural, relationship, accessibility, and responsive regression gates pass.
