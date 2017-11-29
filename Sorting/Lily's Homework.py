n = int(input())
a = list(map(int, input().split()))
sa = sorted(a)
rsa = sorted(a, reverse=True)
pos = {}
for j in range(n):
    pos[a[j]] = j
ac = a[:]
pos_c = pos.copy()


def count_swaps(u, tab, s):
    swaps = 0
    for i in range(n):
        if s[i] != u[i]:
            tab[u[i]] = tab[s[i]]
            u[i], u[tab[s[i]]] = u[tab[s[i]]], u[i]
            swaps += 1
    return swaps


print(min(count_swaps(ac, pos_c, sa), count_swaps(a, pos, rsa)))
