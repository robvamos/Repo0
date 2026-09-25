# Workshop — Secure Coding with Codex

## Format

**Title:** Secure Coding with Codex: From Prompt to Reviewed Pull Request

**Audience:** developers, DevSecOps engineers, security professionals, and technical students

**Duration:** 90 minutes, expandable to 120 minutes

**Mode:** in person or remote, individual or pairs

**Prerequisites:** Git, Python 3.10+, a local clone; Codex is optional for participants following the prepared comparison

## Learning objectives

Participants should leave able to:

- translate a security concern into bounded acceptance criteria;
- scope an agent's tools, files, and authority;
- treat repository content and generated output as untrusted;
- inspect a security-sensitive implementation and its tests;
- distinguish passing tests from broader security assurance;
- prepare a traceable review or pull request while retaining human accountability.

## Safe delivery boundary

Use only this repository's synthetic files. Do not request credentials, inspect participant home directories, target external systems, or use employer/customer code. The exercise requires no network access and performs no deployment.

## Facilitator preparation

1. Clone the repository on a clean account or disposable environment.
2. Run the documented unit test command.
3. Read the [threat model](../docs/threat-model.md).
4. Keep both before and after versions available; do not modify the vulnerable example in place.
5. Decide whether Codex will produce a fresh candidate or whether the prepared after version will be reviewed.
6. Prepare a visible timer and a way to collect anonymous, aggregate feedback.

## Agenda

### 1. Frame the boundary — 10 minutes

Explain the task, assets, trust boundary, prohibited data, and human decision points. Ask participants what could go wrong before showing code.

### 2. Inspect unfamiliar code — 10 minutes

Read examples/secure-file-access/before/file_access.py. Identify the trusted workspace, untrusted input, and parent-traversal abuse case.

### 3. Define acceptance criteria — 10 minutes

Compare participant criteria with the list in the demo README. Discuss absolute paths, empty paths, missing files, directories, symlinks, and portability.

### 4. Run a bounded Codex workflow — 20 minutes

Use the suggested task from the demo. Before execution, limit the scope to the demonstration directory, keep deployment out of scope, and require tests plus an explanation of residual limitations.

### 5. Review the change — 15 minutes

Review the diff before running it. Check path resolution, containment, exception behavior, unrelated edits, and newly introduced dependencies.

### 6. Verify and challenge — 15 minutes

Run:

    python -m unittest discover -s examples/secure-file-access/tests -v

Ask participants to propose one additional abuse case. Explain why a green suite does not prove the whole application secure.

### 7. Pull-request handoff — 5 minutes

Draft a concise change description with the trigger, resulting behavior, validation, and residual limitations.

### 8. Feedback and next action — 5 minutes

Collect one useful lesson, one unclear point, and one proposed improvement. Record only aggregate feedback and update the evidence register after the session.

## Optional 30-minute extension

- compare two candidate implementations;
- discuss filesystem races and platform differences;
- map the workflow to enterprise change control;
- have pairs exchange reviews without revealing personal or employer information.

## Facilitator prompts

- Which input crosses a trust boundary?
- What authority does the agent actually need?
- Which behavior must be deterministic before a patch is accepted?
- What can these tests establish, and what can they not establish?
- Which decision still needs an accountable human?

## Completion evidence

A session counts as delivered only when its date, material revision, approximate audience, exercises completed, and aggregate feedback are recorded in docs/evidence.md. A rehearsal must be labeled as a rehearsal.
