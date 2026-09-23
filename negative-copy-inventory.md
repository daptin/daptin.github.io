# Negative-framed copy inventory

This inventory covers visible copy in the site HTML. It includes direct negation and negative framing such as **not**, **no**, **never**, **without**, contractions such as **cannot/don’t**, directives such as **stop/avoid/prevent**, contrasts such as **instead of/rather than**, and explicit failure, error, risk, stale, invalid, partial, hidden, disconnected, or similar adverse wording. Each page occurrence records the positive, active, feature-specific replacement applied to the site or an explicit keep-as-is decision.

Excluded: head metadata (including duplicate social titles), global navigation, global footer copy, scripts/styles, breadcrumbs, and redirect-only pages whose body only says that content moved. Short headings and labels are retained because lines such as “Stop…” and “Avoid…” are part of the requested scope.

- **386 unique copy lines**
- **429 page occurrences**
- **55 pages with matches**

## Inventory by page

### [/404.html](404.html)

- “404 · Page not found”
  - **Decision:** Keep as-is.

### [/developers](developers/index.html)

- “Daptin can connect the accounts, access, files, actions, outside services, and live updates around that idea—without making you understand every mechanism first.”
  - **Proposed replacement:** “Create the customer record once, then use it for sign-in, permissions, files, actions, and status updates.”
- “Update live screens, notify connected systems, or let several people collaborate without inventing a separate identity model.”
  - **Proposed replacement:** “Update live screens, notify connected systems, or let several people collaborate.”
- “A client portal can grow without becoming six unrelated backends.”
  - **Proposed replacement:** “Grow a client portal by adding records, accounts, files, actions, integrations, and live updates to one backend.”
- “You do not need to design every surface on day one.”
  - **Proposed replacement:** “Run the quickstart, create the first resource, and add screens as customer workflows demand them.”

### [/](index.html)

- “Build the product—not the pile of services behind it.”
  - **Proposed replacement:** “Data, identity, permissions, files, jobs, integrations, and APIs—ready for your product.”
- “Stop rebuilding the same backend connections for every product.”
  - **Proposed replacement:** “Create a resource once; Daptin connects its accounts, permissions, files, workflows, and integrations.”
- “The expensive part is not finding each piece—it is making identity, data, permissions, files, background work, and outside services behave like one product.”
  - **Proposed replacement:** “A customer, their records, their files, and their permitted actions share one model from the start.”
- “Explore without learning Daptin's internal vocabulary first.”
  - **Proposed replacement:** “Start with a customer workflow and trace its records, people, files, actions, and integrations through Daptin.”
- “Run them from screens, schedules, or connected services without inventing several versions.”
  - **Proposed replacement:** “Run them from screens, schedules, or connected services.”
- “The administration surface is not a concept mockup.”
  - **Proposed replacement:** “Use the administration surface to inspect and update live application records.”
- “Daptin fits small teams and product builders who want a broad, connected backend they can understand and operate without assembling every recurring foundation again.”
  - **Proposed replacement:** “Daptin fits small teams and product builders who want a broad, connected backend they can understand and operate.”
- “Daptin makes that boundary visible instead of hiding it behind a hosted control plane.”
  - **Proposed replacement:** “Daptin exposes deployment, storage, limits, health, certificates, and recovery settings for your team to operate.”

### [/open-source](open-source/index.html)

- “Your product should not become someone else’s hostage.”
  - **Proposed replacement:** “Run Daptin on infrastructure you control, inspect its source, and export your application data.”
- “Open source matters here because it makes architecture, deployment, and portability inspectable—not because it removes operating responsibility.”
  - **Proposed replacement:** “Inspect Daptin’s architecture, deployment path, and portability while your team operates the production instance.”
- “Do not publish exploit details in a public issue.”
  - **Proposed replacement:** “Report vulnerability details privately through GitHub’s security reporting channel.”

### [/operate](operate/index.html)

- “Ownership without mystery”
  - **Proposed replacement:** “See the database, storage, queues, dependencies, limits, logs, and recovery procedures your team operates.”
- “Keep customer records, files, background work, and connected services visible as one operating responsibility—so your team can answer what is healthy, what is failing, and how to bring the product back.”
  - **Proposed replacement:** “Monitor sign-in, file delivery, queue progress, storage, database access, and provider calls; recover each path from a tested runbook.”
- “Health, logs, queues, limits, storage, and dependencies—not just a green process.”
  - **Proposed replacement:** “Check health endpoints, structured logs, queue age, resource limits, storage reachability, and dependency status.”
- “Self-hosting should create control, not guesswork.”
  - **Proposed replacement:** “Use explicit deployment settings, health checks, logs, backups, and rollback procedures to operate the self-hosted instance.”
- “That reduces the number of separate services your team must connect, but it does not make production responsibility disappear.”
  - **Proposed replacement:** “Daptin consolidates backend services while your team owns deployment, monitoring, backups, upgrades, and recovery.”
- “The most useful operating signal is not “the server is up.” It is “the work customers depend on still completes.””
  - **Proposed replacement:** “Test customer sign-in, protected reads, file downloads, email delivery, and scheduled work alongside process uptime.”
- “There is no single switch that makes an application safe.”
  - **Proposed replacement:** “Layer TLS, strong secrets, least-privilege permissions, request controls, monitoring, backups, and tested recovery.”
- “Review table, record, relationship, file, and action access with representative customer identities—not only an administrator.”
  - **Proposed replacement:** “Test table, record, relationship, file, and action access with representative customer accounts and administrator accounts.”
- “It does not prove a customer can sign in, read a protected record, download a file, receive an email, or see scheduled work complete.”
  - **Proposed replacement:** “Run synthetic checks for customer sign-in, protected reads, file downloads, email delivery, and scheduled completion.”
- “Combine those checks with structured logs, database and storage health, queue age, repeated provider failures, and capacity signals.”
  - **Proposed replacement:** “Combine workflow checks with structured logs, database and storage health, queue age, provider status, and capacity metrics.”
- “Set an acceptable amount of lost work and an acceptable recovery time, then make retention and frequency match those promises.”
  - **Proposed replacement:** “Set recovery-point and recovery-time targets, then configure backup frequency and retention to meet them.”
- “Avoid learning the process during an incident.”
  - **Proposed replacement:** “Rehearse backup restoration, rollback, credential rotation, and dependency recovery before an incident.”
- “Practice without risking the live environment.”
  - **Proposed replacement:** “Run restore and rollback drills in an isolated environment that matches production data volume and configuration.”
- “Daptin is self-hosted software, not an operations team.”
  - **Proposed replacement:** “Your team deploys, monitors, backs up, secures, scales, and upgrades each Daptin instance.”

### [/product/architecture](product/architecture/index.html)

- “Make ownership and team membership part of the same model instead of copying rules into every service.”
  - **Proposed replacement:** “Define ownership and team membership once in the relational model and apply them across records, files, actions, and APIs.”
- “Offer records, files, live updates, sites, feeds, or familiar protocols without creating separate realities.”
  - **Proposed replacement:** “Serve the same records and files through APIs, live events, sites, feeds, and supported protocols.”
- “Reuse records, credentials, certificates, permissions or lifecycle instead of creating a parallel backend”
  - **Proposed replacement:** “Reuse the same records, credentials, certificates, permissions, and lifecycle rules across every delivery surface.”
- “Owns startup, readiness, live coordination, failures, and resource bounds”
  - **Proposed replacement:** “Run startup, readiness, live coordination, outcome handling, and resource bounds through the Daptin runtime.”
- “Live delivery uses PubSub and is not a durable event log.”
  - **Proposed replacement:** “Use PubSub for live event fanout and a durable store or broker for retained replay.”
- “Failure rolls back the transaction unless an individual outcome explicitly allows continuation.”
  - **Proposed replacement:** “Keep protected record changes pending until every required outcome completes, then commit the transaction.”
- “Scheduled work is not a bypass.”
  - **Proposed replacement:** “Run scheduled actions with an explicit account and the same permission checks as interactive requests.”
- “Integration execution resolves the credential as the original request user; internal action execution does not silently lend administrator access to another user’s secret.”
  - **Proposed replacement:** “Resolve integration credentials for the original request user and keep each user’s secrets within that authorization context.”
- “The site never calls PubSub itself a durable queue.”
  - **Proposed replacement:** “Describe PubSub as live fanout and direct durable delivery requirements to stored work or a message broker.”
- “Live fanout, not durable replay”
  - **Proposed replacement:** “Use PubSub for live fanout and a durable store for replay.”
- “Network ambiguity prevents an exactly-once promise; DNS/reputation are operator-owned”
  - **Proposed replacement:** “Record delivery attempts and design idempotent messages while operators manage DNS and sender reputation.”
- “No universal compatibility claim; DAV is deliberately scoped”
  - **Proposed replacement:** “Document the supported DAV operations and test every required client workflow against that scope.”

### [/product/capabilities](product/capabilities/index.html)

- “No matching capability.”
  - **Proposed replacement:** “Try a feature name, customer outcome, or operating concern to find the closest capability.”
- “Serve several languages without creating disconnected copies of the product.”
  - **Proposed replacement:** “Store translated fields beside shared records, categories, owners, files, and actions.”
- “Let customers connect outside accounts without sharing their passwords.”
  - **Proposed replacement:** “Let customers authorize outside accounts through OAuth and store delegated access on the backend.”
