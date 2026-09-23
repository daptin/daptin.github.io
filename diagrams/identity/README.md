# Identity domain diagrams

These maps show how people sign in, join teams, share business information,
recover an account, approve an outside service, and connect a trusted app. The
evidence notes below connect those familiar ideas to the implementation.

## Audience takeaway

Daptin keeps one account for each person and remembers which teams they belong
to. Every customer, case, document, order, or other saved item can have an
owner, a shared team, and clear choices for what the owner, team, visitors, and
administrators may do. The same account supports password sign-in, one-time
codes, recovery email, familiar outside accounts, and trusted apps that connect
to Daptin.

## Diagram set

- `01-account-and-groups.mmd` — how one person, their account, their teams,
  their business information, and their approved services stay connected.
- `02-record-access.mmd` — how the owner, a shared team, public visitors, and
  administrators receive clear choices for each saved item.
- `03-account-security.mmd` — everyday sign-in, one-time-code setup, password
  recovery, and the fresh sign-in that follows a password change.
- `04-connected-identity.mmd` — how a person can approve Google, GitHub, or
  another familiar service, and how a trusted app can connect to Daptin.

The `.mmd` files contain Mermaid source only. Each relationship is written as
a short verb phrase so the maps remain useful without technical narration.

## Words used in the maps

| Term | Plain-language meaning |
|---|---|
| Account | One person's name, email, sign-in details, teams, and owned business information in Daptin. |
| Signed-in visit | The period after sign-in when Daptin recognizes the person and their teams on each page. |
| Team | People who share access to the same work. |
| Team membership | The saved connection between a person and a team. |
| Owner | The person responsible for a saved customer, case, document, order, or other item. |
| Shared team | The team invited to work with a saved item. |
| Who can do what | Clear choices for who may find, view, add, change, remove, use, or connect an item. |
| Administrator | A trusted person who can manage every item in the product. |
| One-time code | A short-lived code that confirms account setup or password recovery and works once. |
| Recovery email | A message sent to the account email with the code for changing the password. |
| Familiar service | Google, GitHub, or another outside account service a person already uses. |
| Protected connection | Daptin's saved record of a person's approved connection to another service or app. |
| Trusted app | An app registered with a known name, return address, and allowed account details. |
| One-use handoff | A short-lived return message that only the trusted app can use to finish connecting. |
| Account controls | Ways to share allowed account details, check a connection, and disconnect an app. |

## Source evidence

The diagrams summarize current code paths, schema relationships, tests, and
canonical documentation in the sibling Daptin repository.

### Accounts, memberships, groups, and sessions

- `../daptin/system_schema.json`, decoded `user_account`, `usergroup`, and
  `user_account_user_account_id_has_usergroup_usergroup_id` definitions:
  establishes the durable account, group, and membership entities.
- `../daptin/server/auth/auth.go`, `SessionUser`, `UserGroupSelectQuery`, and
  `AuthCheckMiddlewareWithHttp`: resolves a signed-in account together with
  its persisted group memberships and their relation permissions.
- `../daptin/server/auth/auth_test.go`,
  `TestAuthCheckMiddlewareJWTAuthVersionLifecycle`: proves the signed-in
  account context includes current groups and the account's authentication
  version.
- `../daptin/server/resource/resource_create.go`, record creation and group
  relation creation: assigns the active account as owner and attaches group
  relationships through normal Daptin resources.
- `../daptin/wiki/Users-and-Groups.md`, **User Groups**: documents account to
  group membership as the reusable sharing relationship.

### Ownership and access choices

- `../daptin/server/resource/dbfunctions_check.go`, `CheckRelations`: supplies
  the owner relationship and a `has_many usergroup` relationship to ordinary
  resources.
- `../daptin/server/permission/permission.go`, `PermissionInstance` and its
  `CanPeek`, `CanRead`, `CanCreate`, `CanUpdate`, `CanDelete`, `CanExecute`,
  and `CanRefer` checks: grounds the owner, group, public, and administrator
  audiences and the seven access choices shown in the map.
- `../daptin/server/resource/middleware_objectaccess_permission.go`,
  `ObjectAccessPermissionChecker`: applies each record's owner, related groups,
  and access choices to view, change, and removal operations.
