"""
Example of Nested Dictionary
"""

dic = {"a": 1, "b": 2, "c": 3, "d": {"e": 4, "f": 5, "g": 7}, "h": {"i": 8, "j": 9}, "z": {"aa": 10}}
my_dict = isinstance(dic, dict)
print("my_dict is a dict:", my_dict)

for ab in dic.keys():
    # print(type(dic[ab])
    bb = type(dic[ab])
    # print(bb)
    if type(dic[ab]) is dict:
        print("It is dictionary")
        print(ab)
        for a, b in dic[ab].items():
            print(f'{a}:{b}')
    else:
        print(f"The key is {ab} and value is {dic[ab]}")

d1 = {"a": 1, "b": 2, "c": {"e": 1, "f": 2, "g": 3}}
for x in d1.keys():
    if type(d1[x]) is dict:
        print(f"x is dictionary")
        for x, y in d1[x].items():
            print(f"key is {x} and value is {y}")
    else:
        print(f"key is {x} and value is {d1[x]}")
