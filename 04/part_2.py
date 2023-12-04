def get_card_matches(card: tuple[set[int], set[int]]) -> int:
    return sum(number in card[0] for number in card[1])


def main() -> None:
    with open('input.txt') as file:
        # noinspection PyTypeChecker
        cards: list[tuple[set[int], set[int]]] = [
            tuple(
                set(map(int, part.split()))
                for part in line.partition(': ')[2].split(' | ')
            )
            for line in file
        ]

    match_counts = [[get_card_matches(card), 1] for card in cards]
    for i, match_count in enumerate(match_counts):
        for new_card_index in range(i + 1, i + match_count[0] + 1):
            match_counts[new_card_index][1] += match_count[1]

    print('Day 4.2 Answer:', sum(match_count[1] for match_count in match_counts))


if __name__ == '__main__':
    main()
