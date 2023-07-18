total = list(range(1,31))

for n in range(28):
    s = int(input())
    total.remove(s)

print(min(total))
print(max(total))