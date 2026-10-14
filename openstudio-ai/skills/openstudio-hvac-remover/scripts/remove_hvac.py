"""Run this skill's entrypoint from the complete OpenStudio AI plugin."""
import hashlib
import json
from pathlib import Path
import runpy
import sys

try:
    library = Path(__file__).resolve().parents[3] / "sdk"
    bundle = json.loads((library / "bundle.json").read_text(encoding="utf-8"))
    files = bundle["files"]
    identity = hashlib.sha256(json.dumps(files, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    if bundle.get("layout_version") != 1 or identity != '2d428ea860eea573dca03698554db565b42af5ce9deb493dba5f8bea64795cde' or bundle.get("bundle_id") != identity:
        raise ValueError("SDK library does not match this skill launcher")
    for relative, expected in files.items():
        payload = library / relative
        if payload.is_symlink() or not payload.resolve().is_relative_to(library.resolve()) or hashlib.sha256(payload.read_bytes()).hexdigest() != expected:
            raise ValueError("SDK library file is missing or mismatched: " + relative)
except (OSError, ValueError, KeyError, TypeError, IndexError) as exc:
    print(json.dumps({"ok": False, "ready": False, "status": "plugin_incomplete", "error": str(exc)[:400], "next_action": "Restore or reinstall the complete OpenStudio AI plugin, including sdk/; do not copy a skill alone."}))
    raise SystemExit(2)
sys.path.insert(0, str(library))
runpy.run_path(str(library / 'remove_hvac.py'), run_name="__main__")
