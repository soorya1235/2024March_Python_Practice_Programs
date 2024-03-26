"""
This program will count the occurences of vowles in the string
"""
data = "aaaaaaaaessstttttttttttttttuuuuuuuuuuuuuuuuurrrrrrrrrrrrrrrrsssssvvvvvvvvvvvvvxt"
vowels = {"a", "e", "i", "o", "u"}
vow_freq = {}
for value in data:
    if value in vowels:
        vow_freq[value] = vow_freq.get(value, 0) + 1
print(f"The Vowels frequency is : {vow_freq}")

for data, value in vow_freq.items():
    print("Data is {} and Value is {}".format(data, value))
