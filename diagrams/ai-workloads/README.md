# AI workloads domain maps

These diagrams explain Daptin's AI workload domain to product owners, operators, and other non-technical readers. They describe the concepts a product gains and how those concepts relate; they deliberately avoid HTTP handlers, database transactions, and other implementation plumbing.

## Audience takeaway

- A stable public model name can connect a product to one or more provider deployments.
- Each model declares the work and product features it supports, including tools, files, streaming, and structured output.
- Files, batches, batch items, and their results are durable, permissioned Daptin records.
- Model permission and usage admission answer separate questions: who may use a model, and how much an account may use.
- Plans, reservations, measured usage, calculated cost, completion, quota totals, and usage history form one accountable lifecycle.

## Diagram candidates

1. [`01-model-catalog.mmd`](01-model-catalog.mmd) — the relationship between a product-facing model, its deployments, provider accounts, credentials, routing, capacity, and pricing.
2. [`02-workload-landscape.mmd`](02-workload-landscape.mmd) — the kinds of AI work available through the shared model catalog and the features that enrich that work.
3. [`03-files-and-batches.mmd`](03-files-and-batches.mmd) — how durable files support model context and multi-request batches with per-item and aggregate results.
4. [`04-usage-and-limits.mmd`](04-usage-and-limits.mmd) — the customer-facing meaning of plans, admission, reservations, measured cost, completion, quota state, and usage records.

The diagrams share a visual vocabulary:

- Blue: the product or customer account entering the domain.
- Purple: durable catalog or usage records managed by Daptin.
- Amber: policies, controls, and configuration.
- Green: work and results delivered to the product.
- Gray: external providers and provider-specific details.

## Plain-language glossary

| Term | Meaning |
|---|---|
| Public model | The stable name a product uses, independent of the provider model that ultimately performs the work. |
| Provider account | A configured connection to an AI provider. It holds connection settings and refers to a protected credential. |
| Deployment | One usable pairing of a public model with a provider model, including routing, capacity, health, pricing, and time limits. |
| Capability | An explicitly enabled model feature such as tools, files, vision, structured output, reasoning, or parallel tools. |
| Streaming | Delivery of generated output as it becomes available. |
| Embedding | A numeric representation of meaning that products can use for similarity and retrieval. |
| AI file | A permissioned record that gives an uploaded Daptin document a purpose, processing status, and optional expiry. |
| Batch | A durable collection of named model requests read from an input file and summarized with status and request totals. |
| Batch item | One request in a batch, with its own completion state and response. |
| Plan membership | The link that applies a usage plan to an account for a defined period. |
| Admission | The decision that checks applicable plan limits before provider work begins. |
| Reservation | Capacity held against the applicable quota window while work is in progress. |
| Measured usage | Provider-reported or safely estimated units such as input tokens, output tokens, search units, or OCR pages. |
| Measured cost | Usage measures converted with the selected deployment's fixed-point pricing. |
| Completion | The step that reconciles the reservation, records final measures, and updates quota totals. Cancellation closes the same lifecycle and releases reserved capacity. |
| Usage record | The durable history of one admitted operation, including its state, measures, cost context, and terminal result. |

## Evidence in the Daptin codebase

All paths below are relative to the sibling `daptin` repository.

### Catalog, providers, and models

- `server/resource/columns.go:3146-3218` defines provider accounts, public models, deployments, model operations and capabilities, fallback models, routing settings, capacity controls, pricing, and health settings.
- `server/resource/columns.go:113-115` defines provider-to-credential and deployment-to-model/provider relations.
- `server/llm/catalog.go:39-50` loads enabled providers, models, and deployments into one catalog; `server/llm/catalog.go:157-181` builds deployments with their model and provider identities.
- `server/llm/catalog_test.go:56-88` constructs the credential → provider ← deployment → model relationship and verifies it through the catalog.
- `server/llm/catalog_test.go:138-201` exercises pricing, fallback models, weighting, and live catalog updates.
- `wiki/LLM-Providers.md:13-20` documents the three main catalog resources and their relationship in product terms.
- `wiki/LLM-Providers.md:140-170` lists model operations and optional capabilities.
- `wiki/LLM-Providers.md:286-302` documents deployment eligibility, weighted selection, fallback behavior, and pricing measures.

### Workloads and product-facing features

- `wiki/LLM-Providers.md:306-337` lists the implemented chat, completion, responses, embeddings, image, moderation, reranking, audio, search, OCR, files, batches, and model-discovery surfaces, including streaming behavior.
- `wiki/LLM-Providers.md:341-424` traces durable files into file-assisted responses and tool-backed web search while preserving independent file and model permissions.
- `server/actions/action_llm_chat.go:27-99` exposes chat as a reusable Daptin action and returns content, model, finish reason, tool calls, and usage.
- `server/actions/action_llm_embedding.go:23-64` exposes embeddings through the same action system and returns vectors plus usage.
- `server/llm/catalog_test.go:244-343` verifies responses with files and web-search tools through the catalog and records their usage.
- `server/llm/catalog_test.go:396-455` verifies streaming work, cancellation, and terminal usage state.

### Files and batches

- `server/resource/columns.go:116-119` defines file-to-document, batch-to-input/output-file, and batch-item-to-batch relations.
- `server/resource/columns.go:3244-3294` defines the durable fields for AI files, batches, and batch items.
- `server/resource/llm_gateway_schema_test.go:101-117` verifies that files use canonical Daptin documents and that batches use required input files, optional output files, and related batch items.
- `server/llm/files.go:55-105` stores an uploaded AI file through a Daptin document and AI file record.
- `server/llm/batches.go:20-67` creates a batch from a purpose-specific input file and initializes its status and totals.
- `server/llm/batch_processor.go:225-316` turns input lines into durable batch items and advances the batch into progress.
- `server/llm/batch_processor.go:340-453` executes pending items and records each result and aggregate totals.
- `server/llm/batch_processor.go:510-519` links the completed batch to its output file.

### Permission, plans, usage, and limits

- `server/llm/ports.go:56-77` applies the ordinary model execute permission to invocation.
- `server/llm/ports.go:90-181` admits, completes, and cancels model usage through the shared metering service.
- `server/resource/columns.go:3173-3179` enables metering for model invocation.
- `server/resource/columns.go:120-124` relates memberships, usage records, and quota state to plans.
- `server/resource/columns.go:3221-3240` defines named plan limits.
- `server/resource/columns.go:3297-3353` defines memberships, usage reservations and measures, and quota windows with reserved and consumed totals.
- `server/llm/ports_test.go:35-181` verifies completed and cancelled usage records, including embeddings and guest-account attribution.
- `wiki/API-Metering.md:247-281` documents the separate model-permission and quantity gates, normalized LLM measures, deployment pricing, and account ownership.
- `wiki/API-Metering.md:283-294` documents reservation, completion, cancellation, expiry, and quota reconciliation.

## Editorial notes

- “AI” is used in visitor-facing labels; exact resource names remain in this evidence section.
- “Provider model” and “public model” remain separate because that distinction is a concrete product benefit: products can keep one stable model name while deployments change underneath it.
- Deployment safeguards and customer plan limits remain separate. Capacity controls protect provider routes; plan limits define customer usage.
- Permission and admission remain visibly separate: model access evaluates entitlement, while plan admission evaluates quantity.
