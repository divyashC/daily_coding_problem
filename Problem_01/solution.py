# Day 1
# Problem 1
# Date 10 Feb 2022
# Time 12:12 AM

# input -> [10, 15, 3, 7]
#       -> 17
# output -> [10, 7]

arr = input()
k = int(input())

for i in range(len(arr)):
    for j in range(i, len(arr)):
        if (arr[i] + arr[j] == k and i != j):
            print([arr[i],  arr[j]])
            break
