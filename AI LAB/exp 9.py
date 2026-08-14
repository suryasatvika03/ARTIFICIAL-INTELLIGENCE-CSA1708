colors = ["Red", "Green", "Blue"]

states = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

result = {}

for state in states:
    used = [result[n] for n in states[state] if n in result]
    for color in colors:
        if color not in used:
            result[state] = color
            break

print(result)
