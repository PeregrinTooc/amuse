import abc


class JokeProvider(object):
    """Anything capable of producing a joke."""

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def provide(self, context):
        raise NotImplementedError

    @abc.abstractproperty
    def priority(self):
        raise NotImplementedError
