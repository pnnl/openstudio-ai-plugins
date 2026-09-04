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
