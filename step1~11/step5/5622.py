S = list(map(str,input()))

ls = ["0","0","ABC","DEF","GHI","JKL", "MNO", "PQRS","TUV", "WXYZ"]

result = 0
for el in ls:
    for s in S:
        if el.find(s) != -1:
            result += ls.index(el) + 1

print(result)