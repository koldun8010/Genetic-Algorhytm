from typing import Tuple

from creature.creature import Creature
from .hybridization import HybridizationImpl


class SimpleHybridization(HybridizationImpl):

    def hybridize_creatures(self, creature_1: Creature, creature_2: Creature) -> Tuple[str, str]:
        parent_1_encoded = creature_1.get_encoded()
        parent_2_encoded = creature_2.get_encoded()
        return self._hybridize_by_switching_halfs(parent_1_encoded, parent_2_encoded)

    def _hybridize_by_switching_halfs(self, code_1: str, code_2: str) -> Tuple[str, str]:
        assert len(code_1) == len(code_2)

        step = len(code_1) // 2

        child_1 = "".join([code_1[i:step] + code_2[i + step:] for i in range(0, len(code_1), step)])
        child_2 = "".join([code_2[i:step] + code_1[i + step:] for i in range(0, len(code_2), step)])

        return child_1, child_2
