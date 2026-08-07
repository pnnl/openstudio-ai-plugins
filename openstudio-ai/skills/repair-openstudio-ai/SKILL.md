---
name: repair-openstudio-ai
description: Guide non-destructive repair of the OpenStudio AI runtime.
---

# Repair OpenStudio AI

First run the doctor skill. If the runtime is missing, ask for approval before running `python ${CLAUDE_SKILL_DIR}/../setup-openstudio-ai/scripts/install_runtime.py`. Do not delete user models, simulation outputs, or project files. If the installer found the command beside its Python but Claude cannot find it, follow the setup skill's PATH diagnosis. Do not hard-code a project virtualenv path into a marketplace `.mcp.json`. Describe each repair step in plain language for an energy modeler.
