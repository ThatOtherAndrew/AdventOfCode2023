def get_symbol_coords(schematic: list[str]) -> list[tuple[int, int]]:
    symbol_coords = []

    for y, row in enumerate(schematic):
        for x, cell in enumerate(row):
            if not cell.isdigit() and cell != '.':
                symbol_coords.append((x, y))

    return symbol_coords


def get_part_numbers(schematic: list[str], symbol_coords: list[tuple[int, int]]) -> list[int]:
    part_numbers = []
    number = ''
    adjacent = False
    for y, row in enumerate(schematic):
        for x, cell in enumerate(row):
            if not cell.isdigit():
                if adjacent:
                    part_numbers.append(int(number))
                number = ''
                adjacent = False
                continue

            number += cell
            if any(
                abs(x - symbol[0]) <= 1 and abs(y - symbol[1]) <= 1
                for symbol in symbol_coords
            ):
                adjacent = True

    return part_numbers


def main() -> None:
    with open('input.txt') as file:
        schematic = [line.strip() for line in file]

    part_numbers = get_part_numbers(schematic, get_symbol_coords(schematic))
    print('Day 3.1 Answer:', sum(part_numbers))


if __name__ == '__main__':
    main()
