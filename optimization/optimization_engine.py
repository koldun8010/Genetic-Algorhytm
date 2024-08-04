import random
from typing import List, Tuple

from creature_factory.creature_factory import CreatureFactory
from creature.creature import Creature
from modifications.modifications import Modifications


class OptimizationEngine:
    _creature_factory: CreatureFactory

    _start_population_number: int = 2 ** 8

    def __init__(self,
                 creature_factory: CreatureFactory,
                 start_population: int = None):
        self._creature_factory = creature_factory

        if start_population:
            self._start_population_number = start_population

    def optimize(self, k) -> Tuple[float, float]:
        population: List[Creature] = self._creature_factory.create_start_population(self._start_population_number)

        counter = 0
        minimum_fitness = None
        minimum_point = None
        for i in range(k):
            children: List[Creature] = []
            elite: List[Creature] = []
            mods = Modifications()

            for _ in range(0, len(population) - 1, 2):
                parent_1, parent_2 = self.choose_parents_pair(population, mods)

                elite = mods.find_elite(len(population), elite, parent_1, parent_2)

                child_1, child_2 = self._creature_factory.hybridize(parent_1, parent_2)
                if child_1:
                    children.append(child_1)

                if child_2:
                    children.append(child_2)

                child_1_fitness = child_1.get_fitness()
                if minimum_fitness is None or child_1_fitness < minimum_fitness:
                    minimum_fitness = child_1_fitness
                    minimum_point = child_1._coordinates  # это надо поправить - нарушение инкапсуляции

                child_2_fitness = child_2.get_fitness()
                if minimum_fitness is None or child_2_fitness < minimum_fitness:
                    minimum_fitness = child_2_fitness
                    minimum_point = child_2._coordinates  # это надо поправить - нарушение инкапсуляции

            # for child in children:
            #     child = mods.mutate(child) // ХЗ ЧО ДЕЛАТЬ С МУТАЦИЯМИ. 0 ИНФЫ

            population.clear()
            population.extend(elite)
            population.extend(children[0:len(population) - len(elite)])
            counter += 1

        return minimum_point

    def choose_parents_pair(self, population: List[Creature], mods) -> Tuple[Creature, Creature]:
        scaled_population = []
        for elem in population:
            m = 1
            m = mods.niching(elem, population)
            value = 1 - abs(elem.get_fitness()) / m
            if value <= 0:
                value = 1e-100
            scaled_population.append(value)

        winner_1 = mods.tournamenting(population, scaled_population)
        winner_2 = mods.tournamenting(population, scaled_population)

        #picked_parents = random.choices(winners,
        #                                weights=[value for value in scaled_population], k=2)

        return winner_1, winner_2
