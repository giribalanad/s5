"""
Experiment 2: Farmer, Wolf, Goat, and Cabbage Puzzle using Logical Programming / Search

Algorithm:
1. Represent each state as the positions of Farmer, Wolf, Goat, and Cabbage.
2. Farmer can cross the river alone or with one item.
3. A state is invalid if:
   * Wolf and Goat are left together without Farmer.
   * Goat and Cabbage are left together without Farmer.
4. Generate all possible valid moves.
5. Use DFS/Backtracking to search for a solution.
6. Stop when all four reach the opposite side.
"""


def safe(s):
    f, w, g, c = s
    return not ((w == g != f) or (g == c != f))


def solve(s, path, seen):
    if s == (1, 1, 1, 1):
        print(*path, sep="\n")
        return True

    for i in [0, 1, 2, 3]:
        if i and s[i] != s[0]:
            continue

        ns = list(s)
        ns[0] ^= 1
        if i:
            ns[i] ^= 1

        ns = tuple(ns)

        if safe(ns) and ns not in seen:
            if solve(ns, path + [ns], seen | {ns}):
                return True


solve((0, 0, 0, 0), [(0, 0, 0, 0)], {(0, 0, 0, 0)})

# INPUT:
# Initial state: Farmer, Wolf, Goat, Cabbage = Left
# Goal state:    Farmer, Wolf, Goat, Cabbage = Right

# OUTPUT:
# (0, 0, 0, 0)
# (1, 0, 1, 0)
# (0, 0, 1, 0)
# (1, 1, 1, 0)
# (0, 1, 0, 0)
# (1, 1, 0, 1)
# (0, 1, 0, 1)
# (1, 1, 1, 1)
