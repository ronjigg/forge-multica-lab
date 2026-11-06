# Forge Next: impartial audition protocol (2026-11-06)

> **AUDITION ONLY.** Never operate on the production Ubuntu Forge service or repository. Vendor claims, successful installation, and listed providers are not execution proof. No credentials, tokens or personal data in this public repository.

## Objective
Choose an engine for our own Forge Wall and orchestration logic, supporting **Codex, Antigravity, Muse, OpenCode, Copilot** with safe true parallelism, accurate model selection, recovery, independent operation and control from **ChatGPT Plus on a phone**. The live Forge stays untouched until an independently authorised promotion.

## Mandatory acceptance gates

| Gate | Test and required evidence | Result |
|---|---|---|
| S0 - source and licence | Pin upstream commit and dependency versions; inspect licence, install scripts, update policy, telemetry, credentials, auth, sandbox/process permissions, known advisories. | UNTESTED |
| S1 - zero-credential startup | Start candidate in throwaway isolated runner or VM using synthetic project; gather version, startup health, configuration and exit codes. No host credentials, provider logins or live Forge mounts. | UNTESTED |
| S2 - real five-worker tasks | One disposable bounded task per approved CLI; record actual executable, requested/actual provider/model, start/finish, exit, output, usage receipt and failure reason. Provider in catalog ≠ PASS. | UNTESTED |
| S3 - genuine concurrency | At least 2 tasks execute with overlapping timestamps, separate directories/worktrees and no cross-task edits; one failure must not stall another. | UNTESTED |
| S4 - failure recovery | Test missing provider/model, cancellation, daemon crash/restart, queue stale state and watchdog; no stuck STARTING without reason; no double dispatch. | UNTESTED |
| S5 - Forge Wall independence | Read-only adapter produces real worker grid: active/queued/done/attention counts, timers, worker and model names, job evidence, failure reason. Without proprietary UI dependence. | UNTESTED |
| S6 - phone and Plus | Submit read-only status request from ChatGPT Plus via existing GitHub connector; receive authenticated result with Windows desktop off. Do not assume local MCP is available in this chat. | UNTESTED |
| S7 - policy and cost | Prove deterministic model routing, no silent fallback, spend limits, safe stop and source/test/install separation with audit receipts. | UNTESTED |

**Hard gate:** a candidate with unrestricted execution must remain inside a locked-down disposable VM/container/user with no home LAN access, no production credentials and narrowly scoped outbound network. Do not enable unattended jobs on user's main PC or production server. Tests that would require unsafe authentication should be marked BLOCKED, not simulated as success.

## Evidence format
For every test preserve: UTC timestamp; candidate and exact upstream commit/release; test ID; host/runtime type; commands or test script; actual provider/model; outcome PASS/FAIL/BLOCKED; logs with secrets redacted; independent reviewer note; reproducible steps. Never infer task success from enqueue/HTTP 200. Use provider-side usage where possible.

## Stop/go criteria
No migration until all mandatory gates pass, including **real** parallel worker execution and phone-to-worker end-to-end proof. If multiple candidates pass, compare time-to-recovery, observed reliability, cost, customisation effort and trust surface. Keep Windows Forge 3.2 and live Ubuntu Forge unchanged.

## Multica-specific starting evidence / risks
- Source: https://github.com/multica-ai/multica (source-available with additional licence conditions; read licence before forking/custom UI).
- Local private controller v0.1.4 was reported to start and expose 12 tools, but `connection_status` returned `not connected: call connect_multica` — **not an authenticated or worker pass**.
- Focus on full permissions of daemon workers, noninteractive token scopes, self-hosted auth, independent API and isolated runtime.
- GitHub Action/job must not be given access to the live Forge repository or broad personal PAT.

## Next concrete test
S0 independent source/security check, then S1 no-provider synthetic startup in isolated ephemeral environment. Do not authorise an audition run before security and runtime boundary checks.

## Privacy and supply-chain security gate (added 2026-11-06)

**No sensitive data in GitHub audition repositories.** These are public code/test labs. Use only synthetic fixtures and disposable repositories; never commit prompts with personal content, real project files, keys, PATs, provider cookies, environment files, crash dumps or identifying worker logs. No audition is authorised to clone/read/write the private live Forge repository.

Before credentials or real workloads, produce a security review with links to reproducible evidence:

1. **Source provenance and integrity:** pin exact upstream commit/release and record SHA-256 of fetched binaries/images; review installer and auto-update behaviour and publisher workflow. Avoid `curl | sh`/unsigned executables as a trust shortcut.
2. **Static and dependency scanning:** run static-analysis/security rules appropriate to the language; scan dependencies and lockfiles against current advisories; secret scan; generate software bill of materials (SBOM); review vendored code, GitHub Actions, containers, and external scripts. Triaged HIGH/CRITICAL issues block release unless demonstrably unreachable and documented.
3. **Data-flow map:** enumerate local and remote endpoints, telemetry/analytics defaults, auth endpoints, LLM providers, Git providers, upload/sync routes, crash reporting, logs/backups, and whether credentials, prompts or code can leave the host. Packet/egress checks must corroborate code/docs where possible.
4. **Privilege boundary:** inspect how agents launch subprocesses, shell commands, plugins, worktrees and mounts; reject unrestricted host/user execution in trials. Run in a disposable locked-down environment with network allowlist and a kill switch. Check traversal/symlinks/command injection/webhooks/API permissions.
5. **Credentials and identity:** use synthetic or narrowly scoped accounts only after S0/S1 pass, no third-party hosted workspace sign-in for the test, no persistent credentials in repo/workflow logs. Verify local-only login where supported and access revocation.
6. **Permissioned operations:** use allowlisted read/status commands initially. No automatic production promotion; testing from ChatGPT Plus via GitHub is limited to non-sensitive command IDs/results until an independently reviewed private channel exists.
7. **Security conclusion:** record PASS / FAIL / BLOCKED and open residual risks; don't call the platform 'secure' solely because scans pass. Human review of dangerous execution paths is mandatory.

**Special Multica requirement:** its documented self-hosted deployment telemetry is enabled by default. For isolated trials set `DO_NOT_TRACK=1`, and separately inspect optional analytics integrations; verify by network egress observation. Authentication for the self-hosted instance must not rely on a vendor-hosted account. See https://github.com/multica-ai/multica/blob/main/SELF_HOSTING.md .
