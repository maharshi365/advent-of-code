from typing import TypedDict


class Game1(TypedDict):
    id: int
    game: list[dict[str, int]]


class Game2(TypedDict):
    id: int
    game: dict[str, int]


with open("input.txt", "r") as f:
    data = f.readlines()


## PART 1
targets = {"red": 12, "green": 13, "blue": 14}


def parse_info1(line: str) -> Game1:
    gameText, rest = line.split(":")

    _, id = gameText.split()

    subsets = rest.split(";")

    game = []
    for subset in subsets:
        picks = subset.split(",")

        round = {}
        for pick in picks:
            count, color = pick.split()

            round[color] = int(count)

        game.append(round)

    return {"id": int(id), "game": game}


def is_possible1(game: Game1) -> int:
    for round in game["game"]:
        for color, count in round.items():
            if color not in targets:
                return 0
            if count > targets[color]:
                return 0

    return game["id"]


## PART 2
def parse_info2(line: str) -> Game2:
    gameText, rest = line.split(":")

    _, id = gameText.split()

    subsets = rest.split(";")

    game = {}
    for subset in subsets:
        picks = subset.split(",")
        for pick in picks:
            count, color = pick.split()

            if color not in game:
                game[color] = int(count)
            else:
                game[color] = max(game[color], int(count))

    return {"id": int(id), "game": game}


def get_power2(game: Game2) -> int:
    power = 1
    for _, count in game["game"].items():
        power *= count

    return power


print(sum([get_power2(parse_info2(line)) for line in data]))
