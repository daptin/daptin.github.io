# Daptin website design and UX/UI inconsistency audit

Audit date: 2026-09-02
Scope: all 59 HTML files in this repository, the shared stylesheet, navigation, internal links, responsive rules, metadata, and the three reported examples.
Primary artifact reviewed: the current static source that publishes to `https://daptin.github.io/`.

## Executive summary

The site is visually coherent at the level of color, typography, and repeated components, but that consistency is superficial. The same small set of layouts is applied to marketing pages, feature explanations, implementation guides, and operations documentation even though those page types serve different user needs. This creates four dominant problems:

1. **Documentation often looks complete while containing too little actionable information.** Eleven guides contain only 85–154 words in `<main>`. They name areas to configure but do not give settings, accepted values, defaults, examples, commands, verification steps, failure cases, or links to the exact source of truth.
2. **Most pages are link deserts.** The footer contains an enormous directory, while most feature and guide pages contain only one or two distinct destinations in their main content. Relationships are mentioned in prose but are usually not linked where the user encounters them. This is a missing-link problem, not a broken-link problem.
3. **Navigation does not communicate place or progress.** None of the 59 pages marks the current navigation item with `aria-current`; the structured-data breadcrumbs are not shown visually; docs have no local navigation, table of contents, or consistent previous/next path.
4. **The component system is used inconsistently.** The reported hero spacing defect is one instance: `/use-cases/` places a button directly after `.hero-facts`, whereas feature pages wrap hero actions in `.actions`. The result depends on accidental margins rather than a shared hero-action contract.

This is not primarily a polish problem. The first work should improve task completion and information architecture; visual cleanup should follow.

## Severity and priority

- **P0 — Blocking:** can prevent a user from completing a core evaluation, setup, or production task.
- **P1 — High:** repeatedly causes disorientation, missing context, or a misleading page.
- **P2 — Medium:** creates friction, inconsistency, accessibility risk, or weak discoverability.
- **P3 — Low:** polish, metadata consistency, or maintainability issue with limited immediate task impact.

## Findings

### IA-01 — Documentation has no documentation navigation

- **Priority:** P0
- **Affected:** every page under `/docs/` except the two index-like pages, especially long guides such as `/docs/authentication/`, `/docs/permissions/`, `/docs/sites/`, `/docs/apis/`, and `/docs/oauth-provider/`.
- **Evidence:** detail pages use the same seven-item marketing header as the rest of the site. There is no docs sidebar, section navigation, visible breadcrumb, on-page table of contents, or consistent previous/next guide control.
- **Impact:** a user entering from search cannot see the guide hierarchy, nearby prerequisites, related operations topics, or how far they are through a task. Returning to “All guides” and scanning a large directory is the only reliable recovery path.
- **Recommendation:** add a docs shell with visible breadcrumbs, collapsible section navigation, an on-page TOC for multi-section guides, and previous/next links based on deliberate learning paths.
- **Acceptance:** every docs detail page shows `Docs / section / page`, highlights the current page, exposes siblings without requiring the footer, and has a meaningful next step.

### IA-02 — Contextual links are scarce; the footer is doing the information architecture

- **Priority:** P1
- **Affected:** all 19 feature detail pages and most docs detail pages; acute on `/use-cases/`, `/features/sites/`, and `/docs/server-configuration/`.
- **Evidence:** after excluding same-page anchors, 15 of 19 feature detail pages have exactly two unique destinations in `<main>`; two have only one, and only two have three. Of 30 docs detail pages, 26 have exactly two. These small counts often include the same matching feature/guide destination repeated at both the top and bottom, so they do not represent two different user journeys. The shared footer, by contrast, contains more than 50 destinations. `/use-cases/` describes data modeling, permissions, files, actions, schedules, state tracking, integrations, AI routing, metering, and realtime, but its four use-case sections contain no contextual links.
- **Impact:** users must translate product vocabulary into footer labels and hunt for the relevant page. The content explains that concepts connect without letting users follow those connections.
- **Recommendation:** add inline links at first meaningful mention and a small “Works with / Next” block per section. Link each use case to a runnable example, relevant feature pages, and implementation guides.
- **Acceptance:** every major concept that has a dedicated page is linked in context; each detail page has 3–6 curated related links rather than relying on the global footer.

#### Link-desert inventory

This inventory is about links that should exist but do not. Passing the broken-link check does not reduce the severity.

| Main-content destinations | Pages |
|---|---|
| Only 1 | `/features/mail/`, `/features/protocols/` |
| Exactly 2 | `/features/actions/`, `/features/ai-routing/`, `/features/authentication/`, `/features/cloud-storage/`, `/features/collaboration/`, `/features/files/`, `/features/integrations/`, `/features/metering/`, `/features/oauth-provider/`, `/features/operations/`, `/features/permissions/`, `/features/realtime/`, `/features/scheduled-work/`, `/features/sites/`, `/features/state-tracking/` |
| Exactly 2 | `/docs/actions/`, `/docs/ai-routing/`, `/docs/cloud-storage/`, `/docs/clustering/`, `/docs/collaboration/`, `/docs/data-modeling/`, `/docs/database-setup/`, `/docs/email-actions/`, `/docs/files/`, `/docs/getting-started/`, `/docs/graphql/`, `/docs/integrations/`, `/docs/mail/`, `/docs/metering/`, `/docs/monitoring/`, `/docs/oauth-provider/`, `/docs/operations/`, `/docs/permissions/`, `/docs/production-deployment/`, `/docs/realtime/`, `/docs/scheduled-work/`, `/docs/server-configuration/`, `/docs/state-tracking/`, `/docs/tls-certificates/`, `/docs/two-factor-auth/`, `/docs/webdav/` |

