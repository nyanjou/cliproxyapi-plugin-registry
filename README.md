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

- `cliproxyapi-cursor`: Nyanjou's experimental provider backed exclusively by Cursor's documented official `agent` CLI. It preserves the Cursor agent harness, uses direct argv in read-only ask mode with the CLI sandbox disabled for unsupported proxy hosts, creates a fresh private workspace per invocation, exposes a management-authenticated Cursor account/quota page, strips `CURSOR_API_KEY`, and never reads/stores Cursor OAuth credentials or calls private Cursor endpoints directly.
- Reviewed release: `v0.2.1`, source commit `6013518828798289992286b2cf74eb5468d75cdd`, Linux amd64.
- Release ZIP SHA-256: `a9b9f39897e7d8a6795ba25176aa04b647dfc86c4283220bcafe7986955b5d3a`.
- Plugin SHA-256: `a67d3cd1ef2856ad9bf8a5b47072eb3a984a9e10496f063bf8687de95717d634`.
- Verification passed: real external management RPC registration, setup and quota resources with authenticated route separation, explicit-confirmation full installation, strict official installer parsing, bounded safe archive extraction, real official-package fresh install/upgrade, transactional activation fault injection and rollback, sandbox-disabled argv coverage, quota-field redaction tests, tests, race detector, vet, staticcheck, Go 1.26.7 vulnerability scan, Linux c-shared build, ABI exports, and one-file ZIP layout in disposable CLIProxyAPI v7.2.138.
- The registry pins the reviewed release as a direct HTTPS artifact with its SHA-256 and size, so installation does not depend on GitHub's unauthenticated release API rate limit.

The Cursor plugin from official-store PR #96 passed the local code, release, and runtime security audit, but was withdrawn from this registry because it calls Cursor's private, non-public client endpoints. Cursor staff explicitly identifies that implementation category as contrary to the Terms' use restrictions and says even personal local proxies can trigger abuse enforcement. Code safety does not make it account-policy safe.

For Cursor automation, use only Cursor's documented CLI, Agent SDK, or public Cloud Agents API. The listed adapter preserves the official agent harness rather than exposing a raw model API. Do not share or resell access, bypass usage limits, or present it as a Cursor-hosted service.

CLIProxyAPI dynamic-library plugins execute inside the host process. A valid checksum and archive layout prove artifact integrity, not behavioral or account-policy safety; source, release, and upstream-policy review are mandatory before listing.

## Duplicate-ID cleanup

If the official source later adds `cliproxyapi-cursor`, remove it from this registry before refreshing the store. Keeping the same plugin ID in both sources requires explicit source selection and creates avoidable ambiguity. The direct-endpoint community plugin uses the separate ID `cursor` and is not this official-CLI adapter.

## Contract

`registry.json` follows schema version 2 so reviewed artifacts can be pinned directly by HTTPS URL, SHA-256, and size without a GitHub API metadata request. Packaging follows the rules documented by the official [CLIProxyAPI Plugins Store](https://github.com/router-for-me/CLIProxyAPI-Plugins-Store).
