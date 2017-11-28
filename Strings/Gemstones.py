def gemstones(arr):
    a = set(arr[0])
    for i in range(1, len(arr)):
        a = a.intersection(set(arr[i]))
    return len(a)


n = int(input().strip())
arr = []
for arr_i in range(n):
    arr_t = str(input().strip())
    arr.append(arr_t)
result = gemstones(arr)
print(result)
