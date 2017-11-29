n = int(input())
A = list(map(int, input().split()))
e = A[-1]
j = n-2
while j >= 0 and A[j] > e:
    A[j + 1] = A[j]
    j = j-1
    print(*A)
A[j + 1] = e
print(*A)
