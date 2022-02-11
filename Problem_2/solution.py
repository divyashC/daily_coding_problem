# Day 2
# Problem 2
# Date 11 Feb 2021
# Time 8:20 AM

arr = [1, 2, 3, 4, 5]
product = []

for i in range(len(arr)):
    currProduct = 1
    for j in range(len(arr)):
        if arr[i] != arr[j]:
            currProduct *= arr[j]
    product.append(currProduct)

print(product)
