def read_input():
    output = []

    with open("data/problem.txt", "r") as file:
        for line in file.readlines():
            result, operands = line.split(": ")

            result = int(result)
            operands = list(map(int, operands.split(" ")))

            output.append((result, operands))

    return output


def puzzle1():
    def recurse(result, operands):
        if len(operands) == 1:
            return result == operands[0]

        else:
            item1, item2, *rest = operands

            add = item1 + item2
            mult = item1 * item2

            return recurse(result, [add, *rest]) or recurse(result, [mult, *rest])

    instructions = read_input()

    total = 0
    for instruction in instructions:
        result, operands = instruction

        if recurse(result, operands):
            total += result

    print(f"Total: {total}")


def puzzle2():
    def recurse(result, operands):
        if len(operands) == 1:
            return result == operands[0]

        else:
            item1, item2, *rest = operands

            add = item1 + item2
            mult = item1 * item2
            concat = int(str(item1) + str(item2))

            return (
                recurse(result, [add, *rest])
                or recurse(result, [mult, *rest])
                or recurse(result, [concat, *rest])
            )

    instructions = read_input()

    total = 0
    for instruction in instructions:
        result, operands = instruction

        if recurse(result, operands):
            total += result

    print(f"Total: {total}")


puzzle2()
