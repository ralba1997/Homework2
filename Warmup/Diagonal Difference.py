n = int(input().strip())
a = []
result = 0
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
    result = result + a[a_i][a_i] - a[a_i][n-1-a_i]
print(abs(result))
