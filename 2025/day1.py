moves = [(1 if line[0] == "R" else -1) * int(line[1:]) for line in open(0).read().split()]

a = b = 0
pos = 50
for move in moves:
    div, rem = divmod(pos + move, 100)
    a += not bool(rem)
    b += abs(div)
    if div < 0 and pos == 0:
        b -= 1
    if move < 0 and rem == 0:
        b += 1
    pos = rem

print(a, b)
