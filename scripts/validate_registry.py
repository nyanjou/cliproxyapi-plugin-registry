#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry.json"
ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$")
REPO_RE = re.compile(r"^https://github\.com/[^/]+/[^/]+$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
REQUIRED = {"id", "name", "description", "author", "repository"}


def main() -> int:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    assert data.get("schema_version") == 2, "schema_version must be 2"
    plugins = data.get("plugins")
    assert isinstance(plugins, list), "plugins must be a list"
    seen: set[str] = set()
    for index, plugin in enumerate(plugins):
        assert isinstance(plugin, dict), f"plugins[{index}] must be an object"
        missing = REQUIRED - plugin.keys()
        assert not missing, f"plugins[{index}] missing {sorted(missing)}"
        plugin_id = plugin["id"]
        assert isinstance(plugin_id, str) and ID_RE.fullmatch(plugin_id), f"invalid id: {plugin_id!r}"
        assert plugin_id not in seen, f"duplicate id: {plugin_id}"
        seen.add(plugin_id)
        repository = plugin["repository"]
        assert isinstance(repository, str) and REPO_RE.fullmatch(repository), f"invalid repository: {repository!r}"
        parsed = urlparse(repository)
        assert parsed.scheme == "https" and parsed.netloc == "github.com", f"invalid repository host: {repository!r}"
        version = plugin.get("version")
        assert version is None or (isinstance(version, str) and not version.startswith("v")), "legacy version must not start with v"
        install = plugin.get("install")
        if install is not None:
            assert version, f"direct install requires a pinned version: {plugin_id}"
            assert isinstance(install, dict) and install.get("type") == "direct", f"invalid install plan: {plugin_id}"
            artifacts = install.get("artifacts")
            assert isinstance(artifacts, list) and artifacts, f"direct install requires artifacts: {plugin_id}"
            platforms: set[tuple[str, str]] = set()
            for artifact in artifacts:
                assert isinstance(artifact, dict), f"invalid artifact: {plugin_id}"
                goos, goarch = artifact.get("goos"), artifact.get("goarch")
                assert isinstance(goos, str) and isinstance(goarch, str), f"artifact platform missing: {plugin_id}"
                assert (goos, goarch) not in platforms, f"duplicate artifact platform: {plugin_id} {goos}/{goarch}"
                platforms.add((goos, goarch))
                artifact_url = artifact.get("url")
                parsed_artifact = urlparse(artifact_url) if isinstance(artifact_url, str) else None
                assert parsed_artifact and parsed_artifact.scheme == "https" and not parsed_artifact.query and not parsed_artifact.fragment, f"invalid artifact URL: {plugin_id}"
                assert SHA256_RE.fullmatch(str(artifact.get("sha256", ""))), f"invalid artifact SHA-256: {plugin_id}"
                assert isinstance(artifact.get("size"), int) and artifact["size"] > 0, f"invalid artifact size: {plugin_id}"
    print(f"registry valid: {len(plugins)} plugin(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
