# Actions and automation domain maps

These diagrams present Daptin's actions and scheduled tasks as product concepts. They intentionally describe what a product owner can configure and what the product gains, while leaving request handlers, transactions, and performer registries out of the artwork.

## Diagram set

- `action-domain-map.mmd` — the broad domain: a named action combines accepted inputs, input rules, access, and ordered outcomes that connect records, integrations, templates, events, and product responses.
- `outcome-palette.mmd` — a vocabulary map for the concrete work an ordered outcome can perform, including conditions, repeated work over a bounded list, and reuse of earlier results.
- `scheduled-automation-map.mmd` — the saved task domain: name, schedule, target action, saved inputs, active status, and the account whose identity and groups govern each run.

All three use the same color language:

- blue: the reusable action at the center;
- amber: timing, validation, identity, and access decisions;
- purple: selectable work performed by outcomes;
- green: records, responses, events, and product-visible results;
- gray: saved descriptive fields.

## Product takeaways

1. A named action is a reusable product operation attached to a resource. It carries its input definition, input cleanup and checks, access rules, and ordered outcomes together.
2. An outcome names concrete work. It can work with Daptin records, call a registered capability or integration operation, render saved content, publish a permitted event, or return a response for the product UI.
3. Outcomes run in definition order. Conditions can select a step, references can pass earlier results forward, and `ForEach` can apply an outcome to a bounded collection.
4. A saved task schedules an existing action through the shared action path. It supplies the action name, resource, inputs, schedule, active state, and execution account.
5. Scheduled work uses the selected account and its current groups, so recurring work remains attributable and follows the same action access checks.
6. Action completion is expressed through typed responses and the records or events produced by its outcomes. Product-specific durable history can be one of those records.

## Glossary

| Term | Audience-facing meaning | Grounded Daptin concept |
|---|---|---|
| Named action | A reusable operation such as sending a message, preparing a report, or updating an order. | `Action.Name`, attached to `Action.OnType` / the `world` resource. |
| Inputs | The values an action accepts from the caller or a saved task. | `Action.InFields`; task `attributes`. |
| Input rules | Cleanup and checks applied before work begins. | `Conformations` and `Validations`. |
| Permission | The people and groups allowed to run the action on its resource or selected record. | Resource, action-row, and subject-row `CanExecute` checks. |
| Ordered outcome | One concrete step in an action, evaluated in sequence. | `Action.OutFields` / `Outcome`. |
| Earlier result | A named outcome result available to following outcomes. | `Outcome.Reference` and evaluated action context. |
| Record work | Reading, creating, updating, or deleting a Daptin resource. | `GET`, `GET_BY_ID`, `POST`, `PATCH`, and `DELETE` outcome methods. |
| Daptin capability | A registered operation for mail, files, identity, imports, AI, templates, integrations, and other shared capabilities. | `ActionPerformerInterface` and registered action handlers. |
| Provider operation | An enabled operation installed from an integration definition and invoked as an outcome. | Integration action performer and operation map. |
| Template | Saved content combined with action data to produce rendered content. | `template` resource and `template.render` performer. |
| Published event | A message sent to a permitted resource or live topic. | `__publish_to_topic` performer and CRUD event publication. |
| Product response | A typed result the calling product can use, such as data, a notice, redirect, download, or rendered content. | `ActionResponse.ResponseType` and `Attributes`; `ACTIONRESPONSE`. |
| Saved task | A persisted instruction to run a named action on a schedule. | `task` resource / `task.Task`. |
| Execution account | The account whose current identity and groups are loaded for a scheduled run. | `task` → `user_account` relation through `as_user_id`. |

## Evidence in the Daptin codebase

Paths below are relative to the sibling `daptin` repository.

- `server/actionresponse/action_pojo.go:12-67` defines typed action responses, requests, outcomes, and the action fields for resource attachment, permissions, inputs, ordered outcomes, validation, and conformation.
- `server/resource/columns.go:98-100` declares that an action belongs to a `world` resource; `server/resource/columns.go:2684-2724` defines the persisted action record and its schema.
- `server/resource/handle_action.go:268-308` loads an optional subject and checks subject, resource, and action execution permissions.
- `server/resource/handle_action.go:321-378` gathers inputs, conforms and validates them, and builds the shared context used by outcomes.
- `server/resource/handle_action.go:422-446` processes outcomes in definition order, including bounded `ForEach` execution and conditions.
- `server/resource/handle_action.go:479-664` dispatches record operations, registered capabilities, and typed action responses.
- `server/resource/handle_action.go:961-1007` places referenced results into the action context and controls which results are returned to the caller.
- `server/resource/action_foreach_test.go:179-192` verifies that the `ForEach` and `MaxItems` vocabulary survives action-schema storage and loading.
- `server/resource/action_transaction_permission_test.go` exercises action behavior across action and transaction permission boundaries.
- `server/action_provider/action_provider.go:13-273` assembles the shared capability catalog, including templates, integrations, and topic publication.
- `server/actions/action_render_template.go:34-157` loads a named template and renders it with the action's current data.
- `server/actions/action_integration_execute.go:70-160` resolves an enabled integration operation and prepares its provider call.
- `server/actions/action_publish_to_topic.go:34-125` checks access to a topic and publishes the event with its source and data.
- `server/resource/columns.go:2173-2235` defines integration names, specifications, authentication configuration, and enabled state.
- `server/resource/columns.go:2296-2355` defines saved template content, MIME type, headers, and configuration.
- `server/resource/columns.go:130` relates a task to its execution account; `server/resource/columns.go:2238-2293` defines task name, action, resource, schedule, active state, inputs, and category.
- `server/resource/dbfunctions_get.go:341-393` loads active tasks and resolves the related account reference.
- `server/resource/task_scheduler.go:71-86` loads persisted tasks; `server/resource/task_scheduler.go:106-168` loads the execution account and groups, invokes the shared action handler, and commits the completed run.
- `server/resource/task_scheduler.go:171-195` registers the schedule and converts the saved task into the same action request used elsewhere.
- `server/resource/task_scheduler_test.go:50-205` verifies task persistence, the execution-account relation, updates, and the requirement for an execution account.
- `README.md:118-129` is the canonical high-level description of actions, scheduled tasks, state tracking, and data exchange as related building blocks.

## Editorial notes

- “Provider operation” keeps the diagrams focused on the product relationship across REST, GraphQL, gRPC, and WebSocket providers.
- “Account that runs it” communicates the accountability carried by the `as_user_id` relation in audience-friendly language.
- “Product response” groups Daptin's response directives into the benefit they deliver to an application.
- State machines and data exchange are adjacent automation domains. Dedicated maps can give each domain the space it deserves while this set stays focused on named actions and scheduled tasks.
