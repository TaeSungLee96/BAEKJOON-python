N = int(input())
m = 0
while True:
    if N == 1:
        break
    m += 1
    a = int(2 + (6 * m * (m - 1) / 2))
    b = int(2 + (6 * m * (m + 1) / 2))
    if N in range(a, b):
        break
print((m + 1))