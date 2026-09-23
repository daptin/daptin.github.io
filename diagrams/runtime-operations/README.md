# How Daptin stays available

These drawings show how Daptin protects business information, serves customers, runs recurring automations, and restarts cleanly. Every label names something a product owner or business team can recognize.

## Drawing choices

- `operational-landscape.mmd` connects customer and business records, uploaded files, product settings, customer requests, recurring automations, availability checks, activity history, and backups. It is the broadest overview.
- `service-lifecycle.mmd` follows one running copy of Daptin as it opens business records, begins serving customers, and later finishes accepted requests before stopping.
- `scheduled-work.mmd` shows the information saved for each recurring automation and what Daptin does when its chosen time arrives.
- `operator-view.mmd` connects availability checks, traffic measurements, activity history, backups, and restoration practice to clear decisions for the team responsible for the product.

The four Mermaid files share one color language: blue for saved information, purple for customer-facing capabilities, amber for information shared between Daptin copies, green for successful outcomes, and gray for checks and history.

## Product takeaways

1. Daptin keeps customer records, business records, product settings, and recurring automation plans in the selected database. It keeps uploaded documents and media in the selected file storage.
2. Multiple running copies exchange recently requested information, record-change alerts, request counts, duplicate-prevention markers, and their presence. The database and stored files remain the saved source of truth.
3. One Daptin application can deliver websites, app connections, email, file access, feeds, live updates, collaborative documents, AI requests, connected providers, and recurring automations.
4. Each recurring automation records its day and time, account, group access, business record, chosen action, and input values. At the chosen time, Daptin applies the same account permissions and action rules used for a customer request.
5. One check confirms that Daptin answers. A second confirms that the database is connected and that Daptin can safely receive customer traffic.
6. During a restart, Daptin first asks the traffic router to stop sending new requests. It pauses new automations, mail sessions, and file sessions; finishes accepted requests and live connections; then closes the database connection.
7. Teams can inspect customer traffic, database activity, memory, disk space, machine load, and request or error history.
8. A complete recovery practice backs up and restores the business records and uploaded files together.

## Words used in the drawings

| Phrase | Plain-language meaning |
|---|---|
| Running Daptin copy | One copy of Daptin currently serving customers. Several copies can serve the same product. |
| Recurring automation | A saved action that Daptin starts at the selected day or time using a selected account. |
| Ready for customers | Business records are reachable and this Daptin copy can safely receive new requests. |
| Record-change alert | An immediate notice that a customer or business record changed. |
| Duplicate-prevention marker | A short-lived marker that lets one Daptin copy run an automation while the other copies leave it alone. |
| Request and error history | Timestamped details that help the team find a failed request or automation. |
| Restoration practice | A rehearsal that proves business records and uploaded files can be recovered together. |

## Source notes for reviewers

Paths below are relative to the `daptin.github.io` repository root and point into the sibling `daptin` source repository. The descriptions use customer-facing language; the cited files contain the exact implementation.

### How Daptin starts and stores information

- `../daptin/main.go:194-215` selects the database, file location, peer addresses, and time allowed for a clean stop.
- `../daptin/main.go:318-329` opens and verifies the selected database before customer-facing capabilities start.
- `../daptin/main.go:466-472` builds the running Daptin copy and connects its traffic check to the database check.
- `../daptin/server/server.go:69-130` loads product settings, saved kinds of business records, existing records, and recently requested files.
- `../daptin/server/server.go:270-335` connects account sign-in, business records, customer requests, and record-change alerts to the same database.
- `../daptin/server/server.go:680-720` gathers mail sending, inbox access, file transfer, recurring automations, live updates, collaborative documents, AI requests, and provider updates under one running Daptin copy.
- `../daptin/server/runtime.go:19-39` lists everything that one running Daptin copy owns until it stops.

### How multiple Daptin copies stay in sync

- `../daptin/main.go:355-445` finds the other Daptin copies, joins them, and prepares shared information.
- `../daptin/main.go:447-464` announces when a Daptin copy joins and receives the same announcements from its peers.
- `../daptin/server/middleware_ratelimit.go:82-153` shares request counts for short time windows.
- `../daptin/server/resource/middleware_eventgenerator.go:95-109` sends record-change alerts.
- `../daptin/server/llm/gateway.go:52-64` shares AI request counts, duplicate-prevention markers, and recent results.
- `../daptin/server/websockets/web_socket_connection_handler.go:181-207` delivers shared alerts to live customer connections.
- `../daptin/olric_config_test.go` and `../daptin/scripts/testing/cluster-test-websocket-pubsub.sh` verify that multiple Daptin copies discover each other and deliver the same live alerts.

### How recurring automations run

- `../daptin/server/resource/task_scheduler.go:20-68` starts and stops recurring automations and returns expired usage reservations to the available balance.
- `../daptin/server/resource/task_scheduler.go:71-86` loads saved automation records when Daptin starts.
- `../daptin/server/resource/task_scheduler.go:88-130` groups every database change so they save or cancel together, confirms the selected account, and runs the chosen action.
- `../daptin/server/resource/task_scheduler.go:140-180` loads the account and its groups, confirms the chosen kind of business record exists, and registers the chosen time.
- `../daptin/server/server.go:530-592` adds mail refresh, messages waiting to be sent, data exchange, file copying, expired-reservation recovery, and pending AI requests to the recurring automation plan.
- `../daptin/server/resource/task_scheduler_test.go` verifies that saved automations start, finish, and stop as expected.

### How Daptin reports status and restarts

- `../daptin/lifecycle.go:9-44` separates “Daptin answers” from “Daptin can safely receive customer traffic” and includes the database in the second answer.
- `../daptin/lifecycle_test.go:14-48` verifies those two answers; `:50-101` verifies that a request already accepted finishes during a restart.
- `../daptin/main.go:559-622` opens regular and secure website connections and then announces that Daptin is ready for traffic.
- `../daptin/main.go:622-660` stops new traffic, pauses new automations, finishes accepted requests, closes live connections, and finally closes shared information and the database.
- `../daptin/server/runtime.go:41-97` pauses new mail, file, and automation activity; finishes live connections and AI requests; and closes recent-result stores.
- `../daptin/server/statistics.go:341-410` reports requests, database connections, CPU, memory, disk, machine identity, load, and Daptin's own memory and CPU use.
- `../daptin/main.go:110-157` saves request and error history to the console and, when configured, to files with size, age, and retention limits.

### How teams deploy and recover Daptin

- `../daptin/kubernetes/base/deployment.yaml:45-75` checks startup, customer-traffic readiness, and continued response separately.
- `../daptin/kubernetes/README.md:71-84` explains shared file storage, traffic removal before restart, stop timing, and restore practice for PostgreSQL and local files.
- `../daptin/docker-compose.yml:42-43` gives Daptin a defined period to finish accepted requests during a container restart.
