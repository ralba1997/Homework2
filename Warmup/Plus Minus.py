n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
pos = 0
neg = 0
for x in arr:
    if x > 0:
        pos += 1
    elif x < 0:
        neg += 1
zeros = len(arr) - pos - neg
print(pos/len(arr))
print(neg/len(arr))
print(zeros/len(arr))
