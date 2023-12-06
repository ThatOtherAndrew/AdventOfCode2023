from functools import reduce


def get_time(hold_duration: int, race_time: int) -> int:
    return hold_duration * (race_time - hold_duration)


def main() -> None:
    with open('input.txt') as file:
        times, distances = tuple(tuple(map(int, line.split()[1:])) for line in file)
        races = list(zip(times, distances))

    win_margins = [
        sum(get_time(hold_time, race_time) > distance for hold_time in range(race_time))
        for race_time, distance in races
    ]
    print('Day 6.1 Answer:', reduce(lambda x, y: x * y, win_margins))


if __name__ == '__main__':
    main()
