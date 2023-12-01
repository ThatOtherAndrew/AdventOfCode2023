def transform_digits(line: str) -> str:
    digits = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    indices = []

    for key in digits.keys():
        for i in range(len(line)):
            if line.startswith(key, i):
                indices.append((i, key))

    if not indices:
        return line

    indices.sort()
    line = line.replace(indices[0][1], digits[indices[0][1]], 1)
    line = digits[indices[-1][1]].join(line.rsplit(indices[-1][1], 1))
    return line


def main() -> None:
    with open('input.txt') as file:
        digits = [tuple(filter(lambda char: char.isdigit(), transform_digits(line))) for line in file]

    for digit in digits:
        if not digit:
            continue
        print(''.join(digit), digit[0] + digit[-1])

    answer = sum(
        int(digit[0] + digit[-1])
        for digit in digits
        if digit
    )

    print('Day 1.2 Answer:', answer)


if __name__ == '__main__':
    main()
