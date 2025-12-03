banks = [list(map(int, line)) for line in open(0).read().split()]

# Cleaned up after submission
def max_joltage(n):
    j = 0
    for bank in banks:
        start = 0
        nums = []
        for end in range(len(bank) - n + 1, len(bank) + 1):
            m = 0
            m_i = start
            for i in range(start, end):
                if bank[i] == 9:
                    m_i = i
                    break
                if bank[i] > m:
                    m = bank[i]
                    m_i = i
            nums.append(str(bank[m_i]))
            start = m_i + 1
        j += int("".join(nums))
    return j


print(max_joltage(2), max_joltage(12))
