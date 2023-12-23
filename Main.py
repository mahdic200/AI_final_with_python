from Genetic import Genetic
from Genetic.Enums import CrossOverTypes
import matplotlib.pyplot as plt


x = Genetic(10, 10, 0.1, 500, CrossOverTypes.TwoPoint)
(best, bests) = x.start_loop()
print(f"best : {best.gens}, conflicts: {best.intersects()}")

plt.plot(bests)
plt.show()
