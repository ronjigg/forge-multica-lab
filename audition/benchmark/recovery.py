"""Synthetic task C: stale STARTING must not be silently RUNNING."""
def review_recovery(jobs, now, max_starting_seconds=30):
    """Return independent copies of all jobs. If a 'starting' job is older
    than max_starting_seconds, set status=attention, reason=START_TIMEOUT.
    Leave everything else unchanged, and never double-dispatch.
    """
    raise NotImplementedError("agent task C")
