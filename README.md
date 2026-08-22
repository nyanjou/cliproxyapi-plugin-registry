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

No plugins are currently published.

The Cursor plugin from official-store PR #96 passed the local code, release, and runtime security audit, but was withdrawn from this registry because it calls Cursor's private, non-public client endpoints. Cursor staff explicitly identifies that implementation category as contrary to the Terms' use restrictions and says even personal local proxies can trigger abuse enforcement. Code safety does not make it account-policy safe.

For Cursor automation, use only Cursor's documented CLI, Agent SDK, or public Cloud Agents API. A future Cursor adapter listed here must preserve the official agent harness and must not reverse-engineer or call private endpoints directly.

CLIProxyAPI dynamic-library plugins execute inside the host process. A valid checksum and archive layout prove artifact integrity, not behavioral or account-policy safety; source, release, and upstream-policy review are mandatory before listing.

## Duplicate-ID cleanup

If the official source later adds `cursor`, remove it from this registry before refreshing the store. Keeping the same plugin ID in both sources requires explicit source selection and creates avoidable ambiguity.

## Contract

`registry.json` follows schema version 1 and the packaging/release rules documented by the official [CLIProxyAPI Plugins Store](https://github.com/router-for-me/CLIProxyAPI-Plugins-Store).
