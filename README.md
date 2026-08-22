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

- `cursor` points to `davidfarah2003/cliproxy-cursor-provider`, currently proposed to the official store in PR #95.
- The plugin speaks an undocumented Cursor backend and is unofficial. Install only for an account and subscription you own or are explicitly authorized to use.
- A CLIProxyAPI dynamic-library plugin executes inside the host process. Verify the release checksum and review the source before installation.

This registry entry is provisional while the competing Cursor submissions are independently audited. It may be switched before installation if the other implementation proves safer.

## Duplicate-ID cleanup

If the official source later adds `cursor`, remove it from this registry before refreshing the store. Keeping the same plugin ID in both sources requires explicit source selection and creates avoidable ambiguity.

## Contract

`registry.json` follows schema version 1 and the packaging/release rules documented by the official [CLIProxyAPI Plugins Store](https://github.com/router-for-me/CLIProxyAPI-Plugins-Store).
