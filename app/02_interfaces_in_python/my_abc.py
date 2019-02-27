import abc


class MyABC(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def do_something(self, value):
        """Required method"""

    @property
    def some_property(self):
        """Required method"""
