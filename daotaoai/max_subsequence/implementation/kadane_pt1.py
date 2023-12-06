arr = [3, -1, -3, 5, 2, 5, 0, -1, 5, 4]
lenarr = len(arr)

# lenarr = int(input())
# arr = [int(val) for val in input().split()]

result = 0
current_sum = 0

for i in range(0, len(arr)):
  current_sum += arr[i]
  if current_sum < 0:
    current_sum = 0
  elif current_sum > result:
    result = current_sum

print(result)
