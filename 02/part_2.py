from typing import Iterable


class Turn:
    def __init__(self, turn_str: str) -> None:
        self.red = 0
        self.green = 0
        self.blue = 0

        for move in map(str.split, turn_str.split(', ')):
            setattr(self, move[1], int(move[0]))

    def is_possible(self) -> bool:
        return self.red <= 12 and self.green <= 13 and self.blue <= 14

    def __repr__(self) -> str:
        return f'<Turn red: {self.red}, green: {self.green}, blue: {self.blue}>'


def get_power(game: Iterable[Turn]) -> int:
    return (
        max(turn.red for turn in game)
        * max(turn.green for turn in game)
        * max(turn.blue for turn in game)
    )


def main() -> None:
    with open('input.txt') as file:
        games = [
            tuple(map(Turn, line.partition(': ')[2].split('; ')))
            for line in file
        ]

    total_power = sum(map(get_power, games))
    print('Day 2.2 Answer:', total_power)


if __name__ == '__main__':
    main()
