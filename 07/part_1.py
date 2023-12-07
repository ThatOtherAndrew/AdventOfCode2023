CARDS = '23456789TJQKA'


def get_strength(hand: str) -> int:
    counts = sorted(hand.count(card) for card in set(hand))
    return (
        [1, 1, 1, 1, 1],
        [1, 1, 1, 2],
        [1, 2, 2],
        [1, 1, 3],
        [2, 3],
        [1, 4],
        [5],
    ).index(counts)


def main() -> None:
    with open('input.txt') as file:
        hands = [line.split() for line in file]

    hands.sort(key=lambda hand: (
        get_strength(hand[0]),
        tuple(map(CARDS.index, hand[0]))
    ))
    winnings = sum(
        int(hand[1]) * (i + 1)
        for i, hand in enumerate(hands)
    )

    print('Day 7.1 Answer:', winnings)


if __name__ == '__main__':
    main()
