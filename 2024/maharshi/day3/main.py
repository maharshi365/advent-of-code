import re

with open("data/day3.txt", "r") as f:
    data = f.read()


def puzzle1():
    regex = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)")

    # find all the matches
    matches = regex.findall(data)

    s = 0
    for match in matches:
        a, b = map(int, match[4:-1].split(","))
        s += a * b

    print(s)


def puzzle2():
    single_search = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)|don't\(\)|do\(\)")

    matches = single_search.findall(data)

    enabled = True
    s = 0
    for match in matches:
        if match == "don't()":
            enabled = False

        if match == "do()":
            enabled = True

        if enabled and "mul" in match:
            a, b = map(int, match[4:-1].split(","))
            s += a * b

    print(s)


puzzle2()
