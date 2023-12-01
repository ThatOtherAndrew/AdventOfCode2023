with open('input.txt') as file:
    digits = [tuple(filter(lambda char: char.isdigit(), line)) for line in file]

print('Day 1.1 Answer:', sum(int(digit[0] + digit[-1]) for digit in digits))
