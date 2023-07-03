a = int(input())
b = input()

result = []
for c in b:
    result.append(a*int(c))
result.reverse()

for s in result:
    print(s)
print(a*int(b))