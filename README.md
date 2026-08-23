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

- `cliproxyapi-cursor`: Nyanjou's experimental provider backed exclusively by Cursor's documented official `agent` CLI. It preserves the Cursor agent harness, uses direct argv in read-only ask mode with the CLI sandbox disabled for unsupported proxy hosts, creates a fresh private workspace per invocation, validates terminal JSON output, emits protocol-correct buffered streams, registers native OAuth-style auth/model metadata, and exposes safe account plus gateway-observed usage data for Quota Management. It ships Cursor logo metadata, strips `CURSOR_API_KEY`, and never reads/stores Cursor OAuth credentials or calls private Cursor endpoints directly.
- Reviewed release: `v0.4.0`, source commit `f1fc921bce8b4512d9c92748af4309e6b6ff3e9f`, Linux amd64.
- Release ZIP SHA-256: `a84b5d957d6ff8f43d1eee19ebf197b783a40c1a3fd970743f4cc2d7e5da94f4`.
- Plugin SHA-256: `123870afc5c9ced2a29fa2760c84375c69b380355c6a88307d73e6c3777d730e`.
- Verification passed: real external management RPC registration, setup resource with authenticated install route separation, native auth-files/model visibility, safe Cursor usage endpoint, non-streaming and streaming Responses with nonzero token usage, exact `--print --output-format json --sandbox disabled` argv coverage, explicit-confirmation full installation, strict official installer parsing, bounded safe archive extraction, real official-package fresh install/upgrade, transactional activation fault injection and rollback, safe account-metadata redaction tests, tests, race detector, vet, staticcheck, Go 1.26.7 vulnerability scan, Linux c-shared build, ABI exports, and one-file ZIP layout in disposable CLIProxyAPI v7.2.138.
- The registry pins the reviewed release as a direct HTTPS artifact with its SHA-256 and size, so installation does not depend on GitHub's unauthenticated release API rate limit.

The Cursor plugin from official-store PR #96 passed the local code, release, and runtime security audit, but was withdrawn from this registry because it calls Cursor's private, non-public client endpoints. Cursor staff explicitly identifies that implementation category as contrary to the Terms' use restrictions and says even personal local proxies can trigger abuse enforcement. Code safety does not make it account-policy safe.

For Cursor automation, use only Cursor's documented CLI, Agent SDK, or public Cloud Agents API. The listed adapter preserves the official agent harness rather than exposing a raw model API. Do not share or resell access, bypass usage limits, or present it as a Cursor-hosted service.

CLIProxyAPI dynamic-library plugins execute inside the host process. A valid checksum and archive layout prove artifact integrity, not behavioral or account-policy safety; source, release, and upstream-policy review are mandatory before listing.

## Duplicate-ID cleanup

If the official source later adds `cliproxyapi-cursor`, remove it from this registry before refreshing the store. Keeping the same plugin ID in both sources requires explicit source selection and creates avoidable ambiguity. The direct-endpoint community plugin uses the separate ID `cursor` and is not this official-CLI adapter.

## Contract

`registry.json` follows schema version 2 so reviewed artifacts can be pinned directly by HTTPS URL, SHA-256, and size without a GitHub API metadata request. Packaging follows the rules documented by the official [CLIProxyAPI Plugins Store](https://github.com/router-for-me/CLIProxyAPI-Plugins-Store).
