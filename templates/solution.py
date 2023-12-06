# Read from a file
with open("/home/teebow1e/dsa/daotaoai/max_subsequence/implementation/input.txt", "r") as input_file:
    # Assume input contains 2 lines, line 1 is an int, line 2 is an arr
    data = [line.strip() for line in input_file.readlines()]
    lenarr = int(data[0])
    arr = [int(val) for val in data[1].split()]

# Read from user input
lenarr = int(input())
arr = [int(val) for val in input().split()]