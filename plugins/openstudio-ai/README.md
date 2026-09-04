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
- `openstudio-modeling-orchestrator`
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
