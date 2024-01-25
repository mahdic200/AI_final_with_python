from Genetic.Enums import CrossOverTypes
from Genetic.Chromosome import Chromosome
import random

class Genetic:

    def __init__(self,
        chromosome_length: int,
        population_size: int,
        per_mutation: int,
        maxiter: int,
        crossover_type: CrossOverTypes
    ) -> None:
        self.__chromosome_length = chromosome_length
        self.__population_size = population_size
        self.__per_mutation = per_mutation
        self.__population: [] = []
        self.__maxiter = maxiter
        self.__crossover_type = crossover_type

        self.init_population()

    def __str__(self):
        result = ""
        for item in self.__population:
            result += f"{item}\n"
        return result

    @property
    def population(self) -> [Chromosome]:
        return self.__population

    @property
    def population_size(self):
        return self.__population_size

    @property
    def chromosome_length(self):
        return self.__chromosome_length

    @property
    def crossover_type(self):
        return self.__crossover_type

    @property
    def maxiter(self):
        return self.__maxiter

    @property
    def per_mutation(self):
        return self.__per_mutation

    # completed
    def init_population(self) -> None:
        dataset = [
            [5, 5, 15, 15, 2, 2, 7, 7, 17, 17],
            [1, 15, 15, 25, 25, 25, 12, 17, 22, 3],
            [10, 10, 10, 20, 20, 7, 2, 12, 12, 3],
            [1,10,15,15,2,2,7,7,12,22],
            [5,5,20,25,20,25,12,12,17,3],
            [10,10,20,15,25,25,2,7,22,22],
            [5,5,15,20,20,7,7,7,12,22],
            [10,15,15,25,20,2,2,12,17,17],
            [10,10,20,25,25,2,7,12,12,17],
            [5,15,20,20,2,2,2,22,22,17],
        ]
        for item in dataset:
            self.__population.append(Chromosome(item))

    # completed
    def random_chromosome(self) -> Chromosome:
        rand_list = []
        for i in range(0, self.chromosome_length):
            rn = random.randint(0, 26)
            rand_list.append(rn)
        return Chromosome(rand_list)

    # completed
    def fitness_summation(self) -> float:
        summation = 0.0
        for chromo in self.__population:
            summation += chromo.fitness
        for chromo in self.__population:
            chromo.set_summation(summation)

        return summation

    # completed
    def init_probability_range(self) -> None:
        temp = 0.0
        for chr in self.population:
            temp_ = temp + chr.fitness_ratio
            chr.set_probability_range((temp, temp_))
            temp = temp_

    # completed
    def parent_selection(self) -> [Chromosome]:
        self.fitness_summation()
        self.init_probability_range()

        new_parents = []
        while len(new_parents) < len(self.__population):
            for chromo in self.population:
                rand_no = random.randint(0, 100) / 100
                if chromo.is_chosen(rand_no):
                    new_parents.append(chromo)
                    break
        return new_parents

    # completed
    def one_point_crossover(self, parent_1: Chromosome, parent_2: Chromosome) -> (Chromosome, Chromosome):
        parent_1 = parent_1.gens
        parent_2 = parent_2.gens

        i = random.randint(0, 100) % self.chromosome_length
        new_child_1 = parent_1[:i] + parent_2[i:]
        new_child_2 = parent_2[:i] + parent_1[i:]

        return (Chromosome(new_child_1), Chromosome(new_child_2))

    # completed
    def two_point_crossover(self, parent_1: Chromosome, parent_2: Chromosome) -> (Chromosome, Chromosome):
        parent_1 = parent_1.gens
        parent_2 = parent_2.gens

        a = random.randint(0, 100) % self.chromosome_length
        b = random.randint(0, 100) % self.chromosome_length
        
        if b < a : t = a;a = b;b = t;
        
        new_child_1 = parent_1[:a] + parent_2[a:b] + parent_1[b:]
        new_child_2 = parent_2[:a] + parent_1[a:b] + parent_2[b:]

        return (Chromosome(new_child_1), Chromosome(new_child_2))

    # completed
    def uniform_crossover(self, parent_1: Chromosome, parent_2: Chromosome) -> (Chromosome, Chromosome):
        parent_1 = parent_1.gens
        parent_2 = parent_2.gens

        new_child_1 = []
        new_child_2 = []
        for i in range(len(parent_1)):
            rn = random.randint(1, 2)
            if rn == 1:
                new_child_1.append(parent_1[i])
                new_child_2.append(parent_2[i])
            else:
                new_child_1.append(parent_2[i])
                new_child_2.append(parent_1[i])


        return (Chromosome(new_child_1), Chromosome(new_child_2))

    # completed
    def crossover(self, parent_1: Chromosome, parent_2: Chromosome) -> (Chromosome, Chromosome):
        if self.crossover_type == CrossOverTypes.OnePoint:
            return self.one_point_crossover(parent_1, parent_2)
        elif self.crossover_type == CrossOverTypes.TwoPoint:
            return self.two_point_crossover(parent_1, parent_2)
        elif self.crossover_type == CrossOverTypes.Uniform:
            return self.uniform_crossover(parent_1, parent_2)
        else:
            raise Exception("no invalid crossover type is chosen for Genetic class !")

    # completed
    def recombination(self, parents: [Chromosome]):
        offsprings = []

        for i in range(0, len(parents) - 1, 2):
            (child1, child2) = self.crossover(parents[i], parents[i + 1])

            offsprings.append(child1)
            offsprings.append(child2)

        return offsprings

    # completed
    def swap_mutation(self, chromosome: Chromosome) -> Chromosome:
        new_gens = chromosome.gens
        if (random.randint(0, 100) / 100) <= self.per_mutation:
            i = random.randint(0, len(new_gens) - 1)
            j = random.randint(0, len(new_gens) - 1)
            t = new_gens[i]
            new_gens[i] = new_gens[j]
            new_gens[j] = t

        return Chromosome(new_gens)

    # completed
    def mutation(self, offsprings: [Chromosome]) -> [Chromosome]:
        for i in range(0, len(offsprings)):
            offsprings[i] = self.swap_mutation(offsprings[i])
        return offsprings

    # completed
    def maximum_fitness(self, parents) -> Chromosome:
        max_fit = parents[0]
        for chromo in parents:
            if max_fit.fitness < chromo.fitness:
                max_fit = chromo

        return max_fit

    def start_loop(self) -> (Chromosome, [float]):
        best_fitnesses = []
        best = self.random_chromosome()
        for i in range(0, self.maxiter):
            parents = self.parent_selection()
            offsprings = self.recombination(parents)
            offsprings = self.mutation(offsprings)
            self.__population = offsprings
            new_best = self.maximum_fitness(offsprings)
            best_fitnesses.append(new_best.fitness)
            if best.fitness < new_best.fitness:
                best = new_best
            if i == len(self.population) - 1:
                print("final population: ")
                for chromosome in self.population:
                    print(chromosome.gens, " , fitness : ", chromosome.fitness)
        return (best_fitnesses)