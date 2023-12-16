from collections import defaultdict
from itertools import repeat

import numpy as np


def pos_in_range(shape: tuple[int, ...], pos: tuple[int, ...]):
    for width, index in zip(shape, pos):
        if not 0 <= index < width:
            return False
    return True


TRANSFORMATIONS = {
    '.': lambda row, col: ((row, col),),
    '/': lambda row, col: ((-col, -row),),
    '\\': lambda row, col: ((col, row),),
    '|': lambda row, col: ((1, 0), (-1, 0)) if col else ((row, col),),
    '-': lambda row, col: ((0, 1), (0, -1)) if row else ((row, col),),
}


class Contraption:
    def __init__(self, grid: np.ndarray, start: tuple[int, ...] = (0, -1)) -> None:
        # For some reason PyCharm 2023.3.1 (#PY-233.11799.298) dies when type hinting start to tuple[int, int]
        # As in, Python functionality literally freezes and crashes
        # I have no idea why this happens but I cannot be bothered to deal with it

        self.grid = grid
        self.beams = [(
            start,
            tuple(
                0 if start[axis] in range(grid.shape[axis]) else -min(1, start[axis])
                for axis in (0, 1)
            ),
        )]
        self.energized_cells = defaultdict(list)

    def step(self) -> None:
        new_beams = []
        for head, direction in self.beams:
            next_pos = (head[0] + direction[0], head[1] + direction[1])
            if not pos_in_range(self.grid.shape, next_pos):
                continue

            new_directions = TRANSFORMATIONS[self.grid[next_pos]](*direction)
            new_beams.extend(
                (next_pos, new_direction)
                for new_direction in new_directions
                if new_direction not in self.energized_cells[next_pos]
            )
            self.energized_cells[next_pos].extend(new_directions)

        self.beams = new_beams

    def render(self) -> str:
        return '\n'.join(
            ' ' + ''.join(
                '*' if any(beam[-1] == (row_i, column_i) for beam, _ in self.beams) else (
                    '#' if (row_i, column_i) in self.energized_cells else cell
                )
                for column_i, cell in enumerate(row)
            )
            for row_i, row in enumerate(self.grid)
        )


def main() -> None:
    with open('input.txt') as file:
        grid = np.array([list(line.rstrip()) for line in file])

    height, width = grid.shape
    max_coverage = 0
    for start in [
        *zip(repeat(-1), range(width)),
        *zip(repeat(height), range(width)),
        *zip(range(height), repeat(-1)),
        *zip(range(height), repeat(width)),
    ]:
        # This could definitely be optimised using some clever method of reusing previously computed beam paths
        # However, it's fast enough, and I'm lazy, so oh well!
        contraption = Contraption(grid, start)
        while contraption.beams:
            contraption.step()
            if start == (-1, 3):
                contraption.render()
        max_coverage = max(max_coverage, len(contraption.energized_cells))

    print('Day 16.2 Answer:', max_coverage)


if __name__ == '__main__':
    main()
