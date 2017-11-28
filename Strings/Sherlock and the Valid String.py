def isValid(s):
    characters = []
    frequencies = []
    valid = "NO"
    for char in s:
        if char not in characters:
            characters += char
    for i in characters:
        frequencies += [s.count(i)]
    if len(set(frequencies)) == 1:
        valid = "YES"
    elif len(set(frequencies)) == 2:
        if frequencies.count(1) == 1:
            valid = "YES"
        elif max(frequencies) - min(frequencies) == 1 and frequencies.count(max(frequencies)) == 1:
            valid = "YES"
    return valid


s = input().strip()
result = isValid(s)
print(result)
