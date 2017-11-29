n = int(input())
ar = list(map(int, input().split()))
pivot = ar[0]
left = []
right = []
for i in ar:
    if i < pivot:
        left += [i]
    elif i > pivot:
        right += [i]
print(*left, pivot, *right)
