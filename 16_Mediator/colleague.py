from abc import ABCMeta, abstractmethod


class Colleague(metaclass=ABCMeta):

    def set_mediator(self, mediator: 'Mediator'):
        pass

    def set_colleague_enabled(self, enabled: bool):
        pass