- “Use outside services without exposing reusable secrets to product clients.”
  - **Proposed replacement:** “Call outside services from backend actions that resolve protected credentials for the authorized user.”
- “Transactions and failure control”
  - **Proposed replacement:** “Control transaction boundaries and action outcomes explicitly.”
- “Keep related record changes together and make failure behavior explicit.”
  - **Proposed replacement:** “Commit required record changes together and declare the continuation rule for each optional outcome.”
- “Run important product behavior at the right time without a separate shadow system.”
  - **Proposed replacement:** “Run important product behavior at the right time.”
- “Move information around record changes without losing whose work it is.”
  - **Proposed replacement:** “Move information through record-triggered actions that retain the initiating user and affected record.”
- “Choose where bytes live without changing what they mean to the product.”
  - **Proposed replacement:** “Move file bytes between local and rclone-backed storage while preserving record identity, ownership, and permissions.”

### [/product/features/actions](product/features/actions/index.html)

- “Expose an operation people understand instead of client-side choreography.”
  - **Proposed replacement:** “Expose invite, publish, archive, send, and synchronize as named backend operations.”
- “Present invite, publish, archive, send, or synchronize—not a sequence of hidden API calls.”
  - **Proposed replacement:** “Present one named invite, publish, archive, send, or synchronize action to the customer.”
- “Improve the action once instead of coordinating updates across every client.”
  - **Proposed replacement:** “Update a named backend action once and give every screen, schedule, API, and integration the revised behavior.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Reuse each action from screens, schedules, integrations, and APIs with the same permissions.”
- “Include outside services without moving orchestration into the frontend.”
  - **Proposed replacement:** “Add provider calls to backend actions alongside validation, record updates, templates, and events.”
- “Actions are declarative backend operations, not an unlimited visual workflow suite.”
  - **Proposed replacement:** “Use Daptin actions for declarative backend operations and choose a dedicated visual workflow tool for process authoring.”
- “Make actions part of the product—not another disconnected service.”
  - **Proposed replacement:** “Define an action once; screens, schedules, APIs, and integrations run the same permissioned operation.”

### [/product/features/admin](product/features/admin/index.html)

- “Manage data without building an internal tool first”
  - **Proposed replacement:** “Inspect and update live records, relationships, and files in the generated administration interface.”
- “Your first internal tool should not delay your first customer-facing feature.”
  - **Proposed replacement:** “Add specialized editorial, support, or analytics interfaces for workflows that need them.”
- “That makes the admin useful as a starting point, an operational window, and a source of product proof—not a disconnected demo database.”
  - **Proposed replacement:** “Use the generated admin to inspect live records, verify permissions, and support early customer workflows.”
- “The administration interface works with live application records, not a separate management copy.”
  - **Proposed replacement:** “The administration interface works with live application records.”
- “Authorized teammates can inspect and manage structured information without writing API requests.”
  - **Proposed replacement:** “Authorized teammates can inspect and manage structured information.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Use the same model and permissions in the administration UI and customer-facing APIs.”
- “It is not a replacement for every specialized editorial, support, or analytics experience your team may eventually need.”
  - **Proposed replacement:** “Use the generated administration UI for record operations, then add specialized editorial, support, or analytics interfaces as workflows mature.”
- “Make administration part of the product—not another disconnected service.”
  - **Proposed replacement:** “Model a resource and Daptin gives authorized teammates a live screen to inspect and update it.”

### [/product/features/aggregations](product/features/aggregations/index.html)

- “Count, group, compare, and summarize the records already powering your product—without first copying them into a separate reporting service.”
  - **Proposed replacement:** “Count, group, compare, and summarize live application records through backend aggregations.”
- “Power summaries without hand-writing a reporting endpoint for each question.”
  - **Proposed replacement:** “Define reusable aggregations for totals, grouped counts, comparisons, and time-based summaries.”
- “People need answers, not another export-and-spreadsheet ritual.”
  - **Proposed replacement:** “Answer operational questions directly from grouped, counted, and summarized application records.”
- “An operator wants failed jobs by day.”
  - **Proposed replacement:** “Group job records by completion state and day so operators can track unsuccessful runs over time.”
- “Because the report starts from the same application records, the team does not have to maintain a second definition of what a request, owner, or status means.”
  - **Proposed replacement:** “Build each report from the request, owner, and status fields already used by the application.”
- “Summarize pending, completed, and failed work over time.”
  - **Proposed replacement:** “Chart work by status and time period from the live operational records.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Build dashboards from the same request, owner, status, and permission definitions that power the product.”
- “It is not a full analytical warehouse, visualization suite, or substitute for a dedicated BI system when scale and modelling needs demand one.”
  - **Proposed replacement:** “Use Daptin for operational aggregates and connect a warehouse or BI platform for large-scale analytical modelling.”
- “Make reports and aggregations part of the product—not another disconnected service.”
  - **Proposed replacement:** “Count, group, and compare the records already serving your product.”

### [/product/features/audit-history](product/features/audit-history/index.html)

- “Review the sequence instead of guessing”
  - **Proposed replacement:** “Open the record history and read each stored change and state transition in order.”
- “Give operators and product teams a place to begin when something looks wrong.”
  - **Proposed replacement:** “Start investigations from the affected record, its change history, and its state transitions.”
- “Without history, a surprising record becomes a debate about memory.”
  - **Proposed replacement:** “Use stored change evidence to explain how a record reached its current value.”
- “The current row shows the outcome but not the path that produced it.”
  - **Proposed replacement:** “Show the current row together with the ordered changes that produced it.”
- “The evidence remains connected to the underlying record rather than living in a separate spreadsheet.”
  - **Proposed replacement:** “The evidence remains connected to the underlying record.”
- “Review the sequence behind a record instead of only its latest state.”
  - **Proposed replacement:** “Review each stored change and transition that produced the record’s current state.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Review who changed a record, what changed, and how its state progressed from one history trail.”
- “Audit history is an application capability, not a compliance certification.”
  - **Proposed replacement:** “Use audit history as record-level evidence and apply your organization’s retention, immutability, access, and compliance controls.”
- “Make audit history part of the product—not another disconnected service.”
  - **Proposed replacement:** “Keep each record’s change trail beside the data your team investigates.”

### [/product/features/authentication](product/features/authentication/index.html)

- “Handle account creation, sign-in, sessions, password recovery, and optional one-time codes without creating a separate identity backend.”
  - **Proposed replacement:** “Handle account creation, sign-in, sessions, password recovery, and optional one-time codes.”
- “A login screen is the beginning, not the identity system.”
  - **Proposed replacement:** “Create accounts, verify credentials, issue sessions, recover access, and connect each signed-in account to its records and groups.”
- “Because accounts live in the same model as groups, ownership, and records, identity becomes useful application context rather than a token checked at the edge and forgotten.”
  - **Proposed replacement:** “Each signed-in account carries its groups and record ownership into APIs, files, and actions.”
- “Avoid rebuilding common account flows”
  - **Proposed replacement:** “Create accounts, verify credentials, issue sessions, recover access, and verify one-time codes in Daptin.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Carry the signed-in account into ownership, groups, permissions, files, and actions.”
- “Authentication features do not remove the need for secure transport, strong signing and encryption secrets, account-abuse controls, email deliverability, administrator protection, and a deliberate session lifetime.”
  - **Proposed replacement:** “Configure TLS, signing and encryption secrets, sign-in throttling, recovery email, administrator access, and session lifetimes.”
- “Make authentication part of the product—not another disconnected service.”
  - **Proposed replacement:** “Accounts, sessions, recovery, and one-time codes use the same identity that owns records and joins groups.”

### [/product/features/certificates](product/features/certificates/index.html)

- “The deployment must connect hostnames, certificate material, listeners, renewal, and failure handling.”
  - **Proposed replacement:** “Your team schedules renewal, validates reachability, rotates keys, and monitors certificate expiry.”
- “That brings TLS into the same operating picture as the services it protects, instead of leaving it as an invisible manual step on one server.”
  - **Proposed replacement:** “Manage each hostname, certificate, listener, and renewal check beside the service it protects.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Manage TLS configuration beside the services, hostnames, and deployment settings it protects.”
- “Certificate generation is not automatic lifecycle management.”
  - **Proposed replacement:** “Generate certificate material in Daptin, then schedule renewal, validate reachability, rotate keys, and monitor expiry.”
- “Make tls certificates part of the product—not another disconnected service.”
  - **Proposed replacement:** “Attach generated TLS certificates to the hostnames and listeners serving your application.”

### [/product/features/cloud-storage](product/features/cloud-storage/index.html)

- “Connect local or rclone-backed storage to records and sites, so changing where bytes live does not require changing what they mean.”
  - **Proposed replacement:** “Your team validates credentials, consistency, regions, encryption, recovery, costs, and provider quotas.”
- “Avoid remodelling the application”
  - **Proposed replacement:** “Keep the same file records, ownership, and permissions when switching storage providers.”
- “Your storage provider should hold the bytes, not define your product.”
  - **Proposed replacement:** “Keep product identity, ownership, and permissions in Daptin while the selected provider stores the bytes.”
- “Move or synchronize content without teaching clients a new object-store contract.”
  - **Proposed replacement:** “Move or synchronize content through Daptin file records while clients keep the same API contract.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Keep record identity, ownership, and permissions stable when bytes move between storage providers.”
