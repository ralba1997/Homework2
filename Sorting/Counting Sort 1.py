n = int(input())
ar = list(map(int, input().split()))
counter = [0] * 100
for i in ar:
    counter[i] += 1
print(*counter)
