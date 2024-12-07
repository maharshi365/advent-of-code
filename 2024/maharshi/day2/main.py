def string_to_array_int(string):
    return [int(x) for x in string.split(" ")]


def is_good(report: list[int]) -> bool:
    inc_or_dec = report == sorted(report) or report == sorted(report, reverse=True)

    ok = True
    for i in range(len(report) - 1):
        if not 1 <= abs(report[i] - report[i + 1]) <= 3:
            ok = False
            break
    return ok and inc_or_dec


with open("data/day2.txt") as f:
    data = f.readlines()
data = [x.strip() for x in data]

data = [string_to_array_int(x) for x in data]

p1 = 0
p2 = 0

for report in data:
    if is_good(report):
        p1 += 1

    good = False
    for j in range(len(report)):
        sub_report = report[:j] + report[j + 1 :]
        if is_good(sub_report):
            good = True
            break
    if good:
        p2 += 1

print(p1)
print(p2)
