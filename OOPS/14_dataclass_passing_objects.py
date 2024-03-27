"""
Example of using dataclass
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class ArgsContainer:
    """
    A dataclass to contain arguments.
    """
    arg1: Any
    arg2: Any
    # Add more arguments as needed...


def my_function(args: ArgsContainer):
    """
    Function that takes an instance of ArgsContainer and processes its arguments.

    Args:
        args (ArgsContainer): An instance of ArgsContainer containing the arguments.
    """
    print("Using my_function:")
    print("arg1:", args.arg1)
    print("arg2:", args.arg2)
    # Process arguments...


if __name__ == "__main__":
    # Example usage
    args = ArgsContainer(arg1='value1', arg2='value2')
    my_function(args)
