# Demo 01 — Secure File Access

This dependency-free exercise shows how to turn a broad request such as “prevent path traversal” into a bounded, reviewable Codex task.

The example is intentionally small. It demonstrates an engineering workflow and does not claim that one helper function is a complete production security boundary.

## Scenario

An application reads a user-selected text file from a configured workspace. The implementation in before/file_access.py joins the workspace and user input directly, allowing paths such as ../secret.txt to escape the intended root.

## Acceptance criteria

- Read an existing regular file inside the workspace.
- Reject relative traversal outside the workspace.
- Reject absolute paths outside the workspace.
- Reject empty paths, NUL bytes, and directories.
- Do not add a third-party dependency.
- Preserve a clear error boundary for unsafe input.

## Suggested Codex task

> Review examples/secure-file-access/before/file_access.py as untrusted code. Implement the acceptance criteria in a separate after/ version. Add focused regression tests using only the Python standard library. Do not access files outside a temporary test directory. Explain the security impact and residual limitations.

## Run the verified implementation

From the repository root:

    python -m unittest discover -s examples/secure-file-access/tests -v

The tests use temporary synthetic files and require no network connection, credentials, or external service.

## Review guide

1. Confirm that the trusted workspace is resolved independently from user input.
2. Check that the candidate is resolved before the containment decision.
3. Verify the behavior for absolute paths, traversal, missing files, and directories.
4. Inspect whether the implementation introduced dependencies or unrelated changes.
5. Run the tests and review the diff before accepting the patch.

## Residual limitations

- The example assumes Python 3.9 or newer for Path.is_relative_to; the project supports Python 3.10 or newer.
- Filesystem race conditions may matter when untrusted users can mutate paths concurrently.
- Symbolic-link and platform behavior must be evaluated for the real deployment environment.
- Authorization, file size limits, content validation, logging, and privacy controls remain outside this demonstration.
- Passing these tests does not establish that a larger application is secure.
