import numpy as np


def roll_rock(platform: np.ndarray, rock_pos: tuple[int, int]):
    original_pos = rock_pos

    next_pos = rock_pos[0] - 1, rock_pos[1]
    while rock_pos[0] > 0 and platform[next_pos] == '.':
        rock_pos = next_pos
        next_pos = rock_pos[0] - 1, rock_pos[1]

    platform[rock_pos] = 'O'
    if rock_pos != original_pos:
        platform[original_pos] = '.'


def get_total_load(platform: np.ndarray) -> int:
    return sum(np.count_nonzero(row == 'O') * (len(platform) - i) for i, row in enumerate(platform))


def main() -> None:
    with open('input.txt') as file:
        platform = np.array([list(line.rstrip()) for line in file])

    for rock_pos in zip(*np.nonzero(platform == 'O')):
        roll_rock(platform, rock_pos)
    total_load = get_total_load(platform)
    print('Day 14.1 Answer:', total_load)


if __name__ == '__main__':
    main()