- `../daptin/server/permission/permission_test.go`: exercises owner, signed-in,
  public, group, and administrator decisions.
- `../daptin/wiki/Permissions.md`, **Permission Basics** and **Who Gets
  Checked**: provides the canonical public vocabulary for operations and
  audiences.
- `../daptin/access_groups_real_e2e_test.go`: verifies that a group's table
  access and a record's row access remain connected but distinct decisions.

### Passwords, one-time codes, recovery, and session closure

- `../daptin/server/resource/columns.go`, `user_account` and
  `user_otp_account` definitions plus the `primary_user_otp` relation: grounds
  password protection and the encrypted per-account one-time-code profile.
- `../daptin/server/actions/action_generate_jwt_token.go` and
  `auth_session_token.go`: verify account credentials and issue a signed-in
  session carrying the account authentication version.
- `../daptin/server/actions/action_otp_generate.go`: creates the encrypted
  per-account code profile and generates a fresh short-lived code.
- `../daptin/server/actions/action_otp_login_verify.go`: verifies the account
  owner's code, marks enrollment verified, limits attempts, and prevents code
  replay.
- `../daptin/system_schema.json`, decoded `register_otp`, `send_otp`,
  `verify_otp`, `reset-password`, and `reset-password-verify` actions: links
  account lookup, code generation, recovery mail, code verification, and
  password replacement.
- `../daptin/server/resource/resource_update.go`, password update handling:
  increments `auth_version` and invalidates cached account context when the
  password changes.
- `../daptin/server/resource/auth_lifecycle_test.go`,
  `TestUserAccountPasswordUpdateIncrementsAuthVersion`, together with
  `../daptin/server/auth/auth_test.go`, `TestValidateJWTAuthVersion`: proves a
  password change makes earlier signed-in tokens stale.
- `../daptin/server/actions/auth_session_token_test.go`: verifies enrollment,
  recovery-purpose code handling, replay protection, and session-token output.

### Outside providers and Daptin-issued identity

- `../daptin/server/resource/columns.go`, `oauth_connect`, `oauth_state`,
  `oauth_token`, `oauth_app`, `oauth_code`, `oauth_access`, `oauth_refresh`,
  `oauth_grant`, and `oauth_key`: establishes provider connections, saved
  provider access, registered apps, authorization handoffs, issued tokens,
  grants, and signing keys.
- `../daptin/system_schema.json`, decoded `oauth_login_begin` and
  `oauth.login.response` actions: connects provider configuration, approval,
  token exchange, profile lookup, account lookup or creation, home-group
  membership, and the resulting Daptin sign-in.
- `../daptin/server/actions/action_oauth_client.go` and
  `action_oauth_login_response.go`: implement the outside-provider redirect,
  callback validation, and encrypted token persistence.
- `../daptin/server/endpoint_oauth.go`: exposes OAuth authorization, token,
  revocation, introspection, user-information, discovery, and public-key
  endpoints when Daptin serves as the identity provider.
- `../daptin/server/resource/oauth_provider.go`: validates registered apps,
  callbacks, scopes, PKCE, one-time authorization codes, access and refresh
  tokens, account ownership, expiry, and revocation.
- `../daptin/server/resource/oauth_provider_test.go`: proves code exchange,
  PKCE checks, refresh rotation, token inspection, revocation, and signed ID
  token behavior.
- `../daptin/wiki/Authentication.md`, **OAuth Authentication**, and
  `../daptin/wiki/OAuth-Provider.md`, **OAuth Consumer vs OAuth Provider** and
  **Authorization Code Flow**: document the two customer-facing OAuth roles.

## Implementation notes

- “Session” means Daptin's signed JWT plus the resolved `SessionUser` account
  context; customers experience it as their signed-in state.
- A group is a general sharing audience that a product can use for teams,
  workspaces, departments, tenants, or another business grouping.
- “Access choices” is the reader-facing name for the record permission value;
  the diagram names the allowed work instead of exposing bit positions.
- The password recovery map describes the connected outcome: a verified code
  replaces the account password and invalidates earlier sessions. The delivery
  details remain in the mail domain.
- `oauth_grant` stores explicit grant records. The authorization-code path
  validates the registered app's configured scopes directly, so the diagram
  presents signed-in authorization and scope selection as the active path.
