from itertools import groupby


def super_reduced_string(s):
    reducible = True

    while reducible:
        red = ""
        for c, g in groupby(s):
            red += c * (len(list(g)) % 2)
        if red == s:
            reducible = False
        else:
            s = red
    if len(s) > 0:
        return s
    else:
        return "Empty String"


s = input().strip()
result = super_reduced_string(s)
print(result)
