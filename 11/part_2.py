import itertools

import numpy as np


def get_galaxy_distance(
    blank_rows: set[int],
    blank_columns: set[int],
    start: tuple[int, int],
    end: tuple[int, int]
) -> int:
    distance = 0
    for i, line in enumerate((blank_rows, blank_columns)):
        distance += sum(1_000_000 if index in line else 1 for index in range(*sorted((start[i], end[i]))))
    return distance


def get_distance_sum(space: np.ndarray) -> int:
    blank_rows = {i for i, row in enumerate(space) if not any(row)}
    blank_columns = {i for i, column in enumerate(space.T) if not any(column)}
    return sum(
        get_galaxy_distance(blank_rows, blank_columns, *pair)
        for pair in itertools.combinations(
            list(zip(*np.nonzero(space))),
            2
        )
    )


def main() -> None:
    with open('input.txt') as file:
        space = np.array([[char == '#' for char in line] for line in file.read().splitlines()], dtype=np.bool_)

    distance_sum = get_distance_sum(space)
    print('Day 11.2 Answer:', distance_sum)


if __name__ == '__main__':
    main()
