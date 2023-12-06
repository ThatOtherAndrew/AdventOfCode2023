def main() -> None:
    with open('input.txt') as file:
        race_time, distance = [int(line.replace(' ', '').partition(':')[2]) for line in file]

    # The below optimised code was planned out in Desmos: https://www.desmos.com/calculator/ugjfmsczwq
    midpoint = race_time / 2
    offset = (race_time ** 2 - 4 * distance) ** 0.5 / 2
    win_margin = int(midpoint + offset) - int(midpoint - offset)

    print('Day 6.2 Answer:', win_margin)


if __name__ == '__main__':
    main()
