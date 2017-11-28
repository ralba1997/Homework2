def timeConversion(s):
    if s[:2] == "12":
        s = "00" + s[2:]
    if s[-2:] == "AM":
        s = s[:-2]
    if s[-2:] == "PM":
        s = str(int(s[:2]) + 12) + s[2:-2]
    return s


s = input().strip()
result = timeConversion(s)
print(result)
