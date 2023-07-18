total = int(input())
N = int(input())

ls = []
for n in range(N):
    a, b = map(int, input().split())
    ls.append(a*b)

result = 0
for el in ls:
    result += el

if result == total:
    print("Yes")
else:
    print("No")