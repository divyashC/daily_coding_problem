arr = [10, 15, 3, 7]
k = 17

for i in range(len(arr)):
    for j in range(i, len(arr)):
        if (arr[i] + arr[j] == k and i != j):
            print(arr[i],  arr[j])
            break
