"""
Below is an example of generator functions
"""


def fibonacci(max):
    a = 0
    b = 1
    counter = 0
    while True:
        yield a
        a, b = b, a + b
        counter += 1
        if counter == max:
            raise StopIteration


abcd = fibonacci(10)
print(next(abcd))
print(next(abcd))
print(next(abcd))
print(next(abcd))
print(next(abcd))
print(next(abcd))
print(next(abcd))
print(next(abcd))
print(next(abcd))
print(next(abcd))
print(next(abcd))
print(next(abcd))
print(next(abcd))
print(next(abcd))
print(next(abcd))
print(next(abcd))


