# Public Demo Lab

Each demonstration is public, synthetic, dependency-light, and designed to be reproduced on a local workstation.

## Available

### Demo 01 — Secure file access

Turn a path-traversal requirement into explicit acceptance criteria, a bounded implementation, regression tests, a review guide, and documented residual limitations.

- [Exercise and instructions](secure-file-access/README.md)
- Verification: python -m unittest discover -s examples/secure-file-access/tests -v

## Planned

- **Demo 02 — Legacy modernization:** analyze and refactor a small public legacy component incrementally.
- **Demo 03 — Security review:** compare agent findings against deterministic tooling on intentionally vulnerable code.
- **Demo 04 — Documentation from code:** derive architecture documentation and validate it against the implementation.
- **Demo 05 — Agent guardrails:** demonstrate least privilege, protected files, hostile instructions, and approval gates.

Planned demonstrations are not evidence of completed work. Their status is tracked in [the public evidence register](../docs/evidence.md).