Examples of absent links with direct UX consequences:

- `/use-cases/` names feature families and guides inside every scenario but links none of those mentions.
- `/features/sites/` mentions data, identity, actions, files, realtime, certificates, scheduling, FTP, APIs, and static output, yet its only external in-body destinations are the Sites guide and Cloud storage.
- `/docs/server-configuration/` names database, network, storage, protocols, integrations, pools, request limits, and timeouts without linking those terms to a reference or focused guide.
- `/features/mail/` describes actions, storage, TLS, DNS, retry behavior, and operations but gives the reader only its matching Mail guide.
- `/features/protocols/` combines FTP/FTPS, WebDAV-style routes, and feeds but offers only its matching Protocols guide rather than a path for each task.

The remediation should not pursue an arbitrary link count. Each page needs the links required to answer four questions: **What must I do first? How does this connect to the rest of Daptin? Where are the exact implementation steps? Where can I verify it works?**

### IA-03 — Feature-to-guide pairing is narrow and one-directional

- **Priority:** P1
- **Affected:** all `/features/*/` and `/docs/*/` pairs.
- **Evidence:** feature pages generally offer a guide CTA at the top and bottom, while guides generally link back to only their matching feature page. Cross-capability dependencies are mostly plain text.
- **Impact:** users learn isolated capabilities instead of workflows. For example, sites depend on storage, certificates, routing, optional FTP, templates/static output, data APIs, and permissions, but only cloud storage receives a final related link.
- **Recommendation:** model explicit relationships: prerequisites, used-by, works-with, security considerations, operations considerations, and runnable examples. Render the relationships consistently on both sides.

### IA-04 — `/docs/` and `/docs/feature-guides/` substantially duplicate the same directory

- **Priority:** P2
- **Affected:** `/docs/`, `/docs/feature-guides/`.
- **Evidence:** both pages use the same hero, capability directory, operations directory, and footer with only small copy differences.
- **Impact:** two destinations appear to promise different scopes but offer nearly the same choice set, adding a redundant level to the hierarchy and risking future drift.
- **Recommendation:** keep `/docs/` as the documentation home and either redirect `/docs/feature-guides/` to an anchored section or make it a genuinely task-oriented learning-path page.

### IA-05 — Use cases are not connected to concrete proof

- **Priority:** P1
- **Affected:** `/use-cases/`.
- **Evidence:** a single “Open runnable examples” CTA precedes four use cases. Individual claims such as “schema samples,” “cloud-storage guide,” “import and action guides,” and named demos are plain text.
- **Impact:** the reader cannot move directly from a relevant scenario to its model, guide, or demo and cannot easily validate a claim.
- **Recommendation:** add per-use-case links for “See the data model,” “Understand permissions,” “Implementation guide,” and “Run this flow.” Do not use one generic CTA as a substitute for four different journeys.

### NAV-01 — No page exposes a current navigation state

- **Priority:** P1
- **Affected:** all 59 HTML files.
- **Evidence:** the stylesheet defines `.desktop-nav a[aria-current="page"]`, but no HTML file contains `aria-current`.
- **Impact:** visual location feedback and the screen-reader current-page announcement are both missing. The dead CSS suggests the intended behavior was never wired up.
- **Recommendation:** set `aria-current="page"` on the appropriate primary item. For feature detail pages highlight Features; for all docs pages highlight Docs; define a sensible rule for the home and 404 pages.

### NAV-02 — Breadcrumbs exist only for search engines

- **Priority:** P1
- **Affected:** all detail pages with `BreadcrumbList` JSON-LD.
- **Evidence:** page heads contain structured breadcrumb data, but the body renders no breadcrumb component.
- **Impact:** machines receive hierarchy that users do not. This is especially harmful on visually identical feature and docs templates.
- **Recommendation:** render the same breadcrumb data visibly above the H1 and keep the visual and structured versions generated from one source.

### NAV-03 — Mobile navigation is a hidden horizontal scroller

- **Priority:** P1
- **Affected:** all pages at widths below 900px.
- **Evidence:** `.desktop-nav` remains a single-line row with `overflow-x: auto`, while both standard and WebKit scrollbars are hidden. The primary CTA is removed with `display: none`.
- **Impact:** items beyond the viewport have no visible affordance, keyboard focus may move off-screen unexpectedly, and the key “Run Daptin” action disappears.
- **Recommendation:** use an accessible menu button and disclosure panel, or allow a visible wrapped navigation. Keep the primary CTA in the menu. Test keyboard, screen reader, 320px, 375px, 768px, and 200% zoom behavior.

### NAV-04 — The global header has too many equal-weight destinations

