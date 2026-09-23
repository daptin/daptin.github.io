# Data-domain diagrams

These maps explain how Daptin turns a product's own vocabulary into connected,
usable information. They use familiar examples such as customers, products,
categories, orders, articles, and cases. Implementation terms appear only in
the evidence notes.

## Audience takeaway

Daptin lets a team name the kinds of information its product needs, describe
the facts each kind carries, and connect records with meaningful
relationships. Every record receives a stable public identity plus ownership
and sharing context. The same product model can add language editions, change
history, states and transitions, measured usage, summaries, imports, and
exports.

Categories are a useful example of Daptin's composition model. A category is a
normal product concept with its own fields and records. A relationship connects
categories to products, articles, or any other concept the product defines.

## Diagram set

- `01-product-vocabulary.mmd` — the broad domain map: models, fields, rules,
  relationships, records, stable references, ownership, ordering, and optional
  record capabilities. Use this as the data-modeling overview.
- `02-connected-catalog-example.mmd` — a concrete product vocabulary with
  categories, products, variants, customers, orders, and order lines. Use it to
  show that Daptin represents real business concepts and their connections.
- `03-record-context.mmd` — three kinds of context attached to the same record:
  language editions, change history, and states with named transitions. Use it
  near localization, audit history, or workflow copy.
- `04-data-movement-and-insights.mmd` — structured import, filters, grouping,
  related data, summaries, and export formats. Use it near import/export or
  aggregation features.

Each `.mmd` file contains Mermaid source only. The labels are deliberately
short enough for responsive SVG rendering and use concrete verbs on every
relationship.

## Plain-language glossary

| Term | Meaning on the website | Daptin source concept |
|---|---|---|
| Product model | One kind of information the product keeps, such as a customer, product, order, article, or case. | `TableInfo` / `world` entry |
| Field | One named fact carried by every record of a model, such as title, price, status, or date. | `ColumnInfo` |
| Field rule | A requirement or cleanup rule applied to a field, including required values, formats, uniqueness, validation, conformation, and defaults. | Column properties, `Validations`, and `Conformations` |
| Record | One actual item in a product model, such as a particular customer or order. | Resource row / API model |
| Public reference | The stable identifier used to refer to a record across product-facing interfaces. | `reference_id` |
| Relationship | A named connection between models and their records. | `TableRelation` |
| One connected record | A required connection from one record to one other record. | `belongs_to` |
| One optional record | An optional connection from one record to one other record. | `has_one` |
| Collection | A record connected to several records of another model. | `has_many` |
| Many on both sides | Several records on either side connected through one named relationship. | `has_many_and_belongs_to_many` |
| Category | An ordinary product model used to organize other records; its meaning and fields belong to the product. | A user-defined resource connected by a relation |
| Language edition | Language-specific field values connected to the same underlying record. | Generated `{model}_i18n` resource selected by `language_id` |
| Change history | An earlier record snapshot with the source reference and operation that created it. | Generated `{model}_audit` resource |
| State definition | An initial state plus named events and their permitted source and destination states. | `smd` / `LoopbookFsmDescription` |
| Current state | The durable workflow position of one record. | Generated `{model}_state` resource |
| Summary | A grouped or filtered answer such as count, total, average, minimum, or maximum. | Aggregation API / `DataStats` |
| Import | Creating records from JSON, CSV, or an Excel workbook. | `__data_import` and streaming import parsers |
| Export | Packaging selected record fields as JSON, CSV, Excel, PDF, or HTML. | `__data_export` and streaming export writers |

## Source evidence

The diagrams follow the current code, tests, and canonical guides in the
sibling Daptin repository.

### Product models, fields, and records

- `../../../daptin/server/table_info/tableinfo.go#L106-L132`, `TableInfo`:
  establishes the model name, fields, state definitions, relationships,
  visibility, state/history/language switches, groups, validation,
  conformation, ordering, keys, indexes, and metering configuration.
- `../../../daptin/server/resource/columns.go#L2454-L2529`, the `world`
  resource: persists each model's name and complete schema and records its
  presentation and state-tracking choices.
