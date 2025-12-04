G = {i + j * 1j for i, r in enumerate(open(0)) for j, c in enumerate(r.strip()) if c == "@"}

D = [
    (-1 - 1j),
    (0 - 1j),
    (1 - 1j),
    (-1 + 0j),
    (1 + 0j),
    (-1 + 1j),
    (0 + 1j),
    (1 + 1j),
]

prev = -1
a = b = 0
p1 = True
while prev < b:
    prev = b
    for p in (T := G.copy()):
        empty = 0
        for d in D:
            if (p + d) not in T:
                empty += 1
                if empty >= 5:
                    G.remove(p)
                    b += 1
                    break
    if p1:
        a = b
        p1 = False

print(a, b)
