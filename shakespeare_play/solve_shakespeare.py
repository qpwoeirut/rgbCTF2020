with open("play", 'r') as f:
    lines = [line for line in f]

with open("some_numbers.txt", 'r') as f:
    nums = [list(map(int, line.split(','))) for line in f]

flag = ""
for pair in nums:
    flag += lines[pair[0]][pair[1]]

print(flag)
