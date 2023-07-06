ls =[]
for n in range(9):
    N = int(input())
    ls.append(N)
print(max(ls))
print(ls.index(max(ls))+1)