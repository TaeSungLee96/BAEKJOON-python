N = int(input())

ls = []
for n in range(N):
    a, b = map(int, input().split())
    ls.append({sum:a+b, "a":a, "b":b})

i = 1
for el in ls:
    print(f"Case #{i}: {el['a']} + {el['b']} = {el[sum]}")
    i+=1
