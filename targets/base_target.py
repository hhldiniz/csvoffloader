import abc


class BaseTarget(abc.ABC):

    @abc.abstractmethod
    def offload(self, json_str: str):
        pass
