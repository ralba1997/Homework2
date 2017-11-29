n = int(input())
A = list(map(int, input().split()))
sA = sorted(A)
d = {}
for j in range(1, len(sA)):
    diff = abs(sA[j]-sA[j-1])
    if d.get(diff) is None:
        d[diff] = tuple([sA[j-1], sA[j]])
    else:
        d[diff] += tuple([sA[j-1], sA[j]])
print(*d[min(k for k in d)])
