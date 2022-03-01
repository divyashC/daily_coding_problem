# Day 2
# Problem 2
# Date 11 Feb 2022
# Time 8:20 AM

# input -> [1, 2, 3, 4, 5]
# output -> [120, 60, 40, 30, 24]

arr = input()
product = []

for i in range(len(arr)):
    currProduct = 1
    for j in range(len(arr)):
        if arr[i] != arr[j]:
            currProduct *= arr[j]
    product.append(currProduct)

print(product)
