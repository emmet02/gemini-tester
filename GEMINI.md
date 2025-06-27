# Python Project Skeleton

## Overview

This document provides an overview of the project, its purpose, and key components. This project is a basic Python skeleton set up with `uv` for dependency management, `ruff` for linting and formatting, `pyright` for type checking, and `pytest` for unit testing.

## Getting Started

### Prerequisites

- Python 3.9+
- `uv` (can be installed via `pip install uv`)

### Installation

1.  **Create a virtual environment and install dependencies (including development tools):**
    ```bash
    uv venv
    .venv/Scripts/activate  # On Windows
    # source .venv/bin/activate  # On Linux/macOS
    uv sync --extra dev
    ```

### Running the Application

To run the main application file:

```bash
.venv/Scripts/activate
python src/main.py
```

### Running Tests and Code Analysis

After activating the virtual environment:

```bash
.venv/Scripts/activate
ruff check .
pyright
pytest
```

## Project Structure

```
.github/             # GitHub Actions workflows
.venv/               # Python virtual environment
src/                 # Main application source code
├── __init__.py
└── main.py
tests/               # Unit tests
├── conftest.py
└── test_main.py
.gitignore           # Specifies intentionally untracked files to ignore
GEMINI.md            # Project overview and documentation
pyproject.toml       # Project configuration and dependencies
README.md            # General project information
uv.lock              # Locked dependency versions for reproducible builds
```

## Key Technologies

- Python
- `uv` (package manager and virtual environment creator)
- `ruff` (linter and formatter)
- `pyright` (type checker)
- `pytest` (testing framework)

## Contributing

Guidelines for contributing to the project.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'feat: Add new feature'`).
5. Push to the branch (`git push origin feature/YourFeature`).
6. Open a Pull Request.

## License

Specify the licensing for the project (e.g., MIT, Apache 2.0).

## Contact

Provide contact information for questions or support.

## Development Environment Notes

### GitHub CLI (gh)

When interacting with GitHub from the command line, the `gh` CLI tool is recommended. For creating pull requests, you can use:

```bash
gh pr create --base <base-branch> --head <head-branch> --title "Your PR Title" --body "Your PR description"
```

If you encounter issues with complex multi-line bodies or special characters, consider writing the body to a file and using the `--body-file` flag:

```bash
gh pr create --base <base-branch> --head <head-branch> --title "Your PR Title" --body-file /path/to/your/pr_body.txt
```

Alternatively, to open a web browser for PR creation (which bypasses command-line parsing issues):

```bash
gh pr create --base <base-branch> --head <head-branch> --web
```

### File-Based Commit Messages and PR Bodies

Due to potential issues with command-line argument parsing, especially on Windows, it is often more reliable to use a file-based approach for longer commit messages or pull request bodies. This involves writing the message/body content to a temporary file and then referencing that file in the Git or GitHub CLI command.

For Git commits:

```bash
# Write message to a temporary file
echo "Your commit message" > /path/to/temp/commit_message.txt
# Commit using the file
git commit -F /path/to/temp/commit_message.txt
```

For GitHub CLI pull requests:

```bash
# Write body to a temporary file
echo "Your PR body" > /path/to/temp/pr_body.txt
# Create PR using the body file
gh pr create --base <base-branch> --head <head-branch> --title "Your PR Title" --body-file /path/to/temp/pr_body.txt
```

Temporary files for this purpose should be stored in the `/temp` directory within the project root, which is already configured to be ignored by Git.

### Windows Environment and Line Endings

This project is developed on a Windows operating system. Be aware that Windows typically uses CRLF (Carriage Return + Line Feed) for line endings, while Linux/macOS use LF (Line Feed). Git is configured to handle these differences, but if you encounter unexpected issues related to line endings (e.g., in shell scripts or when collaborating across different OS environments), ensure your Git configuration (`core.autocrlf`) is set appropriately or use a text editor that can manage line endings consistently.

For shell commands executed within the agent, commands like `del` or `rm` might require specific syntax (e.g., backslashes for paths, proper quoting) due to the Windows command-line interpreter's requirements.