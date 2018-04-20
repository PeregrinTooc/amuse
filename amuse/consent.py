CONSENT_TEXT = """
We would like to tell you a joke.

To tell you this joke we process the following categories of personal data:
the fact that you were told a joke, the time at which you were told it, and
(if laughter is detected) the fact that you laughed.

Your data will be retained for 30 days. You may withdraw consent at any time
by running `amuse --forget`, which will erase the joke.

Do you consent? [y/N] """


def obtain_consent():
    return raw_input(CONSENT_TEXT).strip().lower() == "y"
