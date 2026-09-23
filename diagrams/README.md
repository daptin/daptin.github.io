# Daptin product-story diagrams

This folder contains the editable Mermaid sources used to explain Daptin through familiar business situations. Each folder explores one part of the customer experience, and the diagrams now appear beside the corresponding explanations across the product pages.

## Website use

- Editable sources live in this `diagrams/` tree.
- Production SVG files mirror the same paths under `images/diagrams/`.
- Each SVG is embedded on the most specific matching product page with a descriptive caption, alt text, and a full-size link.
- Regenerate an SVG with `npx -y @mermaid-js/mermaid-cli -i diagrams/<domain>/<name>.mmd -o images/diagrams/<domain>/<name>.svg` after changing its source.

## Diagram principles

- Show recognizable product concepts and the relationships between them.
- Use plain-language labels in the diagram; keep code identifiers in the accompanying source notes.
- Make each diagram understandable without reading implementation documentation.
- Prefer a small, focused map over one exhaustive technical architecture chart.
- Describe capabilities Daptin currently provides, without release-history or future-availability language.
- Keep Mermaid source editable and accessible, with a short prose explanation beside each diagram.

## Diagram catalog

The collection contains 37 Mermaid diagrams across ten customer stories. Each folder has its own README with audience takeaways, a glossary, suggested uses, and links to the supporting Daptin code and documentation.

| Customer story | Folder | Candidates | What the diagrams make visible |
|---|---|---:|---|
| Plans and allowances | `usage-plans/` | 3 | What a plan includes, what customers have used, when allowances renew, and what happens when a limit is reached |
| AI in your product | `ai-workloads/` | 4 | Customer-facing AI choices, conversations, writing, images, audio, documents, large request lists, prices, and allowances |
| Company email | `mail/` | 4 | Company addresses, mailboxes, incoming messages, personal emails, delivery progress, and trusted sender setup |
| Accounts and teams | `identity/` | 4 | Sign-in, teams, shared access, account recovery, extra sign-in protection, and trusted app connections |
| Files and published content | `files-content/` | 4 | Uploads, cloud file destinations, downloads, image changes, websites, subscriber feeds, calendars, and contacts |
| Repeatable business tasks | `actions-automation/` | 3 | Required details, approved people, ordered results, connected services, customer responses, and scheduled routines |
| Your business information | `data-domain/` | 4 | Customers, products, orders, useful details, business connections, languages, change history, progress stages, imports, and reports |
| Connected business services | `integrations/` | 4 | Payments, CRM, shipping, support, personal approvals, company connections, and reliable follow-ups |
| Websites and subscriber updates | `sites-publishing/` | 3 | Website files, web addresses, secure visitor access, pages prepared for each visitor, and subscriber feeds |
| Keeping Daptin available | `runtime-operations/` | 4 | Customer requests, recurring routines, multiple Daptin copies, availability checks, activity history, backups, and safe restarts |
