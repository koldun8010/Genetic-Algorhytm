from abc import ABC, abstractmethod
from typing import Tuple

from creature.creature import Creature


class HybridizationImpl(ABC):

    @abstractmethod
    def hybridize_creatures(self, creature_1: Creature, creature_2: Creature) -> Tuple[str, str]:
        pass
