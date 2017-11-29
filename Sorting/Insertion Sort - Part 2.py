n = int(input())
A = list(map(int, input().split()))
for i in range(1, len(A)):
    e = A[i]
    j = i-1
    while j >= 0 and A[j] > e:
        A[j + 1] = A[j]
        j = j-1
    A[j + 1] = e
    print(*A)
