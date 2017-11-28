def solve(a0, a1, a2, b0, b1, b2):
    cpA = 0
    cpB = 0
    A = [a0, a1, a2]
    B = [b0, b1, b2]
    for i in range(3):
        if A[i] > B[i]:
            cpA += 1
        elif A[i] < B[i]:
            cpB += 1
    return cpA, cpB


a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print(" ".join(map(str, result)))
