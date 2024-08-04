import random
from typing import Callable, Tuple

from .creature import Creature


class TwoVariablesFunctionPoint(Creature):

    _function = None

    _coordinates: Tuple[float, float] = None

    def __init__(self,
                 code: str,
                 function: Callable[[float, float], float],
                 x_coord: float,
                 y_coord: float):
        super().__init__(code)
        assert isinstance(function, Callable)
        self._check_coordinates(x_coord, y_coord)

        self._function = function
        self._coordinates = (x_coord, y_coord)

    def get_fitness(self) -> float:
        return self._function(self._coordinates[0], self._coordinates[1])

    def get_coordinates(self) -> tuple[float, float]:
        return self._coordinates[0], self._coordinates[0]

    def get_encoded(self) -> str:
        return self._code

    def _check_coordinates(self, x_coord: float = 0., y_coord: float = 0.):
        assert isinstance(x_coord, float)
        assert isinstance(y_coord, float)

    def mutate(self):
        code = list(self._code)

        for i in range(len(code)):
            if random.choices(range(0, 100), k=1) == 0:
                code[i] = "0" if code[i] == "1" else "1"

        self._code = "".join(code)
