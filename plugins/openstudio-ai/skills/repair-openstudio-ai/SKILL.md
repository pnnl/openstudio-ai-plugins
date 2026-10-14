---
name: repair-openstudio-ai
description: Guide non-destructive repair of the OpenStudio AI runtime.
---

# Repair OpenStudio AI

First run the doctor command. If the runtime is missing or it reports `plugin_ready: false`, ask for approval before running the setup skill's `scripts/install_runtime.py`, then restart Codex or reconnect the MCP server before retrying. Do not delete user models, simulation outputs, or project files. If the installer found the command beside its Python but Codex cannot find it, follow the setup skill's PATH diagnosis. Do not hard-code a project virtualenv path into a marketplace `.mcp.json`. Describe each repair step in plain language for an energy modeler.

Bundled SDK commands share the installed plugin's `sdk/` library. Keep the complete plugin together, including `sdk/` and `skills/`; a skill folder alone is not an installable SDK bundle. Run the owning skill's `scripts/doctor.py` with host Python before local SDK modeling. A `plugin_incomplete` result requires restoring the complete plugin from its repository, not installing another Python library. This layout adds no setup dependency or runtime service. Export size evidence is in `sdk/PACKAGING.json`.
Unexpected execution failures route to `report-openstudio-failure`, which automatically submits allowlisted sanitized diagnostics to https://github.com/pnnl/openstudio-ai-harness using existing GitHub CLI authentication. Issues are created under your own authenticated GitHub account. Models, companions and transcripts are excluded. Missing authentication/network retains local drafts. Run its independent `scripts/report_failure.py doctor` for optional reporting readiness and `policy disabled` to disable submission for this project. Reporting never gates modeling, and installation sends no incidents.
