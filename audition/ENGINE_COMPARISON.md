# Forge Next engine comparison — evidence-led, preliminary (2026-11-06)

**Project rule:** Our Forge Wall, operator interface, trusted model policy and runtime boundary remain ours. Compare third-party engines as replaceable backends; no migration to production until audited, benchmarked, and proved controllable from ChatGPT Plus on a phone with the desktop off.

## Current desktop/documentation comparison

| Candidate | Scheduling / ongoing work (documented, not tested) | Independent deployment / no vendor account | Our Forge interface feasibility | Source/licence and trust caveat |
|---|---|---|---|---|
| **Multica** | Autopilots: cron/webhook triggers, runbooks, create-issue vs run-only, run history; 'run-only' skips if runtime offline, create-issue queues until online. | Own Docker API/web/DB and local verification codes possible; self-hosted still has *local* login; no need to use vendor cloud. | API + daemon and independent Forge Wall adapter plausible; modifying Multica's own UI invokes retained-branding licence rules. | Source-available custom Multica licence, default daemon runs with OS-user authority; self-host telemetry defaults on, disable via `DO_NOT_TRACK=1` and verify egress. |
| **Paseo** | Cron schedules create new agents; heartbeats wake an existing agent; separate self-hostable Hub adds external triggers. | Local daemon and own web/Android client, no forced vendor login; direct/VPN connection avoids official relay; Hub may also be self-hosted with local operator account. | Plugin API supports screens, panels, sidebar, themes and RPC; can additionally build independent Forge Wall adapter. | Apache-2.0; plugins are trusted **unsandboxed** host-side code, and supported agent providers still need their own credentials. |
| **Horde** | Durable coordinator/delegation/daemon, job progress and notifications; scheduling product surface not verified. | Local-first CLI/daemon; no required vendor workspace indicated in current README; off-desktop chat bridge still needed. | Rich API/CLI and our own Wall likely necessary; verify five current providers. | Apache-2.0; describes itself as early single-user release. Earlier audition onboarding timed out without reaching a model; **inconclusive**. |
| **Emdash** | Desktop Classic supports cron automations; remote project Workspace Server can own scheduling when desktop disconnected. | Local-first desktop with remote projects; no evidence yet of standalone Forge-style Android control equivalent. | UI-first developer app; backend adapter may require more work. | Apache-2.0 in official generalaction/emdash repo; telemetry optional; verify what changes in Emdash 2.0 separately. |

## Main questions that decide the choice

1. **Ownership:** Can we show the exact existing Forge Wall grid/roles/model labels and use our own operator login without having to interact with a vendor-branded front end every day? For Multica, keep legal attribution and licence requirements.
2. **Autonomy:** Can a scheduled run queue across offline runtimes, recover a failed attempt, keep model selection deterministic, avoid double dispatch, and emit an actionable reason? Documented schedules alone do not pass.
3. **Secure local control:** Are all logs, prompts, repo contents and auth secrets stored where we choose? Separate vendor daemon/relay, hosted model-provider outbound calls, GitHub storage and optional telemetry. Never treat self-hosting or 'E2EE' as a complete sandbox.
4. **Five genuine workers:** Codex, Antigravity, Muse, OpenCode, Copilot tested with real disposable workloads and actual provider/model/run receipts; native support claims ≠ execution pass.
5. **Remote Clive:** ChatGPT Plus GitHub connector may submit restricted synthetic requests, but a remotely executing bridge, readback receipts and phone test are still **UNBUILT**. Native Paseo Android access is *not* evidence ChatGPT can call it directly.
6. **Migration cost:** Measure time and lines needed to adapt two real status/worker APIs to Forge Wall rather than judging aesthetic similarity.

## Immediate neutral experiment

- Security gate S0: pin upstream commit and scan install scripts, dependencies, auth, telemetry, unsandboxed execution and licensing, without provider credentials.
- S1: disposable, credential-free bootstrap. No `curl | bash` shortcuts on production hosts.
- Run `audition/benchmark` as a common RED baseline, then three bounded real agent tasks with recorded evidence and a parallelism check only in isolated runner.
- Test one *read-only* Forge Wall adapter against each finalist and one scheduled job while daemon is offline; distinguish queue/wait, skip, retry and stuck STARTING.
- Winner requires security + execution + privacy + phone/Plus proofs. Document **BLOCKED** honestly where runner, credentials, or tool access is missing.

## Original project references

- Multica: https://multica.ai/docs/autopilots ; https://multica.ai/docs/self-host-quickstart ; https://github.com/multica-ai/multica/blob/main/LICENSE ; https://github.com/multica-ai/multica/blob/main/SELF_HOSTING.md
- Paseo: https://paseo.sh/docs/schedules ; https://paseo.sh/docs/security ; https://paseo.sh/docs/plugins ; https://paseo.sh/docs/hub/self-hosting ; https://github.com/getpaseo/paseo
- Horde: https://github.com/gethamster/horde
- Emdash: https://emdash.com/docs/automations ; https://github.com/generalaction/emdash

**Results today:** Document review and benchmark publication only. No candidate has passed a live agent security/execution test; no external provider or production system was accessed by these auditions.
