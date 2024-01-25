from Genetic import Genetic
from Genetic.Enums import CrossOverTypes
import matplotlib.pyplot as plt

class Boot:

    def __init__(self) -> None:
        self.boot()

    def error(self, message):
        st = "*" * 15
        print(f"\n{st}\n{message}\n\n{st}\n")

    def boot(self):
        while True:
            per_mutation = input("Enter permutation between 0 and 1: ")
            try:
                per_mutation = float(per_mutation)
                if per_mutation < 0 or per_mutation >= 1:
                    self.error('permutation is out of range !')
                    continue
                break
            except:
                self.error('invalid input !')
        
        while True:
            maxiter = input("Enter maxiter between 1 and 10000 (suggested: 5000): ")
            try:
                maxiter = int(maxiter)
                if maxiter < 0 or maxiter > 10000:
                    self.error('maxiter is out of range !')
                    continue
                break
            except:
                self.error('invalid input !')
        
        while True:
            print("(1) => one point")
            print("(2) => two point")
            print("(3) => uniform")
            crossover_type = input("Select crossover type: ")
            try:
                crossover_type = int(crossover_type)
                if crossover_type < 1 or crossover_type > 3:
                    self.error('invalid crossover type !')
                    continue
                else:
                    if crossover_type == 1:
                        crossover_type = CrossOverTypes.OnePoint
                    elif crossover_type == 2:
                        crossover_type = CrossOverTypes.TwoPoint
                    elif crossover_type == 3:
                        crossover_type = CrossOverTypes.Uniform

                break
            except:
                self.error('invalid input !')
        
        
        x = Genetic(10, 10, per_mutation, maxiter, crossover_type)
        (bests) = x.start_loop()

        plt.plot(bests)
        plt.show()