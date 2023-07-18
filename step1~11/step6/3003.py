S = list(map(int, input().split()))
ls = [1, 1, 2, 2, 2, 8]
c = [i - j for i, j in zip(ls, S)]
print(" ".join(str(s) for s in c ))