import abc

from targets.base_target import BaseTarget


class BaseSource(abc.ABC):

    def __init__(self, target: BaseTarget):
        self.target = target

    @abc.abstractmethod
    def consume(self):
        pass
