def birthdayCakeCandles(n, ar):
    count = 0
    maxn = max(ar)
    for i in range(n):
        if ar[i] == maxn:
            count += 1
    return count


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
