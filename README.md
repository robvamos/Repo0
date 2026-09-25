# Codex for Secure Enterprise Engineering

Public portfolio by [Roberto Sica](https://github.com/robvamos) for practical, security-conscious use of OpenAI Codex in software engineering, cybersecurity, and regulated environments.

> This is an independent personal project. It does not claim membership in the OpenAI Codex Ambassadors program and does not represent or imply endorsement by OpenAI, Intesa Sanpaolo, or any other employer.

## Mission

Turn hands-on Codex experience into reproducible learning material that helps developers and security practitioners move from a bounded requirement to a reviewed, tested, and traceable change.

The distinctive focus is the intersection of coding agents with cybersecurity, digital assets, distributed-ledger technologies, and the Digital Euro. Employer and customer information is never used: examples are public, synthetic, or intentionally created for education.

## Start here

- [Ambassador candidacy communication](CANDIDACY_COMMUNICATION.md)
- [Application working draft](AMBASSADOR_APPLICATION.md)
- [Professional positioning](docs/profile.md)
- [Security principles for coding agents](docs/security-principles.md)
- [Threat model and safe demonstration policy](docs/threat-model.md)
- [Secure Coding with Codex workshop](workshops/secure-coding-with-codex.md)
- [Demo 01: secure file access](examples/secure-file-access/README.md)
- [Public evidence index](docs/evidence.md)
- [Roadmap](ROADMAP.md)

## What is available now

| Asset | Audience | Status | Verification |
|---|---|---|---|
| Security principles | Developers and security practitioners | Published | Editorial review |
| Secure file access demo | Developers, DevSecOps, students | Reproducible | `python -m unittest discover -s examples/secure-file-access/tests -v` |
| Secure Coding with Codex workshop | Facilitators and technical communities | Facilitator-ready draft | Timed agenda and exercises included |
| Ambassador application material | Codex Community Team | Working draft | Claims checklist included |

## Learning path

1. Read the [security principles](docs/security-principles.md).
2. Run the [secure file access demo](examples/secure-file-access/README.md).
3. Use the [workshop](workshops/secure-coding-with-codex.md) for a 90–120 minute community session.
4. Share corrections or reproducible improvements through an issue or pull request.

## Working principles

- **Human accountability:** people retain responsibility for architecture, security decisions, review, and deployment.
- **Least privilege:** tools, repositories, credentials, and network access are scoped to the task.
- **Untrusted inputs:** generated code and external instructions are reviewed before use.
- **Verification:** tests and deterministic tools support, rather than replace, expert judgment.
- **Traceability:** objectives, changes, evidence, limitations, and approval remain inspectable.
- **Safe disclosure:** public and synthetic material only.

## Project requirements

The portfolio and its first demo require only Git and Python 3.10 or newer. No Codex plugin, cloud account, credential, or employer system is required. See [project-manifest.json](project-manifest.json) for the portable inventory and [docs/workstation-setup.md](docs/workstation-setup.md) for validation. GitHub Actions checks the manifest, local links, and demonstration tests on every push and pull request.

## Current program status

OpenAI currently lists Codex Ambassador applications as paused while it supports the current cohort. This repository continues building public evidence for a future application. See the [official program page](https://developers.openai.com/community/codex-ambassadors).

## License and contributions

Educational content and demo code are available under the [MIT License](LICENSE). Contributions must follow [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).
