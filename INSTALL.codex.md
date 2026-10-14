# Install OpenStudio AI In Codex

This export is a Codex marketplace containing the OpenStudio AI plugin.

## 1. Validate The Plugin

From the OpenStudio AI harness repository:

```bash
python -m json.tool <path-to-this-plugin-json>
```

## 2. Add The Local Marketplace

Use this marketplace file with Codex:

```bash
codex plugin marketplace add <path-to-this-marketplace-folder>
```

## 3. Install Or View The Plugin

Open the Codex plugin UI and install `openstudio-ai` from `openstudio-ai-local`.

## 4. Add The Modeler Policy To A Project

Codex plugins load skills and MCP tools, but they do not activate a plugin agent prompt as the main thread. In each project where plain-language OpenStudio requests should consistently enter the workflow router, install the managed OpenStudio block into `AGENTS.md`:

```bash
openstudio-ai install codex --target-dir <path-to-project>
```

Use `--dry-run` to preview. If the project already has an unmanaged `AGENTS.md`, use `--force` only after reviewing the proposed append. Later runs update only the marked OpenStudio block.

## Runtime Setup

After installation, invoke the setup skill with `$setup-openstudio-ai` (or ask Codex in plain language to set up OpenStudio AI). `/setup-openstudio-ai` is not a Codex CLI skill command. The setup skill checks Python, checks `openstudio-ai-mcp`, and explains any missing installation steps in energy-modeler language.

Bundled SDK commands share the installed plugin's `sdk/` library. Keep the complete plugin together, including `sdk/` and `skills/`; a skill folder alone is not an installable SDK bundle. Run the owning skill's `scripts/doctor.py` with host Python before local SDK modeling. A `plugin_incomplete` result requires restoring the complete plugin from its repository, not installing another Python library. This layout adds no setup dependency or runtime service. Export size evidence is in `sdk/PACKAGING.json`.
Unexpected execution failures route to `report-openstudio-failure`, which automatically submits allowlisted sanitized diagnostics to https://github.com/pnnl/openstudio-ai-harness using existing GitHub CLI authentication. Issues are created under your own authenticated GitHub account. Models, companions and transcripts are excluded. Missing authentication/network retains local drafts. Run its independent `scripts/report_failure.py doctor` for optional reporting readiness and `policy disabled` to disable submission for this project. Reporting never gates modeling, and installation sends no incidents.
