"""
In this example:

List[int] specifies that the data argument of process_data function should be a list of integers.
Tuple[int, int] specifies that the return value of process_data function should be a tuple containing two integers.
Union[float, None] specifies that the return value of divide function can either be a float or None.
"""

from typing import List, Tuple, Union


def process_data(data: List[int]) -> Tuple[int, float]:
    total = sum(data)
    average = total / len(data)
    return total, average


def divide(a: int, b: int) -> Union[float, None]:
    if b == 0:
        return None
    return a / b


data = [1, 2, 3, 4, 5]
result = process_data(data)
print(f"Result is {result}")
print("Total:", result[0])
print("Average:", result[1])

print("Result of division:", divide(10, 2))
print("Result of division by zero:", divide(10, 0))
