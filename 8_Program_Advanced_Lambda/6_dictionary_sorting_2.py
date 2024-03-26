from operator import itemgetter

dic = {"a": 5, "e": 1, "b": 20, "f": 45, "g": 12}

d1 = sorted(dic.items(), key=lambda x: x[0])
d2 = sorted(dic.items(), key=lambda x: x[1])

d3 = sorted(dic.items(), key=itemgetter(0))
d4 = sorted(dic.items(), key=itemgetter(1))

print(d1)
print(d2)

print(d3)
print(d4) 