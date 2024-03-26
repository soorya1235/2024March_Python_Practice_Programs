"""
Below is an example of using iterators implementation
"""


class Iterator:

    def __init__(self, number):
        self.counter = number
        self.cur_fib = 0
        self.next_fib = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == 0:
            raise StopIteration
        self.counter -= 1
        self.next_fib = self.cur_fib + self.next_fib
        self.cur_fib = self.next_fib
        return self.cur_fib


obj1 = Iterator(3)
for obj in obj1:
    print(obj)
