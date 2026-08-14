rooms = {'A':'Dirty', 'B':'Dirty'}

for room in rooms:
    if rooms[room] == "Dirty":
        print("Cleaning Room", room)
        rooms[room] = "Clean"

print("Final State:", rooms)
