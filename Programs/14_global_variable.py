"""
Below is an example of global variable function
"""
X = 10


def update_x():
    """
    This function is an example of using the global function
    :return:
    """
    global X
    X = 20


update_x()
print(X)  # Output will be 20