- “Rclone supports many providers, but that is not a promise that every provider and option is tested.”
  - **Proposed replacement:** “Validate the exact rclone provider, operations, credentials, consistency, and options used by your deployment.”
- “Make cloud storage part of the product—not another disconnected service.”
  - **Proposed replacement:** “Move file bytes between local and cloud storage while record identity and access stay consistent.”

### [/product/features/clustering](product/features/clustering/index.html)

- “Use the distributed runtime for cache, live event fanout, counters, and shared claims when one application instance is no longer the whole topology.”
  - **Proposed replacement:** “Share cache entries, live event fanout, counters, and queue claims across every Daptin node.”
- “Adding nodes should not create several independent versions of the same live backend.”
  - **Proposed replacement:** “Share caches, event fanout, counters, and queue claims so every Daptin node sees the same runtime state.”
- “Rate counters, permission caches, and queue claims also need a shared view or the cluster behaves like unrelated servers.”
  - **Proposed replacement:** “Give rate counters, permission caches, and queue claims a cluster-wide shared view.”
- “Clustering coordinates Daptin nodes; it does not automatically make every dependency highly available.”
  - **Proposed replacement:** “Use Daptin clustering for shared runtime state and provide highly available databases, storage, networking, and load balancing.”
- “Reduce stale runtime decisions”
  - **Proposed replacement:** “Synchronize permission caches, rate counters, and background claims across the cluster.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Give every node the same view of permission caches, rate counters, live events, and background claims.”
- “Clustering is not automatic high availability.”
  - **Proposed replacement:** “Combine Daptin clustering with redundant databases, shared storage, load balancing, health checks, capacity planning, and recovery tests.”
- “You own peer networking, discovery, load balancing, shared database and storage, split-brain risks, rolling changes, capacity, and recovery testing.”
  - **Proposed replacement:** “Operate peer discovery, load balancing, shared databases, shared storage, rolling updates, capacity, and cluster recovery tests.”
- “Make clustering and distributed state part of the product—not another disconnected service.”
  - **Proposed replacement:** “Add Daptin nodes while caches, counters, live events, and queue claims stay coordinated.”

### [/product/features/collaboration](product/features/collaboration/index.html)

- “Let several people work in the same document without overwriting one another.”
  - **Proposed replacement:** “Let several people work in the same document.”
- “Persist the collaborative document instead of treating it as an ephemeral chat.”
  - **Proposed replacement:** “Save collaborative document state as application data after participants edit the shared room.”
- “A shared document should feel like one place, not a race between Save buttons.”
  - **Proposed replacement:** “Synchronize edits through one document room and persist the resulting collaborative state.”
- “Building collaborative state as a separate service also risks bypassing document access.”
  - **Proposed replacement:** “Apply the document’s ownership and permission rules when participants join its collaboration room.”
- “See changes and collaborator awareness without refreshing the whole record.”
  - **Proposed replacement:** “Stream document changes and participant presence to everyone in the collaboration room.”
- “Isolate updates by document room rather than broadcasting them across the product.”
  - **Proposed replacement:** “Send collaborative updates only to participants authorized for the matching document room.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Persist collaborative document state beside its record, ownership, and access rules.”
- “It is not a full editor, commenting system, version-review product, or guaranteed offline merge experience by itself.”
  - **Proposed replacement:** “Use Daptin for collaborative state synchronization and add the editor, comments, review flow, and offline experience your product requires.”
- “Make live collaboration part of the product—not another disconnected service.”
  - **Proposed replacement:** “Give each document a shared editing room protected by its existing record permissions.”

### [/product/features/configuration](product/features/configuration/index.html)

- “Manage environment-aware runtime settings for services, limits, logging, and behavior without hiding the deployment contract across unrelated scripts.”
  - **Proposed replacement:** “Manage environment-aware runtime settings for services, limits, logging, and behavior.”
- “This improves visibility but does not make every setting safe to change live.”
  - **Proposed replacement:** “Show runtime settings explicitly and apply restart-sensitive changes through a tested deployment procedure.”
- “Avoid treating local defaults as production policy.”
  - **Proposed replacement:** “Your team validates production values, restart requirements, change procedures, secrets, and rollback plans.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Keep environment-specific settings visible beside the services and deployment they control.”
- “Make configuration part of the product—not another disconnected service.”
  - **Proposed replacement:** “Set service ports, paths, limits, origins, and logging through one runtime configuration.”

### [/product/features/credentials](product/features/credentials/index.html)

- “Use outside services without putting their secrets in your product screens.”
  - **Proposed replacement:** “Call providers from authorized backend actions that resolve protected credentials.”
- “The browser never needs the reusable secret”
  - **Proposed replacement:** “Keep reusable provider credentials in protected backend records.”
- “Avoid shipping provider keys to browsers or mobile apps.”
  - **Proposed replacement:** “Resolve provider keys on the server after checking the caller’s permission.”
- “Rotate without redesigning the product”
  - **Proposed replacement:** “Rotate a stored provider credential once and let every authorized action use the replacement.”
- “A useful integration should not turn a provider key into an application-wide secret.”
  - **Proposed replacement:** “Store each provider key as a protected credential and resolve it only for authorized actions.”
- “Treat credentials as protected application data rather than ambient configuration.”
  - **Proposed replacement:** “Store credentials as protected application records with explicit ownership and access rules.”
- “Replace or revoke a connection without teaching every client a new secret.”
  - **Proposed replacement:** “Replace or revoke one stored connection and let authorized clients keep the same product action.”
- “Call a CRM, support tool, or provider without exposing its key.”
  - **Proposed replacement:** “Call CRM, support, and provider APIs from backend actions that resolve stored credentials.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Connect CRM, support, storage, and provider calls while keeping reusable credentials on the server.”
- “Connect file storage without changing record ownership.”
  - **Proposed replacement:** “Attach storage credentials to file operations while Daptin retains record ownership and access rules.”
- “Make credentials part of the product—not another disconnected service.”
  - **Proposed replacement:** “Keep provider secrets on the backend and resolve them only for authorized calls.”

### [/product/features/data-exchange](product/features/data-exchange/index.html)

- “Move application data where it needs to go without losing who the work belongs to.”
  - **Proposed replacement:** “Move application data where it needs to go.”
- “Standalone scripts can move data, but they often lose the original user, product context, and failure boundary.”
  - **Proposed replacement:** “Run each transfer as a named action that records its initiating user, affected records, mapping, and outcome.”
- “That keeps the exchange connected to the record lifecycle and makes its responsibility easier to understand than an unrelated background script.”
  - **Proposed replacement:** “Attach each exchange to the affected record lifecycle and show its owner, action, and recorded outcome.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Run imports, exports, and provider transfers through named actions with explicit ownership and mapping.”
- “Data exchange is not automatically conflict-free or exactly once.”
  - **Proposed replacement:** “Define ownership, idempotency keys, conflict policy, retry behavior, and replay handling for every data exchange.”
- “Define ownership, mapping, retries, replay safety, provider limits, and what happens when the outside system is unavailable.”
  - **Proposed replacement:** “Declare transfer ownership, field mappings, idempotency, retry policy, provider quotas, and recovery steps.”
- “Make data exchange part of the product—not another disconnected service.”
  - **Proposed replacement:** “Move records between systems with the initiating user, field mapping, and retry policy attached.”

### [/product/features/data-modeling](product/features/data-modeling/index.html)

- “Model real business ideas instead of hand-writing plumbing.”
  - **Proposed replacement:** “Define customers, projects, orders, content, and their relationships as one relational model.”
- “The backend follows deliberate model changes instead of drifting across services.”
  - **Proposed replacement:** “Apply deliberate field and relationship changes to the shared model, APIs, administration, and permissions.”
- “Your product should not have five different versions of the same idea.”
  - **Proposed replacement:** “Define each customer, project, order, and content concept once in the shared relational model.”
- “The result is not merely a generated database.”
  - **Proposed replacement:** “Generate APIs, administration, permissions, files, actions, and events from the relational model.”
- “Create a relational foundation without first building migrations, CRUD handlers, and an admin surface by hand.”
  - **Proposed replacement:** “Create the relational model and let Daptin generate migrations, resource APIs, and administration views.”
- “Grow without losing the map”
  - **Proposed replacement:** “Extend the model with explicit fields and relationships that remain visible in APIs and administration.”
- “Attach permissions, files, actions, events, and services without remodelling the product.”
  - **Proposed replacement:** “Attach permissions, files, actions, events, and services to the existing relational model.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Generate APIs, administration, permissions, files, actions, events, and services from the shared model.”
- “See and manage the live model without building an internal tool first.”
  - **Proposed replacement:** “Inspect and update the live model through Daptin’s generated administration interface.”
- “Daptin gives the model a running backend, but it does not decide your product vocabulary for you.”
  - **Proposed replacement:** “Use Daptin to run the model while your product team defines its domain terms, relationships, and constraints.”
- “Make data models part of the product—not another disconnected service.”
  - **Proposed replacement:** “Define a resource once; APIs, administration, permissions, files, actions, and events follow its model.”

### [/product/features/databases](product/features/databases/index.html)

- “Infrastructure choice does not redefine the product”
  - **Proposed replacement:** “Your team matches engine choice, pools, backups, restore tests, and capacity plans to production concurrency.”
- “Choosing a database should be an operating decision, not a rewrite of the product.”
  - **Proposed replacement:** “Choose SQLite, MySQL, or PostgreSQL for the deployment while keeping the Daptin model and API contract stable.”
