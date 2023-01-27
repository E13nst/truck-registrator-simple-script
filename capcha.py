PLUS = [
    0b000,
    0b010,
    0b111,
    0b010,
    0b000,
]

MINUS = [
    0b000,
    0b000,
    0b111,
    0b000,
    0b000,
]

ZERO = [
    0b111,
    0b101,
    0b101,
    0b101,
    0b111,
]

ONE = [
    0b01,
    0b11,
    0b01,
    0b01,
    0b01,
]

TWO = [
    0b111,
    0b001,
    0b111,
    0b100,
    0b111,
]

THREE = [
    0b111,
    0b001,
    0b111,
    0b001,
    0b111,
]

FOUR = [
    0b101,
    0b101,
    0b111,
    0b001,
    0b001,
]

FIVE = [
    0b111,
    0b100,
    0b111,
    0b001,
    0b111,
]

SIX = [
    0b111,
    0b100,
    0b111,
    0b101,
    0b111,
]

SEVEN = [
    0b111,
    0b001,
    0b010,
    0b100,
    0b100,
]

EIGHT = [
    0b111,
    0b101,
    0b111,
    0b101,
    0b111,
]

NINE = [
    0b111,
    0b101,
    0b111,
    0b001,
    0b111,
]

NUMBERS = [MINUS, ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE]


def decode(d):
    i = -1
    for number in NUMBERS:
        if number == d:
            # print("=%i=" % i)
            return i
        i = i + 1
    return 0


def operation(d):
    if d == PLUS:
        # print("+PLUS+")
        return True
    else:
        # print("-MINUS-")
        return False


def calculate(a, b, plus):
    if plus:
        return a + b
    else:
        return a - b