- **Priority:** P2
- **Affected:** all pages.
- **Evidence:** Product, Features, Engineering, Use cases, Deploy, Examples, and Docs are presented as seven peers, plus the Run Daptin CTA.
- **Impact:** the distinction between learning what Daptin is, proving it, and implementing it is unclear. At intermediate widths this also causes the hidden-overflow behavior.
- **Recommendation:** group the destinations into a smaller top-level model, for example Product, Solutions, Resources, Docs, with Deploy/Examples/Engineering under an appropriate group.

### NAV-05 — The footer is oversized and repeats the whole site on every page

- **Priority:** P2
- **Affected:** all pages.
- **Evidence:** the footer uses eight heading groups and more than 50 links. On small screens it becomes a single long column. Footer headings are `<h2>` elements, inflating every page’s heading outline.
- **Impact:** it overwhelms short pages, makes page-length cues misleading, and is a poor substitute for contextual navigation. On `/docs/server-configuration/`, the footer contains roughly twice as much text as the entire page body.
- **Recommendation:** reduce the footer to high-value groups and use contextual navigation in the body. Consider non-heading labels or an appropriate footer heading hierarchy that does not dominate the document outline.

### UI-01 — Hero facts and actions have inconsistent spacing

- **Priority:** P1
- **Affected:** `/use-cases/`; compare `/features/sites/` and other `.feature-detail` pages.
- **Evidence:** `.hero-facts` has `margin: 1.25rem 0 0`, so it creates no space below itself. `/use-cases/` places `.button` immediately after the list. `/features/sites/` places its links in `.actions`, which adds `margin-top: 1.5rem` (and receives a feature-detail override of `1.4rem`).
- **Impact:** the three fact tags visually collide with “Open runnable examples,” while nominally similar heroes have different vertical rhythm.
- **Recommendation:** make hero actions a required component immediately following facts, and define the relationship with parent `gap` or a single adjacent-sibling rule. Remove page-specific dependence on incidental margins.
- **Acceptance:** the gap between facts and actions is identical on `/use-cases/`, `/features/sites/`, and all other page heroes at desktop and mobile widths.

### UI-02 — Page taxonomy is not visible in the design

- **Priority:** P1
- **Affected:** feature details and docs details.
- **Evidence:** both use `.feature-detail`, `.page-hero`, `.content-section`, `.split`, `.detail-grid`, `.detail-card`, and `.final-cta`. Several docs are effectively a marketing-card grid followed by a CTA.
- **Impact:** a guide looks like an overview and sets the wrong expectation. Users seeking exact implementation details receive benefit statements or terse summaries.
- **Recommendation:** create distinct templates: marketing feature, conceptual explanation, procedural guide, reference, and operations checklist. Guides need steps, code, tables, notes/warnings, anchors, and verification; feature pages need outcomes and proof.

### UI-03 — Repeated two-column card grids flatten hierarchy

- **Priority:** P2
- **Affected:** nearly all feature pages and many docs pages.
- **Evidence:** unrelated concepts, prerequisites, boundaries, use cases, and steps all use identical white bordered `.detail-card` blocks in a two-column grid.
- **Impact:** everything appears equally important and equally actionable. Sequential processes are visually represented as unordered peers.
- **Recommendation:** use ordered steps for sequences, definition tables for settings, callouts for warnings, diagrams for relationships, and cards only for genuinely parallel choices.

### UI-04 — Typography is too small in navigation, tags, cards, and code

- **Priority:** P1
- **Affected:** all pages.
- **Evidence:** primary nav and CTA are `0.76rem`; eyebrow text `0.67rem`; hero fact tags `0.66rem`; footer labels `0.65rem`; footer links `0.76rem`; several code/card styles are `0.70–0.78rem`.
- **Impact:** reading and target recognition become difficult on high-density screens, mobile devices, and zoomed layouts. Monospace uppercase labels compound the issue.
- **Recommendation:** establish a minimum body/supporting size, preferably 0.875rem or larger for secondary text and 1rem for content; validate WCAG reflow and zoom instead of using very small type to fit the layout.

### UI-05 — Link styling is not globally distinguishable

- **Priority:** P1
- **Affected:** all pages, especially prose links and final CTAs.
- **Evidence:** the global `a` rule removes underlines and inherits text color. Only a few component-specific hover styles restore an affordance.
- **Impact:** links embedded in prose can be indistinguishable from text; users must hunt via hover, which does not exist on touch devices.
- **Recommendation:** underline inline content links by default, reserve button styling for actions, and make visited/focus states clear. Never rely only on color or hover.

### UI-06 — Interactive motion is abrupt and layout-adjacent

- **Priority:** P3
- **Affected:** every `.button`.
- **Evidence:** hover/focus applies `transform: translateY(-2px)` without a transition declaration.
- **Impact:** controls jump on focus, which is distracting and inconsistent with otherwise static pages.
- **Recommendation:** either remove movement or add a subtle, consistent transition while retaining the reduced-motion override. Prefer non-moving focus treatment.

### UI-07 — Visual evidence is concentrated on only three pages

