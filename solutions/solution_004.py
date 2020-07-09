ROMAN_NUMERALS = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}


def solution(n: int):
    result = []
    for roman_numeral, num in ROMAN_NUMERALS.items():
        count = int(n / num)
        result.append(roman_numeral * count)
        n -= num * count
    return "".join(result)
