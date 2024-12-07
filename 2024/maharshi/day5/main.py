from collections import defaultdict

with open("data/day5t.txt", "r") as f:
    rules = defaultdict(set)
    updates = []

    for line in f.readlines():
        if "|" in line:
            pre, post = map(int, line.split("|"))

            rules[post].add(pre)

        elif "," in line:
            updates.append(list(map(int, line.strip().split(","))))
        elif line.strip() == "":
            continue
        else:
            raise ValueError(f"Invalid input: {line}")


def check(rules, update):
    seen = set()
    interested = set()

    for val in update:
        interested.add(val)

    for val in update:
        if val not in rules:
            seen.add(val)
            continue

        for r in rules[val]:
            if r not in interested:
                continue

            if r not in seen:
                return False

        seen.add(val)

    return True


def reorder(rules, update):
    toReturn = []
    interested = set()
    toPlace = set()

    return toReturn


total = 0
for update in updates:
    if check(rules, update):
        continue
    else:
        new_update = reorder(rules, update)

        mid = len(new_update) // 2
        total += new_update[mid]

print(total)

print(rules)
