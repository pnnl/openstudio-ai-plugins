# Install OpenStudio AI In Claude Code

This export is a Claude Code marketplace containing the OpenStudio AI plugin. Use this exported marketplace folder.

## 1. Validate The Export

From the OpenStudio AI harness repository:

```bash
claude plugin validate <path-to-this-marketplace-folder>
```

## 2. Add The Local Marketplace

Open Claude Code in the target project and run:

```text
/plugin marketplace add <path-to-this-marketplace-folder>
```

## 3. Install The Plugin

Still inside Claude Code, run:

```text
/plugin install openstudio-ai@openstudio-ai-local
```

If Claude Code asks for scope, choose local or project scope for testing.

## 4. Reload Plugins

```text
/reload-plugins
```

## 5. Try The Plugin

Use one of the namespaced skills:

```text
/openstudio-ai:add-vav-reheat
/openstudio-ai:simulate
/openstudio-ai:query-results
```

The plugin also contributes the OpenStudio modeler agent and an `openstudio_ai` MCP server.

## Runtime Setup

After installation, run the setup skill:

```text
/openstudio-ai:setup-openstudio-ai
```

The setup skill checks Python, checks `openstudio-ai-mcp`, and explains any missing installation steps in energy-modeler language.
