import itertools

import numpy as np


def expand_space(space: np.ndarray) -> np.ndarray:
    expansions = 0
    for row_index in range(space.shape[0]):
        if not any(space[row_index + expansions]):
            space = np.insert(space, row_index + expansions, 0, axis=0)
            expansions += 1

    expansions = 0
    for column_index in range(space.shape[1]):
        if not any(space.T[column_index + expansions]):
            space = np.insert(space, column_index + expansions, 0, axis=1)
            expansions += 1

    return space


def get_distance_sum(space: np.ndarray) -> int:
    return sum(
        abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
        for pair in itertools.combinations(
            list(zip(*np.nonzero(space))),
            2
        )
    )


def main() -> None:
    with open('input.txt') as file:
        space = np.array([[char == '#' for char in line] for line in file.read().splitlines()], dtype=np.bool_)

    space = expand_space(space)
    distance_sum = get_distance_sum(space)
    print('Day 11.1 Answer:', distance_sum)


if __name__ == '__main__':
    main()
