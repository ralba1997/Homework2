V = float(input())
n = int(input())
ar = list(map(float, input().split()))
i = 0
while ar[i] < V:
    i += 1
print(i)
