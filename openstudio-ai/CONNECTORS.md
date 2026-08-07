# OpenStudio AI Connectors

This plugin uses one local MCP server.

| Connector | Type | Purpose |
| --- | --- | --- |
| `openstudio_ai` | local stdio MCP | OpenStudio model lifecycle, simulation, results, approved measures, and SDK documentation lookup |

The current `.mcp.json` points to the installed runtime command:

- `openstudio-ai-mcp --transport stdio`

OpenStudio and EnergyPlus availability depends on the local environment.
