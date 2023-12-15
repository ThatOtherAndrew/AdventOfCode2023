from functools import reduce


def hash_character(cumulative_hash: int, character: str) -> int:
    return (cumulative_hash + ord(character)) * 17 % 256


def main() -> None:
    with open('input.txt') as file:
        strings = file.read().split(',')

    hash_sum = sum(reduce(hash_character, string, 0) for string in strings)
    print('Day 15.1 Answer:', hash_sum)


if __name__ == '__main__':
    main()
