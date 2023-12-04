def main() -> None:
    with open('input.txt') as file:
        cards = [
            tuple(
                set(map(int, part.split()))
                for part in line.partition(': ')[2].split(' | ')
            )
            for line in file
        ]

    scores = [
        int(2 ** (sum(number in card[0] for number in card[1]) - 1))
        for card in cards
    ]
    print('Day 4.1 Answer:', sum(scores))


if __name__ == '__main__':
    main()
