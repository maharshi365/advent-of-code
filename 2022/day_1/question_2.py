import heapq

with open("input.txt") as f:
    lines = f.read().splitlines()


cals = []
currCal = 0
for line in lines:
    if line == "":
        cals.append(currCal)
        currCal = 0
        continue
    currCal += int(line)

cals.append(currCal)

print(sum(heapq.nlargest(3, cals)))
