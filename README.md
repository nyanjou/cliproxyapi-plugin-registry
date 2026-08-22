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

## Current entries

No plugins are currently published. The provisional Cursor entry from official-store PR #95 was removed after source review found that v0.4.0 renders account email, subscription, billing, spend-limit, and usage data from an unauthenticated CLIProxyAPI resource route. It must not be restored unless that privacy issue is fixed and the replacement release passes a complete review.

CLIProxyAPI dynamic-library plugins execute inside the host process. A valid checksum and archive layout prove artifact integrity, not behavioral safety; source and release review are mandatory before listing.

## Duplicate-ID cleanup

If the official source later adds `cursor`, remove it from this registry before refreshing the store. Keeping the same plugin ID in both sources requires explicit source selection and creates avoidable ambiguity.

## Contract

`registry.json` follows schema version 1 and the packaging/release rules documented by the official [CLIProxyAPI Plugins Store](https://github.com/router-for-me/CLIProxyAPI-Plugins-Store).
