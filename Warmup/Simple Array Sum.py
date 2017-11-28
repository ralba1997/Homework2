def simpleArraySum(n, a):
    add = 0
    for i in range(n):
        add += a[i]
    return add


m = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(m, ar)
print(result)
