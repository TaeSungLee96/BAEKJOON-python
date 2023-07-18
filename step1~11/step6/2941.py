S = input()
ls = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for s in ls:
    if S.find(s) != -1:
        S = S.replace(s, "*", S.count(s))
print(len(S))
