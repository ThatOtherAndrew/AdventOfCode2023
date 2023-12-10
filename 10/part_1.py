import numpy as np


def step_cursors(cursors: list[tuple[int, int]], pipes: np.ndarray, distances: np.ndarray) -> list[tuple[int, int]]:
    up = -1, 0
    down = 1, 0
    left = 0, -1
    right = 0, 1

    new_cursors = []
    directions = {
        '|': (up, down),
        '-': (left, right),
        'L': (up, right),
        'J': (up, left),
        '7': (down, left),
        'F': (down, right),
        '.': (),
        'S': (up, down, left, right),
    }

    for cursor in cursors:
        for direction in directions[pipes[cursor].item()]:
            new_pos = cursor[0] + direction[0], cursor[1] + direction[1]
            if distances[new_pos] == -1 and any(
                direction[0] + new_direction[0] == direction[1] + new_direction[1] == 0
                for new_direction in directions[pipes[new_pos].item()]
            ):
                distances[new_pos] = distances[cursor] + 1
                new_cursors.append(new_pos)

    return new_cursors


def main() -> None:
    with open('input.txt') as file:
        pipes = np.array([list(line) for line in file.read().splitlines()])

    distances = np.full(pipes.shape, -1, dtype=np.int32)
    cursors = list(zip(*np.where(pipes == 'S')))
    distances[cursors[0]] = 0
    while cursors:
        cursors = step_cursors(cursors, pipes, distances)

    print('Day 10.1 Answer:', np.max(distances))


if __name__ == '__main__':
    main()
