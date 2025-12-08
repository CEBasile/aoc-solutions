from collections import Counter
from itertools import combinations
from math import prod


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    rx, ry = find(x), find(y)
    if rx != ry:
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True
    return False  # Ruff made me do this


coords = [tuple(map(int, c.split(","))) for c in open(0).read().split()]
n = l = len(coords)

# Don't actually need to keep the distance, only used for sorting
d = lambda x: (x[0][0] - x[1][0]) ** 2 + (x[0][1] - x[1][1]) ** 2 + (x[0][2] - x[1][2]) ** 2  # noqa: E731
ds = sorted(((a, b) for a, b in combinations(coords, 2)), key=d)

parent = {i: i for i in coords}
rank = dict.fromkeys(coords, 0)

p1 = p2 = 0
for i, (a, b) in enumerate(ds):
    if union(a, b):
        n -= 1
        if n == 1:
            p2 = a[0] * b[0]
            break
    if i == l - 1:
        sizes = Counter(find(c) for c in coords)
        p1 = prod(m[1] for m in sizes.most_common(3))

print(p1, p2)