- “Avoid operating a separate database when an embedded one truly fits.”
  - **Proposed replacement:** “Use SQLite for deployments whose concurrency, backup, and availability needs fit an embedded database.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Keep the model and API contract stable when deployment moves between supported database engines.”
- “Supported engines do not have identical concurrency or operational characteristics.”
  - **Proposed replacement:** “Load-test the selected engine and configure its pools, backups, recovery, and capacity for the production workload.”
- “Make database choices part of the product—not another disconnected service.”
  - **Proposed replacement:** “Choose SQLite, MySQL, or PostgreSQL while the resource model and API contract stay consistent.”

### [/product/features/dav](product/features/dav/index.html)

- “Avoid a proprietary client requirement”
  - **Proposed replacement:** “Expose supported files and collections through Daptin’s DAV-style endpoints.”
- “Know that basic file and collection access is supported—not complete calendar semantics.”
  - **Proposed replacement:** “Know that basic file and collection access is supported.”
- “Offering a familiar path can avoid building a custom synchronization client for basic file access.”
  - **Proposed replacement:** “Teams test required WebDAV, CalDAV, and CardDAV operations against each client before adoption.”
- “Those paths build on document and collection storage rather than creating a separate data island.”
  - **Proposed replacement:** “Those paths build on document and collection storage.”
- “The deliberate boundary matters: this is basic DAV-style access, not a claim of full calendar or contact server compatibility.”
  - **Proposed replacement:** “The deliberate boundary matters: this is basic DAV-style access.”
- “Adopt for the supported operation set without assuming every calendar or address-book feature.”
  - **Proposed replacement:** “Adopt Daptin for the documented DAV operations after testing each required calendar and address-book workflow.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Let compatible file clients reach document and collection storage through familiar paths.”
- “Daptin does not claim complete CalDAV or CardDAV semantics.”
  - **Proposed replacement:** “Adopt Daptin for its documented DAV operation set and test every required calendar or contact client operation.”
- “Make dav-style access part of the product—not another disconnected service.”
  - **Proposed replacement:** “Connect compatible file clients to the same documents, collections, and permissions used by your application.”

### [/product/features/deployment](product/features/deployment/index.html)

- “Prepare for change and failure”
  - **Proposed replacement:** “Keep pinned artifacts, tested backups, restore procedures, and rollback steps ready for each deployment.”
- “Monitor, back up, restore, upgrade, and roll back the whole system.”
  - **Proposed replacement:** “Operate the database, file storage, secrets, listeners, queues, and Daptin binary as one deployment.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Deploy, monitor, back up, restore, upgrade, and redeploy a pinned previous release for the complete Daptin stack.”
- “Daptin is self-hosted software, not a managed control plane.”
  - **Proposed replacement:** “Your team provisions infrastructure, deploys Daptin, monitors health, performs backups, and applies upgrades.”
- “Make deployment part of the product—not another disconnected service.”
  - **Proposed replacement:** “Deploy one self-hosted runtime for APIs, files, jobs, mail, and integrations.”

### [/product/features/documents-collections](product/features/documents-collections/index.html)

- “Build the next part without starting over.”
  - **Proposed replacement:** “Use document and collection records across APIs, administration, sites, feeds, and synchronization.”
- “Documents and collections are foundational records, not a complete document-management or records-retention suite.”
  - **Proposed replacement:** “Use documents and collections as application records, then add the retention, review, versioning, and publication workflows your domain requires.”
- “Make documents and collections part of the product—not another disconnected service.”
  - **Proposed replacement:** “Store documents in collections that already work with permissions, files, APIs, sites, and feeds.”

### [/product/features/event-publication](product/features/event-publication/index.html)

- “Publish a named topic from an action so connected clients can respond to business events, not only raw record changes.”
  - **Proposed replacement:** “Publish a named topic from an action so connected clients can respond to business events.”
- “Publish “request approved” instead of forcing clients to infer it.”
  - **Proposed replacement:** “Publish a request-approved topic when the approval action completes.”
- “A client can observe that a status field changed, but it may not know that a review completed, an import finished, or a publication became live.”
  - **Proposed replacement:** “Use a durable broker when consumers require retained messages and replay.”
- “Connected clients can then refresh the right view or start the next experience without each one reverse-engineering the database change.”
  - **Proposed replacement:** “Connected clients can then refresh the right view or start the next experience.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Let permitted clients subscribe to product events and refresh the relevant experience.”
- “Topic publication is live delivery, not a durable message bus.”
  - **Proposed replacement:** “Use topic publication for live client updates and a durable broker for retained delivery and replay.”
- “Make custom event publication part of the product—not another disconnected service.”
  - **Proposed replacement:** “Publish a named business event from an action so subscribed clients know exactly what completed.”

### [/product/features/feeds](product/features/feeds/index.html)

- “Offer standards instead of lock-in”
  - **Proposed replacement:** “Publish selected records through RSS, Atom, or JSON Feed for standard feed readers.”
- “Not every useful product experience needs another app screen or notification channel.”
  - **Proposed replacement:** “Publish records through RSS, Atom, or JSON Feed so customers can follow updates in tools they already use.”
- “This extends the product through established formats and gives people a low-friction way to follow information without learning a Daptin-specific client.”
  - **Proposed replacement:** “This extends the product through established formats and gives people a low-friction way to follow information.”
- “Avoid copying updates into a separate feed-only content store.”
  - **Proposed replacement:** “Generate feeds from the same published records, categories, owners, and permissions used by the product.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Let customers follow product updates from standard feed readers and existing tools.”
- “Feeds are pull-based publication, not realtime push or guaranteed delivery.”
  - **Proposed replacement:** “Use feeds for reader-driven updates and realtime events or messaging for immediate delivery workflows.”
- “Make rss, atom, and json feeds part of the product—not another disconnected service.”
  - **Proposed replacement:** “Publish existing records as RSS, Atom, or JSON Feed from the same categories and ownership rules.”

### [/product/features/files-images](product/features/files-images/index.html)

- “Avoid a separate file identity system”
  - **Proposed replacement:** “Attach every file to an application record with shared ownership and permissions.”
- “When files live in a disconnected bucket, every application feature must rebuild that ownership and access context.”
  - **Proposed replacement:** “Represent stored bytes as Daptin file records so APIs, actions, sites, and transformations reuse their ownership and access context.”
- “The same file can then participate in APIs, administration, image transformations, actions, sites, and synchronization without becoming an ungoverned side channel.”
  - **Proposed replacement:** “The same file can then participate in APIs, administration, image transformations, actions, sites, and synchronization.”
- “Use record access rather than relying on hard-to-audit public object URLs.”
  - **Proposed replacement:** “Attach files and images to records with the same ownership and permission context.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Use one file record across APIs, administration, image transformations, actions, sites, and synchronization.”
- “Make files and images part of the product—not another disconnected service.”
  - **Proposed replacement:** “Attach a file to a record once; APIs, actions, sites, and image transforms keep its owner and permissions.”

### [/product/features/ftp](product/features/ftp/index.html)

- “Let established file clients manage published content without escaping its site boundary.”
  - **Proposed replacement:** “Let established FTP or FTPS clients manage published content inside an enforced site root.”
- “Reject path escape and cross-site movement.”
  - **Proposed replacement:** “Confine every FTP operation to its configured site root and permitted path.”
- “The file client works with a familiar directory view while the backend guards the permitted site boundary and rejects path escape or cross-site rename.”
  - **Proposed replacement:** “Give file clients a familiar directory view while Daptin enforces site-root paths and same-site rename rules.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Map each file session to one site boundary and enforce path and rename rules there.”
- “FTP sends credentials and content without transport protection unless FTPS is correctly configured.”
  - **Proposed replacement:** “Configure FTPS with valid certificates and protected credentials for encrypted file transfers.”
- “Make ftp and ftps part of the product—not another disconnected service.”
  - **Proposed replacement:** “Expose a site root to FTP or FTPS clients while Daptin confines every path to that site.”

### [/product/features/graphql](product/features/graphql/index.html)

- “Give data-heavy interfaces a flexible query surface without creating a second model or a second set of access rules.”
  - **Proposed replacement:** “Give data-heavy interfaces GraphQL field selection over the shared model and record permissions.”
- “Rich screens should not force the backend into a collection of screen-specific endpoints.”
  - **Proposed replacement:** “Use GraphQL field selection and relationships to serve data-heavy screens from the shared model.”
- “Teams can use the predictable resource API for ordinary flows and GraphQL for views that benefit from nested selection, without splitting the application's meaning across two backends.”
  - **Proposed replacement:** “Teams can use the predictable resource API for ordinary flows and GraphQL for views that benefit from nested selection.”
- “Avoid over-fetching a full record when a compact view needs only a few fields.”
  - **Proposed replacement:** “Query related records through GraphQL with field selection and shared access rules.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Use resource APIs for predictable flows and GraphQL for screens that need nested, selective reads.”
- “GraphQL changes how clients select data; it does not remove the need to design good relationships or prevent inherently expensive queries.”
  - **Proposed replacement:** “Design clear relationships, pagination, query budgets, and caching around the GraphQL selection surface.”
- “Make graphql part of the product—not another disconnected service.”
  - **Proposed replacement:** “Query related records through GraphQL under the same model and permissions as the resource APIs.”

### [/product/features/import-export](product/features/import-export/index.html)

