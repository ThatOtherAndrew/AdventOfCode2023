from collections import defaultdict


def get_gear_coords(schematic: list[str]) -> list[tuple[int, int]]:
    symbol_coords = []

    for y, row in enumerate(schematic):
        for x, cell in enumerate(row):
            if cell == '*':
                symbol_coords.append((x, y))

    return symbol_coords


def get_gear_numbers(
    schematic: list[str],
    symbol_coords: list[tuple[int, int]]
) -> list[tuple[int, tuple[int, int]]]:
    gear_ratio_numbers = []
    number = ''
    adjacent_gear = None
    for y, row in enumerate(schematic):
        for x, cell in enumerate(row):
            if not cell.isdigit():
                if adjacent_gear:
                    gear_ratio_numbers.append((int(number), adjacent_gear))
                number = ''
                adjacent_gear = None
                continue

            number += cell
            for symbol in symbol_coords:
                if abs(x - symbol[0]) <= 1 and abs(y - symbol[1]) <= 1:
                    adjacent_gear = symbol
                    break

    return gear_ratio_numbers


def calculate_gear_ratios(gear_numbers: list[tuple[int, tuple[int, int]]]) -> list[int]:
    gears = defaultdict(list)
    for gear_number in gear_numbers:
        gears[gear_number[1]].append(gear_number[0])

    return [numbers[0] * numbers[1] for numbers in gears.values() if len(numbers) == 2]


def main() -> None:
    with open('input.txt') as file:
        schematic = [line.strip() for line in file]

    gear_numbers = get_gear_numbers(schematic, get_gear_coords(schematic))
    gear_ratios = calculate_gear_ratios(gear_numbers)
    print('Day 3.2 Answer:', sum(gear_ratios))


if __name__ == '__main__':
    main()
