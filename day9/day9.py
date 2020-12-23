import itertools

f = open('day9_input', 'r').readlines()
data = [int(str.strip()) for str in f]

from itertools import chain, combinations


def par1_solution(preamble=5):
    for index in range(preamble, len(data)):
        comb = itertools.combinations(data[index - preamble:index], 2)
        list_of_sims = [sum(i) for i in comb]
        if data[index] not in list_of_sims:
            print(data[index])
            return data[index]


def part2_solution(preamble):
    for i in range(len(data)):
        for j in range(i, len(data)):
            if sum(data[i:j]) == 15353384:
                subset = data[i:j]
                local_min, local_max = min(subset), max(subset)
                print(local_min + local_max)
                return local_min + local_max


# par1_solution(preamble=5)

part2_solution(preamble=25)
