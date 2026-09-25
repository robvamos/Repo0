from pathlib import Path


def read_workspace_file(workspace: Path, requested_path: str) -> str:
    """Intentionally vulnerable example: do not use in production."""
    return (workspace / requested_path).read_text(encoding="utf-8")
