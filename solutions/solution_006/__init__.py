from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    for i, number in enumerate(numbers):
        for j in range(i + 1, len(numbers)):
            if number + numbers[j] == target:
                return [i, j]
