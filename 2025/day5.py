class Inventory:
    def __init__(self, ranges):
        ranges = sorted(ranges, key=lambda x: x[0])
        self.fresh_ranges = []

        self.fresh_ranges = [ranges[0]]
        for cur in ranges[1:]:
            prev = self.fresh_ranges[-1]
            if cur[0] <= prev[1]:
                self.fresh_ranges[-1] = (prev[0], max(prev[1], cur[1]))
            else:
                self.fresh_ranges.append(cur)

    def __contains__(self, i):
        return any(r[0] <= i <= r[1] for r in self.fresh_ranges)


ranges = []
items = []
for line in open(0).read().split():
    if "-" in line:
        start, end = map(int, line.split("-"))
        ranges.append((start, end))
    else:
        items.append(int(line))

inv = Inventory(ranges)

print(sum(item in inv for item in items), sum(r[1] - r[0] + 1 for r in inv.fresh_ranges))
