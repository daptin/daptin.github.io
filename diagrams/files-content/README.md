# Files, content, and storage domain maps

These diagrams explain how Daptin connects product records, files, storage, publishing, feeds, calendars, and contacts. They are intended for product owners and other non-technical readers, so they name the durable concepts and customer-visible results rather than handlers, transactions, caches, or storage libraries.

## Audience takeaways

- A file field belongs to an ordinary product record and can hold one or more named files.
- Daptin keeps file details with the record while the file content can live in the database, local storage, or a configured cloud storage location.
- The same file relationship supports direct uploads, provider uploads, multipart uploads for large S3 objects, downloads, media seeking, and requested image variants.
- A site combines a hostname, a folder in storage, synchronization, and Daptin permissions to publish files and optionally manage them through FTP or FTPS.
- A feed combines readable source records, a content stream, feed identity, and any enabled RSS, Atom, and JSON Feed formats.
- CalDAV calendars and CardDAV address books are owned by Daptin accounts and persist as ordinary Daptin collections and records.

## Diagram candidates

1. [`01-files-and-storage.mmd`](01-files-and-storage.mmd) — the durable relationship between a product record, its file field, file metadata, file content, and reusable storage destinations.
2. [`02-file-journey.mmd`](02-file-journey.mmd) — how ordinary, provider, and multipart uploads become record attachments that can be downloaded, streamed in ranges, or transformed as images.
3. [`03-sites-and-file-access.mmd`](03-sites-and-file-access.mmd) — how a site relates its hostname and storage folder to website delivery and permission-aware FTP/FTPS access.
4. [`04-feeds-and-personal-collections.mmd`](04-feeds-and-personal-collections.mmd) — two compact content domains: publishing records as feeds, and synchronizing personal calendars and address books through standard protocols.

The diagrams share a visual vocabulary:

- Blue: a product, account, application, or audience entering the domain.
- Purple: durable records and content managed by Daptin.
- Amber: configuration, decisions, and permissions.
- Green: content delivered through a customer-facing surface.
- Gray: storage destinations and file content outside the product record.

## Plain-language glossary

| Term | Meaning |
|---|---|
| Product record | Any ordinary Daptin resource, such as a product, article, profile, or order. |
| File field | A named field on a resource that accepts one or more files. Daptin calls this an asset column in the implementation. |
| Attached file | A named file listed on a product record, together with details such as media type, size, path, and upload state. |
| File content | The actual bytes of an image, document, audio file, video, or other binary object. |
| Storage location | A reusable `cloud_store` record that names a provider, root path, optional credential, and provider settings. It can describe local as well as remote storage. |
| Inline storage | File content encoded in the record's database field. |
| Provider upload | An upload sent directly to its configured storage destination with provider-specific upload details supplied by Daptin. |
| Multipart upload | A large S3 file divided into parts, then finalized as one stored object before its record attachment is marked complete. |
| Image variant | An image produced on request by applying operations such as resize, crop, rotation, color adjustment, or format conversion. |
| Byte-range delivery | Delivery of a requested segment of an audio or video file so a player can seek without fetching the entire file first. |
| Site | A named publishing record that connects a hostname and folder path to one storage location. |
| Site synchronization | The scheduled refresh that copies a site's configured storage folder into Daptin's serving area. |
| Content stream | A configured selection and shape of readable Daptin records used as feed items. |
| Feed | Publishing metadata plus a related content stream, with independently enabled RSS, Atom, and JSON Feed outputs. |
| Calendar collection | An account-owned group of calendar events exposed through CalDAV. |
| Address book | An account-owned group of contacts exposed through CardDAV. |

## Evidence in the Daptin codebase

All paths below are relative to the sibling `daptin` repository. The implementation and its tests are treated as authority; wiki pages are included where they describe the same current relationship in user-facing terms.

### Files, file fields, and storage locations

- `server/resource/binary_column.go:17-88` distinguishes inline binary values from file-list values backed by a `cloud_store`, keeps file content separate from its metadata, and reads the configured content back through the same field.
- `server/asset_upload_handler.go:77-188` validates that an upload targets a cloud-storage file field, writes the object, and attaches its name, size, and media type to the selected record.
- `server/resource/dbresource.go:1011-1265` stores one or more file entries on a resource field and manages completed, pending, and removed attachments; `server/resource/dbmethods.go:3521-3578` resolves their metadata and optionally includes stored content when records are read.
- `server/resource/columns.go:3094-3143` defines a reusable storage location with a name, type, provider, root path, optional credential name, and provider parameters.
- `server/rootpojo/cloud_store.go:11-18` resolves a storage name beneath the configured local or remote root.
- `server/asset_column_sync.go:17-98` connects schema-level file fields to named storage locations and schedules cached remote fields for synchronization.
- `server/resource/binary_column_test.go:13-84` verifies both inline binary content and cloud-storage file values.
- `asset_upload_real_e2e_test.go:1-260` exercises a real resource record, its file field, upload, metadata, and download together.
- `wiki/Asset-Columns.md:5-26` documents inline file fields and file field types; `wiki/Asset-Columns.md:96-188` documents the file-field-to-storage relationship and file metadata.
- `wiki/Cloud-Storage.md:1-120` documents storage records, credentials, providers, paths, and file-field selection.

