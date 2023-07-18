loop = int(input())

ls = []
for n in range(loop):
    a, b = map(int, input().split())
    ls.append(a+b)

for el in ls:
    print(el)