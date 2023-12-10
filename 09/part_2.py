from math import prod


def lagrange_extrapolate(sequence: list[int]) -> float:
    # https://math.libretexts.org/Courses/Angelo_State_University/Mathematical_Computing_with_Python/3%3A_Interpolation_and_Curve_Fitting/3.2%3A_Polynomial_Interpolation
    return sum(
        sequence[i] * prod(
            (-1 - j) / (i - j)  # literally the only line that's changed from part 1 lmao
            for j in range(len(sequence))
            if i != j
        )
        for i in range(len(sequence))
    )


def main() -> None:
    with open('input.txt') as file:
        sequences = [list(map(int, line.split())) for line in file]

    sum_predictions = round(sum(map(lagrange_extrapolate, sequences)))
    print('Day 9.2 Answer:', sum_predictions)


if __name__ == '__main__':
    main()
