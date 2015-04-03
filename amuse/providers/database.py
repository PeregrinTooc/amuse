from amuse.providers.base import JokeProvider


class DatabaseJokeProvider(JokeProvider):
    """Reserved for when the jokes live in a database.

    There is currently no database. There is currently one joke file with
    three jokes in it. This provider exists so that the migration, when it
    happens, is a configuration change rather than a code change.
    """

    def provide(self, context):
        raise NotImplementedError("no database yet")

    @property
    def priority(self):
        return 200
