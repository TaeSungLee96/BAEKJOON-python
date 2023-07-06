ls = []
for n in range(10):
    a = int(input())
    b = a%42
    ls.append(b)
result = list(set(ls))
print(len(result))
