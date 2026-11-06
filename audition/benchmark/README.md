# Forge Next neutral worker benchmark

Synthetic fixtures only. No credentials or connection to live Forge.

Each candidate must run three separate disposable tasks with separate worktrees: (A) implement `summarise_jobs`; (B) implement `choose_model`; (C) implement `review_recovery`. Do not edit the tests. For each actual run collect runtime, agent, requested and actual provider/model, UTC start and finish, exit, raw receipt, token usage (if available) and errors. A platform supporting a provider in its catalogue does not constitute a pass.

Before authenticating providers, from the repository root run `python3 -m unittest discover -s audition/benchmark -p 'test_*.py' -v` to verify intentional RED tests. **Do not run agent CLIs in this preflight.** Once the source/security and isolation checks are green, assign each task to a real worker and require the tests to be GREEN. Two run intervals must genuinely overlap to claim parallelism.

All files here are synthetic and non-sensitive. Do not give the runner production credentials, live Forge mounts, home LAN access or a broad GitHub PAT.
