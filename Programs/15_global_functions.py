a = 10
x = 100


def sum():
    global x
    globals()['a'] = 100
    # a = a + 100
    print(a)


sum()
print(a)
print(globals())
