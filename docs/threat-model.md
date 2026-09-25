# Threat Model for Public Codex Demonstrations

## Scope

This model covers public workshops, examples, and repository workflows in this portfolio. It is educational guidance, not a security assessment of OpenAI, an employer, or a production system.

## Assets

- source code and repository integrity;
- credentials and personal information;
- participant workstations and accounts;
- accuracy of security claims;
- traceability of human decisions.

## Main threats and controls

| Threat | Example | Minimum control |
|---|---|---|
| Instruction injection | A README tells an agent to exfiltrate files | Treat repository and web content as untrusted; review tool calls |
| Excessive privilege | An exercise can access unrelated directories | Use a disposable repository and task-scoped permissions |
| Secret exposure | A token appears in a prompt, log, or commit | Use synthetic values; scan diffs; revoke any exposed secret |
| Unsafe generated code | A patch weakens path or input validation | Define abuse cases and run regression tests before acceptance |
| Dependency risk | A generated patch introduces an unnecessary package | Prefer the standard library; review provenance and transitive risk |
| False assurance | Passing tests are presented as proof of security | State test scope, residual risk, and required expert review |
| Sensitive disclosure | A real internal architecture appears in teaching material | Use public or purpose-built examples only |
| Irreversible action | An agent deploys or deletes during a demo | Keep deployment out of scope and require explicit human approval |

## Demonstration boundary

Exercises must run locally against intentionally created material. They must not target public services, employer systems, customer systems, real credentials, or third-party data. Network access is unnecessary for the first demonstration.
