with open("input.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]


def get_digits(line: str) -> int:
    first = ""
    last = ""

    i = 0
    while i < len(line):
        if line[i].isnumeric():
            last = line[i]

            if first == "":
                first = line[i]

        i += 1

    return int(first) * 10 + int(last)


valid = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def parse_digits(line: str):
    first = ""
    last = ""

    i = 0
    while i < len(line):
        char = line[i]
        if char.isnumeric():
            last = int(char)
            if first == "":
                first = int(char)
            i += 1
        else:
            found = False
            for j in [3, 4, 5]:
                if found:
                    break
                if i + j <= len(line):
                    digit = "".join(line[i : i + j])
                    if digit in valid:
                        val = valid[digit]
                        last = val
                        if first == "":
                            first = val

                        i += 1
                        found = True
                        continue
            if not found:
                i += 1

    return 10 * int(first) + int(last)


nums = [parse_digits(line) for line in lines]
print(sum(nums))
