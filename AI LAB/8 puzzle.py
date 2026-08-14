start = [1,2,3,4,0,5,6,7,8]
goal = [1,2,3,4,5,0,6,7,8]

if start != goal:
    start[4], start[5] = start[5], start[4]

print("Goal State:")
print(start)
