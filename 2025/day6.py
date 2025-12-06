from math import prod

rows = open(0).read().splitlines()
t = [line.split() for line in rows]

problems = [list(row) for row in zip(*t, strict=True)]
ops = {"*": prod, "+": sum}
a = b = 0

for problem in problems:
    nums, op = map(int, problem[:-1]), problem[-1]
    a += ops[op](nums)

width = len(rows[0])
problems = []
current = []
for i in range(width):
    col = "".join(row[i] for row in rows).strip()
    if not col:
        problems.append(current)
        current = []
    elif not current:
        current = [col[-1], col[:-1]]
    else:
        current.append(col)

problems.append(current)

for problem in problems:
    nums, op = map(int, problem[1:]), problem[0]
    b += ops[op](nums)
print(a, b)
