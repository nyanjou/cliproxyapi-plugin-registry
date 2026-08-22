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

- `cliproxyapi-cursor`: Nyanjou's experimental provider backed exclusively by Cursor's documented official `agent` CLI. It preserves the Cursor agent harness, uses direct argv in read-only ask mode, enables sandboxing, creates a fresh private workspace per invocation, strips `CURSOR_API_KEY`, and never reads/stores Cursor OAuth credentials or calls private Cursor endpoints directly.
- Reviewed release: `v0.2.0`, source commit `e4529f5c8b6ee0a71dc76665633eb5d3ca157983`, Linux amd64.
- Release ZIP SHA-256: `b0147e981af128fa707f2e9c010ce7afea0b338e58d1b4a3c595cc68c9647757`.
- Plugin SHA-256: `395fadf28aced1c85e18b90bc317f3bbac57de80756ae597b3b8b73bb5080ae8`.
- Verification passed: real external management RPC registration, setup resource and authenticated route separation, explicit-confirmation full installation, strict official installer parsing, bounded safe archive extraction, real official-package fresh install/upgrade, transactional activation fault injection and rollback, tests, race detector, vet, staticcheck, Go 1.26.7 vulnerability scan, Linux c-shared build, ABI exports, and one-file ZIP layout in disposable CLIProxyAPI v7.2.138.
- The registry pins the reviewed release as a direct HTTPS artifact with its SHA-256 and size, so installation does not depend on GitHub's unauthenticated release API rate limit.

The Cursor plugin from official-store PR #96 passed the local code, release, and runtime security audit, but was withdrawn from this registry because it calls Cursor's private, non-public client endpoints. Cursor staff explicitly identifies that implementation category as contrary to the Terms' use restrictions and says even personal local proxies can trigger abuse enforcement. Code safety does not make it account-policy safe.

For Cursor automation, use only Cursor's documented CLI, Agent SDK, or public Cloud Agents API. The listed adapter preserves the official agent harness rather than exposing a raw model API. Do not share or resell access, bypass usage limits, or present it as a Cursor-hosted service.

CLIProxyAPI dynamic-library plugins execute inside the host process. A valid checksum and archive layout prove artifact integrity, not behavioral or account-policy safety; source, release, and upstream-policy review are mandatory before listing.

## Duplicate-ID cleanup

If the official source later adds `cliproxyapi-cursor`, remove it from this registry before refreshing the store. Keeping the same plugin ID in both sources requires explicit source selection and creates avoidable ambiguity. The direct-endpoint community plugin uses the separate ID `cursor` and is not this official-CLI adapter.

## Contract

`registry.json` follows schema version 2 so reviewed artifacts can be pinned directly by HTTPS URL, SHA-256, and size without a GitHub API metadata request. Packaging follows the rules documented by the official [CLIProxyAPI Plugins Store](https://github.com/router-for-me/CLIProxyAPI-Plugins-Store).
