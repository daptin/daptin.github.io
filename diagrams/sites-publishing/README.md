# Sites and publishing domain maps

These diagrams show how a team can publish websites, pages filled with current business information, and subscriber updates with Daptin. The labels focus on the result people recognize while the evidence notes connect each statement to the implementation.

## Diagram set

- `01-site-portfolio.mmd` — how website files move from a local folder or cloud drive to a secure public web address.
- `02-pages-for-each-visitor.mmd` — how a page combines its saved design, details from the web address, and current customer, article, or order information for each visitor.
- `03-feed-publishing.mmd` — how articles, news, or product updates reach subscribers through RSS, Atom, and JSON Feed.

The diagrams use the same visual language:

- Blue identifies the website, page, or subscriber feed at the center of the story.
- Green identifies the words, images, and business information being published.
- Purple identifies a choice the publisher controls.
- Orange identifies visitors, subscribers, and what they receive.
- Gold identifies a secure connection for a public web address.

## Product takeaways

- Publish several websites from one Daptin installation, with a separate web address and content folder for each website.
- Keep website files in a local folder or cloud drive, then let Daptin maintain the latest copy visitors receive.
- Publish ready-made website files or turn a Hugo website project into finished pages.
- Give a page a memorable address such as `/profiles/alex`, and use `alex` plus the visitor's other choices to personalize what appears.
- Fill each page with the current customer, article, or order details chosen for that address.
- Keep a page design inside Daptin or alongside the rest of the website files.
- Choose whether a public address returns a web page, shared data, or plain text, and set freshness rules that speed up repeat visits.
- Choose which articles, news, or product updates belong in a subscriber feed and how many recent entries it includes.
- Publish the same subscriber feed for RSS readers, Atom readers, and apps that understand JSON Feed.
- Give every enabled website a secure connection matched to its web address.

## Glossary

**Website**  
A named collection of pages and files published at its own web address from its chosen content folder.

**Web address**  
The public domain that opens a website, such as `docs.example.com`.

**Content home**  
The local folder or cloud drive where a website's source files live.

**Website folder**  
The part of a content home that contains one website's pages, design files, and images.

**Published website files**  
The latest synchronized files Daptin delivers to visitors. For a Hugo website, these include the finished pages generated from the project.

**Page design**  
A saved layout that combines headings, text, and presentation with current details before a visitor sees the page.

**Page address**  
A public path such as `/profiles/alex`. Parts of the address can supply details such as the profile name.

**Current business information**  
Customer, article, order, or other saved details selected by a Daptin action to fill a page.

**Update selection**  
The choice of business content and the order in which subscribers receive the entries.

**Subscriber feed**  
A named publication with a title, summary, author, website link, number of recent entries, and chosen reader formats.

**Feed update**  
One article, news item, or product update with a headline, link, summary, author, and date.

**Secure connection**  
The certificate matched to a website's address so visitors can open it over HTTPS.

## Implementation evidence for reviewers

The notes below deliberately retain Daptin's code and database names so reviewers can verify every audience-facing statement. The sibling `daptin` repository is the implementation authority used for these maps.

### Websites and content homes

- `../daptin/server/resource/columns.go:125` defines the site-to-storage relationship.
- `../daptin/server/resource/columns.go:3094-3145` defines storage name, type, provider, root path, credential name, and provider settings.
- `../daptin/server/resource/columns.go:3356-3407` defines site name, hostname, path, enabled state, FTP option, and site type.
- `../daptin/server/resource/columns.go:825-866` defines site creation from a selected storage location, hostname, path, and site type.
- `../daptin/server/actions/action_cloudstore_site_create.go:50-137` resolves the site folder, optionally initializes Hugo content, and creates the site record through the resource path.
- `../daptin/server/subsites.go:54-168` loads sites and storage locations, associates each site with its folder, hostname router, and synchronized serving copy, and schedules recurring storage synchronization.
- `../daptin/server/actions/action_site_sync_storage.go:39-115` synchronizes the configured storage folder into the serving copy and builds Hugo output into `public`.
- `../daptin/server/resource/columns.go:490-504` defines the site storage synchronization action from the site's persisted relationships.
- `../daptin/server/resource/columns.go:967-1037` defines site file listing, retrieval, and deletion by path.
- `../daptin/wiki/Subsites.md:9-16`, `../daptin/wiki/Subsites.md:128-145`, and `../daptin/wiki/Subsites.md:164-199` are the canonical user guide for site capabilities, fields, storage path resolution, and multi-site hostname routing.

### Web addresses and secure connections

- `../daptin/server/resource/columns.go:1999-2063` defines certificate hostname, issuer, generated time, certificate chain, encrypted private key, and public key.
- `../daptin/server/resource/certificate_manager.go:142-171` loads enabled sites and resolves their TLS configuration by hostname.
- `../daptin/wiki/Certificate-Actions.md:12-24` documents the certificate record, and `../daptin/wiki/Certificate-Actions.md:177-198` describes its HTTPS use.

### Pages filled for each visitor

- `../daptin/server/resource/columns.go:2296-2367` defines template name, content, action configuration, cache configuration, response type, headers, and URL patterns.
- `../daptin/server/subsite/template_handler.go:96-124` registers every stored URL pattern on the site routers.
- `../daptin/server/subsite/template_handler.go:175-243` supplies route/query values, invokes the configured action, and renders the template response.
- `../daptin/server/actions/action_render_template.go:38-159` loads template content, resolves `site://` and `subsite://` file references, renders supplied values, and returns content with its response type and headers.
- `../daptin/server/subsite/template_handler.go:150-173` and `../daptin/server/subsite/template_handler.go:245-329` apply the template's cache policy, compression, validators, response type, and headers.
- `../daptin/server/subsite/template_handler_test.go:31-94` verifies that routed template headers, validators, and cached representations are preserved.
- `../daptin/wiki/Template-Rendering.md:1-34`, `../daptin/wiki/Template-Rendering.md:97-117`, and `../daptin/wiki/Template-Rendering.md:328-343` are the canonical guide for the two template uses, site-file content sources, and routed responses.

### Subscriber updates

- `../daptin/server/resource/columns.go:100` defines each feed as belonging to a stream.
- `../daptin/server/resource/columns.go:2066-2170` defines feed identity, author, enabled state, RSS/Atom/JSON choices, and item limit.
- `../daptin/server/resource/columns.go:2535-2563` defines stream name, enabled state, and stream contract.
- `../daptin/server/feed_handler.go:95-119` connects stored feeds to their stored streams.
- `../daptin/server/feed_handler.go:158-225` selects the stream, applies the feed's item limit, and shapes stream records into feed items.
- `../daptin/server/feed_handler.go:228-245` renders the same feed as RSS, Atom, or JSON Feed.
- `../daptin/server/feed_handler_test.go:8-50` verifies persisted feed settings and the required shape of stream items.

## Placement ideas for later review

- Use the website map where the site explains multi-site hosting, web addresses, or cloud-backed website files.
- Use the personalized-page map where the site explains custom page addresses, page designs, or pages filled with current business information.
- Use the subscriber-feed map where the site explains feeds, publishing, or sharing updates beyond the website.
- An overview page could place the three maps side by side as “websites,” “pages for each visitor,” and “subscriber updates.”
