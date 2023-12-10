from math import lcm


def count_steps(network: dict[str, tuple[str, str]], instructions: str, starting_pos: str) -> int:
    steps = 0
    position = starting_pos
    while not position.endswith('Z'):
        position = network[position][instructions[steps % len(instructions)] == 'R']
        steps += 1

    # This code only works in the special case that the step loop length matches the distance to the first --Z node.
    # This appears to be true for the input data (as shown by `steps % len(instructions)` always being 0)
    # However, this is not true for the example provided (test_3.txt).
    print(f'{starting_pos} -({steps})-> {position}  |  '
          f'<{instructions[steps % len(instructions)]}[{steps % len(instructions)}]: '
          f'{network[position][instructions[steps % len(instructions)] == "R"]}>')
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

    steps = [count_steps(network, instructions, node) for node in network.keys() if node.endswith('A')]
    print('Day 8.2 Answer:', lcm(*steps))


if __name__ == '__main__':
    main()
