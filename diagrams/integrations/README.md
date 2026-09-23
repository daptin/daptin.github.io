# Connected services: diagram candidates

These diagrams show how Daptin connects a product to payment, CRM, shipping, support, and other business services. They focus on recognizable product ideas: available tasks, approved account connections, business-item changes, delivery attempts, returned details, and clear next steps.

## Candidate 1: ready-to-use service tasks

[The service-tasks diagram](01-provider-operations.mmd) shows how one connected-service setup gives a product a list of useful tasks. A task keeps the details it needs, the account connection it uses, and the details it returns together. Product screens, automatic sequences, and connected tools can all start the same task.

Good fit: the integrations page opening section. It answers, “What does connecting a business service add to my product?”

## Candidate 2: personal and company connections

[The account-connections diagram](02-connected-access.mmd) separates two common choices. A person can approve access to their own account, or a company can securely save sign-in details for a dedicated company account. Daptin confirms that the selected connection belongs to the account starting the task.

Good fit: a section about personal accounts, shared company accounts, and protected sign-in details. It answers, “Which connected account completes this task?”

## Candidate 3: follow a business-item change

[The record-change diagram](03-record-change-follow-up.mmd) begins with an order, customer, shipment, or support ticket being created, edited, or deleted. A matching rule records the next step, sends the selected details to its destination, and keeps the attempt count, completion time, or concise error for review.

Good fit: a section about keeping another business service or Google Sheet in step with product changes. It answers, “What happens after this business item changes?”

## Candidate 4: details, answers, and next steps

[The returned-details diagram](04-inputs-results-and-follow-up.mmd) follows one service task from the business details it needs to the answer it returns. Daptin can save that answer for the next step, such as updating an order, showing a confirmation, or continuing an automatic sequence.

Good fit: a deeper section about turning business details into a service task and using the answer inside the product. It answers, “How does the connected service's answer become useful product behavior?”

## Product takeaways

- One connected-service setup supplies a named list of tasks such as creating a payment, finding a customer, or updating a ticket.
- Each task keeps its required details, sign-in choice, returned details, and completion status together.
- A product screen, an automatic sequence, and a connected tool can start the same task with the same permission rules.
- A personal connection begins when someone approves the requested access to their account.
- A company connection keeps a service key, token, or username and password encrypted for a dedicated company account.
- Daptin confirms ownership before it adds saved sign-in details to a service task.
- A follow-up rule connects a specific business-item change to product automation, another business service, or a Google Sheet.
- Each background delivery keeps its attempt count, next attempt time, completion time, and concise error so administrators can see what happened.

## Plain-language guide

| Website phrase | What it means | Maintainer reference |
|---|---|---|
| Connected service | A named setup for a payment, CRM, shipping, support, or other business service. | `integration` |
| Service description | The service-supplied document that lists available tasks, required details, returned details, and sign-in requirements. | `integration.specification`; OpenAPI document |
| Service task | One named thing the connected service can do, such as creating a checkout, listing tasks, or updating a customer. | OpenAPI `operationId`; installed action `{provider}/{operationId}` |
| Required details | The customer, order, amount, ticket, or other values one service task expects. | OpenAPI parameters and request-body schema; `action.InFields` |
| Returned details | The answer from the connected service, saved together with its completion status. | `{provider}.{operation}.response`; `{provider}.{operation}.statusCode` |
| Saved answer | A name attached to returned details so the next step can use them. | `Outcome.Reference`; action execution context |
| Connection setup | The sign-in page, requested permissions, and service endpoints used when a person connects their own account. | `oauth_connect` |
| Secure account connection | Encrypted access created after a person approves the requested permissions. | `oauth_token` |
| Secure sign-in details | An encrypted service key, token, username, or password used for a company account. | `credential.content` |
| Account starting the task | The person or dedicated company account Daptin recognizes when the task begins. Saved access must belong to this account. | `auth.SessionUser`; `SWITCH_USER` for a later trusted step |
| Sign-in choice | The saved rules that choose a personal connection or company sign-in details and place them where the business service expects them. | `authentication_type`; `authentication_specification` |
| Follow-up rule | A named rule that connects selected changes on one kind of business item to product automation, another business service, or a Google Sheet. | `data_exchange` |
| Delivery record | The saved status of one follow-up, including the changed item, assigned account, attempt count, next attempt, error summary, and completion time. | `exchange_run` |
| Assigned account | The account whose current access to the changed business item is checked before sending it onward. | `data_exchange.as_user_id`; `exchange_run.as_user_id` |
| Attempt allowance | A fixed number of delivery attempts. Temporary failures wait progressively longer, up to one hour, before trying again. | `attempt_count`; `max_attempts`; `next_attempt_at`; `exchangeRetryDelay` |

## Maintainer evidence

