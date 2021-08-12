import abc


class Moto(abc.ABC):
    @abc.abstractmethod
    def run(self, speed):
        """行驶"""

    @abc.abstractmethod
    def refueling(self, litre):
        """加油"""
