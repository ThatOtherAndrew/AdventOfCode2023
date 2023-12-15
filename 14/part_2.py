from functools import cache

import numpy as np


@cache
def pos_in_range(shape: tuple[int, ...], pos: tuple[int, ...]):
    for width, index in zip(shape, pos):
        if not 0 <= index < width:
            return False
    return True


def roll_rocks(platform: np.ndarray, direction: tuple[int, int]):
    rocks = list(zip(*np.nonzero(platform == 'O')))
    rocks.sort(key=lambda pos: pos[direction[0] == 0] * (-sum(direction)))

    for original_pos in rocks:
        rock_pos = original_pos

        next_pos = rock_pos[0] + direction[0], rock_pos[1] + direction[1]
        while pos_in_range(platform.shape, next_pos) and platform[next_pos] == '.':
            rock_pos = next_pos
            next_pos = rock_pos[0] + direction[0], rock_pos[1] + direction[1]

        platform[rock_pos] = 'O'
        if rock_pos != original_pos:
            platform[original_pos] = '.'


def get_total_load(platform: np.ndarray) -> int:
    return sum(np.count_nonzero(row == 'O') * (len(platform) - i) for i, row in enumerate(platform))


def main() -> None:
    with open('input.txt') as file:
        platform = np.array([list(line.rstrip()) for line in file])

    previous_states = {}
    # noinspection PyUnresolvedReferences
    while (state_hash := hash(platform.tobytes())) not in previous_states:
        previous_states[state_hash] = (len(previous_states), platform.copy())
        for direction in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            roll_rocks(platform, direction)

    cycle_start = previous_states[state_hash][0]
    cycle_offset = (1_000_000_000 - cycle_start) % (len(previous_states) - cycle_start)
    final_platform_state = list(previous_states.values())[cycle_start + cycle_offset][1]
    total_load = get_total_load(final_platform_state)
    print('Day 14.2 Answer:', total_load)


if __name__ == '__main__':
    main()