- **Priority:** P2
- **Affected:** most of the site.
- **Evidence:** aside from the logo/footer logo, only the home and product pages contain product screenshots; other feature and docs pages are almost entirely text and cards.
- **Impact:** pages describing dashboard behavior, site configuration, permissions, actions, state tracking, monitoring, and integrations do not show the interface or resulting system, reducing comprehension and credibility.
- **Recommendation:** add purposeful screenshots, annotated configuration examples, data-flow diagrams, and result previews. Each visual should answer a user question, not serve as decoration.

### DOC-01 — Eleven core guides are critically thin

- **Priority:** P0
- **Affected and current `<main>` word counts:** `/docs/clustering/` (85), `/docs/database-setup/` (99), `/docs/email-actions/` (93), `/docs/getting-started/` (154), `/docs/graphql/` (113), `/docs/monitoring/` (104), `/docs/production-deployment/` (116), `/docs/server-configuration/` (85), `/docs/tls-certificates/` (99), `/docs/two-factor-auth/` (87), `/docs/webdav/` (103).
- **Evidence:** these pages consist mainly of a short hero, four terse cards, and a final CTA.
- **Impact:** titles promise “Configure,” “Deploy,” “Monitor,” or “Getting started,” but the pages cannot independently support those tasks.
- **Recommendation:** treat each as unfinished. Add prerequisites, tested version, exact UI/API/CLI path, accepted values and defaults, copyable examples, security implications, verification, rollback, troubleshooting, and related guides. Word count is diagnostic, not the target; task completion is the target.

### DOC-02 — Server configuration is a directory of nouns, not a guide

- **Priority:** P0
- **Affected:** `/docs/server-configuration/`.
- **Evidence:** the full instructional body has four cards totaling roughly 85 words. “Select the driver and connection details, then bound the connection pool” does not state where to select them, which flags or environment variables exist, what formats are accepted, defaults, safe bounds, restart requirements, or how to verify the connection.
- **Impact:** the sentence cannot help a user configure a server and may create false confidence that the page is complete.
- **Recommendation:** replace the summary cards with a configuration reference and task flows. At minimum cover precedence (CLI/environment/config table), database flags and connection-string examples, pool settings/defaults, bind/public URL, request/time limits, storage/site settings, optional-service toggles and ports, secrets, restart semantics, and verification commands. Link to database, TLS, storage, protocols, mail, clustering, monitoring, and deployment guides at the exact relevant sections.

### DOC-03 — Getting started does not demonstrate a complete success path

- **Priority:** P0
- **Affected:** `/docs/getting-started/`.
- **Evidence:** only 154 main-content words support a page titled “Getting started.”
- **Impact:** a new evaluator needs a copy/paste install/run command, expected output, first authenticated or unauthenticated request, model creation, verification, cleanup, and next path. A conceptual four-step summary is not onboarding.
- **Recommendation:** provide one tested 10-minute path with exact commands and expected responses, then branch to Docker/native and deeper guides.

### DOC-04 — Production, monitoring, TLS, clustering, and database guides lack operational depth

- **Priority:** P0
- **Affected:** `/docs/production-deployment/`, `/docs/monitoring/`, `/docs/tls-certificates/`, `/docs/clustering/`, `/docs/database-setup/`.
- **Evidence:** each has 85–116 main-content words and no comprehensive reference tables or runnable procedures.
- **Impact:** operational pages are the highest-risk place for vague copy. Users cannot derive backup scope, restore tests, probes, alert thresholds, certificate renewal, topology, failure behavior, pool sizing, or upgrade procedures.
- **Recommendation:** make them operational runbooks with deployment diagrams, config examples, health semantics, failure modes, checklists with proof, and links between every dependency.

### DOC-05 — Feature relationships are asserted but not explained as a system

- **Priority:** P1
- **Affected:** `/features/sites/` and analogous feature pages.
- **Evidence:** the Sites page mentions data, identity, actions, files, realtime, storage, certificates, scheduler, FTP, APIs, and static output. It does not show a relationship diagram, data entities, permission boundary, template/build path, or links for most of those terms.
- **Impact:** the user cannot answer “what do I configure first?”, “which model owns this?”, “how is access enforced?”, or “how does dynamic data reach a static frontend?”
- **Recommendation:** add a system map: `data model → APIs/actions → built frontend/static files → cloud_store → site route → TLS/auth`, with permissions annotated at each boundary. Link each node to its feature and implementation guide. Explicitly explain templates/build tooling and the limits of static hosting.

### DOC-06 — Feature pages repeat a formula instead of supplying differentiated proof

- **Priority:** P2
- **Affected:** the 19 feature detail pages.
- **Evidence:** most have about 300–345 main words, exactly 13 main headings, the same hero facts, two 2×2 card grids, a boundary statement, and a final CTA.
- **Impact:** distinctive capabilities feel interchangeable; scanning several pages produces repetition rather than deeper understanding. Claims often lack UI screenshots, schema samples, requests/responses, or linked demos.
- **Recommendation:** keep a shared shell but require feature-specific evidence: API features show requests; permissions show a matrix; state tracking shows a state diagram; sites show routing/storage flow; collaboration shows client/server persistence; operations shows signals and topology.

### DOC-07 — Copy often states intent without supplying a decision or action

