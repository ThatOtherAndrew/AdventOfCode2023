from collections import defaultdict

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
    def __init__(self, grid: np.ndarray) -> None:
        self.grid = grid
        self.beams = [([(0, -1)], (0, 1))]  # turns out I didn't need to track the history of a beam of light. Oh well!
        self.energized_cells = defaultdict(list)

    def step(self) -> None:
        new_beams = []
        for beam, direction in self.beams:
            head = beam[-1]
            next_pos = (head[0] + direction[0], head[1] + direction[1])
            if not pos_in_range(self.grid.shape, next_pos):
                continue

            beam.append(next_pos)
            new_directions = TRANSFORMATIONS[self.grid[next_pos]](*direction)
            new_beams.extend(
                (beam.copy(), new_direction)
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

    contraption = Contraption(grid)
    while contraption.beams:
        contraption.step()

    print(contraption.render())

    print('Day 16.1 Answer:', len(contraption.energized_cells))


if __name__ == '__main__':
    main()
