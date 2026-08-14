from itertools import permutations

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(graph)
cities = range(1, n)

min_cost = float('inf')

for path in permutations(cities):
    cost = graph[0][path[0]]

    for i in range(len(path)-1):
        cost += graph[path[i]][path[i+1]]

    cost += graph[path[-1]][0]

    min_cost = min(min_cost, cost)

print("Minimum Cost =", min_cost)
