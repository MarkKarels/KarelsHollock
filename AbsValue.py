def solution(a):
    c = a.copy()
    b = []
    final = 0

    for x in c:
        b.append(final)
        final = 0
        for i in c:
            final += abs(i - x)
    b.append(final)
    position = 0
    final = 10 ** 7
    for i in range(1, len(b) - 1):
        if b[i] < final:
            position = i - 1
            final = b[i]

    return c[position]


a = [-100000, -10000, -1000, -100, -10, 0 , 10 , 100, 1000, 10000, 100000]
print(solution(a))