- “Avoid a blank-slate migration”
  - **Proposed replacement:** “Import spreadsheet data into Daptin records and export product records for analysis or migration.”
- “Export product data instead of trapping it behind a UI.”
  - **Proposed replacement:** “Export selected application records into portable structured files for analysis or migration.”
- “Adopting a backend should not mean re-entering everything by hand.”
  - **Proposed replacement:** “Import existing spreadsheet rows into mapped Daptin records during adoption.”
- “Move useful spreadsheet structure into a backend instead of discarding it.”
  - **Proposed replacement:** “Map spreadsheet columns and relationships into Daptin records during import.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Map spreadsheet columns to the application model and preserve useful structure during onboarding.”
- “Import cannot infer every business rule from a spreadsheet, and export alone is not a complete backup.”
  - **Proposed replacement:** “Validate imported business rules and maintain database, file, configuration, and secret backups alongside exports.”
- “Make import and export part of the product—not another disconnected service.”
  - **Proposed replacement:** “Map spreadsheet columns into records and export those records through a portable structured format.”

### [/product/features/integrations](product/features/integrations/index.html)

- “Bring useful provider operations into Daptin, connect approved credentials, and use them inside product actions instead of exposing integration plumbing to customers.”
  - **Proposed replacement:** “Bring useful provider operations into Daptin, connect approved credentials, and use them inside product actions.”
- “Customers do not want an API integration.”
  - **Proposed replacement:** “Give customers a named outcome such as import-from-storage, enrich-lead, or send-to-support.”
- “The provider is a component of the experience, not the experience itself.”
  - **Proposed replacement:** “Wrap each provider call in a named action that validates input, updates records, and returns the result the screen needs.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Keep provider credentials in the backend and combine each call with records, templates, schedules, and events.”
- “Daptin supports compatible operations, but you must inspect the generated inputs, test authentication and error cases, respect provider terms and limits, and avoid promising universal compatibility.”
  - **Proposed replacement:** “Your team inspects generated inputs and tests authentication, responses, quotas, terms, and compatibility.”
- “Make integrations part of the product—not another disconnected service.”
  - **Proposed replacement:** “Turn a compatible provider operation into a backend action with stored credentials and record updates.”

### [/product/features/large-files](product/features/large-files/index.html)

- “Move large files without forcing every byte through one fragile path.”
  - **Proposed replacement:** “Send large files through multipart, ranged, cached, or provider-assisted transfer paths.”
- “Transfer strategy can change without losing context”
  - **Proposed replacement:** “Switch transfer strategies while preserving the file record, owner, permissions, and application reference.”
- “A product video and a profile icon should not be forced through the same transfer assumptions.”
  - **Proposed replacement:** “Use multipart or provider-assisted upload for product video and a direct image path for profile icons.”
- “Large media, archives, and documents may need multipart upload, storage-provider handoff, ranged reads, or caching to avoid fragile transfers and repeated work.”
  - **Proposed replacement:** “Upload and deliver large media, archives, and reports through multipart, ranged, cached, or provider-assisted paths.”
- “That separation lets the team improve delivery without turning the storage provider into the product's source of identity.”
  - **Proposed replacement:** “Tune multipart upload, ranged reads, and caching while Daptin retains file identity and ownership.”
- “Let clients work with application records rather than provider-specific object identities.”
  - **Proposed replacement:** “Give clients Daptin file records while the backend resolves provider-specific object identifiers.”
- “Move sizeable reports or evidence without one monolithic request.”
  - **Proposed replacement:** “Transfer sizeable reports and evidence through multipart uploads or ranged downloads.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Keep the record, owner, permissions, and file identity stable across transfer strategies.”
- “Make large-file delivery part of the product—not another disconnected service.”
  - **Proposed replacement:** “Use multipart upload, ranged reads, caching, or provider handoff while clients keep one file record.”

### [/product/features/localization](product/features/localization/index.html)

- “Avoid duplicate content silos”
  - **Proposed replacement:** “Store translated fields beside the shared record, category, owner, files, and actions.”
- “Add languages without cloning the entire backend.”
  - **Proposed replacement:** “Add translated fields to the existing content records and relationships.”
- “A new language should not create a second, disconnected product catalogue.”
  - **Proposed replacement:** “Store each translation beside the shared product record, category, owner, files, and actions.”
- “Categories, files, owners, and actions do not need to be reinvented per language.”
  - **Proposed replacement:** “Reuse the same categories, files, owners, and actions for every localized record.”
- “Translate the records and languages that matter without duplicating everything.”
  - **Proposed replacement:** “Add translated fields to selected records while reusing their categories, owners, files, and actions.”
- “Localize articles without splitting categories and ownership.”
  - **Proposed replacement:** “Store localized article fields while every locale shares the same categories and owner.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Add locales to articles and catalogues while every translation uses the same relationships.”
- “Localization organizes translated application data; it does not translate copy automatically or decide editorial fallback, locale negotiation, cultural adaptation, or translation-review workflow.”
  - **Proposed replacement:** “Use Daptin to organize localized records while your team supplies translation, fallback, locale negotiation, cultural adaptation, and review.”
- “Make localized data part of the product—not another disconnected service.”
  - **Proposed replacement:** “Add translated fields to a record while its categories, owner, files, and actions stay consistent.”

### [/product/features/mail](product/features/mail/index.html)

- “Email becomes more valuable when it stops being an isolated inbox.”
  - **Proposed replacement:** “Connect incoming and outgoing email to customer records, permissions, actions, and workflows.”
- “Outbound work can enter a persisted queue instead of disappearing into an unobservable send call.”
  - **Proposed replacement:** “Persist outbound messages with recipient, content, attempt history, and next retry time.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Connect messages and outbound queues to customer records, permissions, actions, and workflows.”
- “Operating internet mail requires DNS, MX routing, reverse DNS, SPF, DKIM, DMARC, reputation, spam and abuse controls, port access, monitoring, and backup.”
  - **Proposed replacement:** “Operate MX, SPF, DKIM, DMARC, reverse DNS, sender reputation, spam controls, monitoring, and backups.”
- “Daptin supplies mail capabilities, not managed deliverability.”
  - **Proposed replacement:** “Daptin receives, stores, queues, and sends mail; your team manages DNS, sender reputation, spam controls, monitoring, and backups.”
- “Make mail server part of the product—not another disconnected service.”
  - **Proposed replacement:** “Receive, store, queue, and send mail as records connected to customers and workflows.”

### [/product/features/monitoring](product/features/monitoring/index.html)

- “The process may answer while sign-in fails, the database is saturated, files cannot reach storage, or a queue is falling behind.”
  - **Proposed replacement:** “Check sign-in, database capacity, storage reachability, and queue age alongside process health.”
- “Treating one ping as proof of the whole product hides the failures that matter.”
  - **Proposed replacement:** “Run workflow checks for authentication, protected reads, file delivery, email, schedules, and integrations.”
- “Notify operators on failure, latency, queue age, or resource pressure.”
  - **Proposed replacement:** “Alert operators when workflow completion, latency, queue age, or capacity crosses its configured threshold.”
- “Watch pending age, failed attempts, and listener reachability.”
  - **Proposed replacement:** “Check sign-in, database access, file storage, queues, listeners, and schedules alongside process health.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Expose health, statistics, logs, and profiling signals to the monitoring stack your operators use.”
- “Observe delays and failures in background product behavior.”
  - **Proposed replacement:** “Track schedule latency, queue age, attempt results, and completion time for background work.”
- “Daptin exposes operational signals; it does not provide a managed monitoring service, incident response, log warehouse, or universal service-level objective.”
  - **Proposed replacement:** “Send Daptin health, statistics, logs, and profiling signals to the monitoring, incident, log, and service-level systems your team operates.”
- “Protect profiling endpoints and avoid leaking sensitive data into logs.”
  - **Proposed replacement:** “Restrict profiling endpoints and redact credentials, tokens, and customer secrets from logs.”
- “Make health and monitoring part of the product—not another disconnected service.”
  - **Proposed replacement:** “Track sign-in, database access, storage reachability, queue age, listeners, and scheduled work.”

### [/product/features/oauth-connections](product/features/oauth-connections/index.html)

- “Let customers connect the tools they already use—without handing you their passwords.”
  - **Proposed replacement:** “Let customers authorize provider accounts through OAuth and store delegated access on the backend.”
- “Do not expose reusable provider tokens to the browser.”
  - **Proposed replacement:** “Resolve reusable provider tokens on the server when an authorized action calls the connected service.”
- ““Connect account” should feel like a product feature, not an integration project.”
  - **Proposed replacement:** “Give customers one Connect account flow that handles provider authorization, token storage, and product return.”
- “Asking for their password is unsafe; asking them to repeat a manual export every time makes the feature feel unfinished.”
  - **Proposed replacement:** “Use delegated OAuth authorization and refreshable server-side tokens for recurring provider access.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Resolve provider tokens on the server when an authorized action calls the connected service.”
- “OAuth support does not guarantee compatibility with every provider.”
  - **Proposed replacement:** “Test scopes, redirects, refresh, revocation, quotas, and account recovery for every supported OAuth provider.”
- “Make oauth connections part of the product—not another disconnected service.”
  - **Proposed replacement:** “Let customers authorize a provider once, then resolve the delegated token in backend actions.”

### [/product/features/oauth-provider](product/features/oauth-provider/index.html)

