def parse_seed_map(seed_map: str) -> tuple[range, range]:
    numbers = tuple(map(int, seed_map.split()))
    return range(numbers[1], numbers[1] + numbers[2]), range(numbers[0], numbers[0] + numbers[2])


def get_location(seed: int, maps: list[list[tuple[range, range]]]) -> int:
    for resource_map in maps:
        for source, destination in resource_map:
            if seed in source:
                seed = destination[source.index(seed)]
                break

    return seed


def main() -> None:
    with open('input.txt') as file:
        seeds = tuple(map(int, file.readline().removeprefix('seeds: ').split()))
        maps = [
            list(map(parse_seed_map, block.splitlines()[1:]))
            for block in file.read().lstrip().split('\n\n')
        ]

    locations = [get_location(seed, maps) for seed in seeds]
    print('Day 5.1 Answer:', min(locations))


if __name__ == '__main__':
    main()
