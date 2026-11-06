"""Synthetic task B: deterministic model admission."""
def choose_model(worker, catalogue, requested=None):
    """Return model string. catalogue = {worker: {'default': str, 'allowed': [str]}}.
    Reject unknown worker/model and default not in allowed. No fallback.
    """
    raise NotImplementedError("agent task B")
