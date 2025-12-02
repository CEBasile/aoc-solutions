ids = [pair.split("-") for pair in open(0).read().split(",")]

a = b = 0
for start, end in ids:
    for pid in range(int(start), int(end) + 1):
        num = str(pid)
        m = len(num) // 2
        for n in range(m, 0, -1):
            d, r = divmod(len(num), n)
            if r:
                continue

            if num[:n] * d == num:
                if d == 2:
                    a += pid
                b += pid
                break

print(a, b)
