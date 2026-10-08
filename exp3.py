"""
Experiment 3: Sudoku Generation using Genetic Algorithm (Metaheuristic Search)

Algorithm:
1. Create a population of random Sudoku boards.
2. Calculate fitness based on duplicate numbers in rows, columns, and 3x3 blocks.
3. Select the fittest boards.
4. Apply crossover to create new boards.
5. Apply mutation by swapping numbers.
6. Repeat until a board has fitness = 0.
7. The resulting board is a valid Sudoku.
"""
import random

N = 9


def fitness(b):
    score = 0
    for i in range(N):
        score += 9 - len(set(b[i]))
        score += 9 - len(set(b[j][i] for j in range(N)))

    for r in range(0, N, 3):
        for c in range(0, N, 3):
            block = [b[i][j] for i in range(r, r + 3) for j in range(c, c + 3)]
            score += 9 - len(set(block))
    return score


def mutate(b):
    r = random.randrange(9)
    a, c = random.sample(range(9), 2)
    b[r][a], b[r][c] = b[r][c], b[r][a]


# Population representation: list of 9x9 boards
population = [[random.sample(range(1, 10), 9) for _ in range(9)] for _ in range(20)]

while True:
    population.sort(key=fitness)
    if fitness(population[0]) == 0:
        break

    new = population[:2]
    while len(new) < 20:
        p = random.choice(population[:10])
        child = [row.copy() for row in p]
        mutate(child)
        new.append(child)
    population = new

for row in population[0]:
    print(*row)

# INPUT:
# No user input; Sudoku is generated randomly.

# OUTPUT:
# A valid 9x9 Sudoku grid, for example:
# 5 3 4 6 7 8 9 1 2
# 6 7 2 1 9 5 3 4 8
# 1 9 8 3 4 2 5 6 7
# 8 5 9 7 6 1 4 2 3
# 4 2 6 8 5 3 7 9 1
# 7 1 3 9 2 4 8 5 6
# 9 6 1 5 3 7 2 8 4
# 2 8 7 4 1 9 6 3 5
# 3 4 5 2 8 6 1 7 9
