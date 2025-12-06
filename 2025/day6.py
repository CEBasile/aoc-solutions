rows = open(0).readlines()

t = [line.split() for line in rows]
problems = [list(row) for row in zip(*t, strict=True)]

total = 0
for problem in problems:
    if problem[-1] == "*":
        solution = 1
        for i in map(int, problem[:-1]):
            solution *= i
    else:
        solution = sum(map(int, problem[:-1]))

    total += solution
print(total)

width = len(rows[0])
problems = []
current = []
total = 0

for i in range(width):
    col = "".join(row[i] for row in rows)
    if not col.strip():
        if current:
            problems.append(current)
            current = []
    elif not current:
        current = [col[-1], col[:-1].strip()]
    else:
        current.append(col[:-1].strip())

for problem in problems:
    match problem[0]:
        case "*":
            c = 1
            nums = [int(num) for num in problem[1:]]
            for num in nums:
                c *= num
            total += c
        case "+":
            nums = [int(num) for num in problem[1:]]
            total += sum(nums)
print(total)
