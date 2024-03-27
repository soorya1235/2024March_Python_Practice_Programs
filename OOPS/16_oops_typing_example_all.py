"""
Example of using
Certainly! Here's an updated example that includes usage of All, Any, List, Tuple, Union, and Optional from the typing
module:
"""

from typing import List, Tuple, Union, Optional, Any


def process_data(data: List[int]) -> Tuple[int, float]:
    """
    Process a list of integers and return the total sum and average.

    Args:
        data (List[int]): A list of integers.

    Returns:
        Tuple[int, float]: A tuple containing the total sum and average of the input data.
    """
    total = sum(data)
    average = total / len(data)
    return total, average


def divide(a: int, b: int) -> Union[float, None]:
    """
    Divide two integers and return the result.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        Union[float, None]: The result of the division. If the denominator is 0, returns None.
    """
    if b == 0:
        return None
    return a / b


def any_or_all(value: Any, check_all: bool) -> bool:
    """
    Check if the given value satisfies the condition.

    Args:
        value (Any): The value to be checked.
        check_all (bool): If True, check if all elements are truthy.
                          If False, check if any element is truthy.

    Returns:
        bool: True if the condition is satisfied, False otherwise.
    """
    if check_all:
        return all(value)
    else:
        return any(value)


def process_optional_value(value: Optional[int]) -> Optional[int]:
    """
    Process an optional integer value.

    Args:
        value (Optional[int]): An optional integer value.

    Returns:
        Optional[int]: The processed value if it is not None, otherwise returns None.
    """
    if value is not None:
        return value * 2
    else:
        return None


# Example usage
data = [1, 2, 3, 4, 5]
total, average = process_data(data)
print("Total:", total)
print("Average:", average)

result = divide(10, 2)
print("Result of division:", result)
breakpoint()
print("Any:", any_or_all([True, False, False], check_all=False))
print("All:", any_or_all([True, False, False], check_all=True))

optional_value = 5
processed_optional_value = process_optional_value(optional_value)
print("Processed optional value:", processed_optional_value)
