import abc

"""
Base class from all components that will define the destiny for csv files
"""


class BaseTarget(abc.ABC):

    """
    :param json_str: Content to be offloaded in a string representation of a json/dict.
    :type str
    :return None
    """
    @abc.abstractmethod
    async def offload(self, json_str: str) -> None:
        pass
