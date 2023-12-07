CARDS = 'J23456789TQKA'


def get_strength(hand: str) -> int:
    joker_count = hand.count('J')
    counts = sorted(hand.count(card) for card in set(filter(lambda card: card != 'J', hand))) or [0]
    counts[-1] += joker_count
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

    print('Day 7.2 Answer:', winnings)


if __name__ == '__main__':
    main()
