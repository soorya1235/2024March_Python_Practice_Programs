"""
Program to reverse the entire list 
"""
s = 'python is cool'
sl = s.split()
print(sl)
ln = len(sl) - 1
x = 0
output = []
while x <= ln:
    print(sl[x][::-1])
    output.append(sl[x][::-1])
    x += 1
print(output)
print(' '.join(output))
