def extract_digits(line: str) -> int:
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digit = ''

    for i in range(len(line)):
        if line[i].isdigit():
            digit += line[i]
            break
        elif any(line[i:].startswith(match := number) for number in numbers):
            digit += str(numbers.index(match))
            break

    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            digit += line[i]
            break
        elif any(line[i:].startswith(match := number) for number in numbers):
            digit += str(numbers.index(match))
            break

    return int(digit)


def main() -> None:
    with open('input.txt') as file:
        digits = list(map(extract_digits, file))

    print('Day 1.2 Answer:', sum(digits))


if __name__ == '__main__':
    main()
