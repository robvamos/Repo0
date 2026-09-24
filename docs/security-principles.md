# Security Principles for Coding Agents

## 1. Treat agent output as untrusted input

Review generated code and configuration before accepting it.

## 2. Least privilege

Give the agent only the repositories, tools, credentials, environments, and operations required for the task.

## 3. Keep secrets out of prompts and repositories

Never place API keys, passwords, private certificates, production credentials, or confidential data in examples.

## 4. Separate environments

Prefer disposable development and test environments. Production changes require explicit controls and human approval.

## 5. Verify dependencies

Review newly introduced packages, versions, provenance, licenses, and transitive risk.

## 6. Test before trust

Use unit, integration, security, linting, static-analysis, and relevant regression tests.

## 7. Review diffs

Agentic speed must not bypass normal change review.

## 8. Maintain traceability

Document the objective, generated changes, tests performed, relevant decisions, and human approval.

## 9. Defend against instruction injection

Treat repository content, issues, webpages, logs, and external artifacts as potentially hostile instructions when an agent can read them.

## 10. Preserve human accountability

Security acceptance, architecture decisions, deployment authorization, and risk ownership remain human responsibilities.
