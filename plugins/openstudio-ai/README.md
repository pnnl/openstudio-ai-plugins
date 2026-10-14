# OpenStudio AI

OpenStudio AI is a Codex plugin package for building-energy modeling workflows using OpenStudio, MCP tools, reusable skills, and reviewed knowledge.

## What It Includes

- `.mcp.json`: registers the `openstudio_ai` MCP server.
- `skills/`: Codex-native workflows for orchestration, setup, model editing, simulation, results, learning capture, and HVAC workflows.
- `skills/*/references/`: reviewed SDK context packs, prompt contracts, blackboard schemas, and learning schemas used by the owning skills.
- `skills/setup-openstudio-ai/scripts/`: marketplace runtime setup helpers.

## Skills

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
- `openstudio-modeling-orchestrator`
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

Bundled SDK commands share the installed plugin's `sdk/` library. Keep the complete plugin together, including `sdk/` and `skills/`; a skill folder alone is not an installable SDK bundle. Run the owning skill's `scripts/doctor.py` with host Python before local SDK modeling. A `plugin_incomplete` result requires restoring the complete plugin from its repository, not installing another Python library. This layout adds no setup dependency or runtime service. Export size evidence is in `sdk/PACKAGING.json`.
Unexpected execution failures route to `report-openstudio-failure`, which automatically submits allowlisted sanitized diagnostics to https://github.com/pnnl/openstudio-ai-harness using existing GitHub CLI authentication. Issues are created under your own authenticated GitHub account. Models, companions and transcripts are excluded. Missing authentication/network retains local drafts. Run its independent `scripts/report_failure.py doctor` for optional reporting readiness and `policy disabled` to disable submission for this project. Reporting never gates modeling, and installation sends no incidents.