The audience-facing phrases above map to these canonical files in the Daptin repository:

- [Connected-service and encrypted sign-in fields](../../../daptin/server/resource/columns.go#L1973-L2001) and [service-description fields](../../../daptin/server/resource/columns.go#L2173-L2237): `credential` stores encrypted content; `integration` stores the service name, description, sign-in choice, encrypted connection rules, and enabled state.
- [Personal-connection setup and saved access](../../../daptin/server/resource/columns.go#L2765-L2894) and [saved-access fields](../../../daptin/server/resource/columns.go#L2977-L3019): `oauth_connect` holds the shared setup, while each account's encrypted access is stored separately in `oauth_token`.
- [Turning a service description into ready-to-use tasks](../../../daptin/server/actions/action_integration_install.go#L160-L288): each declared task becomes a named action with sign-in selection, required fields, and a matching provider outcome.
- [Sharing the same task across entry points](../../../daptin/server/integration_operation_handler.go#L78-L103) and [GraphQL reuse](../../../daptin/server/integration_operation_graphql.go#L70-L101): direct calls and generated GraphQL fields resolve and execute the same installed action.
- [Returned details and completion status](../../../daptin/server/actions/action_integration_execute.go#L307-L377): every supported connection style returns consistently named response details and status.
- [Saving an answer for later steps](../../../daptin/server/resource/handle_action.go#L962-L1006): an outcome with `Reference` places returned attributes and saved-record results into the shared action context.
- [Reading sign-in needs from the service description](../../../daptin/server/resource/integration_security.go#L17-L76): each declared service task determines whether provider sign-in is used and required.
- [Checking saved access against the account](../../../daptin/server/actions/action_integration_execute.go#L763-L827), [matching personal connections](../../../daptin/server/actions/action_integration_execute.go#L1243-L1271), and [placing company sign-in details](../../../daptin/server/actions/action_integration_execute.go#L1274-L1367): Daptin validates the selected access for the current account and places it according to the saved rules.
- [Follow-up rule and delivery fields](../../../daptin/server/resource/columns.go#L2896-L2975): `data_exchange` names the watched change and destination; `exchange_run` stores the changed item, status, attempts, timing, error, and completion fields.
- [Creating a delivery and checking item access](../../../daptin/server/resource/exchange_execution.go#L36-L135): a matching change creates one saved delivery and verifies that the assigned account can read the changed item.
- [Sending to the destination and recording completion](../../../daptin/server/resource/exchange_execution.go#L180-L239) plus [destination choices](../../../daptin/server/resource/exchange.go#L65-L92): one delivery can invoke a Daptin action or a configured outside destination and records success or failure afterward.
- [Further attempts and completion](../../../daptin/server/resource/exchange_execution.go#L489-L568) and [administrator-requested attempts](../../../daptin/server/resource/exchange_execution.go#L578-L617): successful deliveries retain completion time, temporary failures wait progressively longer, the attempt limit marks items for review, and an administrator can grant a fresh bounded allowance.
- [Product-automation destination](../../../daptin/server/resource/exchange_action.go#L18-L83) and [business-service destinations](../../../daptin/server/resource/exchange_rest.go#L20-L45): a follow-up can pass the changed item to a Daptin action, a configured outside request, or the built-in Google Sheets append choice.
- [Canonical connected-services guide](../../../daptin/wiki/Integrations.md#L9-L112) and [canonical follow-up guide](../../../daptin/wiki/Data-Exchange.md#L1-L53): source documentation for installed actions, permissions, account ownership, watched changes, and destinations.
- [Saved-access tests](../../../daptin/server/actions/action_integration_auth_test.go), [service-setup tests](../../../daptin/server/actions/action_integration_install_test.go), [shared-entry tests](../../../daptin/integration_transport_real_e2e_test.go), and [delivery-lifecycle tests](../../../daptin/server/resource/exchange_execution_test.go): executable evidence for generated tasks, account-bound access, shared execution, bounded attempts, and administrator-requested attempts.

## Editorial notes

- “Service description” keeps the audience focused on the list of available tasks. The underlying file follows the OpenAPI standard.
- “Secure account connection” distinguishes a person's approved connection from the shared setup for the business service.
- “Service task” covers every supported way Daptin connects to another service while keeping the product relationship consistent.
- Returned details become a saved answer for later steps. A record change remains explicit: the automatic sequence names the order, customer, shipment, or ticket to update.
- The record-change diagram focuses on background follow-ups created after a business item changes. A separate advanced diagram can explain rules that contact the destination before saving the change.
- Protected third-party accounts use a connected service as the follow-up destination, preserving account ownership and service matching.
- Colors stay consistent across candidates: blue for accounts and business items, amber for saved setup and rules, purple for an active delivery or protected details, green for successful results, and gray for another business service.
