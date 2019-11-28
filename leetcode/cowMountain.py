import sys
num = input()
red = sys.stdin.readline().strip('')
red = list(map(int, red.split()))
lens = len(red)
count = 0
for ind in range(lens - 1, 0, -1):
    if red[ind] > 0:
        start = (ind + 1) // 2 - 1
        count = count + red[ind]
        red[start] = red[start] - red[ind]
        if ind % 2 == 0:
            red[ind - 1] = red[ind - 1] - red[ind]
        red[ind] = 0

if red[0] > 0:
    count = count + red[0]

print(count)
