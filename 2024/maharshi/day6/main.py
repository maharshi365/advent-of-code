with open("data/day6.txt", "r") as file:
    grid = file.read().split("\n")

ROWS = len(grid)
COLS = len(grid[0])

CHECK_UP = (-1, 0)
CHECK_RIGHT = (0, 1)
CHECK_DOWN = (1, 0)
CHECK_LEFT = (0, -1)

CHECK_DIRS = [CHECK_UP, CHECK_RIGHT, CHECK_DOWN, CHECK_LEFT]

# find the gaurd position indicated by ^
guardPosition = (0, 0)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "^":
            guardPosition = (i, j)
            break


def puzzle1(initialPos):
    currPos = initialPos
    currCheckDir = 0

    distinctPositions = set()
    distinctPositions.add(currPos)

    while True:
        if (
            currPos[0] == 0
            or currPos[0] == ROWS - 1
            or currPos[1] == 0
            or currPos[1] == COLS - 1
        ):
            break

        check_pos = (
            currPos[0] + CHECK_DIRS[currCheckDir][0],
            currPos[1] + CHECK_DIRS[currCheckDir][1],
        )

        if grid[check_pos[0]][check_pos[1]] != "#":
            currPos = check_pos
            distinctPositions.add(currPos)

        else:
            currCheckDir = (currCheckDir + 1) % 4
            continue

    print(f"Number of distinct positions visited: {len(distinctPositions)}")


def puzzle2(initialPos):
    def is_loop(initialPos):
        currPos = initialPos
        currCheckDir = 0

        distinctPositions = set()
        distinctPositions.add((currPos[0], currPos[1], currCheckDir))

        while True:
            if (
                currPos[0] == 0
                or currPos[0] == ROWS - 1
                or currPos[1] == 0
                or currPos[1] == COLS - 1
            ):
                break

            check_pos = (
                currPos[0] + CHECK_DIRS[currCheckDir][0],
                currPos[1] + CHECK_DIRS[currCheckDir][1],
            )

            if grid[check_pos[0]][check_pos[1]] != "#":
                currPos = check_pos

                if (currPos[0], currPos[1], currCheckDir) in distinctPositions:
                    return True
                else:
                    distinctPositions.add((currPos[0], currPos[1], currCheckDir))

            else:
                currCheckDir = (currCheckDir + 1) % 4
                continue

        return False

    count = 0
    for r in range(ROWS):
        for c in range(COLS):

            # dont bother with creating a obstacle where the guard is
            if r == initialPos[0] and c == initialPos[1]:
                continue

            # dont bother with creating a obstacle where one already exists
            if grid[r][c] == "#":
                continue

            # create a obstacle
            grid[r] = grid[r][:c] + "#" + grid[r][c + 1 :]

            # check if the current position is a loop
            if is_loop(guardPosition):
                print(f"Obstacle at {r}, {c} creates a loop")
                count += 1
            else:
                print(f"Processed {r}, {c}")

            # remove the obstacle
            grid[r] = grid[r][:c] + "." + grid[r][c + 1 :]

    print("\n")
    print(f"Total number of obstacles that create a loop: {count}")


puzzle1(guardPosition)
