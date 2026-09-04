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
- `delegated-nlr-modeling`
- `hvac-sizing-assistant`
- `openstudio-hvac-air-loop-creator`
- `openstudio-hvac-central-cooling-coil-creator`
- `openstudio-hvac-central-heating-coil-creator`
- `openstudio-hvac-outdoor-air-system-creator`
- `openstudio-hvac-schedule-resolver`
- `openstudio-hvac-sizing-system-configurator`
- `openstudio-hvac-supply-fan-creator`
- `openstudio-hvac-system-validator`
- `openstudio-hvac-vav-terminal-creator`
- `openstudio-sdk-model-editor`
- `openstudio-vav-reheat-system-creator`
- `openstudio-workflow-state`
- `propose-measure`
- `query-results`
- `simulate`
- `view-openstudio-geometry`

## Runtime Note

Runtime mode: `marketplace`.

In `local` mode, this plugin references a source checkout. In `installed` and `marketplace` mode, it expects the `openstudio-ai-mcp` command to be available on the user's machine.

## Claude Code Activation

Claude Code does not automatically read arbitrary plugin instruction files. This package uses the supported `settings.json` `agent` key to activate `agents/openstudio-modeler.md` as the main thread. If a host or managed policy ignores plugin settings, the skills and MCP server still load, but natural-language orchestration will depend on the user invoking the OpenStudio skills explicitly.
