
N = int(input())

ls = []
for n in range(N):
    a, b = map(int, input().split())
    ls.append(a+b)

i = 1
for el in ls:
    print(f"Case #{i}: {el}")
    i+=1
