class Chromosome:
    EPSILON = 0.0000000001

    def __init__(self, gens: [int]) -> None:
        self.__gens = gens
        self.__fitness = None
        self.__summation = None
        self.__fitness_ratio = None
        self.__probability_range = None
        self.fitness

    # completed
    def __str__(self):
        return f"{self.__gens} {self.fitness}"

    @property
    def gens(self):
        return self.__gens

    # completed
    def intersects(self) -> int:
        # -1 because we want to check if each child in list is repeated or not
        # if we loop until len(self.__gens) we cannot check if last child is
        # repeated or not
        fitness = 0
        for i in range(0, len(self.__gens) - 1):
            for j in range(i + 1, len(self.__gens)):
                if self.__gens[i] == self.__gens[j]:
                    fitness += 1
        return fitness

    # completed
    @property
    def fitness(self) -> float:
        if self.__fitness != None:
            return self.__fitness
        else:
            self.__fitness = 1 / (self.intersects() + self.EPSILON)
            return self.__fitness

    # completed
    def set_summation(self, summation: float | int):
        self.__summation = summation
        self.fitness_ratio

    # completed
    @property
    def fitness_ratio(self):
        if self.__fitness_ratio != None:
            return self.__fitness_ratio
        else:
            return self.fitness / self.__summation

    # completed
    def set_probability_range(self, range_: (float, float)) -> None:
        self.__probability_range = range_

    # completed
    def is_chosen(self, number: float):
        if self.__probability_range == None:
            print()
            raise Exception("probability range must be valid or not None in Chromosome structure !")

        if number >= self.__probability_range[0] and number < self.__probability_range[1]:
            return True
        else:
            return False