- **Priority:** P1
- **Affected:** especially the thin docs; also boundary cards across feature pages.
- **Examples:** “Pick deliberately,” “Prepare the rest of the deployment,” “Choose the termination boundary,” “Add monitoring before the launch,” and “Enable only the protocols and integrations the application intends to expose.”
- **Impact:** imperative wording sounds actionable but omits criteria, consequence, location, and method.
- **Recommendation:** edit every instruction to answer: where, exact input/action, allowed/default value, when to choose it, consequence, and how to verify it.

### DOC-08 — No freshness or applicability signal is visible

- **Priority:** P2
- **Affected:** all docs pages.
- **Evidence:** pages do not show the Daptin version tested, last reviewed date, platform assumptions, or source link for the documented behavior.
- **Impact:** users cannot judge whether commands and configuration match their release, especially where older Daptin documentation still ranks in search.
- **Recommendation:** display “Tested with,” “Last reviewed,” source/edit link, and prerequisites on each guide. Generate these values rather than hand-copying them.

### META-01 — Two feature pages canonicalize to the wrong content

- **Priority:** P1
- **Affected:** `/features/mail/`, `/features/protocols/`.
- **Evidence:** their `<link rel="canonical">` values point relatively to `../../docs/mail/` and `../../docs/protocols/`. Their final breadcrumb JSON-LD items repeat those docs paths even though `og:url` points to the feature URLs.
- **Impact:** search engines may consolidate the feature page into the guide page, and the metadata gives contradictory identities for one page.
- **Recommendation:** use absolute self-canonicals and absolute breadcrumb item URLs for the actual feature pages. Add a metadata validator that requires canonical, `og:url`, and breadcrumb leaf to match.

### META-02 — Favicons, theme colors, and social metadata are applied inconsistently

- **Priority:** P3
- **Affected:** 22 pages omit the favicon, 52 omit `theme-color`, and 54 omit `twitter:image`.
- **Evidence:** marketing pages usually contain more complete metadata; many docs and all feature details omit one or more fields.
- **Impact:** browser tabs and shared links feel inconsistent by route, and hand-maintained page heads are drifting.
- **Recommendation:** generate a shared `<head>` template and validate required fields in CI.

### META-03 — Sitemap dates are not trustworthy freshness evidence

- **Priority:** P2
- **Affected:** all URLs in `sitemap.xml`.
- **Evidence:** every entry uses the same future/current audit date `2026-09-02`, independent of page-level content history.
- **Impact:** uniform dates do not tell crawlers or users which pages actually changed and make maintenance signals less credible.
- **Recommendation:** derive `lastmod` from the content source’s last meaningful commit or omit it when reliable dates are unavailable.

### A11Y-01 — Current location and mobile navigation semantics are incomplete

- **Priority:** P1
- **Affected:** all pages.
- **Evidence:** no `aria-current`, no mobile disclosure control, and no visible breadcrumb despite deeply nested content.
- **Impact:** keyboard and screen-reader users receive less orientation than sighted desktop users—and sighted users already receive too little.
- **Recommendation:** address NAV-01 through NAV-03 as accessibility requirements, not only visual enhancements.

### A11Y-02 — Responsive behavior hides controls instead of adapting them

- **Priority:** P1
- **Affected:** all pages below 900px.
- **Evidence:** `.header-cta { display: none; }`; navigation becomes a scrollbar-less overflow region.
- **Impact:** mobile users lose a primary conversion/task action and may never discover later navigation items.
- **Recommendation:** preserve all actions in an accessible mobile menu and test reflow without horizontal page scrolling.

### A11Y-03 — Heading outlines are polluted by footer navigation groups

- **Priority:** P2
- **Affected:** all pages, especially thin docs and the 404.
- **Evidence:** every footer group uses `<h2>`, adding eight apparent content sections after the real page. `/docs/server-configuration/` has seven main headings but fifteen total headings.
- **Impact:** heading navigation suggests that footer directories are peers of the page’s main sections.
- **Recommendation:** add a single hidden or visible footer heading and use list/group labels that preserve a meaningful outline; validate page headings with accessibility tooling.

### QA-01 — Existing automated audit covers only five marketing pages

- **Priority:** P1
- **Affected:** `scripts/audit-site.sh` and the entire site.
- **Evidence:** the script’s `pages` array contains only `/`, `/product/`, `/use-cases/`, `/deploy/`, and `/examples/`. It does not audit the 19 feature pages, 27 docs pages, engineering, 404, link graph, metadata, headings by landmark, or responsive behavior.
- **Impact:** the pages with the largest UX and content problems are outside the guardrail.
- **Recommendation:** expand CI to all HTML pages and add checks for internal links/fragments, current nav state, canonical consistency, required metadata, one H1, landmark/heading structure, content-template requirements, and visual regression at representative breakpoints.

### QA-02 — No local targets are broken, but required links are absent

- **Priority:** P2
- **Affected:** whole site.
- **Evidence:** repository resolution found no missing local targets or fragments. It also found that most detail pages still have only 1–3 unique main-content links.
- **Impact:** a binary link checker can pass while users remain stranded. Validity checks only inspect links authors chose to add; they cannot detect omitted prerequisite, related-feature, example, or next-step links.
- **Recommendation:** add link-graph expectations: minimum contextual links by template, required reciprocal feature/guide links, no orphaned content except intentional utility pages, and per-use-case proof links.

