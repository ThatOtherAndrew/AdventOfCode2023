class Turn:
    def __init__(self, turn_str: str) -> None:
        self.red = 0
        self.green = 0
        self.blue = 0

        for move in map(str.split, turn_str.split(', ')):
            setattr(self, move[1], int(move[0]))

    def is_possible(self) -> bool:
        return self.red <= 12 and self.green <= 13 and self.blue <= 14


def main() -> None:
    with open('input.txt') as file:
        games = [
            tuple(map(Turn, line.partition(': ')[2].split('; ')))
            for line in file
        ]

    # noinspection PyTypeChecker
    # ^ this is needed because PyCharm is stupid https://youtrack.jetbrains.com/issue/PY-64479
    valid_games = sum(
        i + 1
        for i, game in enumerate(games)
        if all(turn.is_possible() for turn in game)
    )
    print('Day 2.1 Answer:', valid_games)


if __name__ == '__main__':
    main()
