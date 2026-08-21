---
name: setup-openstudio-ai
description: Check and prepare the OpenStudio AI runtime for energy modeling.
---

# Setup OpenStudio AI

Help the user get OpenStudio AI ready without assuming programming experience.

1. Explain that OpenStudio AI needs a local runtime command named `openstudio-ai-mcp` so the AI assistant can safely run OpenStudio tools.
2. Check whether Python is available using `python --version`. If that fails, try `python3 --version`.
3. Check whether `openstudio-ai-mcp` is available by running `openstudio-ai-mcp --help`.
4. Run `python ${CLAUDE_SKILL_DIR}/scripts/doctor_runtime.py`. If `python` is unavailable, try `python3 ${CLAUDE_SKILL_DIR}/scripts/doctor_runtime.py`.
5. Review the doctor's `nlr_openstudio` result. NLR OpenStudio-MCP is optional: OpenStudio AI works as it is without NLR, but a user who prefers it can select NLR as the core modeling backend. If NLR is not configured, offer its Docker Quick Start without installing it automatically: https://pnnl.github.io/openstudio-ai-plugins/#quick-start. Explain that Docker Desktop must be installed and running, then the user follows that page to configure the MCP server as `nlr_openstudio` and reloads Claude Code.
6. If the runtime is missing, explain the issue in normal energy-modeler language and ask before running `python ${CLAUDE_SKILL_DIR}/scripts/install_runtime.py`.
7. If installation succeeds but `openstudio-ai-mcp` is still missing, diagnose command discovery before editing plugin files. Run `python -c "import sys, sysconfig; print(sys.executable); print(sysconfig.get_path('scripts'))"` (or `python3`), then check whether that scripts directory is on the PATH used to launch Claude Code. For a marketplace plugin, keep `.mcp.json` set to the portable command `openstudio-ai-mcp`; do not replace it with an absolute `.venv/bin` path. After the user approves a PATH update, restart Claude Code from that environment.
8. If this is intentionally a repository checkout with a project virtual environment, explain that it is local development: re-export with `--runtime-mode local` instead of modifying a marketplace export.
9. When `openstudio-ai` is available, run `openstudio-ai doctor`.
10. If installation changed runtime command availability, tell the user to run `/reload-plugins` or reconnect the failed MCP server so Claude Code starts `openstudio-ai-mcp` again.
11. Summarize readiness for model loading, HVAC workflow support, simulation, results, SDK lookup, and workflow state tracking.
