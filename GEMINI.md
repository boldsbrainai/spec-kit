# Spec Kit (Specify CLI) - Project Context

## Project Overview

Spec Kit is an open-source toolkit that enables Spec-Driven Development (SDD) using AI coding agents. It flips the traditional software development script by making specifications executable, allowing them to directly generate working implementations. The project provides a CLI tool (`specify`) and a set of templates, scripts, and integrations for various AI coding agents (like GitHub Copilot, Claude Code, Gemini CLI, etc.).

**Key Technologies:**
- **Language:** Python 3.11+
- **Package Manager:** `uv` (recommended) or `pipx`
- **Build System:** Hatchling (`hatchling.build`)
- **CLI Framework:** Typer / Click

**Architecture & Structure:**
- `src/specify_cli/`: Python source code for the `specify` CLI.
- `templates/`: Prompt assets and markdown templates that define the SDD workflow and generated artifacts.
- `scripts/`: Bash and PowerShell scripts supporting the workflow.
- `extensions/` & `presets/`: Capabilities to expand or customize Spec Kit workflows without modifying core tooling.

## Building and Running

**Local Setup and Installation:**

1. Install prerequisites: Python 3.11+, `uv`, and Git.
2. Clone the repository.
3. Install dependencies and the CLI locally:
   ```bash
   uv sync --extra test
   uv pip install -e .
   ```
4. Verify the CLI installation:
   ```bash
   uv run specify --help
   ```

**Testing the SDD Workflow Locally:**

1. Initialize a test project in a temporary directory:
   ```bash
   uv run specify init <temp-dir>/speckit-test --integration <agent>
   ```
2. Open the test project directory in your chosen AI coding agent.
3. Test the built-in SDD slash commands in sequence (e.g., `/speckit.constitution`, `/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, `/speckit.implement`).

**Automated Tests:**

Run unit and consistency tests using pytest:
```bash
uv run python -m pytest tests/test_agent_config_consistency.py -q
# Or run all tests:
uv run python -m pytest tests
```

## Development Conventions

- **Environment:** You can use Dev Containers (`.devcontainer/devcontainer.json`) for an out-of-the-box development setup, particularly if using VSCode or GitHub Codespaces.
- **Workflow:** For CLI features and prompt engineering, the recommended validation flow is to run automated tests first, followed by manual workflow tests through an AI coding agent. Ensure you test any slash command behavior changes directly in the agent.
- **Code Quality:** Write tests for new functionality. If adding large changes (new templates, arguments, etc.), ensure they are discussed and agreed upon with maintainers first.
- **AI Usage:** If AI assistance is used to generate code, documentation, or issue responses, it **must** be clearly disclosed in the pull request. Untested or low-effort AI-generated contributions will be closed.
- **Commits:** Provide clear, descriptive commit messages. Keep changes focused and submit separate PRs for unrelated modifications.
