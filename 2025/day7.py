from functools import cache

lines = open(0).read().split()

G = [list(row) for row in lines]
G[1][len(G[0]) // 2] = "|"

splits = 0
for i, row in enumerate(G):
    for j, col in enumerate(row):
        if col == "^" and G[i - 1][j] == "|":
            G[i][j - 1] = G[i][j + 1] = "|"
            splits += 1
        elif G[i - 1][j] == "|":
            G[i][j] = "|"

# Part 2
# Assuming every path goes to the end
nr, nc = len(G), len(G[0])
G = {(i, j): set() for i, r in enumerate(lines) for j, c in enumerate(r.strip()) if c == "^"}

# Fill up the adjancency list
for (i, j), children in G.copy().items():
    for pos in (j - 1), (j + 1):
        for c in range(1, nr):
            found = False
            if (i + c, pos) in G:
                children.add((i + c, pos))
                found = True
                break
        if not found:
            children.add((nr, pos))
            G[(nr, pos)] = set()


@cache
def dfs(pos):
    if not G[pos]:
        return 1
    return sum(dfs(child) for child in G[pos])


print(splits, dfs((2, nc // 2)))