- “Turn Daptin-held identity into a sign-in service for related applications, dashboards, or tools—so people do not need a separate account everywhere.”
  - **Proposed replacement:** “Let approved applications, dashboards, and tools sign customers in through their existing Daptin account.”
- “Continue without creating another password”
  - **Proposed replacement:** “Sign into an approved client with the customer’s existing Daptin identity.”
- “Keep customer identity in one home instead of copying it.”
  - **Proposed replacement:** “Use the Daptin account as the customer identity for approved web, mobile, dashboard, and tool clients.”
- “A second application should not force every customer to become a new person.”
  - **Proposed replacement:** “Let approved web, mobile, dashboard, and tool clients sign customers in through their existing Daptin account.”
- “Connect web, mobile, and tool clients without inventing a private sign-in protocol.”
  - **Proposed replacement:** “Connect web, mobile, and tool clients through Daptin’s OAuth and OpenID provider endpoints.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Register related clients around one customer identity and one consent and token policy.”
- “Register clients carefully, restrict redirects, rotate secrets, use TLS, define consent and token lifetimes, and assess whether Daptin's released provider scope fits your risk and compatibility requirements.”
  - **Proposed replacement:** “Register exact redirect URIs, protect client secrets, require TLS, and set consent scopes and token lifetimes for every OAuth client.”
- “Make oauth and openid provider part of the product—not another disconnected service.”
  - **Proposed replacement:** “Use existing Daptin accounts to sign customers into approved web, mobile, and tool clients.”

### [/product/features/outbound-mail](product/features/outbound-mail/index.html)

- “Queue outbound messages as stored work, record delivery attempts, retry failures, and keep a sent copy when the application account supports it.”
  - **Proposed replacement:** “Queue outbound messages as stored work, record every attempt, retry eligible deliveries, and retain a sent copy.”
- “Delivery work does not vanish into a request”
  - **Proposed replacement:** “Persist message state, attempt history, and next retry time after the request returns.”
- “Process pending messages again instead of reconstructing them.”
  - **Proposed replacement:** “Retry pending messages from their stored content, recipient, state, and attempt history.”
- ““Send email” is not a single reliable moment on the public internet.”
  - **Proposed replacement:** “Track each message from queued work through delivery attempts, provider responses, and final state.”
- “A network can fail before delivery.”
  - **Proposed replacement:** “Persist the message before delivery and retry eligible attempts according to the queue policy.”
- “If the application only waits for a synchronous response, the team cannot tell whether to retry or what the customer experienced.”
  - **Proposed replacement:** “Store delivery state and attempt history so operators can choose the correct retry and customer response.”
- “The model exposes the evidence operators need while keeping the guarantee honest: public mail is not exactly once.”
  - **Proposed replacement:** “Show operators message state, attempt history, provider responses, and idempotency context for public mail delivery.”
- “See failure context instead of relying only on transient logs.”
  - **Proposed replacement:** “Store provider responses, attempt timestamps, recipient context, and next retry state with each message.”
- “Recover routine failures”
  - **Proposed replacement:** “Retry eligible outbound messages from persisted queue state.”
- “Mark success or preserve error and next-retry state.”
  - **Proposed replacement:** “Record delivered state or store the provider response and next retry time.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Show message state, attempt history, next retry time, and delivery context to operators.”
- “No self-hosted mail system can promise exactly-once delivery.”
  - **Proposed replacement:** “Design idempotent product messages and record every public mail delivery attempt.”
- “Monitor queue age and repeated failures, design idempotent product messaging, and operate DNS, reputation, suppression, bounce, and abuse handling.”
  - **Proposed replacement:** “Teams define idempotency, retry, bounce, suppression, reputation, and customer communication policy.”
- “Make outbound mail part of the product—not another disconnected service.”
  - **Proposed replacement:** “Put every outbound message in a stored queue with attempt history and the next delivery time.”

### [/product/features/permissions](product/features/permissions/index.html)

- “Apply access to the record, not only the route.”
  - **Proposed replacement:** “Evaluate permissions on the requested record, its owner, and the caller’s group membership.”
- “Share without opening everything”
  - **Proposed replacement:** “Grant access to selected records, files, and actions through ownership and group membership.”
- “Access should follow the customer and the record—not a maze of endpoints.”
  - **Proposed replacement:** “Apply the customer and record access policy consistently across APIs, files, actions, and realtime events.”
- “A customer should see their own invoices but not another company's.”
  - **Proposed replacement:** “Let each customer read invoices owned by their account or organization.”
- “A project member may update tasks but not delete the project.”
  - **Proposed replacement:** “Grant project members task-update permission and reserve project deletion for approved roles.”
- “These are product rules, not merely authentication settings.”
  - **Proposed replacement:** “Express invoice ownership, project roles, file sharing, and action access as record-level product rules.”
- “Use ownership and group membership instead of inventing a permission system per feature.”
  - **Proposed replacement:** “Use record ownership and group membership to enforce the same permissions across every feature.”
- “Apply access inside shared backend paths rather than duplicating it in every client.”
  - **Proposed replacement:** “Enforce record and action permissions in shared backend paths used by every client.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Evaluate the same access policy across APIs, administration, files, actions, and realtime delivery.”
- “Make permissions part of the product—not another disconnected service.”
  - **Proposed replacement:** “Define a record rule once and enforce it across APIs, files, actions, administration, and live events.”

### [/product/features/protocols](product/features/protocols/index.html)

- “Let existing tools reach the product without making every client Daptin-specific.”
  - **Proposed replacement:** “Expose supported standard protocols so existing tools can reach Daptin records and files.”
- “Interoperability means meeting useful clients without pretending every interface is identical.”
  - **Proposed replacement:** “Document each protocol’s supported operations and test them with the client tools customers use.”
- “Avoid one mandatory client stack”
  - **Proposed replacement:** “Teams test required operations against each released protocol implementation before rollout.”
- “Let standards reach Daptin capabilities rather than building isolated protocol servers.”
  - **Proposed replacement:** “Route supported standard protocols to the same Daptin records, files, and permission checks.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Let existing tools use familiar interfaces while the application keeps one model and permission system.”
- “A protocol name is not a universal compatibility guarantee.”
  - **Proposed replacement:** “Test each required client operation against the documented protocol implementation.”
- “Make protocol services part of the product—not another disconnected service.”
  - **Proposed replacement:** “Expose the same records and files through each documented protocol endpoint.”

### [/product/features/realtime-events](product/features/realtime-events/index.html)

- “Publish live create, update, and delete events so permitted clients can react without repeatedly asking whether something changed.”
  - **Proposed replacement:** “Publish live create, update, and delete events so permitted clients can react.”
- “Reduce stale screens”
  - **Proposed replacement:** “Push permitted record changes to subscribed screens as soon as they occur.”
- “Without live updates, other screens remain stale until someone refreshes or the client polls again.”
  - **Proposed replacement:** “Publish record changes to subscribed screens as soon as permitted create, update, or delete events occur.”
- “Avoid constant polling”
  - **Proposed replacement:** “Publish permitted create, update, and delete events to connected clients as records change.”
- “Keep a connection for relevant events rather than repeating list requests.”
  - **Proposed replacement:** “Subscribe permitted clients to relevant record events over one live connection.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Keep dashboards and collaborative screens current through a live subscription.”
- “Add shared document editing when record-level events are not enough.”
  - **Proposed replacement:** “Use collaboration rooms to synchronize document edits and participant awareness.”
- “Realtime events are live fanout, not a durable event log.”
  - **Proposed replacement:** “Use realtime events for live fanout and reload durable records after reconnecting.”
- “Disconnected or slow clients can miss delivery and should reload durable state.”
  - **Proposed replacement:** “Reload the current record state after a client reconnects or falls behind.”
- “Make realtime events part of the product—not another disconnected service.”
  - **Proposed replacement:** “Subscribe permitted clients to record changes and reload durable state after reconnecting.”

### [/product/features/resource-apis](product/features/resource-apis/index.html)

- “Stop rebuilding routine endpoints”
  - **Proposed replacement:** “Generate list, search, sort, page, create, update, delete, and relationship APIs from the model.”
- “A new screen should not start with another endpoint backlog.”
  - **Proposed replacement:** “Use generated list, search, sort, page, create, update, delete, and relationship APIs for each new screen.”
- “A client can list, search, sort, page through, create, update, delete, and follow relationships without each screen inventing a new contract.”
  - **Proposed replacement:** “A client can list, search, sort, page through, create, update, delete, and follow relationships.”
- “Fetch connected information without flattening the model or creating one-off response shapes for every view.”
  - **Proposed replacement:** “Fetch related records through generated relationships and consistent resource representations.”
- “Avoid an ungoverned shortcut”
  - **Proposed replacement:** “Keep generated resource APIs behind the same record permissions and validation rules.”
- “Give another system a predictable contract without exposing database internals.”
  - **Proposed replacement:** “Give integrations generated resource APIs with stable fields, relationships, pagination, and permission checks.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Give every screen and integration the same resource contract and permission checks.”
- “Add named business operations when CRUD is not enough.”
  - **Proposed replacement:** “Add named actions for business operations and use generated endpoints for routine record work.”
- “Generated resource APIs remove repetitive plumbing, not product-specific behavior.”
  - **Proposed replacement:** “Use generated APIs for routine record operations and named actions for product-specific behavior.”
- “Make resource apis part of the product—not another disconnected service.”
  - **Proposed replacement:** “Every modeled resource gets pagination, filtering, relationships, writes, and record-level permission checks.”

