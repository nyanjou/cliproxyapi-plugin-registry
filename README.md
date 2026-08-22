# Nyanjou CLIProxyAPI Plugin Registry

A small third-party registry for reviewed CLIProxyAPI plugins that are not yet available from the built-in official source.

## Source URL

Add this URL under `plugins.store-sources` or in the management UI's **Third-party Plugin Sources** field:

```text
https://raw.githubusercontent.com/nyanjou/cliproxyapi-plugin-registry/main/registry.json
```

Equivalent YAML:

```yaml
plugins:
  enabled: true
  store-sources:
    - https://raw.githubusercontent.com/nyanjou/cliproxyapi-plugin-registry/main/registry.json
```

The official source remains enabled automatically.

## Current entry

- `cursor` points to the standalone Cursor plugin in `yobo2u/omsub`, proposed to the official store in PR #96.
- Release `v0.5.8` was reviewed at source tag `b9e3542` with the shipped binary built from source commit `c289664` (the tag's source delta after that commit is release-asset synchronization only).
- Local verification passed unit tests, race tests, vet, Go vulnerability scanning with the release's Go 1.25.13 toolchain, checksum/ZIP/ELF/ABI checks, and an isolated load/smoke test against CLIProxyAPI v7.2.138.
- The unauthenticated browser resource contains only a static management shell. Account/model/usage data and mutations are served through management-authenticated routes; missing management credentials returned HTTP 401 in the isolated host test.

The plugin still speaks Cursor's undocumented backend and is unofficial. It may break when Cursor changes the protocol and could carry account-policy risk. Install only for an account/subscription you own or are explicitly authorized to use, keep auth/config backups, and test before depending on it.

CLIProxyAPI dynamic-library plugins execute inside the host process. A valid checksum and archive layout prove artifact integrity, not behavioral safety; source and release review remain mandatory before listing.

## Duplicate-ID cleanup

If the official source later adds `cursor`, remove it from this registry before refreshing the store. Keeping the same plugin ID in both sources requires explicit source selection and creates avoidable ambiguity.

## Contract

`registry.json` follows schema version 1 and the packaging/release rules documented by the official [CLIProxyAPI Plugins Store](https://github.com/router-for-me/CLIProxyAPI-Plugins-Store).
