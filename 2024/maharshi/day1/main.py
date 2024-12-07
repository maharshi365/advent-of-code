from collections import Counter


def puzzle1():
    l1, l2 = list(), list()

    with open("data/day1.txt", "r") as f:
        for line in f:
            n1, n2 = map(int, line.split())
            l1.append(n1)
            l2.append(n2)

    distances = [abs(i - j) for i, j in zip(sorted(l1), sorted(l2))]

    print(sum(distances))


def puzzle2():
    l1, l2 = list(), Counter()

    with open("data/day1.txt", "r") as f:
        for line in f:
            n1, n2 = map(int, line.split())
            l1.append(n1)
            l2[n2] += 1

    similaries = [i * l2[i] if i in l2 else 0 for i in l1]

    print(sum(similaries))


puzzle2()
