import math

from optimization.optimization_engine import OptimizationEngine
from creature_factory.two_variables_function_factory import TwoVariablesFunctionPointsFactory
from hybridization.simple_hybridization import SimpleHybridization


n = 2
search_area = ((-5.12, 5.12), (-5.12, 5.12))
engine = OptimizationEngine(
    TwoVariablesFunctionPointsFactory(
        SimpleHybridization(),
        lambda x, y: 10 * 2 + x ** 2 - 10 * math.cos(2 * math.pi * x) + y ** 2 - 10 * math.cos(2 * math.pi * y),
        search_area
    )
)

print(engine.optimize(10))
