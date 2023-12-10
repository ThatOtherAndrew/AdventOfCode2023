# I have no idea if this code works or not, because it doesn't run in a plausible amount of time!

from collections.abc import Iterator


def ghost_generator(network: dict[str, tuple[str, str]], instructions: str, start_pos: str) -> Iterator[str]:
    steps = 0
    position = start_pos
    while True:
        position = network[position][instructions[steps % len(instructions)] == 'R']
        yield position
        steps += 1


def main() -> None:
    with open('input.txt') as file:
        instructions = file.readline().strip()
        # noinspection PyTypeChecker
        network: dict[str, tuple[str, str]] = {
            line.partition(' ')[0]: tuple(line.partition('(')[2].rstrip(')\n').split(', '))
            for line in file
            if line.strip()
        }

    ghosts = [
        ghost_generator(network, instructions, start_pos)
        for start_pos in network.keys()
        if start_pos.endswith('A')
    ]
    steps = 1
    while True:
        if all(next(ghost).endswith('Z') for ghost in ghosts):
            break
        steps += 1
        if not steps % 1_000_000:
            print(steps)

    print('Day 8.2 Answer:', steps)


if __name__ == '__main__':
    main()
