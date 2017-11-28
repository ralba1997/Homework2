def aVeryBigSum(m, a):
    add = 0
    for i in range(m):
        add += a[i]
    return add


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)