### [/product/features/scheduled-work](product/features/scheduled-work/index.html)

- “Run recurring work without a separate cron service.”
  - **Proposed replacement:** “Schedule named Daptin actions with an explicit account and application context.”
- “Avoid a second implementation”
  - **Proposed replacement:** “Call the same backend action from schedules, screens, and APIs.”
- “Recurring work should not become a shadow version of your product.”
  - **Proposed replacement:** “Run the same named action from schedules, screens, and APIs with an explicit account and shared permissions.”
- “Over time it gains different access, different error handling, and different assumptions from the application.”
  - **Proposed replacement:** “Use the application action’s existing permissions, validation, outcome rules, and provider credentials for scheduled runs.”
- “The team can understand recurring work as part of the backend rather than as invisible machine configuration.”
  - **Proposed replacement:** “Operators can see which account ran each scheduled action, when it ran, and what it changed.”
- “Run for a selected account instead of defaulting to ambient administrator power.”
  - **Proposed replacement:** “Run each scheduled action as an explicitly selected account with its normal permissions.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Use the same action implementation from a screen, API request, or recurring schedule.”
- “Observe failures, delays, and the health of background work.”
  - **Proposed replacement:** “Show each scheduled run’s start time, completion state, duration, actor, and recorded outcome.”
- “Scheduling does not guarantee that outside work happens exactly once.”
  - **Proposed replacement:** “Give scheduled provider calls idempotency keys, overlap rules, attempt history, and recovery procedures.”
- “Plan idempotency, time zones, overlapping runs, provider limits, failure alerting, and recovery for every consequential task.”
  - **Proposed replacement:** “Set each job’s time zone, overlap policy, idempotency key, provider quota, alert threshold, and recovery procedure.”
- “Make scheduled work part of the product—not another disconnected service.”
  - **Proposed replacement:** “Schedule the same authorized action used by screens and APIs, with an explicit account and run history.”

### [/product/features/sites](product/features/sites/index.html)

- “Splitting each concern into an unrelated service can make a small product surprisingly hard to operate.”
  - **Proposed replacement:** “Run site files, content records, credentials, certificates, and synchronization through one Daptin deployment.”
- “Serve a synchronized site root without handing product identity to a hosting provider.”
  - **Proposed replacement:** “Serve synchronized site files while Daptin retains content records, ownership, credentials, and certificates.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Connect content, file ownership, credentials, certificates, and synchronization in one backend.”
- “Daptin sites are a self-hosted serving surface, not a global managed CDN.”
  - **Proposed replacement:** “Serve sites from Daptin and add a CDN or managed edge when the audience requires global caching and delivery.”
- “Make sites part of the product—not another disconnected service.”
  - **Proposed replacement:** “Serve a synchronized site root tied to Daptin files, credentials, certificates, and storage.”

### [/product/features/state-tracking](product/features/state-tracking/index.html)

- “Define the stages an important record may move through, prevent impossible jumps, and keep transition history connected to the subject.”
  - **Proposed replacement:** “Define allowed stages for each record and store every accepted transition beside its subject and actor.”
- “Prevent impossible transitions”
  - **Proposed replacement:** “Permit only the state transitions declared for the record lifecycle.”
- “A request should not jump from draft straight to completed.”
  - **Proposed replacement:** “Require requests to move from draft through the configured review stage before completion.”
- “A cancelled order should not be fulfilled.”
  - **Proposed replacement:** “Permit fulfillment only from the approved order states.”
- “Stop invalid jumps”
  - **Proposed replacement:** “Validate every requested state change against the declared transition map.”
- “See not only where the record is, but how it moved.”
  - **Proposed replacement:** “Show the current state and every accepted transition that produced it.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Record every accepted transition beside the subject, actor, and current state.”
- “State tracking validates finite transitions; it is not a full business-process engine.”
  - **Proposed replacement:** “Use state tracking for finite transitions and compose broader processes with actions, events, and schedules.”
- “Make state tracking part of the product—not another disconnected service.”
  - **Proposed replacement:** “Declare valid record transitions once and store every accepted change beside its actor and subject.”

### [/product/features/storage-sync](product/features/storage-sync/index.html)

- “Use named operations instead of ad hoc provider scripts.”
  - **Proposed replacement:** “Run named copy, move, and synchronization actions with stored credentials and record ownership.”
- “Without a managed path, records point to stale content and operations rely on one-off scripts.”
  - **Proposed replacement:** “Run named synchronization actions that update storage content and its related records together.”
- “Because those operations live beside credentials, actions, schedules, and sites, the team can turn synchronization into visible product behavior rather than hidden server maintenance.”
  - **Proposed replacement:** “Each synchronization job uses a stored credential, a named action, an optional schedule, and a recorded result.”
- “Track failures, provider limits, and stale content as operator concerns.”
  - **Proposed replacement:** “Monitor synchronization completion, provider quotas, cache age, and content freshness.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Connect credentials, actions, schedules, sites, and record ownership around each synchronization job.”
- “Synchronization has timing and failure modes.”
  - **Proposed replacement:** “Define source ownership, completion checks, conflict policy, cache invalidation, monitoring, and recovery for each synchronization job.”
- “Define which side owns truth, how deletion and conflicts behave, when caches invalidate, and how operators detect a partially completed refresh.”
  - **Proposed replacement:** “Declare source ownership, deletion and conflict rules, cache invalidation, and completion checks for each refresh.”
- “Make storage synchronization part of the product—not another disconnected service.”
  - **Proposed replacement:** “Run named copy, move, and sync jobs with stored credentials, schedules, and completion records.”

### [/product/features/templates](product/features/templates/index.html)

- “Define a reusable presentation instead of assembling it in every client.”
  - **Proposed replacement:** “Render one named server-side template from application records for actions, mail, sites, feeds, and API responses.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Use one template from actions, mail, sites, feeds, and API responses.”
- “Templates are server-rendered content, not a full visual page builder or campaign-management suite.”
  - **Proposed replacement:** “Use server-rendered templates for application responses and choose dedicated visual tools for page or campaign authoring.”
- “Make templates and responses part of the product—not another disconnected service.”
  - **Proposed replacement:** “Render one server-side template from application records for actions, mail, sites, feeds, and APIs.”

### [/product/features/traffic-controls](product/features/traffic-controls/index.html)

- “Avoid wasteful responses”
  - **Proposed replacement:** “Set request rates, connection bounds, body sizes, origins, compression, and file-path limits.”
- “Use compression where it helps without breaking range-sensitive content.”
  - **Proposed replacement:** “Enable compression for compatible responses and preserve byte ranges for large-file delivery.”
- “A correct feature can still fail under oversized uploads, too many open connections, aggressive polling, or an unintended browser origin.”
  - **Proposed replacement:** “Set upload sizes, connection bounds, request rates, polling budgets, and allowed browser origins from measured workloads.”
- “A safe operating plan treats limits as part of the product's public contract, not as emergency settings added after overload.”
  - **Proposed replacement:** “Publish and test request rates, body sizes, connection bounds, origins, and file limits as part of the product contract.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Match proxy and Daptin controls to measured uploads, polling patterns, and connection counts.”
- “Built-in limits are one layer, not a complete edge-security or denial-of-service service.”
  - **Proposed replacement:** “Combine Daptin’s request controls with a reverse proxy, network edge, and denial-of-service protection.”
- “Use a reverse proxy or network edge where appropriate, test real workloads, and monitor both accepted and rejected traffic.”
  - **Proposed replacement:** “Teams monitor traffic and add an appropriate reverse proxy, network edge, and denial-of-service protection.”
- “Make traffic and request controls part of the product—not another disconnected service.”
  - **Proposed replacement:** “Set request rates, body sizes, connection bounds, origins, and compression where the application accepts traffic.”

### [/product/features/transaction-control](product/features/transaction-control/index.html)

- “Make related changes succeed together—or leave the data unchanged.”
  - **Proposed replacement:** “Commit every required record change together inside one transaction.”
- “Keep multi-step record work inside a clear success boundary, while choosing which optional outcomes may continue after a recoverable failure.”
  - **Proposed replacement:** “Commit required record changes together and declare which optional outcomes may continue after a recoverable condition.”
- “Transactions and failure control in a product”
  - **Proposed replacement:** “Define transaction boundaries and outcome rules for product actions.”
- “Partial data is not the default outcome”
  - **Proposed replacement:** “Commit required record changes together inside one database transaction.”
- “Avoid saving half of a multi-record operation.”
  - **Proposed replacement:** “Commit all required record changes together inside one database transaction.”
- “Make failure behavior explicit”
  - **Proposed replacement:** “Declare every action outcome as required or optional and assign its continuation rule.”
- “Choose when an optional step may fail without hiding it.”
  - **Proposed replacement:** “Mark the step optional, record its outcome, and continue according to the declared action rule.”
- “A product operation should not leave half a story in the database.”
  - **Proposed replacement:** “Commit all required record changes together or roll the transaction back.”
- “Imagine accepting an invitation but failing to create the membership, or marking an order fulfilled without recording its shipment.”
  - **Proposed replacement:** “Create the invitation membership and shipment record inside the same transaction as their parent operation.”
- “If a required outcome fails, the record changes can roll back together.”
  - **Proposed replacement:** “Commit protected record changes after every required outcome completes successfully.”
