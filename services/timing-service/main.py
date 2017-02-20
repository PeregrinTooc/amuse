"""Comedy is timing. This service owns the pause before the punchline."""
import time

PAUSE_SECONDS = 1.2


def pause():
    time.sleep(PAUSE_SECONDS)
