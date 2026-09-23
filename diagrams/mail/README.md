# Mail domain diagrams

These maps explain Daptin's mail domain as a set of product concepts. Readers
can understand what Daptin manages and how the pieces relate through familiar
mail and product vocabulary.

## Audience takeaway

Daptin treats mail as connected product data. A mail domain has owned sender
accounts; accounts have mailboxes; mailboxes hold messages; messages can expose
useful bodies and attachments to product workflows. Outgoing messages keep a
Sent copy and a delivery record for every recipient, including retry history.
The sender domain's DNS and signing identity travel with that delivery model.

## Diagram set

- `mail-domain-map.mmd` — the stable vocabulary and cardinal relationships:
  mail server, owner, account, mailbox, message, message parts, outbox entry,
  and delivery history. Use this as the broad feature overview.
- `incoming-mail-journey.mmd` — how a message for a known account becomes an
  INBOX or Spam message, then yields bodies and attachments that a product
  workflow can use. Use this near inbound mail or automation copy.
- `outgoing-mail-journey.mmd` — how product data and a template become a
  message, a single Sent copy, per-recipient delivery records, and visible
  retry state. Use this near actions, notifications, or delivery operations.
- `sender-domain-readiness.mmd` — the connected sender-address, mail-host,
  signing-key, and DNS concepts behind a recognizable sending identity. Use
  this for domain setup or production delivery guidance.

The `.mmd` files contain Mermaid source only. Their node labels deliberately
use customer-facing terms. Edge labels carry the verbs so the relationship is
readable even before the surrounding page copy is read.

## Glossary

| Term | Plain-language meaning |
|---|---|
| Mail server | The configured public home that hosts one or more Daptin mail accounts. |
| Mail account | An owned email address that can authenticate, send, receive, and organize mail. |
| Mailbox | A folder such as INBOX, Spam, Sent, or a folder created by the account owner. |
| Message | A stored email with searchable fields, status flags, and its original RFC 822 content. |
| Message parts | The plain-text body, HTML body, inline content, and attachments extracted from a stored message. |
| Template | A reusable message body filled with values from product records. |
| Named action | A product operation that can render a template and queue mail using a selected sender. |
| Sent copy | The sender's mailbox copy, created once when Daptin queues the message. |
| Outbox entry | The durable delivery record Daptin creates for one recipient. |
| Delivery attempt | An attempt to hand an outbox message to the recipient domain's mail provider. |
| Retry record | The attempt count, last error, and next eligible delivery time kept on a pending outbox entry. |
| DKIM | A domain signature that lets the receiving provider verify who signed the message. |
| MX | The DNS direction that identifies where a domain receives mail. |
| SPF | The DNS statement that identifies servers authorized to send for a domain. |
| DMARC | The domain policy that aligns the visible From address with authenticated mail. |
| PTR | Reverse DNS that connects a sending IP address back to its mail hostname. |

## Source evidence

The diagrams faithfully summarize the current mail model implemented by the
code paths and described by the canonical documentation.

### Entities and relationships

- `../daptin/server/resource/columns.go`, `StandardRelations`: `outbox`
  belongs to `mail_server`; `mail_account` belongs to `mail_server`; `mail_box`
  belongs to `mail_account`; `mail` belongs to `mail_box`.
- `../daptin/server/resource/columns.go`, standard table definitions for
  `mail_server`, `mail_account`, `mail_box`, `mail`, and `outbox`: establishes
  the customer-visible fields represented in the maps, including message
  metadata, mailbox flags, attachment presence, sent state, retry count, last
  error, and next retry time.
- `../daptin/server/resource/mail_functions.go`,
  `ResolveMailSenderAccount`, `MailAccountSessionUser`,
  `CreateMailAccountBox`, and `AppendSentMailForSender`: grounds account
  ownership, mailbox creation, sender selection, and the one-time Sent copy.

### Incoming mail and message contents

- `../daptin/server/mail_adapter.go`, inbound recipient branch: resolves the
  recipient mail account, verifies DKIM for spam scoring, chooses INBOX or
  Spam, detects attachments, allocates the mailbox UID, and creates the `mail`
  resource with the account owner.
- `../daptin/server/actions/action_mail_unpack.go`,
  `mailUnpackActionPerformer.DoAction`: exposes preferred text, optional HTML,
  and ordered message parts as reusable file values.
- `../daptin/server/actions/mail_mime.go`, `normalizeMail`: classifies inline
  parts and attachments and records filename, media type, size, content ID,
  and digest.
- `../daptin/server/actions/action_mail_unpack_test.go`,
  `TestMailUnpackConsumesResolvedMailValue`: proves an attachment from a stored
  message is returned as usable decoded content.
- `../daptin/wiki/IMAP-Support.md`, **IMAP Features** and **Folder Structure**:
  documents mailbox operations, automatic INBOX and Spam folders, search,
  flags, copying, deletion, and push notifications.

### Outgoing messages, templates, and delivery records

- `../daptin/server/actions/action_mail_send.go`,
  `mailSendActionPerformer.DoAction`: authorizes the owned sender, selects the
  related mail server, DKIM-signs the message, appends one Sent copy, and
  creates one outbox row per recipient.
- `../daptin/server/actions/action_outbox_process.go`,
  `outboxProcessActionPerformer.processPendingMail` and `markFailed`: grounds
  delivery attempts, success state, last error, bounded retries, and scheduled
  exponential backoff.
- `../daptin/server/actions/action_mail_send_test.go`: confirms the sender's
  mail-server relationship selects the hostname.
- `../daptin/server/actions/action_outbox_process_test.go`: confirms recipient
  domain routing and the configured sender hostname remain distinct.
- `../daptin/wiki/Email-Actions.md`, **Email Templates**: demonstrates a
  template filled with customer and order values before `mail.send` queues the
  message.
- `../daptin/wiki/Production-Mail-Delivery.md`, **Delivery Model**: documents
  the Sent-copy, per-recipient outbox, immediate-attempt, success, failure, and
  retry lifecycle.

### Sender domain and DNS identity

- `../daptin/wiki/Production-Mail-Delivery.md`, **Hostnames And Domains** and
  **DNS Checklist**: distinguishes the SMTP host, visible sender, and DKIM
  domain and lists the MX, PTR, SPF, DKIM, and DMARC relationships.
- `../daptin/server/actions/action_mail_send.go`, DKIM signing and
  `mailSendServerHostname`: grounds signing in the From domain while the
  sender account's relationship selects the mail-server hostname.
- `../daptin/wiki/SMTP-Server.md`, **Email Tables**, **Outgoing Mail**, and
  **Spam Filtering**: corroborates the entity vocabulary, outbound signing,
  and incoming placement concepts.

## Editorial boundaries

- “Product data” and “product workflow” mean ordinary Daptin resources and
  named actions. Customer, order, and case illustrate resources a product can
  define and connect to mail.
- The attachment path represents received-message unpacking. The basic
  `mail.send` path sends its supplied body, while received parts become file
  values that subsequent action outcomes can store.
- A successful outbox attempt represents the recipient's mail provider
  accepting the SMTP handoff. Inbox placement and human receipt remain with
  the receiving provider and recipient.