- “Individual outcomes may explicitly continue after an error when they are truly optional.”
  - **Proposed replacement:** “Allow a declared optional outcome to continue while recording its result for operators.”
- “This creates a predictable data boundary without pretending that outside networks are transactional.”
  - **Proposed replacement:** “Protect database changes with a transaction and persist outside work for idempotent delivery and recovery.”
- “Let a nonessential follow-up fail only when the action says it may.”
  - **Proposed replacement:** “Declare a nonessential follow-up optional and record its outcome beside the action.”
- “Make error handling visible”
  - **Proposed replacement:** “Show each outcome’s required or optional status, continuation rule, and recorded result.”
- “Design the response and recovery path instead of accepting silent partial success.”
  - **Proposed replacement:** “Return a clear action result and record the recovery path for every incomplete optional outcome.”
- “Transactions and failure control does more when it can reuse the records, people, access rules, and workflows already in your application.”
  - **Proposed replacement:** “Apply transaction rules to the same records, users, permissions, and actions that power the application.”
- “A failure stops or continues according to the declared rule.”
  - **Proposed replacement:** “Use each outcome’s declared rule to commit the transaction or continue the action.”
- “Commit on success or roll back the protected database work.”
  - **Proposed replacement:** “Commit protected database changes after every required outcome completes; otherwise roll them back.”
- “Apply related updates without leaving a partially changed set.”
  - **Proposed replacement:** “Apply related record updates inside one transaction and commit them as a complete set.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Mark each action outcome as required or optional and apply its declared continuation rule.”
- “These capabilities share the same application context, so each one makes transactions and failure control more useful.”
  - **Proposed replacement:** “Use shared records, identities, permissions, and actions to define each transaction boundary and outcome rule.”
- “Persist communication work when outside delivery cannot be transactional.”
  - **Proposed replacement:** “Store email and provider work before dispatch, then record each delivery attempt and result.”
- “A database transaction cannot roll back an email already sent or a provider request already accepted.”
  - **Proposed replacement:** “Persist email and provider work before dispatch, then use idempotency keys and recorded outcomes for recovery.”
- “Make transactions and failure control part of the product—not another disconnected service.”
  - **Proposed replacement:** “Apply transaction boundaries and outcome rules inside the same actions that update product records.”

### [/product/features/two-factor-auth](product/features/two-factor-auth/index.html)

- “A stolen password is no longer enough”
  - **Proposed replacement:** “Require a time-based one-time code after password verification.”
- “Administrators, operators, and customers with valuable information face a simple risk: a reused or stolen password can become full account access.”
  - **Proposed replacement:** “Require a second verification factor for administrators, operators, and high-value customer accounts.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Protect administrator, operator, and high-value customer accounts with a second verification factor.”
- “Two-factor authentication is one control, not a complete account-security program.”
  - **Proposed replacement:** “Combine two-factor verification with secure sessions, account recovery, rate controls, support checks, and administrator protection.”
- “Plan enrollment recovery, lost-device handling, support verification, secure secrets, rate limits, and which roles must use it.”
  - **Proposed replacement:** “Teams define enrollment, recovery codes, device-replacement support, rate controls, sessions, and role enforcement.”
- “Make two-factor authentication part of the product—not another disconnected service.”
  - **Proposed replacement:** “Add time-based one-time codes to the same account, session, recovery, and permission flow.”

### [/product/features/users-groups](product/features/users-groups/index.html)

- “Model membership instead of scattering role checks through code.”
  - **Proposed replacement:** “Represent organizations, workspaces, teams, and memberships as user and group relationships.”
- “Build the next part without starting over.”
  - **Proposed replacement:** “Use group membership in ownership, permissions, actions, and shared product experiences.”
- “Groups are flexible building blocks, not a complete organization-management product.”
  - **Proposed replacement:** “Use groups for membership and permissions, then add invitations, billing roles, and organization lifecycle rules for your product.”
- “Make users and groups part of the product—not another disconnected service.”
  - **Proposed replacement:** “Model membership once and use it for record ownership, permissions, actions, and team access.”

### [/product](product/index.html)

- “Every product feature then needs glue: copy identity into another service, recreate permissions, move secrets, reconcile failures, and explain the same business idea in several contracts.”
  - **Proposed replacement:** “The account that owns a record also governs its files, actions, feeds, and protocol access.”
- “The value is not that many things fit in one binary.”
  - **Proposed replacement:** “Daptin applies that ownership rule through APIs, files, sites, feeds, protocols, and workflows.”
- “Let access follow the work instead of each delivery channel.”
  - **Proposed replacement:** “Apply the same ownership and permission rules across APIs, files, actions, sites, feeds, and protocols.”
- “Store, organize, publish, and collaborate without losing ownership.”
  - **Proposed replacement:** “Attach storage, collections, publication, and collaboration to records with explicit owners and permissions.”
- “Provider compatibility, costs, terms, and failure handling”
  - **Proposed replacement:** “Evaluate each provider’s supported operations, pricing, terms, quotas, and recovery behavior.”
- “Choose Daptin for connected product foundations—not every possible backend.”
  - **Proposed replacement:** “Choose Daptin when records, accounts, permissions, files, actions, and integrations must follow the same rules.”
- “Nearly every request is bespoke compute, you need a best-in-class specialist system for one function, a managed provider must own operations, or your workload cannot fit the released compatibility and scaling boundaries.”
  - **Proposed replacement:** “Choose a specialist or managed platform when bespoke compute, one dominant function, outsourced operations, or workload scale drives the architecture.”
- “Inspect the running product—not just the thesis.”
  - **Proposed replacement:** “Run Daptin locally, open the administration UI, call the APIs, and trace one complete customer workflow.”

### [/product/preview/ai-workloads](product/preview/ai-workloads/index.html)

- “The current source explores a shared route from your product to multiple model providers—so credentials, model choices, streaming responses, files, tools, batches, and usage do not become unrelated integrations.”
  - **Proposed replacement:** “Route model selection, provider credentials, streaming, files, tools, batches, and usage through one backend API.”
- “Avoid provider-specific behavior leaking into every client.”
  - **Proposed replacement:** “Keep provider credentials and model selection on the backend while clients use one product API.”
- “A real product may need a model catalogue, several provider accounts, streaming responses, embeddings, uploaded files, batch jobs, tool calls, usage records, and a way to stop or drain outstanding work.”
  - **Proposed replacement:** “Map each product feature to a configured model, provider account, and deployment.”
- “The intended benefit is not a fashionable endpoint.”
  - **Proposed replacement:** “Check how the code selects providers, streams responses, calls tools, processes batches, stores files, and records usage.”
- “Represent available models and product-selected deployments without hard-wiring every client.”
  - **Proposed replacement:** “List available models and assign each product feature to a configured provider deployment.”
- “Do not plan production adoption from this page alone.”
  - **Proposed replacement:** “Base production plans on a release that documents provider routing, streaming, tools, files, batches, and usage as supported.”

### [/product/preview/usage-plans](product/preview/usage-plans/index.html)

- “Close reservations and apply post-use behavior after success or failure.”
  - **Proposed replacement:** “Close each usage reservation with measured cost and a recorded completion state.”
- “Do not promise billing or enforcement behavior from this page.”
  - **Proposed replacement:** “Tie billing and enforcement commitments to a release that documents usage plans as supported.”

### [/use-cases](use-cases/index.html)

- “See the experience—not a bag of backend features.”
  - **Proposed replacement:** “Reuse authentication, billing, storage, queues, and APIs. Spend your time on what customers actually touch.”
- “The product team defines that relationship once instead of recreating tenant rules in every service.”
  - **Proposed replacement:** “Define tenant ownership once and apply it across records, files, actions, APIs, and connected services.”
- “A connected account should unlock a useful experience, not expose a wall of provider mechanics.”
  - **Proposed replacement:** “Turn a connected account into a customer action such as import files, enrich a lead, or send a support update.”
- “The customer authorizes the outside account without sharing its password with you.”
  - **Proposed replacement:** “Let the customer authorize the provider through OAuth and store the delegated connection on the backend.”
- “An incoming message can become application data instead of disappearing into a separate shared inbox.”
  - **Proposed replacement:** “Turn each incoming message into a record linked to its customer, thread, attachments, and workflow.”
- “Outbound work can be queued and retried, keeping delivery attempts visible when something goes wrong.”
  - **Proposed replacement:** “Queue outbound work, record every delivery attempt, and show operators its current state and next retry time.”
- “Customers may never know there is a mail server involved.”
  - **Proposed replacement:** “Turn incoming mail into customer records and send replies through a queue that keeps every delivery attempt.”
- “Let customers choose a plan without putting provider secrets or entitlement decisions in the browser.”
  - **Proposed replacement:** “Let customers choose a plan reference while the backend resolves provider credentials, pricing, and entitlement rules.”
- “The browser supplies a plan reference, not a price or provider credential.”
  - **Proposed replacement:** “Let the browser submit a plan reference while the backend resolves price, currency, provider credential, and entitlement owner.”
- “A redirect or webhook claim alone never grants access.”
  - **Proposed replacement:** “Grant access after the backend verifies the provider event and applies the matching entitlement rule.”
- “Security boundary: customers may start permitted checkout actions, but cannot select the service user, credential, price, currency, or entitlement owner.”
  - **Proposed replacement:** “Let customers start approved checkout actions while the backend selects the service user, credential, price, currency, and entitlement owner.”
