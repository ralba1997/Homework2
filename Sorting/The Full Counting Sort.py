n = int(input())
lines = []
for i in range(n):
    line = list(input().split())
    line[0] = int(line[0])
    if i < n//2:
        line[1] = "-"
    lines += [line]
for line in sorted(lines, key=lambda x: x[0]):
    print(line[1], end=" ")
