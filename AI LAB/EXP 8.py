graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3},
    'C': {'D': 1},
    'D': {}
}

heuristic = {'A':4, 'B':2, 'C':1, 'D':0}

current = 'A'
cost = 0

while current != 'D':
    print(current, end=" -> ")
    next_node = min(graph[current], key=lambda x: graph[current][x] + heuristic[x])
    cost += graph[current][next_node]
    current = next_node

print("D")
print("Cost =", cost)
