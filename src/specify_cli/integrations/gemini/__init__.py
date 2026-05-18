"""Gemini CLI integration."""

from __future__ import annotations

import os

from ..base import TomlIntegration


def _allow_all() -> bool:
    """Return True if the Gemini CLI should run with full permissions (autopilot).

    Checks ``SPECKIT_GEMINI_ALLOW_ALL_TOOLS`` env var.
    When set to ``"0"``, autopilot mode (``--yolo``) is disabled.
    Default when not set: enabled.
    """
    val = os.environ.get("SPECKIT_GEMINI_ALLOW_ALL_TOOLS")
    if val is not None:
        return val != "0"
    return True


class GeminiIntegration(TomlIntegration):
    key = "gemini"
    config = {
        "name": "Gemini CLI",
        "folder": ".gemini/",
        "commands_subdir": "commands",
        "install_url": "https://github.com/google-gemini/gemini-cli",
        "requires_cli": True,
    }
    registrar_config = {
        "dir": ".gemini/commands",
        "format": "toml",
        "args": "{{args}}",
        "extension": ".toml",
    }
    context_file = "GEMINI.md"
    multi_install_safe = True

    def build_exec_args(
        self,
        prompt: str,
        *,
        model: str | None = None,
        output_json: bool = True,
    ) -> list[str] | None:
        # Gemini CLI uses ``gemini -p "prompt"`` for non-interactive mode.
        # --yolo enables autopilot mode (no confirmation prompts).
        # Controlled by SPECKIT_GEMINI_ALLOW_ALL_TOOLS env var (default: enabled).
        args = ["gemini", "-p", prompt]
        if _allow_all():
            args.append("--yolo")
        if model:
            args.extend(["-m", model])
        if output_json:
            args.extend(["--output-format", "json"])
        return args
