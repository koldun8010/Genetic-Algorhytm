import math
import random
from typing import Tuple, List, Callable

from creature.creature import Creature
from creature.two_variables_function_point import TwoVariablesFunctionPoint
from .creature_factory import CreatureFactory
from hybridization.hybridization import HybridizationImpl


class TwoVariablesFunctionPointsFactory(CreatureFactory):
    _hybridization_engine = None

    _encoded_objects: dict[str, Creature] = dict()

    _search_area: Tuple[Tuple[float, float], Tuple[float, float]]

    _function: Callable[[float, float], float]

    def __init__(self, hybridization_impl: HybridizationImpl,
                 function: Callable[[float, float], float],
                 search_area: Tuple[Tuple[float, float], Tuple[float, float]]):
        assert isinstance(hybridization_impl, HybridizationImpl)

        self._hybridization_engine = hybridization_impl
        self._search_area = search_area
        self._function = function

    def create_start_population(self, start_creatures_number: int) -> List[Creature]:
        max_creatures_amount = self._get_max_creatures_amount(start_creatures_number)
        code_length = len(bin(max_creatures_amount).lstrip("0b"))
        assert self._is_power_of_two(max_creatures_amount)\
               and self._is_power_of_two(code_length)
        range_step_x = (self._search_area[0][1] - self._search_area[0][0]) / max_creatures_amount
        range_step_y = (self._search_area[1][1] - self._search_area[1][0]) / max_creatures_amount

        start_x = self._search_area[0][0]
        start_y = self._search_area[1][0]

        y_ratios = list(range(0, max_creatures_amount))
        x_ratios = list(range(0, max_creatures_amount))

        creatures = []
        self._fill_creatures(max_creatures_amount,
                             code_length,
                             start_x,
                             start_y,
                             range_step_x,
                             range_step_y,
                             x_ratios,
                             y_ratios,
                             creatures)
        return random.choices(creatures, k=start_creatures_number)

    def get_from_code(self, code: str) -> Creature:
        return self._encoded_objects.get(code)

    def hybridize(self, creature_1: Creature, creature_2: Creature) -> Tuple[Creature, Creature]:
        children_codes = self._hybridization_engine.hybridize_creatures(creature_1, creature_2)
        return self.get_from_code(children_codes[0]), self.get_from_code(children_codes[1])

    def _is_power_of_two(self, number) -> bool:
        return (number & (number-1) == 0) and number != 0

    def _fill_creatures(self, max_creatures_amount, code_length, start_x, start_y, range_step_x, range_step_y, x_ratios, y_ratios, creatures):
        for i in range(max_creatures_amount):
            code = bin(i).lstrip("0b").rjust(code_length, "0")
            point = TwoVariablesFunctionPoint(code,
                                              self._function,
                                              start_x + range_step_x * x_ratios[i],
                                              start_y + range_step_y * y_ratios[i])
            creatures.append(point)
            self._encoded_objects[code] = point

    def _get_max_creatures_amount(self, start_amount: int) -> int:
        start_amount *= 10
        start_amount_bin = bin(start_amount).lstrip("0b").replace("1", "0")
        while not self._is_power_of_two(len(start_amount_bin)):
            start_amount_bin = "0" + start_amount_bin

        start_amount_bin = "1" + start_amount_bin[1:]
        return int(start_amount_bin, 2)
