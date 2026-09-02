"""Install or repair the OpenStudio AI runtime package for this plugin."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path


DEFAULT_PACKAGE_SPEC = "openstudio-ai"


def run(command: list[str]) -> int:
    print(f"\n$ {' '.join(command)}")
    completed = subprocess.run(command, check=False)
    return completed.returncode


def runtime_command_path(command: str) -> str | None:
    """Find a console script for this interpreter after pip install."""
    path = shutil.which(command)
    if path:
        return path
    scripts_dir = Path(sys.executable).resolve().parent
    candidates = [scripts_dir / command]
    if os.name == "nt":
        candidates.extend(
            [
                scripts_dir / f"{command}.exe",
                scripts_dir / "Scripts" / command,
                scripts_dir / "Scripts" / f"{command}.exe",
            ]
        )
    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)
    return None


def runtime_cli_path() -> str | None:
    """Find the openstudio-ai console script for this interpreter."""
    return runtime_command_path("openstudio-ai")


def main() -> int:
    print("OpenStudio AI runtime installer")
    print("===============================")
    print(f"Python executable: {sys.executable}")
    print(f"Python version: {sys.version.split()[0]}")

    if sys.version_info < (3, 10):
        print(
            "\nOpenStudio AI requires Python 3.10 or newer. Install a supported "
            "Python version, then rerun setup."
        )
        return 2

    package_spec = os.getenv("OPENSTUDIO_AI_PACKAGE_SPEC", DEFAULT_PACKAGE_SPEC)
    if shutil.which("openstudio-ai") and shutil.which("openstudio-ai-mcp"):
        print("\nOpenStudio AI commands are available. Checking for a compatible runtime update.")
    else:
        print("\nOpenStudio AI runtime is not installed yet.")
    print(f"Installing or upgrading runtime package: {package_spec}")
    print(
        "Set OPENSTUDIO_AI_PACKAGE_SPEC to a wheel path, internal index spec, "
        "or pinned version if your organization does not install from PyPI."
    )
    code = run([sys.executable, "-m", "pip", "install", "--upgrade", package_spec])
    if code != 0:
        print(
            "\nRuntime package installation failed. Check Python permissions, "
            "network access, package index access, or ask your support contact "
            "for an approved OpenStudio AI package."
        )
        return code

    runtime_cli = runtime_cli_path()
    if runtime_cli is None:
        print("\nInstalled package, but the openstudio-ai command was not found for this Python environment.")
        return 3
    code = run([runtime_cli, "install-runtime"])
    if code != 0:
        print("\nInstalled package, but runtime initialization failed.")
        return code

    runtime_mcp = runtime_command_path("openstudio-ai-mcp")
    if not shutil.which("openstudio-ai-mcp"):
        print(
            "\nThe package installed, but openstudio-ai-mcp is not on PATH in this shell."
        )
        if runtime_mcp:
            print(f"Installed MCP command: {runtime_mcp}")
            print(
                "Add its parent directory to the PATH used to launch the AI tool, then restart "
                "or reconnect the plugin. Keep marketplace .mcp.json configured with the "
                "portable command `openstudio-ai-mcp`; do not replace it with this absolute path."
            )
        else:
            print(
                "The MCP command was not found beside this Python interpreter. Reinstall the "
                "runtime with this same Python, then rerun doctor."
            )
        return 3

    print("\nOpenStudio AI runtime installation completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
