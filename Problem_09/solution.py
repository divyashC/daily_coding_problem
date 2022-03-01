# Day 9
# Problem 9
# Date 21 Feb 2022
# Time 6:25 PM

# input -> [2, 4, 6, 2, 5]
# output -> 13 (2 + 6 + 5)

# input -> [5, 1, 1, 5]
# output -> 10 (5 + 5)

def largest_sum(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return max(arr)
    else:
        return max(arr[0] + largest_sum(arr[2:]), largest_sum(arr[1:]))


arr = [2, 4, 6, 2, 5]
print(largest_sum(arr))
