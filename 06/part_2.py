def get_time(hold_duration: int, race_time: int) -> int:
    return hold_duration * (race_time - hold_duration)


def main() -> None:
    with open('input.txt') as file:
        race_time, distance = [int(line.replace(' ', '').partition(':')[2]) for line in file]

    win_margin = sum(get_time(hold_time, race_time) > distance for hold_time in range(race_time))
    print('Day 6.2 Answer:', win_margin)


if __name__ == '__main__':
    main()
