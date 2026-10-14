# OpenStudio AI

OpenStudio AI is a Claude plugin package for building-energy modeling workflows using OpenStudio, MCP tools, reusable skills, and a reviewed SDK knowledge base.

## What It Includes

- `.mcp.json`: registers the `openstudio_ai` MCP server.
- `agents/openstudio-modeler.md`: the OpenStudio modeler agent prompt.
- `settings.json`: sets `agent` to `openstudio-modeler`, activating it as the main Claude Code thread while the plugin is enabled.
- `skills/`: Claude-native workflow and model-editing skills.
- `skills/*/references/`: reviewed SDK context packs, schemas, and workflow contracts.
- `monitors/`: passive learning-event notifications for candidate learning workflows.
- `bin/`: monitor helper executables.

## User-Facing Skills

- `/openstudio-ai:add-vav-reheat`: plan and execute a VAV reheat workflow.
- `/openstudio-ai:simulate`: run or prepare an OpenStudio simulation workflow.
- `/openstudio-ai:query-results`: retrieve SQL-backed simulation results.

## Runtime Skills

- `add-vav-reheat`
- `capture-session-lesson`
- `curate-learning`
- `delegated-nlr-modeling`
- `github-issue-submitter`
- `hvac-sizing-assistant`
- `openstudio-cav-system-creator`
- `openstudio-coil-replacer`
- `openstudio-economizer-editor`
- `openstudio-heat-recovery-editor`
- `openstudio-hvac-remover`
- `openstudio-hvac-visualizer`
- `openstudio-outdoor-air-connector`
- `openstudio-plant-loop-creator`
- `openstudio-pump-performance-editor`
- `openstudio-pump-replacer`
- `openstudio-sdk-model-editor`
- `openstudio-supply-fan-performance-editor`
- `openstudio-supply-fan-replacer`
- `openstudio-vav-reheat-system-creator`
- `openstudio-ventilation-editor`
- `openstudio-water-coil-connector`
- `openstudio-water-coil-editor`
- `openstudio-workflow-state`
- `propose-measure`
- `query-results`
- `report-openstudio-failure`
- `simulate`
- `view-openstudio-geometry`

## Runtime Note

Runtime mode: `marketplace`.

In `local` mode, this plugin references a source checkout. In `installed` and `marketplace` mode, it expects the `openstudio-ai-mcp` command to be available on the user's machine.

## Claude Code Activation

Claude Code does not automatically read arbitrary plugin instruction files. This package uses the supported `settings.json` `agent` key to activate `agents/openstudio-modeler.md` as the main thread. If a host or managed policy ignores plugin settings, the skills and MCP server still load, but natural-language orchestration will depend on the user invoking the OpenStudio skills explicitly.

Bundled SDK commands share the installed plugin's `sdk/` library. Keep the complete plugin together, including `sdk/` and `skills/`; a skill folder alone is not an installable SDK bundle. Run the owning skill's `scripts/doctor.py` with host Python before local SDK modeling. A `plugin_incomplete` result requires restoring the complete plugin from its repository, not installing another Python library. This layout adds no setup dependency or runtime service. Export size evidence is in `sdk/PACKAGING.json`.
Unexpected execution failures route to `report-openstudio-failure`, which automatically submits allowlisted sanitized diagnostics to https://github.com/pnnl/openstudio-ai-harness using existing GitHub CLI authentication. Issues are created under your own authenticated GitHub account. Models, companions and transcripts are excluded. Missing authentication/network retains local drafts. Run its independent `scripts/report_failure.py doctor` for optional reporting readiness and `policy disabled` to disable submission for this project. Reporting never gates modeling, and installation sends no incidents.
