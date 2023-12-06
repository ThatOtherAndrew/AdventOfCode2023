def parse_seed_map(seed_map: str) -> tuple[range, range]:
    numbers = tuple(map(int, seed_map.split()))
    return range(numbers[1], numbers[1] + numbers[2]), range(numbers[0], numbers[0] + numbers[2])


def get_range_intersection(range1: range, range2: range) -> range:
    return range(max(range1.start, range2.start), min(range1.stop, range2.stop))


def subtract_ranges(range1: range, range2: range) -> list[range]:
    return list(filter(None, (
        range(range1.start, range2.start),
        range(range2.stop, range1.stop),
    )))


def transform_ranges(input_ranges: list[range], transform_maps: list[tuple[range, range]]) -> list[range]:
    new_ranges = []
    untransformed_parts = input_ranges.copy()

    for source, destination in transform_maps:
        new_parts = []

        for part in untransformed_parts:
            intersection = get_range_intersection(part, source)
            if not intersection:
                new_parts.append(part)
                continue

            new_parts.extend(subtract_ranges(part, intersection))
            offset = destination.start - source.start
            new_range = range(intersection.start + offset, intersection.stop + offset)
            new_ranges.append(new_range)

        untransformed_parts = list(set(filter(None, new_parts)))

    new_ranges.extend(untransformed_parts)
    return new_ranges


def main() -> None:
    with open('input.txt') as file:
        numbers = map(int, file.readline().removeprefix('seeds: ').split())
        seed_ranges = [range(start, start + length) for start, length in zip(numbers, numbers)]

        # I spent 2 hours of my life debugging this code, drawing out complex mapping diagrams by hand
        # Turns out I accidentally left a reversed() below from when I tried to work the problem backwards
        # That's 2 hours of my life which I'll never get back
        # So ummm... yeah. Don't do that.
        maps = [
            list(map(parse_seed_map, block.splitlines()[1:]))
            for block in file.read().lstrip().split('\n\n')
        ]

    for resource_map in maps:
        seed_ranges = transform_ranges(seed_ranges, resource_map)

    print('Day 5.2 Answer:', min(seed_range.start for seed_range in seed_ranges))


if __name__ == '__main__':
    main()
