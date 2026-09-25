from pathlib import Path


class UnsafePathError(ValueError):
    """Raised when a requested file escapes the configured workspace."""


def resolve_workspace_file(workspace: Path, requested_path: str) -> Path:
    if not requested_path or "\x00" in requested_path:
        raise UnsafePathError("A non-empty path without NUL bytes is required")

    root = workspace.resolve(strict=True)
    candidate = (root / requested_path).resolve(strict=True)

    if not candidate.is_relative_to(root):
        raise UnsafePathError("Requested path escapes the workspace")
    if not candidate.is_file():
        raise UnsafePathError("Requested path is not a regular file")

    return candidate


def read_workspace_file(workspace: Path, requested_path: str) -> str:
    return resolve_workspace_file(workspace, requested_path).read_text(encoding="utf-8")
