def count_steps(network: dict[str, tuple[str, str]], instructions: str) -> int:
    steps = 0
    position = 'AAA'
    while position != 'ZZZ':
        position = network[position][instructions[steps % len(instructions)] == 'R']
        steps += 1

    return steps


def main() -> None:
    with open('input.txt') as file:
        instructions = file.readline().strip()
        # noinspection PyTypeChecker
        network: dict[str, tuple[str, str]] = {
            line.partition(' ')[0]: tuple(line.partition('(')[2].rstrip(')\n').split(', '))
            for line in file
            if line.strip()
        }

    print('Day 8.1 Answer:', count_steps(network, instructions))


if __name__ == '__main__':
    main()
