"""
Default args and key word args example
"""


def arguments(x, *args, **kwargs):
    print(x)
    print(args)
    for a in args:
        print(a)
        for k, v in kwargs.items():
            print("key is", k, "value is", v)


arguments(10, 10, 20, 30, name="soorya", salary="10k")
