import pyevolve
from pyevolve import G1DList
from pyevolve import GSimpleGA


def eval_func(chromosome):
        score = 0.0
        sum = 0.0
        
        # iterate over the chromosome
        for value in chromosome:
                sum = value + sum
                score = 1/(1+abs(sum-x)) 
                if sum == x:
                    score+= 1
        return score

genome = G1DList.G1DList(20) #elements in list
x = input("Enter the sum  you want:")
genome.evaluator.set(eval_func)
ga = GSimpleGA.GSimpleGA(genome)#engine
ga.setGenerations(200)
ga.evolve(freq_stats=10)
print ga.bestIndividual()
a = sum(ga.bestIndividual())
print a