"""Tests for GeminiIntegration."""

import pytest

from .test_integration_base_toml import TomlIntegrationTests


class TestGeminiIntegration(TomlIntegrationTests):
    KEY = "gemini"
    FOLDER = ".gemini/"
    COMMANDS_SUBDIR = "commands"
    REGISTRAR_DIR = ".gemini/commands"
    CONTEXT_FILE = "GEMINI.md"


class TestGeminiAutopilot:
    """Tests for GeminiIntegration.build_exec_args / --yolo behaviour."""

    def test_yolo_included_by_default(self, monkeypatch):
        monkeypatch.delenv("SPECKIT_GEMINI_ALLOW_ALL_TOOLS", raising=False)
        from specify_cli.integrations.gemini import GeminiIntegration

        impl = GeminiIntegration()
        args = impl.build_exec_args("do stuff")
        assert "--yolo" in args

    def test_yolo_disabled_by_env_var(self, monkeypatch):
        monkeypatch.setenv("SPECKIT_GEMINI_ALLOW_ALL_TOOLS", "0")
        from specify_cli.integrations.gemini import GeminiIntegration

        impl = GeminiIntegration()
        args = impl.build_exec_args("do stuff")
        assert "--yolo" not in args

    def test_yolo_enabled_when_env_var_is_nonzero(self, monkeypatch):
        monkeypatch.setenv("SPECKIT_GEMINI_ALLOW_ALL_TOOLS", "1")
        from specify_cli.integrations.gemini import GeminiIntegration

        impl = GeminiIntegration()
        args = impl.build_exec_args("do stuff")
        assert "--yolo" in args

    def test_model_flag_included_when_provided(self, monkeypatch):
        monkeypatch.delenv("SPECKIT_GEMINI_ALLOW_ALL_TOOLS", raising=False)
        from specify_cli.integrations.gemini import GeminiIntegration

        impl = GeminiIntegration()
        args = impl.build_exec_args("do stuff", model="gemini-2.5-pro")
        assert "-m" in args
        assert "gemini-2.5-pro" in args

    def test_model_flag_omitted_when_not_provided(self, monkeypatch):
        monkeypatch.delenv("SPECKIT_GEMINI_ALLOW_ALL_TOOLS", raising=False)
        from specify_cli.integrations.gemini import GeminiIntegration

        impl = GeminiIntegration()
        args = impl.build_exec_args("do stuff", model=None)
        assert "-m" not in args

    def test_basic_structure(self, monkeypatch):
        monkeypatch.delenv("SPECKIT_GEMINI_ALLOW_ALL_TOOLS", raising=False)
        from specify_cli.integrations.gemini import GeminiIntegration

        impl = GeminiIntegration()
        args = impl.build_exec_args("hello")
        assert args[0] == "gemini"
        assert "-p" in args
        assert "hello" in args
        assert args is not None
