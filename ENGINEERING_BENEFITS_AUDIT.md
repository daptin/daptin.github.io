# Invisible backend engineering audit for Daptin

Status: source evidence used by the current website copy. Re-run the release checks before changing a claim.

Audit date: 2026-09-02
Audited source: the latest `artpar/daptin` release available on the audit date
Release policy: resolve and inspect the latest GitHub release at audit time; do not carry a pinned version into public copy

## Scope and corrected definition

This audit is limited to **engineering practices that protect or improve applications without an application developer implementing them**. A feature answers “what can Daptin do?” An engineering practice answers “how does Daptin make that behavior correct, safe, bounded, efficient, or operable?”

- Metering is a product feature, so it is excluded from the main list.
- Sending mail is a feature; persisting mail before delivery, leasing work, bounding retries, and keeping SMTP outside the originating transaction are engineering practices.
- Prepared query values are a defense. They do **not** mean “SQL injection is impossible”: identifiers, operators, DDL, and raw fragments are separate attack surfaces.

Labels: **Present** means the implementation and a relevant failure path were traced; **Partial** means a useful practice has a material gap; **Absent** means the expected defense was not found; **Unsafe** means current behavior conflicts with established guidance.

## Research baseline

The review checklist comes from authoritative backend/security guidance:

- [OWASP API4: Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/): rate, concurrency, execution, payload, pagination, and expensive-operation limits.
- [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html): parameterize values, allowlist identifiers/dynamic SQL, and use least database privilege.
- [OWASP REST Security](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html): access control, content types, errors, CORS, security headers, and status codes.
- [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html): authenticated encryption and key lifecycle.
- [OWASP SSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html): destination validation, redirects, DNS and network controls.
- [OWASP Logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html): event coverage, correlation, redaction, sanitization, integrity, and failure behavior.
- [Go database connection management](https://go.dev/doc/database/manage-connections) and [`net/http.Server`](https://pkg.go.dev/net/http#Server): bounded pools, lifetimes, HTTP timeouts, and header limits.
- [PostgreSQL transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html), [RFC 6585](https://www.rfc-editor.org/rfc/rfc6585.html), and [RFC 9562](https://www.rfc-editor.org/rfc/rfc9562.html): atomicity, HTTP 428/429, and UUIDv7.

This is a static source audit, not a penetration test, race-detector run, fuzz campaign, production load test, or compliance certification.

## Good invisible engineering already present

### 1. Hybrid identity: integer joins behind binary UUIDv7 public IDs

**Present in the audited latest release and current source.** Generated records use an auto-incrementing integer primary key internally and a non-null, unique, indexed, binary UUIDv7 `reference_id` externally. Internal IDs are excluded from APIs, and incoming related UUIDs resolve to integer FKs inside the transaction.

Benefit: compact joins/indexes, no public row counter, portable external identity, better insertion locality than UUIDv4, and no textual UUID cost on internal relationships.

Evidence: [standard columns](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/columns.go), [creation/FK resolution](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/resource_create.go), [RFC 9562](https://www.rfc-editor.org/rfc/rfc9562.html#name-uuid-version-7).

Limit: UUIDv7 reveals approximate creation time and is an identifier, not a secret or authorization control.

### 2. Relationship writes verify existence and authorization

**Present.** Daptin resolves the referenced UUID, rejects missing rows, and checks `Refer` permission before storing the integer FK. Knowing a UUID alone does not authorize creating a link.

Evidence: [relationship handling](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/resource_create.go#L107-L149).

### 3. Generated uniqueness and lookup indexes

**Partial.** Schema metadata produces unique/indexed field indexes, composite unique keys, permission lookup indexes, standard timestamp/reference indexes, and unique multi-column indexes on join tables. MySQL/PostgreSQL also receive physical FK DDL.

Benefit: common lookups avoid scans and duplicate business keys or many-to-many links are rejected safely under concurrency.

Evidence: [constraint/index generation](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/dbfunctions_create.go).

Critical limit: DDL failures can be logged and ignored, so declared and physical guarantees may diverge. SQLite does not get equivalent physical FK DDL.

### 4. Core CRUD database work shares one transaction

**Present for database effects; partial for external effects.** Create, update, and delete pass one transaction through middleware and related database writes and commit at the end.

Benefit: primary rows, relation rows, permissions, and successful in-transaction audit writes normally appear together or not at all.

Evidence: [create](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/resource_create.go), [update](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/resource_update.go), [delete](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/resource_delete.go).

Limit: SQL rollback cannot unsend mail, undo HTTP calls, or reliably remove uploaded/deleted cloud files.

### 5. Optimistic write-conflict detection

**Partial.** Updates increment `version`, qualify the update by current version, and error when zero rows match. A regression test covers stale writes.

Evidence: [conditional update](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/resource_update.go#L424-L460), [test](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/action_transaction_permission_test.go#L87-L170).

Gap: `version` is excluded from the API and the server can fetch it just before updating. There is no clear client `If-Match`/`412` contract, so “prevents lost updates” is not yet a safe claim.

### 6. SQL values are usually separated from SQL structure

**Present as a convention, not a proof of impossibility.** CRUD/system paths predominantly use Goqu/Squirrel prepared mode and bind values. Sort and aggregate surfaces validate fields/operators against schema metadata, with hostile-input tests.

Benefit: ordinary API values are treated as data; embedded SQL text does not normally change query intent.

Evidence: [query builder](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/resource_findallpaginated.go), [aggregate security tests](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/resource_aggregate_security_test.go), [sort tests](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/resource_findallpaginated_sort_test.go).

Safe wording: “Daptin parameterizes query values and validates major dynamic query surfaces.” Never say “no chance of SQL injection”: DDL identifiers/table fragments are concatenated, raw-query helpers exist, and schema names are data-driven. Those require strict identifier allowlisting/quoting, least DB privilege, static analysis, and adversarial testing.

### 7. URL/client rate limiting on backend and subsites

**Present in the audited latest release and current source.** Middleware is installed before handlers and:

- keys counts by client IP plus path; subsites also include host;
- ignores query strings, preventing query-parameter bucket evasion;
- supports exact-path requests-per-second configuration;
- applies a 500 rps default to unconfigured paths;
- shares fixed-window counters through Olric across nodes;
- falls back to a mutex-protected process-local counter;
- returns `429`, `Retry-After: 1`, and limit/remaining/reset headers;
- validates configuration and has local/cluster-sharing tests.

Benefit: a client repeatedly hitting one URL is bounded before reaching application handlers, including across a healthy cluster.

Evidence: [middleware](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/middleware_ratelimit.go), [installation](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/server.go), [tests](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/middleware_ratelimit_test.go).

Limits:

- Exact paths are separate buckets; rotating `/api/item/{uuid}` values bypasses a collection-level budget.
- One-second fixed windows permit boundary bursts.
- IP identity penalizes NAT users and does not stop distributed clients.
- Correct attribution depends on safe trusted-proxy configuration.
- Olric failure changes a cluster allowance into one allowance per process.
- 500 rps is not suitable protection for every expensive route.

Recommended evolution: canonical route-template buckets plus global, IP, authenticated-principal, tenant, and expensive-operation token buckets; documented proxy trust; observable fallbacks; explicit fail-open/fail-closed policy.

### 8. Concurrent requests are bounded separately from rate

**Present.** Backend and subsite routers install a maximum-active-request middleware in addition to rate limiting. This matters because requests/second does not bound slow or long-lived requests.

Evidence: [backend order](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/server.go#L200-L205), [subsites](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/subsites.go).

Gap: absent HTTP read/header timeouts let slow clients occupy a slot too long.

### 9. Database pools are bounded and aged

**Present.** Daptin sets maximum open/idle connections, connection lifetime, and idle lifetime.

Benefit: request bursts cannot create unlimited DB connections; idle connections are reused and stale ones retired.

Evidence: [pool configuration](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/database_connection.go#L60-L99), [Go guidance](https://go.dev/doc/database/manage-connections).

Gap: parsed zero/negative values need validation, and saturation/wait statistics should be observable.

### 10. CORS is closed by default and strictly parsed

**Present in the latest release.** Default CORS allows no origins. Parsing rejects unknown fields, unsupported versions, wildcard/`null` origins, origins containing credentials/path/query/fragment, invalid methods/headers, duplicates, excessive max age, and credentials without explicit origins. Invalid stored policy falls back closed.

Benefit: browser cross-origin access must be deliberately and precisely enabled.

Evidence: [CORS implementation](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/cors.go), [tests](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/cors_test.go).

### 11. Central authorization accounts for cache coherence

**Present.** Table, row, owner, group, action, and relationship operations use centralized permission logic. Transactional permission reads avoid stale shared-cache state; relevant mutations invalidate object/row/auth/admin/membership caches. Tests cover stale cache and cross-owner token/credential cases.

Benefit: generated routes are not automatically unrestricted, and recent permission changes are less likely to be bypassed by stale authorization cache.

Evidence: [permission code](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/permission/permission.go), [stale-cache test](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/action_transaction_permission_test.go), [invalidation tests](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/cache_invalidation_test.go).

### 12. Password changes revoke older sessions

**Present and tested.** Passwords use bcrypt. Changes increment `auth_version` and invalidate auth/JWT caches, so tokens minted against the older credential version stop validating.

Evidence: [bcrypt](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/bcrypt_utils.go), [update lifecycle](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/resource_update.go), [tests](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/auth_lifecycle_test.go).

Gap: bcrypt cost 11 is fixed; no adaptive rehash or Argon2id migration policy was found.

### 13. OAuth codes/tokens have lifecycle and ownership defenses

**Present in the latest release.** Exact redirect matching, scope validation, expiring single-use codes, PKCE, hashed opaque-token lookup, refresh rotation/revocation, user/provider ownership checks, and `HttpOnly`/`SameSite=Strict` browser cookies are implemented.

Evidence: [provider](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/oauth_provider.go), [endpoints](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/endpoint_oauth.go), [ownership tests](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/oauth_integration_token_test.go).

Gap: discovery advertises PKCE `plain`; require S256 for new public clients.

### 14. Validation/normalization happens before persistence

**Present.** Write middleware applies configured validation and string conformation rules; action inputs are separately processed.

Benefit: malformed common data is rejected at the backend rather than relying on browser validation.

Evidence: [middleware](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/middleware_datavalidation.go), [column types](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/column_types.go).

### 15. Audit schemas avoid obvious secrets and large blobs

**Partial.** Generated audit tables omit password/bcrypt/encrypted/file/blob/binary, identity, and permission fields and deny guest access. Update audit creation shares the mutation transaction and failure aborts the update.

Evidence: [filtering](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/dbfunctions_create.go#L22-L47), [tests](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/audit_table_test.go).

Gap: delete ignores audit insertion failure. Audit data is mutable, not a tamper-evident ledger.

### 16. Mail delivery is durable, leased, bounded, and retryable

**Present; at-least-once.** Mail is persisted before delivery. Workers claim bounded batches through distributed and database leases, commit the claim before SMTP, use a send timeout, and record success or bounded backoff/retry.

Benefit: SMTP latency/failure does not erase work or hold the originating business transaction open; nodes coordinate delivery.

Evidence: [outbox processor](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/actions/action_outbox_process.go).

Limit: a crash after SMTP acceptance but before recording success can duplicate mail. Do not call it exactly-once.

### 17. Static delivery bounds memory and avoids redundant work

**Present and tested.** Asset/subsite serving uses ETags/`If-None-Match`, representation-specific ETags, `Vary`, reusable gzip sidecars, bounded memory reads, and streaming for larger files.

Benefit: unchanged assets return `304`; compressed variants cache correctly; large files need not fill process memory.

Evidence: [assets](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/asset_route_handler.go), [bounded reads](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/file_serving_utils.go), [tests](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/subsite_engine_test.go).

### 18. FTP paths receive containment and symlink checks

**Present; scope is FTP.** Paths are normalized, checked relative to the configured root, and resolved symlinks are rechecked.

Benefit: `../` and symlink traversal are not trusted as normal filenames.

Evidence: [FTP path handling](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/ftp_server.go).

### 19. Liveness, readiness, graceful draining, and ordered teardown

**Present on `master`, not in the latest release.** Current source separates liveness from DB-aware readiness, becomes unready before shutdown, gracefully stops HTTP, drains WebSockets/events, stops services, and then closes caches, cluster/pub-sub and DB resources under a deadline. Do not sell this as released behavior yet.

Benefit: rolling deployments stop routing new work before teardown and lose less in-flight work.

Unreleased evidence: [main lifecycle](https://github.com/artpar/daptin/blob/master/main.go), [runtime teardown](https://github.com/artpar/daptin/blob/master/server/runtime.go), [tests](https://github.com/artpar/daptin/blob/master/server/connection_tracker_test.go).

### 20. Main HTTP handler panics do not terminate the process

**Present for the backend router.** It uses `gin.Default()`, which installs recovery middleware.

Limit: recovery still needs transaction rollback, safe errors, and alerts. The subsite router uses `gin.New()`; equivalent recovery was not established.

## Missing or unsafe backend practices

### P0 — authenticated secret encryption

**Unsafe.** AES-CFB has a random IV but no tag/MAC; decrypt also ignores base64 errors. Ciphertext changes are not reliably detected. Replace with a versioned AES-GCM or ChaCha20-Poly1305 envelope, contextual associated data, key IDs/rotation, strict errors, separated key storage, and read-old/write-new migration.

Evidence: [current helper](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/encryption_decryption.go), [OWASP guidance](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html#cipher-modes).

### P0 — post-commit reliable events

**Unsafe consistency.** CRUD event middleware queues before commit. A worker can publish a rolled-back change; overflow drops events and publish errors have no durable retry. Store an event in the mutation transaction, dispatch after commit with lease/retry, unique IDs, at-least-once semantics, and idempotent consumers.

Evidence: [event middleware](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/middleware_eventgenerator.go), [commit happens later](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/resource_update.go#L1172-L1197).

### P0 — fail-closed schema enforcement

**Unsafe integrity.** DDL failures are often logged and ignored; constraint code issues `COMMIT` inside a caller transaction; index code continues after `Beginx` failure. Return errors, abort readiness, never commit caller-owned transactions, distinguish “already exists” precisely, quote/allowlist identifiers, and reconcile declared versus physical schema.

Evidence: [DDL paths](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/dbfunctions_create.go#L49-L160).

### P0 — HTTP timeouts, headers, and body limits

**Absent.** Production servers omit `ReadHeaderTimeout`, `ReadTimeout`, `WriteTimeout`, `IdleTimeout`, and `MaxHeaderBytes`; no systematic `MaxBytesReader` policy was found. Add safe defaults, explicit streaming exceptions, route-specific body/upload/decompression caps, minimum TLS version, and slow/oversized-client tests.

Evidence: [server construction](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/main.go), [OWASP API4](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/).

### P0 — pagination and query-complexity bounds

**Absent for general REST pages.** `page[size]` accepts a 32-bit unsigned client value with no maximum. Large pages, included relationships, groupings, and aggregates can consume DB, memory, CPU, and bandwidth. Apply configurable hard maxima and limits for relation depth/count, filter/group complexity, aggregation dimensions, GraphQL complexity/batching, and maximum-plus-one tests.

Evidence: [page-size parsing](https://github.com/artpar/daptin/blob/33716cd93282019ca39fcc8d5593863897348d5d/server/resource/resource_findallpaginated.go#L342-L355).

### P1 — transaction ownership

Several handlers use unconditional deferred commits or ignore commit errors. Update registers rollback before confirming `Beginx`; the outbox replaces a caller-provided transaction. The function beginning a transaction should own it exclusively, defer rollback only after successful begin, commit only on success, propagate commit failure, and never replace/commit caller-owned transactions. Test begin, statement, commit, and panic failures.

### P1 — audit and relationship deletion semantics

Delete should roll back on required audit failure or explicitly report best-effort auditing. Relationship cleanup is substantially commented out and generated FKs lack visible `ON DELETE` policy. Declare restrict/cascade/set-null/soft-delete semantics and test API plus direct-DB deletion on every engine.

### P1 — external side-effect boundaries

Cloud file and declarative network/mail/process effects can occur inside SQL transactions. Persist idempotent intent with the business change, execute after commit, and record retry/compensation state.

### P1 — consistent SSRF defenses

Some outbound clients have timeouts, but a systematic destination policy was not established. Centralize a transport that allowlists schemes/hosts/ports, blocks loopback/private/link-local/metadata destinations unless explicit, revalidates redirects/DNS, and bounds response bodies. See [OWASP SSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html).

### P1 — browser/API security headers

No central HSTS, `X-Content-Type-Options`, frame-ancestor policy, or sensitive-response `Cache-Control: no-store` middleware was found. Configure by response class without breaking hosted sites. See [OWASP REST headers](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html#security-headers).

### P1 — allocation-safe event/config decoding

Binary event decoding trusts a signed length and allocates without a maximum. Event worker/queue environment values also need positive-range validation. Bound values and fuzz the codec.

### P1 — systematic log safety

Logging is extensive, but that is not automatically a best practice. Trace tokens, credentials, URLs/query strings, email, paths and user values; redact secrets/PII; neutralize CR/LF; add correlation IDs; separate security/audit from debug logs; define retention/rotation/failure behavior; test log injection. See [OWASP Logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html).

### P2 — maturity work

- Return `409`/`412` for stale writes and expose `ETag`/`If-Match` or version preconditions.
- Require PKCE S256 for new clients; add adaptive password rehashing.
- Validate DB pool ranges and expose pool saturation/wait metrics.
- Run CRUD/migration/constraint/concurrency/permission suites on SQLite, MySQL, and PostgreSQL.
- Fuzz schema identifiers, query grammar, event frames, URLs, paths, archives, decompression, and JSON.
- Run `go test -race`, constrained-resource load tests, static security analysis, and dependency scanning as release gates.
- Document asynchronous semantics (at-most-once, at-least-once, best-effort) and idempotency requirements.
- Verify recovery on the `gin.New()` subsite router and stored-XSS/content-sniffing safety for rendered/uploaded content.

## Strict website claim matrix for step 2

| Invisible benefit | Status | Safe wording now |
|---|---|---|
| Integer internals + binary UUIDv7 public IDs | Present/released | Compact internal joins with stable public IDs |
| Existence- and permission-checked references | Present | Rejects missing and unauthorized references |
| Generated indexes/unique join constraints | Partial | Describe generation, not guaranteed enforcement |
| Transaction-scoped DB CRUD | Present | Database changes share a transaction |
| No partial external effects | False | Do not claim |
| Stale-write rejection | Public contract unclear | Hold |
| Parameterized query values | Present | Separates ordinary values from SQL structure |
| SQL injection impossible | Unproven/absolute | Never claim |
| Per-IP/per-path URL rate limiting | Present/released | Built-in URL limits with cluster counter and local fallback |
| Comprehensive abuse protection | False | Do not claim |
| Concurrent-request cap | Present | Bounds simultaneous requests |
| Bounded/aged DB pool | Present | Controls DB connection pressure |
| Closed-by-default strict CORS | Present in latest release | Call out carefully |
| Central data authorization/cache invalidation | Present | Model-driven access controls |
| Session revocation after password change | Present | Ready |
| Authenticated secret encryption | Absent | Do not promote encryption yet |
| Sensitive/blob audit exclusion | Present | Ready narrowly |
| Complete/tamper-proof audit | False | Do not claim |
| Durable mail processing | Present | Retryable, leased, at-least-once delivery |
| Reliable post-commit events | False | Do not claim |
| Cache-correct compressed assets | Present | Ready |
| Graceful readiness/drain | Unreleased on `master` | Do not sell yet |
| Slow-client/body/query-cost protection | Incomplete | Do not claim production hardening |

## Fix sequence before copywriting

1. Authenticated/versioned secret encryption.
2. Fail-closed constraints and consistent transaction ownership.
3. HTTP timeout/header/body and pagination/query-complexity bounds.
4. Transactional post-commit event outbox.
5. Canonical multi-dimensional rate limiting and proxy validation.
6. SSRF-hardened shared outbound transport.
7. Consistent audit/deletion and external-effect intent semantics.
8. Security headers, log-safety, fuzz/race/database-matrix release gates.
9. Then convert only the safe matrix rows into sales copy.

## Bottom line

Daptin contains substantial invisible backend engineering: hybrid identity, permission-checked references, transaction-scoped database mutations, generated relational indexes, parameterized values, centralized authorization/cache invalidation, URL rate limiting, request and DB-pool bounds, closed CORS defaults, session invalidation, durable mail processing, efficient static delivery, filesystem containment, and graceful lifecycle management.

The deeper audit also finds unevenness: resource limits are incomplete, events precede commit, schema creation can fail open, secret encryption lacks authenticity, transaction ownership varies, and outbound/network/logging defenses need systematic treatment. Website copy should celebrate only concrete mechanisms that survive those qualifications.