## Page inventory and specific remediation

The following inventory ensures every content route is covered. Systemic findings above apply in addition to the page-specific work below.

| Page(s) | Main inconsistency or missing UX | Recommended content/connection |
|---|---|---|
| `/` | Strongest visual page, but presents many protocols and capabilities before a clear audience choice; footer repeats the taxonomy at greater length. | Add explicit “I want to…” paths to evaluate, model data, add auth, deploy, or operate; preserve proof but shorten the choice surface. |
| `/product/` | Dense, longest page; mixes architecture, benefits, files, actions, integrations, realtime, and optional services without persistent subnavigation. | Add an on-page TOC and link every subsystem to both its feature and guide. |
| `/engineering/` | Technical claims are compact cards with little route to evidence; only three distinct main links. | Link claims to source, tests, operations guidance, and relevant feature/docs pages. |
| `/features/` | Fifty headings and many equal-weight cards make scanning hard. | Add audience/task filters or grouped jump navigation; reduce heading density and clarify category logic. |
| `/use-cases/` | Reported fact-tag/button collision; four scenarios have no inline links to the features, models, guides, or demos they name. | Normalize hero actions and add a curated implementation/proof row to every use case. |
| `/deploy/` | Covers artifacts and production topics on one page but does not consistently bridge each option to exact runbooks. | Connect each artifact to tested commands, persistence, upgrade, health, TLS, and backup guides. |
| `/examples/` | Examples are framed as proof but relationships to use cases and relevant implementation guides are incomplete. | Give each demo prerequisites, expected result, failure proof, related use case, and guide links. |
| `/features/data-modeling/` | Generic card formula; no schema visualization or clear relationship to permissions. | Show a sample entity/relationship model and annotate generated API, IDs, ownership, and permission effects. |
| `/features/apis/` | Protocol choices are described without a decision aid or common model diagram. | Compare JSON:API, GraphQL, metadata, and realtime by task; link to model and permission behavior. |
| `/features/authentication/` | Lifecycle is described but not visualized; permission and 2FA dependencies are underlinked. | Add account lifecycle flow and links to permissions, TOTP, OAuth provider, and runnable auth example. |
| `/features/permissions/` | Rules are represented as generic cards rather than a decision matrix. | Show table/row/owner/group/guest operations as a matrix with worked multi-tenant examples. |
| `/features/oauth-provider/` | Flow claims lack an authorization-code/PKCE sequence diagram. | Add sequence diagram, client model, token lifecycle, security boundaries, example, and guide links. |
| `/features/files/` | Record/storage/access chain is only prose. | Diagram record → file field → cloud store → authorized delivery; link permissions, storage, protocols, and sites. |
| `/features/cloud-storage/` | Provider abstraction is described without setup decision support. | Compare local/MinIO/S3/rclone choices and link files, sites, mail, credentials, and migration guidance. |
| `/features/sites/` | Reported missing system connections; page mentions many dependencies but links only its guide and cloud storage. | Add the end-to-end publishing/data/permission/template diagram described in DOC-05. |
| `/features/actions/` | Multi-step behavior is explained using unordered cards. | Show request → conditions → outcomes → transaction boundary; link permissions, schedules, state, integrations, mail. |
| `/features/scheduled-work/` | Scheduler relationship to actions and acting user is not sufficiently navigable. | Add a lifecycle/timeline, retry/idempotency guidance, and contextual action/permission/operations links. |
| `/features/state-tracking/` | A state-machine feature has no state diagram. | Add a worked transition graph, invalid transition example, history, action boundary, and permission links. |
| `/features/integrations/` | Shared vs per-user credentials are described but not diagrammed. | Add identity/credential flow and links to OAuth, actions, permissions, and runnable provider demo. |
| `/features/ai-routing/` | Provider routing, metering, and streaming boundaries are isolated. | Add client → Daptin → provider flow, capability differences, metering link, credential model, and runnable demo. |
| `/features/realtime/` | Ephemeral notification boundary is stated but no event flow or reconnect UX is shown. | Diagram topics/auth/pubsub/clients and link data model, permissions, clustering, collaboration, and guide. |
| `/features/collaboration/` | Standalone vs record-backed access is critical but buried in copy. | Compare both modes visibly and link persistence, permissions, realtime, files, and editor example. |
| `/features/mail/` | Only one unique main link and an incorrect canonical; operational dependencies are extensive. | Fix metadata; link mail guide, email actions, TLS, DNS/operations, storage, permissions, and a send/receive example. |
| `/features/protocols/` | Only one effective destination is repeated and canonical points to docs. | Fix metadata; split FTP/FTPS, WebDAV-style, and feeds into explicit task paths and related guides. |
| `/features/metering/` | Plan/quota/usage/credit relationships need a model, not four parallel cards. | Add entity/decision flow and link API security, operations signals, AI routing, and runnable quota demo. |
| `/features/operations/` | Broad ops umbrella overlaps `/engineering/`, `/deploy/`, and several docs without clarifying boundaries. | Define scope and route tasks to deploy, configuration, database, monitoring, TLS, clustering, backup, and upgrades. |
| `/docs/` | Useful directory but duplicates Feature guides and offers no learning paths. | Make it the canonical docs home with role/task journeys, search, version, and recently updated content. |
| `/docs/feature-guides/` | Near-duplicate of `/docs/`. | Redirect/merge or turn into ordered implementation paths. |
| `/docs/getting-started/` | 154 words cannot onboard a new user. | Provide one complete, tested, copy/paste quickstart with expected output and cleanup. |
| `/docs/data-modeling/` | More detailed than thin guides but lacks a complete importable model and expected generated result. | Add downloadable schema, relationship example, migration/import behavior, API result, and permissions next step. |
| `/docs/apis/` | Good endpoint breadth but no complete request sequence or navigation within the long guide. | Add auth setup, end-to-end CRUD/query examples, error responses, and API choice table. |
| `/docs/authentication/` | Account lifecycle breadth is good but needs a visible flow and exact prerequisites. | Add lifecycle diagram, endpoint payloads/responses, expiry/revocation behavior, and links to permissions/2FA. |
| `/docs/permissions/` | Many concepts, but no compact test matrix or tenant worked example. | Add role × operation × record matrix, configuration source, expected allow/deny responses, and inheritance rules. |
| `/docs/oauth-provider/` | Needs a complete client setup and token-flow reference that can be followed without guessing. | Add registered-client fields/defaults, PKCE sequence, curl/client example, error cases, rotation/revocation. |
| `/docs/files/` | Describes modes but needs exact upload/download requests and access/cache verification. | Add schema field, store binding, requests/responses, size limits, signed/authorized access tests, cleanup. |
| `/docs/cloud-storage/` | Three-layer concept is useful but setup remains abstract. | Add provider-specific credential/store examples, local first path, verification, sync/migration failures, sites/files links. |
| `/docs/sites/` | One of the stronger guides; still lacks an end-to-end worked deployment and template/build explanation. | Add DNS/TLS/storage/site records, SPA routing, permissions boundary, build/publish workflow, verify and rollback. |
| `/docs/actions/` | Layer model is useful but needs a complete action definition and execution transcript. | Add importable example, inputs/conditions/outcomes, auth, transaction boundary, errors, idempotency, schedule link. |
| `/docs/scheduled-work/` | Conceptual requirements are present, but no complete scheduled-task configuration and observable run. | Add schema/API example, time syntax/timezone, actor, activation/restart, logs, retries, idempotency, disable/rollback. |
| `/docs/state-tracking/` | Explains transitions without a full state definition and response examples. | Add importable graph, valid/invalid calls, history, concurrency, permission, and action side effects. |
| `/docs/integrations/` | Needs a real provider example that covers discovery through user-scoped execution. | Add OpenAPI/provider definition, shared/per-user credentials, calls/responses, token expiry, SSRF/access boundaries. |
| `/docs/ai-routing/` | Provider/client contract is described but configuration fields and tested SDK flow need more specificity. | Add provider/model config, OpenAI SDK example, streaming, capability mismatch, metering, errors, key handling. |
| `/docs/realtime/` | Only 299 words and five main headings for a wire protocol; lacks robust reconnect/error example. | Add handshake/auth/topic format, event schema, reconnect/backoff, lost-event boundary, cluster behavior, runnable client. |
| `/docs/collaboration/` | Needs a complete record-backed and standalone example plus authorization details. | Add connection URLs, Yjs setup, persistence lifecycle, room access, offline/reconnect, deletion/recovery. |
| `/docs/mail/` | Covers components but not enough DNS/TLS/security and executable setup detail. | Add domain records, ports, accounts, relay policy, TLS, storage, SMTP/IMAP test commands, queues/retries/abuse controls. |
| `/docs/protocols/` | Several protocols share one guide, making setup and boundaries hard to scan. | Create anchored per-protocol procedures and link focused WebDAV, sites/FTP, feeds, TLS, and verification. |
| `/docs/metering/` | Entity names are defined but there is no full plan-to-denial setup. | Add data records, request sequence, counters, quota response, concurrency/accounting caveats, reset and observability. |
| `/docs/operations/` | Broad guide overlaps monitoring and production pages; hierarchy is unclear. | Make it an operations hub/runbook and delegate detailed tasks without duplicating vague summaries. |
| `/docs/server-configuration/` | 85-word non-guide; reported sentence is non-actionable. | Replace with complete configuration reference and linked task flows from DOC-02. |
| `/docs/database-setup/` | 99-word choice summary omits commands, connection strings, migrations, backup, TLS, and pools. | Add exact setup per database, defaults, pool sizing criteria, connectivity test, migration/restore, failure messages. |
| `/docs/production-deployment/` | 116-word checklist has no implementation or proof. | Add supported topology, persistence, reverse proxy/TLS, secrets, probes, limits, backups, restore drill, upgrades/rollback. |
| `/docs/monitoring/` | 104-word signal list omits collection, semantics, thresholds, dashboards, and alerts. | Add endpoints/metrics/log fields, scrape examples, alert suggestions, failure interpretation, and links to health checks. |
| `/docs/clustering/` | 85-word component list omits topology and failure behavior. | Add diagram, Olric config, discovery, shared/not-shared state, consistency, node loss, rolling operations, verification. |
| `/docs/graphql/` | 113-word summary does not show a working query or schema behavior. | Add enablement, explorer/introspection, query/mutation/action examples, auth/errors, pagination, REST comparison. |
| `/docs/two-factor-auth/` | 87-word lifecycle list omits enrollment payloads, recovery mechanics, and admin/security behavior. | Add full TOTP setup/confirm/login/recovery flow, codes/responses, replay/rate limits, session invalidation, backup path. |
| `/docs/tls-certificates/` | 99-word option list omits certificate fields, ACME flow, renewal, ports, SNI, and verification. | Add exact Daptin and proxy configurations, DNS/ports, renewal and expiry monitoring, multi-site SNI, test commands. |
| `/docs/email-actions/` | 93-word pattern does not define an action that sends mail. | Add complete action/template/outbox example, validation, permission, delivery/retry semantics, and observable result. |
| `/docs/webdav/` | 103 words do not configure or verify a client; “WebDAV-style” scope is unclear. | State supported methods/limitations, route/auth setup, curl/client examples, permission behavior, errors, compatibility matrix. |
| `/404.html` | Full global footer overwhelms the recovery task; no search or context-sensitive suggestions. | Keep a short recovery page with Home, Docs, Features, and search/sitemap options; do not append the entire directory. |

