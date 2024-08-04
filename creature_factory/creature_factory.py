from abc import ABC, abstractmethod
from typing import Tuple, List

from creature.creature import Creature


class CreatureFactory(ABC):

    @abstractmethod
    def create_start_population(self, start_creatures_number: int) -> List[Creature]:
        pass

    @abstractmethod
    def get_from_code(self, code: str):
        pass

    @abstractmethod
    def hybridize(self, creature_1: Creature, creature_2: Creature) -> Tuple[Creature, Creature]:
        pass
