n = int(input())
numbers = list(map(int, input().split()))
sn = sorted(numbers)
if n % 2 == 0:
    m = (sn[n // 2] + sn[n // 2 + 1]) / 2
else:
    m = sn[n // 2]
print(m)
