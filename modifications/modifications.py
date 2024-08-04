import random
import math

class Modifications:
    def find_elite(self, number, elite, parent_1, parent_2):
        if len(elite) < number // 100 or len(elite) == 0:
            elite.append(parent_1)
            elite.append(parent_2)
        else:
            diff = abs(parent_1.get_fitness() - elite[0].get_fitness())
            replace_idx = 0
            for j in range(1, len(elite) - 1):
                if abs(parent_1.get_fitness() - elite[j].get_fitness()) > diff:
                    replace_idx = j
            elite[replace_idx] = parent_1

            diff = abs(parent_2.get_fitness() - elite[0].get_fitness())
            replace_idx = 0
            for j in range(1, len(elite) - 1):
                if abs(parent_2.get_fitness() - elite[j].get_fitness()) > diff:
                    replace_idx = j
            elite[replace_idx] = parent_2

        return elite

    def niching(self, elem, population):
        alpha = 1
        sigma = 10
        m = 0

        for elem_j in population:
            d = math.dist(elem_j.get_coordinates(), elem.get_coordinates())
            if d < sigma:
                m += 1 - ((d / sigma) ** alpha)
            else:
                m += 0

        return m

    def tournamenting(self, population, scaled_population):
        tournament_size = 2

        contender_1 = random.randint(0, len(population) - 1)
        contender_2 = random.randint(0, len(population) - 1)

        if scaled_population[contender_1] >= scaled_population[contender_2]:
            return population[contender_1]
        else:
            return population[contender_2]

    def three_dot_combining(self, parent_1, parent_2):
        code_1 = parent_1.get_encoded()
        code_2 = parent_2.get_encoded()

        assert len(code_1) == len(code_2)
        size = len(code_1)
        dot1 = size // 3
        dot2 = size // 3 * 2
        dot3 = size // 3 * 2

        child_1 = code_1[0:dot1 - 1] + code_2[dot1:dot2 - 1] + code_1[dot2:dot3 - 1] + code_2[dot3:size - 1]
        child_2 = code_2[0:dot1 - 1] + code_1[dot1:dot2 - 1] + code_2[dot2:dot3 - 1] + code_1[dot3:size - 1]

        return child_1.get_from_code(), child_2.get_from_code()

    # def mutate(self, child):
    #     mutation_probability = 0.0
    #     code = child.get_encoded()
    #
    #     for idx in range(len(code)):
    #         p = random.random()
    #         if p < mutation_probability:
    #             i = 0
    #     return code.get_from_code() //  НАЧАЛ ПИСАТЬ - ЗАКОНЧИТЬ НЕ ЗНАЮ КАК
