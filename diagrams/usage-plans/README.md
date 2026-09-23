# Usage plans and metering: domain-map candidates

These diagrams explain the customer-facing ideas behind Daptin usage plans. They center product concepts and keep database tables, middleware, locks, and request plumbing in the supporting source notes. Their labels describe current Daptin capabilities in plain language.

## Candidate 1: the domain map

[`domain-map.mmd`](domain-map.mmd) is the broadest introduction. It shows how an account receives a plan through an active membership, how the plan supplies limit rules, and how usage and quota records retain the activity for that membership.

Good fit: the usage-plans page hero or the first explanatory section. It answers, “What are the parts, and how do they relate?”

## Candidate 2: reserve, run and settle

[`reservation-lifecycle.mmd`](reservation-lifecycle.mmd) tells the lifecycle story. Daptin checks the account's plan, holds estimated capacity, and then settles the reservation according to the operation's result. Completion, cancellation, and expiry each leave a clear usage outcome.

Good fit: a section about predictable limits, concurrent work, or the difference between a reservation and measured usage. It answers, “What happens to capacity while work is running?”

## Candidate 3: measures and time windows

[`measures-and-windows.mmd`](measures-and-windows.mmd) shows how many product activities share one vocabulary: named measures, plan rules, quota windows, and usage records. It also shows the optional follow-up action for credits, billing, or reporting.

Good fit: a detailed feature section or a cross-link between usage plans, AI workloads, actions, and integrations. It answers, “What can a plan measure?”

## Plain-language glossary

| Term | Meaning on the website | Daptin source concept |
|---|---|---|
| Plan | A named offer containing a price and usage-limit rules. | `api_plan` |
| Membership | The record that connects an account to a plan and can carry a billing period. Daptin uses the newest active membership for metering. | `api_member` |
| Limit rule | A named measure, time window, maximum, and enforcement behavior stored on a plan. | One entry in `api_plan.limits` |
| Admission | The decision made before work begins: Daptin finds the account's active membership and checks available capacity against its plan. | `MeteringService.Admit` |
| Reservation | Estimated capacity held while an admitted operation runs. | `reserved_measures` and `reservation_buckets` on `api_usage`; `reserved` on `api_quota` |
| Named measure | A count that carries its own name, such as requests, bytes, tokens, cost, search units, or a product-specific unit. | `EstimatedMeasures`, `Measures`, and a configured `meter_type` |
| Cost expression | A rule attached to a metered resource or action that calculates its configured measure from request, response, metadata, and user context. | `MeteringConfig.CostExpr` and `completionMeasures` |
| Time window | The period in which a limit applies: minute, hour, day, month, or the membership's own period. | `meteringWindow` |
| Quota record | The durable total for one measure and one time window, including maximum, currently held capacity, and consumed capacity. | `api_quota` |
| Usage record | The durable history of one metered operation: identity, state, reserved and final measures, request and response details, and result. | `api_usage` |
| Completion | The operation finishes; Daptin releases its estimate, adds actual measured usage, and closes the usage record. | `MeteringService.Complete` |
| Cancellation | The operation stops early; Daptin releases its estimate, records reported measures, and closes the usage record as cancelled. | `MeteringService.Cancel` |
| Expiry | A held reservation reaches its deadline; Daptin releases the reserved capacity and closes the usage record as expired. | `MeteringService.ExpireReservations` |
| Hard guardrail | A limit that admits work while enough capacity remains. | `mode: "hard"` |
| Soft tracking | A limit that records activity while allowing admission to continue. | `mode: "soft"` |
| Follow-up action | An optional Daptin action invoked after metering, with the plan, membership, usage, measures, and operation context. | `post_metering_action` |

## Source evidence

The diagrams are grounded in these canonical files in the Daptin repository:

- [Canonical resource relationships](../../../daptin/server/resource/columns.go#L120-L124): memberships point to plans; usage and quota records point to both plans and memberships.
- [Plan, membership, usage, and quota fields](../../../daptin/server/resource/columns.go#L3221-L3240) and [continued entity definitions](../../../daptin/server/resource/columns.go#L3297-L3353): price, named limit rules, membership periods, lifecycle states, reserved and final measures, and quota totals.
- [Admission and reservation creation](../../../daptin/server/resource/metering.go#L156-L277): the active account, newest active membership, plan, estimates, limit reservations, and held usage record are resolved together before metered work begins.
- [Completion, cancellation, and expiry](../../../daptin/server/resource/metering.go#L279-L392): all terminal outcomes release reservations and write the usage outcome; completion and cancellation can settle reported measures.
- [Quota settlement](../../../daptin/server/resource/metering.go#L329-L393) and [quota reservation](../../../daptin/server/resource/metering.go#L594-L655): held capacity moves into consumed capacity using the operation's actual measure.
- [Plan-rule validation and supported windows](../../../daptin/server/resource/metering.go#L750-L826): each rule combines a named measure, unique window, non-negative maximum, and hard or soft behavior.
- [Estimated and final measures](../../../daptin/server/resource/metering.go#L828-L872): requests are counted consistently, bytes are derived from payload sizes, supplied measures are retained, and configured cost expressions calculate a missing measure.
- [Post-metering action context](../../../daptin/server/resource/metering.go#L1000-L1024): an optional action receives the account, usage, plan, membership, measures, and operation details.
- [Operator-facing metering guide](../../../daptin/wiki/API-Metering.md#L1-L340): canonical descriptions of resources, plan rules, supported operation types, LLM measures, reservation settlement, and follow-up billing actions.
- [Lifecycle and concurrency tests](../../../daptin/server/resource/metering_test.go#L25-L113), [actual-measure settlement tests](../../../daptin/server/resource/metering_test.go#L517-L585), and [reservation expiry tests](../../../daptin/server/resource/metering_test.go#L685-L746): executable evidence for one reservation per request, limit enforcement, actual-versus-estimated settlement, cancellation, and expiry.

## Editorial notes

- The diagrams use “customer account” and “membership” in place of internal ownership fields.
- “Capacity held” and “capacity consumed” translate the durable `reserved` and `consumed` quota totals.
- “Plan limit reached” is the audience-facing form of a hard-limit admission response.
- The examples name AI model calls as one metered activity, while the same plan and usage domain also covers resources, actions, schedules, and direct integration operations.
- Diagram colors carry the same roles across candidates: blue for product activity or accounts, amber for plan policy, purple for active work, and green for durable outcomes.
