# Python Project Skeleton

This is a basic Python project skeleton set up with `uv` for dependency management, `ruff` for linting and formatting, `pyright` for type checking, and `pytest` for unit testing.

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

<!-- Trivial commit to enable PR creation -->