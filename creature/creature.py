from abc import ABC, abstractmethod


class Creature(ABC):

    _code = None

    def __init__(self, code: str):
        self._code = code

    @abstractmethod
    def get_fitness(self) -> float:
        pass

    @abstractmethod
    def get_coordinates(self) -> tuple[float, float]:
        pass

    @abstractmethod
    def get_encoded(self) -> str:
        pass

    def mutate(self):
        pass