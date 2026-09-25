# Workstation Setup

## Required

- Git 2.40 or newer
- Python 3.10 or newer

No package installation is required for the current demonstration.

## Validate

From the repository root:

```powershell
git --version
python --version
python scripts/validate_portfolio.py
python -m unittest discover -s examples/secure-file-access/tests -v
```

The equivalent test command works in any shell. All tests should pass.

## Portable configuration

This repository currently needs no machine-specific configuration. If future demonstrations require local paths, devices, accounts, or endpoints, they must use an ignored local configuration derived from a versioned example. Credentials and private keys must never be committed.

## Optional tools

Codex is needed to reproduce the agent-assisted workflow itself, but the code and tests remain inspectable and runnable without it. Editors, security scanners, and presentation tools are optional and are not prerequisites for this repository.
