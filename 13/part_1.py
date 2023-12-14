import numpy as np


def find_symmetry_index(pattern: np.ndarray) -> int:
    for i in range(1, len(pattern)):
        # noinspection PyUnresolvedReferences
        if all((a == b).all() for a, b in zip(reversed(pattern[:i]), pattern[i:])):
            return i
    return 0


def main() -> None:
    with open('input.txt') as file:
        patterns = [
            np.array([[char == '#' for char in line] for line in pattern.splitlines()], dtype=np.bool_)
            for pattern in file.read().split('\n\n')
        ]

    total = 100 * sum(map(find_symmetry_index, patterns)) + sum(map(find_symmetry_index, map(np.transpose, patterns)))
    print('Day 13.1 Answer:', total)


if __name__ == '__main__':
    main()
