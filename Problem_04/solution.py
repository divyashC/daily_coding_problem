# Day 4
# Problem 4
# Date 13 Feb 2022
# Time 9:20 PM

# input -> [3, 4, -1, 1]
# output -> 2

# input -> [1, 2, 0]
# output -> 3

arr = input()

unique = {*arr}
print(unique)
index = 1
while True:
    if index not in unique:
        print(index)
        break
    index += 1
