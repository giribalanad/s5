"""
Experiment 1: Map Coloring Problem using Constraint Satisfaction Problem (CSP) / Backtracking

Algorithm:
1. Represent each region as a variable.
2. Assign a domain of available colors to every region.
3. Store adjacent regions as constraints.
4. Select an uncolored region.
5. Try each available color.
6. Check whether the color conflicts with any adjacent colored region.
7. If valid, assign it and continue using backtracking.
8. If no color works, backtrack and change the previous assignment.
"""


def color_map(regions, colors, graph):
    result = {}

    def solve():
        if len(result) == len(regions):
            return True

        # Select uncolored region
        r = next(x for x in regions if x not in result)

        for c in colors:
            if all(result.get(n) != c for n in graph[r]):
                result[r] = c

                if solve():
                    return True

                del result[r]

        return False

    return result if solve() else None


regions = ['A', 'B', 'C', 'D']
colors = ['Red', 'Green', 'Blue']

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

solution = color_map(regions, colors, graph)
print("Map Coloring:", solution)

# INPUT:
# Regions: A, B, C, D
# Colors: Red, Green, Blue

# OUTPUT:
# Map Coloring: {'A': 'Red', 'B': 'Green', 'C': 'Blue', 'D': 'Red'}