- `../../../daptin/server/resource/dbfunctions_check.go`, `CheckRelations`:
  supplies ordinary models with record ownership and group-sharing relations.
- `../../../daptin/server/resource/resource_create.go#L39-L552` and
  `../../../daptin/server/resource/resource_update.go#L39-L590`: create stable
  public record references, apply configured fields, preserve ownership, and
  maintain related language and history context.
- `../../../daptin/wiki/Schema-Definition.md`, **What Gets Auto-Created** and
  **Common Patterns**: canonical customer-facing examples for models, fields,
  records, ownership, public references, and optional capabilities.

### Relationships and categories

- `../../../daptin/wiki/Relationships.md`, **Relationship Types** and
  **Defining Relationships**: defines required one-to-one, optional one-to-one,
  one-to-many, and many-to-many connections.
- `../../../daptin/server/graphql.go#L54-L185`: generates create and update
  inputs from the same configured relationship names and public references.
- `../../../daptin/server/graphql_relationship_args_test.go#L13-L110`: proves
  required category links, optional updates, product-to-tag collections, and
  relationship reference validation.
- `../../../daptin/wiki/Schema-Examples.md#L20-L165`: provides the canonical
  category, post, comment, and author example that grounds categories as
  normal connected product concepts.

### Language, history, and states

- `../../../daptin/server/resource/dbfunctions_create.go#L338-L439`,
  `CheckTranslationTables`: derives a language-edition resource with a language
  identifier and a connection back to the source model.
- `../../../daptin/server/resource/resource_findone.go#L85-L145` and
  `../../../daptin/server/resource/resource_findallpaginated.go#L1128-L1175`:
  select language-specific values using the request's language preference.
- `../../../daptin/server/resource/dbfunctions_create.go#L491-L585`,
  `CheckAuditTables`: derives a history resource with source reference and
  operation fields while excluding sensitive payloads.
- `../../../daptin/server/resource/resource_update.go#L555-L590` and
  `../../../daptin/server/resource/resource_delete.go#L90-L120`: write history
  entries for record changes and removal.
- `../../../daptin/server/resource/audit_table_test.go#L10-L108`: proves safe
  generated history fields, source references, operation labels, and protected
  default access.
- `../../../daptin/server/fsm/fsm_manager.go#L66-L185`: loads each record's
  current state, checks named events against allowed source states, and resolves
  the next state.
- `../../../daptin/server/resource/fsm.go` and
  `../../../daptin/wiki/State-Machines.md`: connect a state definition and a
  state instance to the product record and describe the public state vocabulary.

### Summaries, imports, and exports

- `../../../daptin/server/resource/resource_aggregate.go#L90-L112` and
  `#L586-L810`, `DataStats`: supports schema-checked filters, groups, related
  models, ordering, and count, sum, average, minimum, maximum, first, and last
  summaries.
- `../../../daptin/server/resource/resource_aggregate_security_test.go`:
  verifies that summary fields and related models stay within the configured
  product schema and access rules.
- `../../../daptin/server/actions/streaming_import_parsers.go#L14-L36` and
  `#L405-L450`: supplies JSON, CSV, and Excel import readers.
- `../../../daptin/server/actions/action_import_data.go#L29-L219`: turns
  imported rows into records for the selected product models and reports the
  resulting record counts.
- `../../../daptin/server/actions/action_export_data.go#L15-L110`: selects
  models and fields and supports JSON, CSV, Excel, PDF, and HTML output.
- `../../../daptin/wiki/Aggregation-API.md`: canonical examples for filters,
  grouping, connected data, ordering, and summaries.

## Editorial boundaries

- The maps say “product model” and “record” where the implementation uses
  table, world, resource, model, and row in different layers.
- The catalog map is an example composition. Daptin supplies the modeling and
  relationship capabilities; each product chooses its own names and fields.
- “Field rules” combines field properties, validation tags, and conformation
  tags into one audience-facing concept.
- “Language edition” describes a language-specific set of field values linked
  to the same record.
- “Change history” describes the generated history record and its source and
  operation context. The diagram stays focused on the value of retained
  history.
- The insights map names familiar outputs and questions. The code retains
  schema validation and permission checks behind those audience-facing terms.
