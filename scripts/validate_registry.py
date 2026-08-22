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
REQUIRED = {"id", "name", "description", "author", "repository"}


def main() -> int:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    assert data.get("schema_version") == 1, "schema_version must be 1"
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
    print(f"registry valid: {len(plugins)} plugin(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
