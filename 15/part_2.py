from collections import defaultdict
from functools import reduce


def hash_character(cumulative_hash: int, character: str) -> int:
    return (cumulative_hash + ord(character)) * 17 % 256


def main() -> None:
    with open('input.txt') as file:
        lenses = [
            (line[:-1], 0) if line.endswith('-') else (line[:-2], int(line[-1]))
            for line in file.read().split(',')
        ]

    boxes = defaultdict(dict)
    for lens in lenses:
        label_hash = reduce(hash_character, lens[0], 0)
        if lens[1]:
            boxes[label_hash][lens[0]] = lens[1]
        elif lens[0] in boxes[label_hash]:
            del boxes[label_hash][lens[0]]

    total_focusing_power = sum(
        sum(
            (box_num + 1) * (lens_index + 1) * focal_length
            for lens_index, focal_length in enumerate(lenses.values())
        )
        for box_num, lenses in boxes.items()
    )

    print('Day 15.2 Answer:', total_focusing_power)


if __name__ == '__main__':
    main()
