import numpy as np


UP = -1, 0
DOWN = 1, 0
LEFT = 0, -1
RIGHT = 0, 1
DIRECTIONS = {
    '|': (UP, DOWN),
    '-': (LEFT, RIGHT),
    'L': (UP, RIGHT),
    'J': (UP, LEFT),
    '7': (DOWN, LEFT),
    'F': (DOWN, RIGHT),
    '.': (),
    'S': (UP, DOWN, LEFT, RIGHT),
}


def step_cursors(cursors: list[tuple[int, int]], pipes: np.ndarray, loop_mask: np.ndarray) -> list[tuple[int, int]]:
    new_cursors = []

    for cursor in cursors:
        for direction in DIRECTIONS[pipes[cursor].item()]:
            new_pos = cursor[0] + direction[0], cursor[1] + direction[1]
            if not loop_mask[new_pos] and any(
                direction[0] + new_direction[0] == direction[1] + new_direction[1] == 0
                for new_direction in DIRECTIONS[pipes[new_pos].item()]
            ):
                loop_mask[new_pos] = 1
                new_cursors.append(new_pos)

    return new_cursors


def point_is_enclosed(point: tuple[int, int], pipes: np.ndarray, loop_mask: np.ndarray) -> bool:
    if loop_mask[point]:
        return False

    crosses = sum(
        1
        for i in range(point[0])
        if (
            loop_mask[i, point[1]]
            and LEFT in DIRECTIONS[pipes[i, point[1]]]  # Assuming the left half of each cell, however RIGHT works too
        )
    )
    return bool(crosses % 2)


def main() -> None:
    with open('input.txt') as file:
        pipes = np.array([list(line) for line in file.read().splitlines()])
        loop_mask = np.zeros(pipes.shape, dtype=np.bool_)

    start_index = next(zip(*np.where(pipes == 'S')))
    cursors = [start_index]
    loop_mask[cursors[0]] = 1
    while cursors:
        cursors = step_cursors(cursors, pipes, loop_mask)

    if start_index[1] > 0 and RIGHT not in DIRECTIONS[pipes[start_index[0], start_index[1] - 1]]:
        # hacky substitution of the start cell for the enclosed cell algorithm to work
        pipes[start_index] = '.'

    # noinspection PyTypeChecker
    enclosed_mask = np.array([
        point_is_enclosed(point, pipes, loop_mask)
        for point in np.ndindex(pipes.shape)
    ]).reshape(pipes.shape)

    print('Day 10.2 Answer:', np.sum(enclosed_mask))


if __name__ == '__main__':
    main()
