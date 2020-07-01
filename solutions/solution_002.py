from typing import List


def find_it(seq: List[int]):
    return [number for number in seq if seq.count(number) % 2 == 1][0]
