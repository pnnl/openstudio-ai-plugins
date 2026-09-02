---
name: setup-openstudio-ai
description: Check and prepare the OpenStudio AI runtime for energy modeling.
---

# Setup OpenStudio AI

Help the user get OpenStudio AI ready without assuming programming experience.

1. Explain that OpenStudio AI needs a local runtime command named `openstudio-ai-mcp` so the AI assistant can safely run OpenStudio tools. Also explain that setup includes adding or updating the OpenStudio AI marked block in the current project's `AGENTS.md`; it preserves all unrelated project instructions.
2. Check whether Python is available using `python --version`. If that fails, try `python3 --version`.
3. Check whether `openstudio-ai-mcp` is available by running `openstudio-ai-mcp --help`.
4. Run the script beside this skill at `scripts/doctor_runtime.py` with `python`; if `python` is unavailable, try `python3`.
5. Treat `core_ready: true` from the doctor as the only successful core setup result. If OpenStudio is missing, perform read-only platform discovery, show the candidate executable to the user, and after approval run `openstudio-ai configure-openstudio --path <confirmed-executable>`. Then restart Codex and rerun doctor. Do not edit a versioned plugin cache file.
6. Review the doctor's optional `nlr_openstudio` capability. NLR OpenStudio-MCP is optional: a missing Docker installation or unconfigured NLR must not block core readiness. If Docker is available and the user wants NLR, offer its Docker Quick Start without installing it automatically: https://pnnl.github.io/openstudio-ai-plugins/#quick-start. Explain that Docker Desktop must be installed and running, then the user follows that page to configure the MCP server as `nlr_openstudio` and restarts Codex.
7. If the runtime is missing, explain the issue in normal energy-modeler language and ask before running `scripts/install_runtime.py` with the same Python command.
8. If installation succeeds but `openstudio-ai-mcp` is still missing, diagnose command discovery before editing plugin files. Run `python -c "import sys, sysconfig; print(sys.executable); print(sysconfig.get_path('scripts'))"` (or `python3`), then check whether that scripts directory is on the PATH used to launch Codex. For a marketplace plugin, keep `.mcp.json` set to the portable command `openstudio-ai-mcp`; do not replace it with an absolute `.venv/bin` path. After the user approves a PATH update, restart Codex from that environment.
9. If this is intentionally a repository checkout with a project virtual environment, explain that it is local development: re-export with `--runtime-mode local` instead of modifying a marketplace export.
10. When `openstudio-ai` is available, run `openstudio-ai doctor`.
11. If installation changed runtime command availability, tell the user to restart Codex or reconnect the failed MCP server so Codex starts `openstudio-ai-mcp` again.
12. Complete project routing as a required part of setup. Preview the managed project guidance with `openstudio-ai install codex --target-dir . --dry-run --force`, then run `openstudio-ai install codex --target-dir . --force`. This creates `AGENTS.md` when absent, updates only the OpenStudio AI marked block when it already exists, or appends that block to an unmanaged file without replacing existing instructions. Do not present this as a separate optional setup process.
13. Summarize core readiness separately from optional capabilities, then report model loading, HVAC workflow support, simulation, results, SDK lookup, workflow state tracking, and project routing.
