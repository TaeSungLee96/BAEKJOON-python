N = int(input())
for i in range(1, N+1, 1):
    print(" " * (N - i) + "*" * (2 * i - 1))
    if i == N:
        for j in range(N-1, 0, -1):
            print(" "*(N-j) + "*"*(2*j-1))