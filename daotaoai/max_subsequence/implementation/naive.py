# lenarr = int(input())
# arr = [int(val) for val in input().split()]

arr = [3, -1, -3, 5, 2, 5, 0, -1, 5, 4]
lenarr = len(arr)

# ý tưởng: tính tổng của subarray dựa trên array tổng dồn bằng cách: 
# tổng(i,j) = tổng_dồn[j] - tổng_dồn[i-1]

cumulative_sum = [arr[0]]
for _ in range(0, lenarr-1):
    cumulative_sum.append(cumulative_sum[_] + arr[_+1])
cumulative_sum.insert(0,0)

def find_sum_subarray(i,j):
    return cumulative_sum[i] - cumulative_sum[j-1]

res = 0
for i in range(0, lenarr+1):
    for j in range(1, i+1):
        temp_res = find_sum_subarray(i,j)
        if temp_res > res:
            res = temp_res

print(res)
# for debugging
# for i in range(0, lenarr+1):
#     for j in range(1, i+1):
#         print(f"{[i,j]} -> {find_sum_subarray(i,j)}")

