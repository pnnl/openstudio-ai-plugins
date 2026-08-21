"""Check whether the OpenStudio AI runtime can be used by this plugin."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys

PLUGIN_VERSION = "0.1.6"
PLUGIN_CONTRACT_VERSION = "2"


def command_status(command: str) -> dict[str, object]:
    path = shutil.which(command)
    return {"command": command, "available": path is not None, "path": path}


def main() -> int:
    report = {
        "python": {
            "executable": sys.executable,
            "version": sys.version.split()[0],
        },
        "openstudio_ai_mcp": command_status("openstudio-ai-mcp"),
        "openstudio_ai": command_status("openstudio-ai"),
    }
    print(json.dumps(report, indent=2))

    if not report["openstudio_ai_mcp"]["available"] or not report["openstudio_ai"]["available"]:
        print(
            "\nOpenStudio AI runtime commands are not fully available. "
            "Ask the user before running install_runtime.py."
        )
        return 2

    doctor = subprocess.run(
        [
            "openstudio-ai",
            "doctor",
            "--json",
            "--plugin-version",
            PLUGIN_VERSION,
            "--plugin-contract-version",
            PLUGIN_CONTRACT_VERSION,
        ],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if doctor.stdout:
        print(doctor.stdout.strip())
    if doctor.returncode != 0:
        print("\nThe OpenStudio AI runtime is not ready for MCP work.")
        if doctor.stderr.strip():
            print(doctor.stderr.strip())
        return doctor.returncode

    try:
        payload = json.loads(doctor.stdout)
    except json.JSONDecodeError:
        print("\nThe runtime doctor returned an unreadable report. Run `openstudio-ai doctor` directly.")
        return 2

    compatibility = payload.get("plugin_compatibility", {})
    if compatibility.get("ok") is False:
        print("\nCompatibility notice: the plugin and runtime use different MCP interface versions.")
        print(compatibility.get("message", "The plugin may use unavailable MCP tools."))
        print("Next step: refresh the plugin or update the OpenStudio AI runtime through pip.")
        print("The MCP server remains connected so existing compatible tools can still be used.")
        return 1

    print("\nOpenStudio AI MCP runtime is ready for this plugin.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
