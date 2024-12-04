DIRECTIONS = [
    (1, 1),  # down-right
    (1, 0),  # down
    (1, -1),  # down-left
    (-1, 1),  # up-right
    (-1, 0),  # up
    (-1, -1),  # up-left
    (0, 1),  # right
    (0, -1),  # left
]


def traverse1(grid, start, direction):
    i, rows, cols = 1, len(grid), len(grid[0])

    while i < 4:
        newR = start[0] + direction[0] * i
        newC = start[1] + direction[1] * i

        if newR < 0 or newR >= rows:
            return False

        if newC < 0 or newC >= cols:
            return False

        if grid[newR][newC] != "XMAS"[i]:
            return False

        i += 1

    return True


def puzzle1():

    with open("data/day4.txt", "r") as f:
        grid = [l.strip() for l in f.readlines()]

    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "X":
                for direction in DIRECTIONS:
                    if traverse1(grid, (i, j), direction):
                        total += 1

    print(total)


def traverse2(grid, start):

    rows, cols = len(grid), len(grid[0])

    # need to have some space as its alwasy going to be 3x3
    if start[0] < 1 or start[0] >= rows - 1:
        return False

    if start[1] < 1 or start[1] >= cols - 1:
        return False

    # check diagonal 1 for MAS (backwards or forwards)
    top_left = grid[start[0] - 1][start[1] - 1]
    bottom_right = grid[start[0] + 1][start[1] + 1]

    top_right = grid[start[0] - 1][start[1] + 1]
    bottom_left = grid[start[0] + 1][start[1] - 1]

    diagnalL = False
    diagnalR = False

    # top left to bottom right diagonal check
    if (
        top_left == "M"
        and bottom_right == "S"
        or top_left == "S"
        and bottom_right == "M"
    ):
        diagnalL = True

    if (
        top_right == "M"
        and bottom_left == "S"
        or top_right == "S"
        and bottom_left == "M"
    ):
        diagnalR = True

    return diagnalL and diagnalR


def puzzle2():
    with open("data/day4.txt", "r") as f:
        grid = [l.strip() for l in f.readlines()]

    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "A":
                if traverse2(grid, (i, j)):
                    total += 1

    print(total)


puzzle2()
