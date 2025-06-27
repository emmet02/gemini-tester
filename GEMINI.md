# Agent Operating Guidelines

## Core Mandates
- **Conventions:** Adhere to existing project conventions. Analyze surrounding code, tests, and configuration.
- **Libraries/Frameworks:** NEVER assume a library/framework is available. Verify its established usage within the project.
- **Style & Structure:** Mimic the style, structure, framework choices, typing, and architectural patterns of existing code.
- **Idiomatic Changes:** Understand the local context to ensure changes integrate naturally and idiomatically.
- **Comments:** Add comments sparingly. Focus on *why* something is done. Do not edit comments separate from code. NEVER talk to the user or describe changes through comments.
- **Proactiveness:** Fulfill the user's request thoroughly, including reasonable, directly implied follow-up actions.
- **Confirm Ambiguity/Expansion:** Do not take significant actions beyond the clear scope of the request without confirming.
- **Explaining Changes:** After completing a code modification, do not provide summaries unless asked.
- **Do Not revert changes:** Do not revert changes unless asked.

## Tool Usage
- **File Paths:** Always use absolute paths.
- **Parallelism:** Execute multiple independent tool calls in parallel when feasible.
- **Command Execution:** Use `run_shell_command`.
- **Background Processes:** Use background processes (via `&`) for commands that are unlikely to stop on their own.
- **Interactive Commands:** Avoid interactive shell commands.
- **Remembering Facts:** Use `save_memory` for user-specific facts or preferences.
- **Respect User Confirmations:** Respect user cancellations of tool calls.

## Security and Safety Rules
- **Explain Critical Commands:** Before executing commands with `run_shell_command` that modify the file system, codebase, or system state, provide a brief explanation of the command's purpose and potential impact.
- **Security First:** Never introduce code that exposes, logs, or commits secrets, API keys, or other sensitive information.

## Git Repository
- Always start by gathering information using `git status`, `git diff HEAD`, and `git log -n 3`.
- Always propose a draft commit message.
- After each commit, confirm success with `git status`.
- Never push changes to a remote repository without being asked explicitly.
- When creating a Pull Request, ensure `CHANGELOG.md` is updated with relevant changes.

## Python Specifics
- **uv:** Always use non-legacy `uv` commands like `uv sync` and `uv run`. Avoid `uv pip install` and direct `pip` calls.
- **Code Analysis:** Use `ruff check .`, `pyright`, and `pytest` for verification.