### Upload choices, delivery, and image variants

- `server/asset_upload_handler.go:211-327` selects multipart S3, provider-presigned, or direct streaming uploads and creates a pending file entry when completion is separate.
- `server/asset_upload_handler.go:340-549` completes the stored object, verifies its size, and changes the record's file metadata to completed.
- `server/asset_route_handler.go:142-260` resolves a file listed on an authorized record and selects image processing, media delivery, inline viewing, or download behavior.
- `server/asset_route_handler.go:302-343` delivers audio and video with byte-range support and keeps range responses independent from compressed responses.
- `server/asset_route_handler_test.go:83-183` verifies partial content responses and the interaction between ranges and compression; `server/asset_route_handler_test.go:206-234` covers audio and video media delivery.
- `server/image.go:20-352` implements requested blur, crop, resize, rotation, color, and output-format operations.
- `wiki/Asset-Columns.md:456-573` documents the visitor-facing image transformation URL and examples.

### Sites, synchronization, and FTP/FTPS

- `server/resource/columns.go:125` relates each site to one storage location; `server/resource/columns.go:3356-3401` defines its name, hostname, folder path, enabled state, FTP state, and site type.
- `server/subsites.go:54-155` loads enabled sites and storage locations, maps hostnames, assigns the site's storage folder, and schedules synchronization.
- `server/actions/action_site_sync_storage.go:30-115` refreshes a site's serving directory from its configured storage path and rebuilds Hugo sites when selected.
- `server/subsite_engine.go:13-45` creates the site-specific serving surface over the synchronized site folder; `server/subsites.go:91-93` maps configured hostnames to their sites.
- `server/endpoint_ftp.go:17-64` exposes only FTP-enabled sites and connects each one to its configured storage location.
- `server/ftp_server.go:245-365` applies site permissions while listing sites and reading or writing their files; `server/ftp_server.go:450-553` applies the same storage adapter to upload, inspect, delete, and rename operations.
- `server/ftp_server_test.go:18-132` verifies that accounts see only the sites allowed by site permissions.
- `wiki/Subsites.md:5-20` describes multi-site hostname routing and storage-backed site files; `wiki/FTP-Server.md:1-22` describes permission-aware file operations through FTP/FTPS.

### Feeds

- `server/resource/columns.go:100` relates a feed to a stream; `server/resource/columns.go:2066-2169` defines feed identity, publishing metadata, enabled formats, and page size.
- `server/feed_handler.go:95-245` resolves the related stream, reads its selected records, creates feed items, and renders enabled RSS, Atom, or JSON Feed output.
- `server/feed_handler_test.go:9-56` verifies accepted boolean settings and feed timestamp values.
- `feed_real_e2e_test.go:1-260` exercises source records, their stream, the related feed, permissions, and all three output formats together.
- `wiki/RSS-Atom-Feeds.md:1-95` documents the source-record-to-stream-to-feed relationship and its three subscriber URLs.

### CalDAV calendars and CardDAV address books

- `server/resource/columns.go:131-132` relates calendar events to calendar collections and contacts to address books.
- `server/resource/caldav_backend.go:25-71` maps CalDAV to `collection` and `calendar` resources, CardDAV to `address_book` and `contact` resources, and scopes both to the authenticated Daptin account.
- `server/resource/caldav_backend.go:97-194` reads and changes DAV content through ordinary authorized Daptin resource operations.
- `server/resource/caldav_backend.go:235-260` keeps objects within their owning collection and reads their content through the configured binary field behavior.
- `server/resource/caldav_backend_test.go:1-420` covers account isolation, collection and object operations, reports, content, and conflict-safe updates.
- `wiki/CalDAV-CardDAV.md:1-35` documents account-owned calendars, events, address books, and contacts and their standard client discovery paths.

## Editorial notes

- “File field” is used in visitor-facing labels because it is clearer than the implementation term “asset column.”
- “Storage location” is used for `cloud_store` because the record also represents local storage; the exact resource name remains in the glossary and evidence.
- The files diagram says “one or more named files” rather than introducing a separate file-collection entity. The implementation stores a list of file metadata on the field, while the actual bytes live inline or at the selected storage destination.
- Site synchronization, FTP/FTPS, feeds, CalDAV, and CardDAV remain distinct customer surfaces. Their connection is that each adapts ordinary Daptin records, storage, identity, and permissions rather than creating a separate ownership model.
