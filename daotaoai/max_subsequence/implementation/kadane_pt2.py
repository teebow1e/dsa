# lenarr = int(input())
# arr = [int(val) for val in input().split()]

arr = [3, -1, -3, 5, 2, 5, 0, -1, 5, 4]
lenarr = len(arr)

current_sum = arr[0]
result = arr[0]

for i in range(1, lenarr):
    # temp = current_sum + arr[i]
    current_sum = max(arr[i], current_sum + arr[i])
    result = max(result, current_sum)

print(result)