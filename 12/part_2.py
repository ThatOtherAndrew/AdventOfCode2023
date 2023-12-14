from functools import cache  # VERY MUCH NO LONGER MINOR speed boost for free


# The two below functions look very similar and there's probably a clever way to merge the two recursive functions
# However, I currently do not have the brain capacity to do so, so if this works out then I probably won't touch it lmao
# - Andrew


@cache
def count_positions(chunk: str, numbers: tuple[int, ...]) -> int:
    if not numbers:
        # Return 1 if no hashtags remaining to fit, otherwise 0 for no solutions
        return int('#' not in chunk)

    solutions = 0
    group_length = numbers[0]
    for position in range(len(chunk) - group_length + 1):
        if '#' in chunk[:position]:
            break
        if not (position + group_length < len(chunk) and chunk[position + group_length] == '#'):
            solutions += count_positions(chunk[position + group_length + 1:], numbers[1:])

    return solutions


@cache
def count_solutions(chunks: tuple[str, ...], numbers: tuple[int, ...]) -> int:
    if not chunks:
        # Return 1 if no numbers remaining to fit, otherwise 0 for no solutions
        return int(not numbers)

    if not numbers and not any('#' in chunk for chunk in chunks):
        return 1

    solutions = 0
    chunk = chunks[0]
    for group_count in range(len(numbers) + 1):
        groups_to_fit = numbers[:group_count]

        solutions += count_positions(chunk, groups_to_fit) * count_solutions(chunks[1:], numbers[group_count:])

    return solutions


def main() -> None:
    with open('input.txt') as file:
        puzzles = []
        for line in file.readlines():
            springs, _, numbers = line.partition(' ')
            numbers = tuple(map(int, numbers.split(',')))
            puzzles.append(('?'.join([springs] * 5), numbers * 5))  # this is the only change!

    arrangements_sum = sum(
        count_solutions(
            tuple(filter(None, puzzle[0].split('.'))),
            puzzle[1]
        )
        for puzzle in puzzles
    )

    print('Day 12.2 Answer:', arrangements_sum)


if __name__ == '__main__':
    main()
