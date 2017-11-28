S = input().strip()
message = "SOS" * (len(S)//3)
count = 0
for i in range(len(S)):
    if S[i] != message[i]:
        count += 1
print(count)