## Cross-capability link map to implement

This minimum map addresses the reported lack of connection between capabilities. Links should appear at the relevant sentence or diagram node, not only in the footer.

| Capability | Must visibly connect to |
|---|---|
| Data modeling | APIs, permissions, files, state tracking, imports/migrations, examples |
| APIs | data model, authentication, permissions, actions, realtime, metering |
| Authentication | permissions, groups/tenancy, 2FA, OAuth/OIDC provider, sessions |
| Permissions | data model, authentication, files, actions, realtime, collaboration |
| Files | data model, permissions, cloud storage, sites, protocols |
| Sites | cloud storage, files, data APIs, permissions/auth, TLS, FTP/protocols, templates/build, scheduler |
| Actions | permissions, transactions, integrations, state tracking, schedules, mail |
| Scheduled work | actions, acting user/permissions, retries/idempotency, monitoring |
| Integrations | OAuth credentials, permissions, actions, AI routing, examples |
| Realtime | data model, permissions, clustering, collaboration, durability boundary |
| Mail | authentication/accounts, storage, actions, TLS/DNS, monitoring |
| Metering | APIs, identity, plans/credits, AI routing, operations, examples |
| Operations | deployment, configuration, database, TLS, monitoring, clustering, backup/restore, upgrades |

## Recommended implementation order

### Phase 1 — unblock evaluation and setup

1. Rewrite Getting started and Server configuration into complete, tested task pages.
2. Expand Database setup, Production deployment, Monitoring, TLS, and Clustering into operational runbooks.
3. Add docs navigation, visible breadcrumbs, current-page state, and accessible mobile navigation.
4. Fix the `/use-cases/` hero spacing defect and canonical errors on Mail and Protocols.

### Phase 2 — connect the product story

1. Add the cross-capability link map and reciprocal feature/guide relationships.
2. Add per-use-case models, permission explanations, guides, and runnable examples.
3. Add differentiated diagrams and evidence to feature pages, beginning with Sites, Permissions, Actions, State tracking, Integrations, and Realtime.
4. Merge or differentiate `/docs/feature-guides/`.

### Phase 3 — visual and accessibility consistency

1. Replace the hidden horizontal mobile navigation with an accessible disclosure menu.
2. Increase small typography and make inline links visibly identifiable.
3. Reduce/restructure the footer and repair heading outlines.
4. Establish reusable content components for steps, configuration tables, warnings, verification, troubleshooting, diagrams, and related links.

### Phase 4 — prevent regression

1. Expand `scripts/audit-site.sh` from five marketing pages to all HTML files.
2. Add link-graph, canonical/metadata, heading/landmark, and template-completeness checks.
3. Add automated accessibility and visual regression checks at desktop, tablet, mobile, 200% zoom, keyboard-only, and reduced-motion settings.
4. Give every docs page an owner, tested version, and review date.

## Definition of done

The redesign should not be considered complete merely when spacing is uniform. It is complete when:

- a first-time user can run Daptin and verify a result from one page;
- every configuration/operations guide provides exact inputs, examples, verification, failure behavior, and recovery;
- users can see where they are and move to prerequisites, siblings, and next steps without using the footer;
- every feature visibly connects to its data, identity/permission, runtime, and operations dependencies;
- each use case links directly to a model, guide, and runnable proof;
- mobile navigation exposes every destination and the primary CTA accessibly;
- current-page, breadcrumb, link, heading, typography, metadata, and responsive rules are consistent across all routes;
- automated checks cover all 59 HTML files and representative rendered breakpoints.

## Audit limitations

The interactive browser connection was unavailable during this audit. Findings are based on the publishable HTML/CSS, repository-wide structural analysis, link resolution, responsive CSS, and the supplied deployed URLs. The spacing defect is directly provable from the differing markup and CSS rules. A follow-up rendered visual/accessibility pass should verify pixel-level layout, color contrast, focus visibility, reading order, target sizes, and browser-specific behavior after fixes are implemented.
